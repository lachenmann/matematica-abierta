---
title: "La construcción de los reales"
subtitle: "Axiomas, cortaduras, unicidad y desigualdad triangular"
language: es
version: M19-v01
revision: MA-2026-10-23
protocolos: [MA-PED-v1.1, MA-STYLE-v2.1, MA-CALIBRO-v3.2, PGE-v1.0]
fecha_revision: 2026-10-23
precedente: DID_LIBRO_LA_CONSTRUCCION_DE_LOS_REALES_M18_v05.md
primer_libro_publicado: DID_LIBRO_LA_CONSTRUCCION_DE_LOS_REALES_M17_v01.md
estado: edicion-de-estudio-publicada-con-reserva-critica
---

# Nota al lector

Medir una diagonal, comparar dos longitudes o estudiar una aproximación nos lleva a utilizar números reales. Cada una de esas acciones descansa sobre una estructura: podemos sumar y multiplicar, comparar resultados y encontrar una menor cota superior cuando el conjunto considerado tiene elementos y está acotado. Construir los reales significa producir un objeto en el que esas operaciones y propiedades queden justificadas. Al recorrer esa construcción, las reglas familiares de cálculo adquieren una razón que podemos examinar y demostrar.

Este libro nació de la lectura y el estudio de cuatro clases del curso *Real Analysis*, publicado en YouTube por el canal **Divergence is Divergence**. Su hilo conductor procede de esas lecciones: primero caracterizamos un sistema de números reales mediante los axiomas de cuerpo ordenado y la propiedad del supremo; después construimos efectivamente un modelo a partir de los racionales; probamos la unicidad de la estructura hasta isomorfismo; y, finalmente, estudiamos el valor absoluto, la desigualdad triangular y sus primeras consecuencias analíticas.

La exposición es una elaboración matemática autónoma en español, organizada a partir de esa secuencia de ideas. Desarrollamos las comprobaciones anunciadas en las clases y explicitamos las obligaciones que acompañan a una definición: representantes, signos, cuantificadores y dominios de validez. Las demostraciones, ejemplos, contraejemplos y ejercicios resueltos amplían el recorrido; las formulaciones que exigieron corrección se reconstruyen con sus hipótesis precisas. La responsabilidad de estas intervenciones corresponde a esta edición.

Cada propiedad se presenta cerca de la definición y de los argumentos que la fundamentan. Los pasos difíciles reciben el espacio necesario para mostrar qué hay que construir y qué resultados permiten hacerlo; las construcciones alternativas se reúnen en los apéndices. Al final de cada capítulo, los ejercicios y sus resoluciones prolongan la investigación: conviene intentar cada problema antes de estudiar la solución y volver después sobre la elección que hizo funcionar su argumento.

La precisión empieza por declarar qué suponemos, qué queremos demostrar y qué permite pasar de una afirmación a la siguiente. Una desigualdad estricta o el orden de dos cuantificadores puede decidir la validez de toda una construcción. Nos detendremos en esas elecciones cuando permitan entender el mecanismo de una prueba, y recurriremos a ellas de nuevo cuando aparezcan en un problema más general.

Esta edición de estudio incorpora revisiones propias de la prosa, la pedagogía, la matemática intervenida y los formatos de lectura, realizadas en pasadas separadas. El cotejo audiovisual integral de las cuatro clases permanece abierto. Las ampliaciones se presentan con responsabilidad editorial propia y el expediente conserva las fuentes, incidencias y decisiones necesarias para continuar esa verificación.

Una vez que hayamos respondido por qué existe un cuerpo ordenado completo y en qué sentido es único, el símbolo $\mathbb R$ dejará de representar únicamente una recta conocida. Representará una construcción y una estructura demostradas. Ésa es la transición que propone este libro: pasar del uso de los reales a la comprensión de su necesidad matemática.

# El problema de definir un sistema numérico

Una fracción permite calcular y un punto dibujado permite orientarse. Para fundamentar esas acciones necesitamos precisar qué estructura sostiene las operaciones y las comparaciones. Buscamos un conjunto con dos operaciones, un orden compatible con ellas y una propiedad que permita recuperar la menor cota superior de los conjuntos adecuados. Esas tres exigencias darán contenido matemático al nombre de sistema real.

Los axiomas fijan las propiedades de la estructura buscada; los teoremas muestran sus consecuencias. Este reparto organiza la tarea: primero precisaremos las condiciones, después construiremos un objeto que las satisfaga y finalmente compararemos cualesquiera dos realizaciones mediante una correspondencia que preserve sus operaciones y su orden.

## El problema de definición

Para caracterizar un sistema numérico debemos especificar sus operaciones, las leyes que cumplen y las relaciones que enlazan sus elementos. En el caso real, la aritmética y el orden se reúnen con una propiedad de existencia de cotas mínimas. La formulación que concentra esas exigencias es la siguiente:

> Un sistema de números reales es un cuerpo ordenado que satisface la propiedad del supremo.
La descripción axiomática fija la estructura buscada. La existencia de un modelo y la unicidad hasta isomorfismo son dos teoremas con obligaciones propias: el primero exhibe un conjunto con operaciones y orden que cumplen los axiomas; el segundo construye una identificación entre dos realizaciones cualesquiera. En el capítulo siguiente partiremos de la aritmética racional para producir el modelo.

### Caracterización, existencia e identificación

La frase «los reales son un cuerpo ordenado completo» reúne **tres exigencias**: leyes para dos operaciones, una relación de orden compatible y existencia de supremos para los conjuntos apropiados. Cada exigencia se formula para un sistema todavía no identificado con un conjunto particular. Una vez precisados los axiomas, se distinguen dos obligaciones de naturaleza diferente: exhibir al menos una realización y demostrar que cualesquiera dos realizaciones están relacionadas por un único isomorfismo de cuerpos ordenados.

Esto impide utilizar en la prueba de existencia la recta real como objeto previamente disponible. En cambio, una vez construido un modelo, sí puede emplearse para ilustrar el comportamiento del supremo. El ejemplo con $\pi$ de la sección «Por qué los racionales no son completos» pertenece a este segundo plano.

## Estructura de cuerpo

Un cuerpo es un conjunto \(F\), equipado con operaciones \(+,·:F\times F\to F\), y elementos \(0,1\in F\), tales que, para cualesquiera \(a,b,c\in F\):

$$
(a+b)+c=a+(b+c),\qquad (ab)c=a(bc),
$$
$$
a+b=b+a,\qquad ab=ba,
$$
$$
a+0=a,\qquad a1=a,
$$
$$
\exists(-a)\in F:\ a+(-a)=0,
$$
$$
a\ne0\Longrightarrow\exists a^{-1}\in F:\ aa^{-1}=1,
$$
$$
a(b+c)=ab+ac.
$$

Exigimos además \(0\ne1\). Sin esta condición, el conjunto de un solo elemento satisface las otras fórmulas y no representa un cuerpo en el sentido requerido. La clausura está incluida en que las operaciones sean funciones \(F\times F\to F\). Esta condición distingue un cuerpo genuino de la estructura trivial y debe figurar expresamente entre sus axiomas.

La distributividad se escribe \(a(b+c)=ab+ac\). La presencia de los paréntesis es estructural: no puede sustituirse por \(ab+c\), que sería otra expresión.

### Consecuencias algebraicas

Derivemos ahora algunas consecuencias de los axiomas, sin utilizar propiedades de los números reales que todavía no hemos construido.

Los neutros son únicos. Si \(e\) es otro neutro aditivo, \(e=e+0=0\); si \(u\) es otro neutro multiplicativo, \(u=u1=1\). Si \(b,c\) son inversos aditivos de \(a\),

$$b=b+0=b+(a+c)=(b+a)+c=c.$$

Si \(a\ne0\) y \(ab=ac=1\), entonces

$$b=b(ac)=(ba)c=c.$$

Sumar \(-a\) a ambos miembros demuestra la cancelación aditiva; multiplicar por \(a^{-1}\) demuestra la multiplicativa cuando \(a\ne0\).

Por distributividad,

$$a0=a(0+0)=a0+a0,$$

y la cancelación aditiva da \(a0=0\). En consecuencia, cero no tiene inverso multiplicativo: \(0b=0\ne1\). Si \(ab=0\) y \(a\ne0\), al multiplicar por \(a^{-1}\) se obtiene \(b=0\); un cuerpo no tiene divisores de cero.

Asimismo,

$$a(-b)+ab=a((-b)+b)=0,$$

por lo que \(a(-b)=-(ab)\). Aplicando la igualdad con \(a=-1\), o de nuevo la unicidad del inverso aditivo, se obtiene \((-a)(-b)=ab\). Finalmente, \(-(-a)=a\). Definimos \(a-b=a+(-b)\) y, para \(b\ne0\), \(a/b=ab^{-1}\).

### Cancelación y dominio de las operaciones

La igualdad $a0=0$ no aparece entre los axiomas de cuerpo: se **deduce** usando la distributividad y la cancelación aditiva. Su prueba ilustra una técnica útil: escribir una expresión de dos formas, cancelar un término y recuperar la propiedad buscada. Aquí el paso decisivo es cancelar $a0$ en $a0=a0+a0$; no es lícito argumentar simplemente que «multiplicar por cero da cero», porque justamente se pretende fundamentar esa regla.

La definición de $a/b=ab^{-1}$ también contiene una condición de dominio: $b\ne0$. En particular, escribir $1/0$ no designa un elemento del cuerpo. El hecho de que $0$ carezca de inverso se deduce de $0b=0$ y $0\ne1$; no es una convención arbitraria.

## Orden total y cuerpo ordenado

Un orden total estricto en \(X\) es una relación \(<\) transitiva que satisface la tricotomía: para cada \(x,y\in X\), exactamente una de las proposiciones \(x<y\), \(x=y\), \(y<x\) es verdadera. Definimos

$$x\le y\iff x<y\ \text{o}\ x=y.$$
La tricotomía excluye \(x<x\) y que simultáneamente \(x<y\) e \(y<x\). La relación \(\le\) es reflexiva; es antisimétrica por tricotomía; y es transitiva al separar los casos de igualdad de aquel en que ambas desigualdades son estrictas.
La irreflexividad y transitividad caracterizan un orden parcial estricto; no obligan a que dos elementos diferentes sean comparables. Por ejemplo, en \(\mathcal P(\{1,2\})\) la inclusión estricta cumple esas propiedades, pero \(\{1\}\) y \(\{2\}\) son incomparables. Un orden total estricto agrega la comparabilidad de cada par distinto. La relación \(\le\) definida arriba es la versión no estricta, de modo que su antisimetría no significa que dos elementos distintos no puedan estar ordenados: significa que \(x\le y\) y \(y\le x\) implican \(x=y\). La diferencia con un orden parcial es, por tanto, la exigencia adicional de que cada par sea comparable.

Un cuerpo ordenado es un cuerpo con un orden total que satisface

$$x<y\Longrightarrow x+z<y+z,$$
$$x<y\ \text{y}\ 0<z\Longrightarrow xz<yz.$$

La condición \(0<z\) es indispensable. Admitir \(z=0\) daría \(0<0\). Si el factor fuese negativo el orden se invertiría, y si fuese cero la desigualdad estricta desaparecería.

**Prueba de necesidad.** Si \(1<2\) y tomamos \(z=0\), sus productos satisfacen \(1z=2z=0\), no \(1z<2z\). Si \(z=-1\), obtenemos \(-1>-2\): el sentido se invierte. La regla válida divide los casos \(z>0\), \(z=0\) y \(z<0\).

### Reglas de signo y desigualdades
La invariancia por traslación funciona en ambos sentidos: a una desigualdad trasladada se le suma \(-z\). Por tanto, \(x<y\iff0<y-x\). Si \(z>0\), multiplicar después por \(z^{-1}>0\) dará también la recíproca; primero justificamos su positividad.

Si \(a>0\), multiplicar \(0<a\) por \(a\) da \(0<a^2\). Si \(a<0\), entonces \(-a>0\), y \(a^2=(-a)^2>0\). Así, todo cuadrado no nulo es positivo. Puesto que \(1\ne0\) y \(1^2=1\), se sigue \(1>0\).

Si \(a>0\), su inverso es no nulo. Si fuese negativo, \(-a^{-1}>0\), y el producto de dos positivos daría \(a(-a^{-1})=-1>0\), contrario a \(1>0\). En efecto, tomar opuestos de la desigualdad que afirma que la unidad es positiva demuestra que su opuesto es negativo; no puede ser simultáneamente positivo. Luego \(a^{-1}>0\).

Si \(x<y\) y \(z<0\), entonces \(-z>0\), por lo que \(x(-z)<y(-z)\). Al cambiar signos mediante traslación se obtiene \(yz<xz\). Si \(z=0\), ambos productos son iguales. Estas tres posibilidades agotan la tricotomía. Las versiones con \(\le\) se deducen añadiendo el caso de igualdad.

En particular, \(2=1+1>0\), \(1/2>0\), y si \(u<v\),

$$u<\frac{u+v}{2}<v,$$

pues las diferencias respecto de los extremos son \((v-u)/2>0\). Este cálculo funciona en cualquier cuerpo ordenado y no utiliza completitud.

### El signo del factor

En la multiplicación de una desigualdad estricta hay que inspeccionar el **signo del factor** antes de operar. Con factor positivo se conserva $<$; con factor negativo se invierte; con factor nulo ambos productos son iguales. La sola hipótesis $x<y$ no determina la relación entre $xz$ y $yz$ cuando no se conoce el signo de $z$. Esta separación en tres casos no es una recomendación de cálculo: corresponde exactamente a la tricotomía del orden.

La totalidad del orden se expresa mediante la condición lógica $x<y\lor x=y\lor y<x$. Un dibujo puede representar una comparación concreta; la condición debe cumplirse para cada par de elementos del conjunto, con independencia de la representación elegida.

## Cotas superiores y supremos

Sea \(A\subseteq X\), donde \(X\) está totalmente ordenado. Un elemento \(u\in X\) es una cota superior de \(A\) si

$$\forall a\in A,\quad a\le u.$$

Un elemento \(s\in X\) es el supremo de \(A\) en \(X\) si es cota superior y es menor o igual que toda cota superior de \(A\). Se escribe \(s=\sup_X A\).
La segunda condición equivale a

$$\forall y\in X,\quad y<s\Longrightarrow\exists a\in A:\ y<a.$$

En efecto, si \(s\) es la menor cota superior y \(y<s\), \(y\) no puede ser cota superior; negar \(\forall a\in A:a\le y\) da, por tricotomía, un \(a\in A\) con \(y<a\). Recíprocamente, si esta condición se cumple y \(u\) es cota superior, no puede ocurrir \(u<s\), pues habría \(a\in A\) con \(u<a\). Por tricotomía, \(s\le u\).
\(y\) recorre el conjunto ambiente \(X\); no se restringe a \(A\). Se necesita \(y<a\), no meramente \(y\le a\). Esta precisión en el dominio del cuantificador es esencial para caracterizar el supremo.

**Por qué importa la desigualdad estricta.** Consideremos \(X=\mathbb Z\), \(A=\{1\}\) y la candidata \(s=2\). Es una cota superior, pero no el supremo (que es \(1\)). Sin embargo, si reemplazamos \(y<a\) por \(y\le a\), todo entero \(y<2\) satisface \(y\le1\). La versión debilitada aceptaría erróneamente \(s=2\).
El supremo es único: si \(s,t\) lo son, entonces \(s\le t\) y \(t\le s\), luego \(s=t\). Si \(s\in A\), es también el máximo. Recíprocamente, un máximo \(m\) es cota superior, y cualquier cota superior \(u\) cumple \(m\le u\) por pertenecer \(m\) a \(A\); luego \(m=\sup_X A\).

### El ejemplo finito
Para

$$A=\{1,2,3,4,5\}\subset\mathbb Z,$$

\(27\) es cota superior, puesto que todos los elementos de \(A\) son menores que \(27\). Su supremo en \(\mathbb Z\) es \(5\): es cota superior y pertenece a \(A\), por lo que es máximo y, en consecuencia, supremo. Alternativamente, para cada \(y\in\mathbb Z\) con \(y<5\), el testigo \(a=5\) pertenece a \(A\) y satisface \(y<a\). Este razonamiento incluye los enteros negativos y cero; no basta comprobar \(y=1,2,3,4\).

**Alcance de la caracterización.** La formulación del supremo como menor cota superior no necesita operaciones algebraicas. En cambio, la equivalencia con la condición «todo \(y<s\) es superado por un \(a\in A\)» utiliza totalidad. Para verlo, en el orden parcial \(X=\mathcal P(\{1,2\})\) por inclusión, el conjunto \(A=\{\{1\},\{2\}\}\) tiene supremo \(s=\{1,2\}\), pero si \(y=\{1\}\subsetneq s\), no existe \(a\in A\) con \(y\subsetneq a\). Por tanto, la caracterización empleada arriba no se extiende automáticamente a órdenes parciales.

### Lectura de los cuantificadores del supremo

La condición $\forall y\in X\,(y<s\Rightarrow\exists a\in A\;y<a)$ expresa que **ningún elemento del ambiente situado por debajo de $s$ sirve como cota superior**. El testigo $a$ puede depender de $y$; no se exige un mismo $a$ que supere simultáneamente todos los elementos inferiores a $s$.

¿Por qué es necesario $y\in X$? Sea $A=\{q\in\mathbb Q:0<q<1\}$ y tomemos la falsa candidata $s=2$. Todo $y\in A$ admite $a=(y+1)/2\in A$ con $y<a$. Así, si se restringiera erróneamente $y$ a $A$, la condición se cumpliría para $s=2$, que no es el supremo. La definición correcta detecta el fallo escogiendo, por ejemplo, $y=3/2\in\mathbb Q\setminus A$: ningún $a\in A$ lo supera.

Esta prueba de estrés muestra que **el conjunto ambiente es parte del enunciado**. Más adelante, cambiar el ambiente de $\mathbb Q$ a $\mathbb R$ cambiará la pregunta sobre el supremo, incluso cuando el subconjunto considerado conserve exactamente los mismos elementos.

## Cotas inferiores e ínfimos

Un elemento \(l\in X\) es cota inferior de \(A\) si \(l\le a\) para todo \(a\in A\). El ínfimo es la mayor de las cotas inferiores. Equivalentemente, \(t=\inf_X A\) si es cota inferior y

$$\forall y\in X,\quad t<y\Longrightarrow\exists a\in A:\ a<y.$$

Si \(t\) es la mayor cota inferior, cualquier \(y>t\) deja de ser cota inferior y existe tal \(a\). A la inversa, una cota inferior \(l>t\) contradiría la condición, al producir \(a<l\). La unicidad sigue de \(t\le t'\) y \(t'\le t\). Cuando el ínfimo pertenece al subconjunto, es su mínimo; el argumento es el dual de la prueba para máximos.

## Un supremo exterior al conjunto

Consideremos

$$A=\{q\in\mathbb Q:0<q<1\}.$$

El conjunto es no vacío, pues \(1/2\in A\), y \(1\) es una cota superior. Aunque \(1\notin A\), se tiene \(\sup_{\mathbb Q}A=1\).

Sea \(y\in\mathbb Q\), \(y<1\). Si \(y\le0\), tomamos \(a=1/2\); así \(a\in A\) y \(y<a\). Si \(0<y<1\), tomamos

$$a=\frac{1+y}{2}.$$

Es racional y

$$a-y=\frac{1-y}{2}>0,\qquad 1-a=\frac{1-y}{2}>0.$$

Por tanto, \(0<y<a<1\), y \(a\in A\). La caracterización del supremo concluye la prueba.

La separación del caso \(y\le0\) es necesaria para cubrir el cuantificador sobre todo \(\mathbb Q\). Para \(y\le-1\), el punto medio \((1+y)/2\) no pertenece a \(A\). Si \(y=p/q\), \(q\ne0\), la fórmula correctamente parentizada es

$$a=\frac12\left(1+\frac pq\right)=\frac{p+q}{2q}.$$

No se requiere la densidad de los racionales entre números reales para esta prueba: la clausura racional y las reglas de desigualdades bastan. El conjunto no tiene máximo, pues para cada \(q\in A\), \((1+q)/2\in A\) es mayor.
El supremo se calcula en el **ambiente** \(\mathbb Q\): \(1\) puede ser el menor de todos los racionales que acotan \(A\) aun sin pertenecer al intervalo. Esto distingue «máximo», que exige pertenencia al subconjunto, de «supremo», que no la exige. La existencia de este supremo particular no hace completo a \(\mathbb Q\).

### Variación del argumento del punto medio

Sean $\alpha,\beta\in\mathbb Q$ con $\alpha<\beta$ y

$$I_{\alpha,\beta}=\{q\in\mathbb Q:\alpha<q<\beta\}.$$

El razonamiento precedente demuestra también $\sup_{\mathbb Q}I_{\alpha,\beta}=\beta$. En efecto, $\beta$ es cota superior. Si $y<\beta$ y $y\le\alpha$, se toma $a=(\alpha+\beta)/2$; si $\alpha<y<\beta$, se toma $a=(y+\beta)/2$. En ambos casos $a\in I_{\alpha,\beta}$ y $y<a$. El método es general: cuando una fórmula de aproximación sólo sirve para una parte del dominio, se separan los casos hasta cubrir todo el cuantificador.

El extremo superior pertenece al ambiente racional pero no al intervalo. Por ello, la existencia del supremo no implica la existencia de un máximo.

## La propiedad del supremo

Un cuerpo ordenado \(F\) es completo si cada subconjunto \(A\subseteq F\), no vacío y acotado superiormente en \(F\), tiene supremo en \(F\).

Consideremos por qué ambas hipótesis son indispensables. El conjunto vacío tiene como cota superior a todo elemento, pero no tiene una menor cota superior en un cuerpo ordenado: si \(u\) fuese la menor, \(u-1<u\) también sería cota superior. El cuerpo entero \(F\) no está acotado superiormente, porque para cualquier \(u\in F\), \(u+1\in F\) es mayor. La completitud no garantiza supremos para ninguno de estos casos.

La propiedad del supremo puede formularse en cualquier conjunto ordenado. Por ejemplo, todo \(A\subseteq\mathbb Z\) no vacío y acotado superiormente tiene máximo. Dada una cota superior entera \(u\), el conjunto \(B=\{u-a:a\in A\}\subseteq\mathbb N_0\) es no vacío. Por buen orden, tiene mínimo \(b_0\); entonces \(u-b_0\in A\) es mayor o igual que cada elemento de \(A\) y constituye su supremo en \(\mathbb Z\). No obstante, \(\mathbb Z\) no es un cuerpo porque \(2\) carece de inverso multiplicativo entero. Lo que caracteriza a los reales es la **conjunción** de estructura de cuerpo, orden compatible y completitud de orden.

La completitud por supremos tampoco debe confundirse sin más con completitud de sucesiones de Cauchy. La equivalencia entre formulaciones requiere una estructura de proximidad y las hipótesis adecuadas; no se presupone aquí como resultado anterior.

La completitud proporciona también ínfimos de subconjuntos no vacíos acotados inferiormente. Si \(A\) es uno de ellos, entonces \(-A=\{-a:a\in A\}\) es no vacío y está acotado superiormente. Sea \(s=\sup(-A)\). De \(-a\le s\) se sigue \(-s\le a\). Para cualquier cota inferior \(l\) de \(A\), \(-l\) es cota superior de \(-A\), de modo que \(s\le-l\), es decir, \(l\le-s\). Luego

$$\inf A=-\sup(-A).$$

### El alcance de la propiedad del supremo

La propiedad del supremo asegura, para cada subconjunto con elementos y una cota superior, la existencia de un menor elemento entre todas sus cotas superiores dentro del ambiente. Su alcance es universal y comprende también los conjuntos cuyo supremo queda fuera de ellos. De hecho, $\mathbb Q$ contiene supremos como el del intervalo de la sección «Un supremo exterior al conjunto», pero basta encontrar **un solo** subconjunto racional no vacío y acotado superiormente sin supremo racional para demostrar que $\mathbb Q$ carece de completitud.

Las dos hipótesis del axioma, $A\ne\varnothing$ y «$A$ acotado superiormente», restringen su alcance. No afirman que el vacío o todo el cuerpo tengan supremo.

## Por qué los racionales no son completos

Consideremos el conjunto

$$A=\{q\in\mathbb Q:q<\pi\}.$$

**Hipótesis externas declaradas:** el ejemplo se interpreta en un sistema real ya disponible, con un elemento \(\pi\) que satisface \(0<\pi<4\) y \(\pi\notin\mathbb Q\). La densidad racional puede deducirse de la propiedad del supremo; más adelante se dará su demostración completa. La definición y la irracionalidad de \(\pi\) no se demostrarán aquí: son datos externos de este ejemplo. El ejemplo es una ilustración posterior a la existencia de un modelo, no una construcción de ese modelo. Su presentación matemática debe leerse, pues, como un análisis **condicional** dentro de una realización real disponible, mientras que la construcción de cortaduras que sigue demostrará la existencia sin depender de \(\pi\). Para evitar circularidad, la propiedad de densidad racional se deducirá previamente de la completitud de un cuerpo ordenado; no se utilizará como premisa para construir el cuerpo de cortaduras.

 \(A\) es no vacío, pues \(0\in A\), y está acotado superiormente en \(\mathbb Q\), pues \(4\) es cota superior. Sea \(s\in\mathbb Q\). Como \(s\ne\pi\), hay dos casos:

- Si \(s<\pi\), la densidad produce \(q\in\mathbb Q\) con \(s<q<\pi\). Entonces \(q\in A\), y \(s\) no es cota superior.
- Si \(\pi<s\), la densidad produce \(t\in\mathbb Q\) con \(\pi<t<s\). Para todo \(q\in A\), \(q<\pi<t\), de modo que \(t\) es una cota superior menor que \(s\). Así \(s\) no es la menor cota superior.

Ningún racional es supremo de \(A\) en \(\mathbb Q\). La mera afirmación \(\pi\notin\mathbb Q\) no habría excluido, por sí sola, otras candidatas.

En cambio, **el mismo conjunto de racionales**, considerado como subconjunto de \(\mathbb R\), tiene supremo \(\pi\). Es cota superior por definición. Si \(y\in\mathbb R\), \(y<\pi\), la densidad proporciona \(q\in\mathbb Q\) con \(y<q<\pi\), por lo que \(q\in A\). La caracterización del supremo da el resultado.

El conjunto \(A\) sigue formado exclusivamente por racionales al cambiar el ambiente de \(\mathbb Q\) a \(\mathbb R\). Esto importa: la expresión \(\mathbb Q\cap(-\infty,\pi)\) designa **el mismo subconjunto**, aunque ahora se lo considere dentro de un conjunto ambiente mayor. No lo sustituiremos por el conjunto de todos los reales menores que \(\pi\), que sería otro objeto.

Si se cambia además el conjunto a \(B=\{x\in\mathbb R:x<\pi\}\), también \(\sup_{\mathbb R}B=\pi\), pero la prueba puede usar directamente \(b=(y+\pi)/2\): para \(y<\pi\), se tiene \(y<b<\pi\). Es otro conjunto y conviene mantener explícita la diferencia.

### Un contraejemplo racional sin recurrir a $\pi$

El ejemplo anterior depende de hechos sobre $\pi$ que no estamos demostrando en este capítulo. Puede obtenerse, sin embargo, un contraejemplo **interno a la aritmética racional**.

**Proposición.** El conjunto

$$S=\{q\in\mathbb Q: q\ge0\text{ y }q^2<2\}$$

es no vacío y acotado superiormente en $\mathbb Q$, pero no admite supremo en $\mathbb Q$.

**Demostración.** Se tiene $1\in S$. Además, $2$ es una cota superior: si $q\ge2$, entonces $q^2\ge4>2$, por lo cual $q\notin S$.

En primer lugar, **ningún racional tiene cuadrado igual a $2$**. Si $(p/q)^2=2$ con $p,q\in\mathbb Z$, $q\ne0$ y la fracción reducida, entonces $p^2=2q^2$. De aquí $p$ es par; escribiendo $p=2k$ resulta $q^2=2k^2$, y $q$ también es par. Esto contradice que la fracción esté reducida.

Sea ahora $s\in\mathbb Q$. Si $s\le0$, no es cota superior porque $1\in S$. Supongamos $s>0$. Como $s^2\ne2$, debemos distinguir dos casos.

Si $s^2<2$, elijamos un racional $\delta>0$ tal que

$$\delta<1,\qquad\delta<\frac{2-s^2}{2s+1}.$$

Entonces $t=s+\delta$ es racional, $t>s$ y

$$t^2=s^2+2s\delta+\delta^2<s^2+(2s+1)\delta<2.$$

Por tanto $t\in S$ y $s$ no es cota superior.

Si $s^2>2$, elijamos un racional $\delta$ con

$$0<\delta<s,\qquad \delta<\frac{s^2-2}{2s}.$$

Poniendo $b=s-\delta$, se tiene $0<b<s$ y

$$b^2=s^2-2s\delta+\delta^2>s^2-2s\delta>2.$$

Para todo $q\in S$ necesariamente $q<b$: si $q\ge b>0$, entonces $q^2\ge b^2>2$, contradicción. Así $b$ es una cota superior racional estrictamente menor que $s$, de modo que $s$ no es la menor cota superior.

Se han descartado todos los candidatos racionales a supremo. En consecuencia, $S$ no tiene supremo en $\mathbb Q$. $\square$

La demostración no ha utilizado $\sqrt2$ como número real ya construido; sólo ha demostrado que ningún racional tiene cuadrado $2$ y ha perturbado racionalmente cada candidato $s$. La técnica reutilizable es doble: si el candidato queda por debajo del valor cuadrático buscado, se produce un elemento del conjunto mayor; si queda por encima, se produce una cota superior menor. La ventaja de este argumento es que demuestra la incompletitud racional sin presuponer un número irracional previamente construido.

## Existencia y unicidad

La caracterización axiomática nos ha dejado dos obligaciones: construir al menos un cuerpo ordenado completo y demostrar que dos cualesquiera son isomorfos. Los siguientes capítulos satisfacen ambas, en ese orden.
En los capítulos siguientes demostraremos:

1. Existe un cuerpo ordenado completo, construido como un conjunto de cortaduras racionales.
2. Para dos cuerpos ordenados completos \(F,G\), existe un único isomorfismo de cuerpos ordenados \(F\to G\).

Podemos pensar en dos tableros de ajedrez fabricados con materiales diferentes: las piezas no son idénticas como objetos, pero las reglas del juego establecen correspondencias entre sus movimientos. La comparación es ilustrativa; en matemáticas debemos construir la función que preserve todas las operaciones y el orden y probar sus propiedades.

Las actividades propuestas permiten comprobar la comprensión de la lógica de cada definición y de las pruebas obtenidas.

## Problemas y soluciones del capítulo

### Ejercicio 1

Explica por qué la división usual $a/b$ (con $b\ne0$) no es una operación binaria $\mathbb Z\times\mathbb Z\to\mathbb Z$. Indica qué exige que una ley sea una operación *bien definida* sobre un conjunto.

**Solución razonada.** Una operación binaria sobre $\mathbb Z$ debe asignar a **cada** par de enteros una salida entera. La regla de división con denominador no nulo falla dos veces como aplicación $\mathbb Z\times\mathbb Z\to\mathbb Z$: no está definida para pares $(a,0)$ y, aun si restringimos el segundo componente a los enteros no nulos, $1/2$ no pertenece a $\mathbb Z$. En cambio, multiplicación y suma sí asignan enteros a todos los pares de enteros.

Para decir que una operación está bien definida hay que fijar su dominio y codominio, demostrar que produce una salida en el codominio para **todo** elemento del dominio y que la salida no cambia cuando un objeto tiene dos representaciones distintas. En la construcción de la copia racional de un cuerpo ordenado, ese último control será esencial: dos fracciones que representen el mismo racional deberán producir exactamente la misma imagen.

### Ejercicio 2

En un cuerpo $F$, demuestra a partir de los axiomas que $a0=0$ para todo $a\in F$. Deduce que $0$ no tiene inverso multiplicativo.

**Solución razonada.** La distributividad proporciona $a0=a(0+0)=a0+a0$. Sumando el inverso aditivo de $a0$ a ambos lados, la asociatividad permite cancelar la misma expresión y obtener $0=a0$. Si $0$ tuviera inverso multiplicativo $b$, se cumpliría $0b=1$. Pero acabamos de demostrar $0b=0$, con lo que $0=1$, contrario al axioma de cuerpo. Es importante que el argumento empiece con una ley *postulada* (distributividad) y termine con una consecuencia *derivada* (producto por cero).

### Ejercicio 3

Supón que se eliminara de los axiomas de cuerpo la exigencia $0\ne1$. Demuestra que en una estructura que satisface los demás axiomas, si $0=1$ entonces todo elemento es cero. Explica por qué dicha exigencia es indispensable.

**Solución razonada.** Supongamos $0=1$. Para cualquier $a$ en la estructura, el neutro multiplicativo da $a=a1=a0$. La demostración del ejercicio 2 utiliza sólo distributividad e inversos aditivos, de modo que sigue siendo válida aun sin exigir $0\ne1$: $a0=0$. Por tanto $a=0$ para todo $a$. La estructura sólo puede tener un elemento. La condición $0\ne1$ excluye este caso degenerado; no se deduce de las demás identidades.

### Ejercicio 4

Sean $x<y$ en un cuerpo ordenado. Determina la relación entre $xz$ y $yz$ si (a) $z>0$, (b) $z=0$, (c) $z<0$. Justifica cada caso a partir de los axiomas.

**Solución razonada.** (a) Para $z>0$, el axioma de compatibilidad multiplicativa da directamente $xz<yz$. (b) Para $z=0$, el ejercicio 2 da $xz=yz=0$; una desigualdad estricta es imposible. (c) Para $z<0$, se tiene $-z>0$, por lo cual $x(-z)<y(-z)$. Multiplicando por $-1$ las dos expresiones en la igualdad algebraica de signos —o sumando sus opuestos— se obtiene $yz<xz$. Estos son todos los casos por tricotomía. La división por $z$ exige además que $z\ne0$; si $z<0$, también invierte la desigualdad.

### Ejercicio 5

En $X=\mathcal P(\{1,2\})$ ordenado por inclusión, considera $A=\{\{1\},\{2\}\}$. Determina su supremo y demuestra por qué la caracterización mediante $y<s\Rightarrow\exists a\in A\;(y<a)$ no puede trasladarse sin más a este orden parcial.

**Solución razonada.** Una cota superior de $A$ en el orden de inclusión debe contener simultáneamente $\{1\}$ y $\{2\}$. La única que lo hace dentro de $X$ es $s=\{1,2\}$, luego es el supremo. Tomemos $y=\{1\}\subsetneq s$. Ningún miembro de $A$ contiene *estrictamente* a $y$: uno es igual a $y$ y el otro es incomparable con él. Por tanto falla la condición $y<s\Rightarrow\exists a\in A\;(y<a)$. No contradice la definición de supremo: la equivalencia con esa caracterización se demostró utilizando tricotomía, que el orden parcial no satisface.

### Ejercicio 6

Sea $A=\{q\in\mathbb Q:0<q<1\}$ y la candidata $s=2$. Demuestra que si en la caracterización del supremo se reemplaza $\forall y\in\mathbb Q$ por $\forall y\in A$, $s$ satisface erróneamente la condición resultante. Encuentra un $y\in\mathbb Q\setminus A$ que muestre el fallo.

**Solución razonada.** Para cada $y\in A$, el racional $a=(y+1)/2$ cumple $y<a<1$, por lo que $a\in A$. Así, con el dominio incorrecto $y\in A$, la condición de aproximación se cumple para $s=2$: todos los elementos de $A$ están por debajo de $2$ y cada uno tiene sucesor mayor dentro de $A$. Sin embargo, $2$ no es la menor cota superior, porque $1$ ya acota $A$. La definición correcta toma **todos** los $y\in\mathbb Q$ inferiores a la candidata. Por ejemplo, $y=3/2<2$ y ningún $a\in A$ satisface $3/2<a$. La candidata queda descartada.

### Ejercicio 7

En $X=\mathbb Z$ considera $A=\{1\}$ y $s=2$. Comprueba que $s$ es cota superior y que para todo entero $y<s$ existe $a\in A$ con $y\le a$. ¿Por qué esto no implica $s=\sup_X A$? Escribe la desigualdad que falta.

**Solución razonada.** $s=2$ es cota superior de $A=\{1\}$, pues $1\le2$. Si $y\in\mathbb Z$ y $y<2$, entonces $y\le1$, de modo que el único $a=1\in A$ verifica $y\le a$. Con la desigualdad débil, la condición no descarta $s=2$. El supremo verdadero es $1$, que pertenece a $A$ y es máximo. La caracterización válida exige $y<a$, no $y\le a$: tomando $y=1<2$ no existe $a\in A$ con $1<a$. De este modo se recupera el carácter *mínimo* de la cota superior.

### Ejercicio 8

Para $A=\{-3,0,4\}\subseteq\mathbb Z$, determina el máximo, mínimo, supremo e ínfimo y demuestra las afirmaciones usando las definiciones, no la posición de los números en una recta.

**Solución razonada.** La comparación de los tres enteros muestra que $-3\le0\le4$. Como $4\in A$ y todo $a\in A$ satisface $a\le4$, el entero $4$ es un máximo. Toda cota superior $u$ de $A$ debe satisfacer $4\le u$, pues $4\in A$. Luego $\sup_{\mathbb Z}A=\max A=4$. Del mismo modo, $-3$ pertenece al conjunto y es menor o igual que todos sus elementos, por lo que es un mínimo; cualquier cota inferior $l$ satisface $l\le-3$. Así $\inf_{\mathbb Z}A=\min A=-3$. La demostración utiliza pertenencia y desigualdades, no una figura de recta.

### Ejercicio 9

Sean $\alpha,\beta\in\mathbb Q$ y $\alpha<\beta$. Prueba que el intervalo racional abierto $I=\{q\in\mathbb Q:\alpha<q<\beta\}$ tiene supremo $\beta$ e ínfimo $\alpha$, pero no tiene máximo ni mínimo.

**Solución razonada.** $I$ no está vacío, porque $m=(\alpha+\beta)/2$ es racional y $\alpha<m<\beta$. Todo elemento de $I$ es menor que $\beta$, por lo que $\beta$ es cota superior. Si $y<\beta$ y $y\le\alpha$, el testigo $a=m$ cumple $a\in I$ y $y<a$. Si $\alpha<y<\beta$, usamos $a=(y+\beta)/2\in I$, con $y<a$. La caracterización del supremo da $\sup_{\mathbb Q}I=\beta$. Aplicando el razonamiento dual (o sustituyendo $q$ por $-q$) se obtiene $\inf_{\mathbb Q}I=\alpha$. Finalmente, dado $q\in I$, $(q+\beta)/2$ es otro elemento de $I$ mayor que $q$, y $(\alpha+q)/2$ es uno menor. Ningún elemento puede ser máximo ni mínimo.

### Ejercicio 10

Si $s=\sup_F A$ existe en un cuerpo ordenado $F$ y $t\in F$, prueba que $\sup_F(A+t)=s+t$, donde $A+t=\{a+t:a\in A\}$.

**Solución razonada.** $s+t$ es cota superior de $A+t$: si $a\le s$, el axioma de traslación da $a+t\le s+t$. Sea $u$ otra cota superior de $A+t$. De $a+t\le u$ para todo $a\in A$, restamos $t$ y obtenemos $a\le u-t$; luego $u-t$ es cota superior de $A$. Por la minimalidad de $s$, $s\le u-t$. Sumando $t$ se obtiene $s+t\le u$. Así $s+t$ es la menor cota superior. No se ha utilizado completitud para demostrar esta regla: basta suponer que $s$ ya existe.

### Ejercicio 11

Si $s=\sup_F A$ y $z>0$, prueba que $\sup_F(zA)=zs$. ¿Qué ocurre cuando $z<0$? Expresa el resultado mediante $\inf_F A$ cuando éste existe. Explica por qué $z=0$ no sirve para conservar desigualdades estrictas.

**Solución razonada.** Para $z>0$, todo $a\in A$ cumple $za\le zs$, por lo que $zs$ es cota superior de $zA$. Si $u$ es otra cota superior, $za\le u$ para todo $a\in A$. Como $z^{-1}>0$, multiplicar por $z^{-1}$ conserva el orden: $a\le u/z$. Por tanto $s\le u/z$ y $zs\le u$. Así $\sup_F(zA)=zs$.

Si $z<0$ y existe $m=\inf_FA$, para cada $a\in A$ la desigualdad $m\le a$ se invierte al multiplicar por $z$, dando $za\le zm$; toda otra cota superior $u$ de $zA$ induce una cota inferior $u/z$ de $A$ (la división por un negativo invierte), luego $u/z\le m$, es decir $zm\le u$. En consecuencia, $\sup_F(zA)=z\inf_FA$. Si $z=0$ y $A\ne\varnothing$, $zA=\{0\}$ y su supremo es $0$, pero ninguna desigualdad estricta entre productos subsiste; el argumento de multiplicación por inversos no puede aplicarse a $z=0$.

### Ejercicio 12

Demuestra que el conjunto vacío no tiene supremo en un cuerpo ordenado y que el cuerpo completo tampoco está acotado superiormente. Relaciona los dos ejemplos con las hipótesis del axioma del supremo.

**Solución razonada.** Todo elemento $u\in F$ es cota superior del vacío, porque la afirmación $\forall a\in\varnothing\;(a\le u)$ es vacuamente verdadera. Si existiera la *menor* de estas cotas, digamos $s$, también $s-1$ sería cota superior y $s-1<s$, contradicción. Por otra parte, $F$ no está acotado superiormente: dado cualquier supuesto límite superior $u$, el elemento $u+1\in F$ satisface $u<u+1$ porque $1>0$. El axioma del supremo exige simultáneamente que el conjunto sea no vacío y tenga cota superior. No afirma la existencia de supremo en ninguno de los dos casos examinados.

### Ejercicio 13

Si $F$ es un cuerpo ordenado completo y $A\subseteq F$ es no vacío y acotado inferiormente, demuestra que $\inf_F A=-\sup_F(-A)$. Identifica en qué paso se usa la completitud.

**Solución razonada.** Como $A$ es no vacío y acotado inferiormente, $-A=\{-a:a\in A\}$ es no vacío y está acotado superiormente; la completitud se usa **ahora** para asegurar que $s=\sup_F(-A)$ existe. Para cada $a\in A$ se cumple $-a\le s$, luego $-s\le a$ al cambiar signos: $-s$ es cota inferior de $A$. Si $l$ es cualquier otra cota inferior, $l\le a$ para todo $a\in A$ implica $-a\le-l$ para todo $a\in A$, de modo que $-l$ es cota superior de $-A$. Por la minimalidad de $s$, $s\le-l$, de donde $l\le-s$. Así $-s$ es la mayor cota inferior: $\inf_FA=-\sup_F(-A)$.

### Ejercicio 14

Sea $c\in\mathbb Q$, $c>0$, y supón que $c$ no es el cuadrado de ningún racional. Prueba directamente que $S_c=\{q\in\mathbb Q:q\ge0,\ q^2<c\}$ no tiene supremo racional. No presupongas la existencia de $\sqrt c$ como real. Elige después $c=3$ como caso concreto.

**Solución razonada.** $S_c$ contiene $0$ y es acotado superiormente; por ejemplo, el racional $M=c+1$ sirve, porque $M>0$ y $M^2=c^2+2c+1>c$, y todo racional $q\ge M$ cumple $q^2\ge M^2>c$.

Sea $s\in\mathbb Q$ candidato. Si $s<0$, $0\in S_c$ lo descarta; si $s=0$, se elige un racional positivo $q<\min(1,c/(1+c))$, que satisface $q^2<q<c$ cuando $q<1$ (y por tanto $q\in S_c$), de modo que $s=0$ tampoco es cota superior. Para $s>0$, la hipótesis asegura $s^2\ne c$.

Si $s^2<c$, tomamos un racional $0<\delta<\min\{1,(c-s^2)/(2s+1)\}$. Entonces $t=s+\delta>s$ y $t^2<s^2+(2s+1)\delta<c$, así $t\in S_c$: $s$ no es cota superior. Si $s^2>c$, tomamos $0<\delta<\min\{s,(s^2-c)/(2s)\}$. Para $b=s-\delta>0$ se tiene $b^2>s^2-2s\delta>c$. Todo elemento no negativo $q$ con $q^2<c$ debe satisfacer $q<b$, pues lo contrario implicaría $q^2\ge b^2>c$. Así $b$ es una cota superior menor que $s$. Ningún racional es supremo de $S_c$.

Para $c=3$ las hipótesis se verifican porque $3$ no es cuadrado de racional alguno. En efecto, si $(p/q)^2=3$ con $p,q$ enteros coprimos y $q\ne0$, entonces $p^2=3q^2$. Un cuadrado de entero deja resto $0$ o $1$ al dividir por $3$; por ello, de $3\mid p^2$ se sigue $3\mid p$. Escribiendo $p=3k$ se deduce $q^2=3k^2$, de modo que $3\mid q$, contradicción con la coprimalidad. No hemos usado $\sqrt3$ como elemento de un cuerpo real ya existente.

**Orientación para los ejercicios 15–18.** Hasta aquí hemos estudiado los axiomas y sus consecuencias, pero todavía no hemos construido el cuerpo de cortaduras. Los cuatro ejercicios finales anticipan nociones que desarrollaremos en el capítulo siguiente y en los apéndices. No son prerrequisitos para iniciar el capítulo II. Quien prefiera una lectura estrictamente deductiva puede resolver los ejercicios 15 y 17 después de estudiar las cortaduras y la propiedad del supremo por unión; el 16, después del apéndice sobre recintos; y el 18, después del capítulo de unicidad. Las soluciones se conservan aquí completas, para que el lector pueda utilizarlas también como una primera exploración.

Para poder abordar ahora esos problemas, adelantemos **solo las definiciones**, no las propiedades que todavía tendremos que demostrar. Una *cortadura inferior* es un conjunto de racionales no vacío y distinto de todos los racionales, cerrado hacia abajo y sin elemento máximo. La *cortadura principal* de un racional $r$ es $C_r=\{q\in\mathbb Q:q<r\}$. Denotaremos por $D$ el conjunto de todas las cortaduras y lo ordenaremos por inclusión. Un par racional $[\ell,u]$, con $\ell<u$, es un *recinto* de una cortadura $A$ si $C_\ell\subseteq A\subseteq C_u$; será un *intervalo admisible* de $A$ si $\ell\in A$ y $u\notin A$. La distinción entre recinto y admisibilidad se demostrará y utilizará cuidadosamente en el primer apéndice. Aquí no damos por construidas las operaciones sobre cortaduras ni la completitud de $D$: son precisamente resultados que se justificarán más adelante.

### Ejercicio 15

Para $r\in\mathbb Q$, sea $C_r=\{q\in\mathbb Q:q<r\}$. Verifica que $C_r$ es una cortadura y demuestra $C_r\subsetneq C_s\iff r<s$.

**Solución razonada.** $C_r$ es no vacía porque $r-1\in C_r$, y propia porque $r\notin C_r$. Si $q\in C_r$ y $p<q$, entonces $p<r$, de modo que $p\in C_r$. Si $q\in C_r$, el punto medio $q'=(q+r)/2$ cumple $q<q'<r$, por lo que $q'\in C_r$; no hay máximo. Para el orden, si $r<s$, todo racional menor que $r$ es menor que $s$, así $C_r\subseteq C_s$; además, $r\in C_s\setminus C_r$, luego la inclusión es estricta. Recíprocamente, si $C_r\subsetneq C_s$ y $s\le r$, tendríamos $C_s\subseteq C_r$, contradicción. Por tricotomía debe ser $r<s$.

### Ejercicio 16

Para $H=C_0$, demuestra que $[0,1]$ es un *recinto* en el sentido de la definición de las cortaduras, pero no un intervalo admisible. Transfórmalo en uno admisible mediante un ensanchamiento racional. Explica por qué la distinción importa al definir la suma de cortaduras.

**Solución razonada.** Para $H=C_0$, se cumple $C_0\subseteq H\subseteq C_1$, así $[0,1]$ es un recinto. Pero $0\notin C_0$, de modo que su extremo inferior no pertenece a $H$: el intervalo no es admisible. Si $\eta>0$ es racional, $[-\eta,1+\eta]$ sí es admisible: $-\eta<0$, por lo que $-\eta\in C_0$, mientras que $1+\eta>0$, de modo que $1+\eta\notin C_0$. Las operaciones de la construcción mediante recintos se definen usando extremos admisibles; aplicar una fórmula de suma o producto directamente a un recinto arbitrario puede emplear datos que no satisfacen las hipótesis de esa definición. Por esta razón, en la construcción alternativa por recintos se ensancha primero el intervalo hasta hacerlo admisible, antes de introducir sus extremos en las operaciones.

### Ejercicio 17

Sea $\mathcal A=\{C_r:r\in\mathbb Q,\ r<1\}$, una familia de cortaduras. Prueba directamente que $\bigcup\mathcal A=C_1$ y deduce $\sup_D\mathcal A=C_1$ en el conjunto ordenado $D$ de cortaduras.

**Solución razonada.** Sea $U=\bigcup_{r<1}C_r$. Si $t\in U$, existe $r\in\mathbb Q$ con $r<1$ y $t<r$. Por transitividad, $t<1$, luego $t\in C_1$. En sentido contrario, dado $t<1$, el racional $r=(t+1)/2$ cumple $t<r<1$, así $t\in C_r\subseteq U$. Por doble inclusión $U=C_1$. Cada $C_r$ de la familia está contenido en $C_1$, y si $T$ es otra cortadura que contiene a todos los $C_r$, contiene también su unión $C_1$. Por tanto $C_1=\sup_D\mathcal A$. Se ha usado el orden por inclusión, no un cálculo con límites reales.

### Ejercicio 18 — Para retomar después del capítulo de unicidad

Este ejercicio anticipa un resultado que todavía no hemos demostrado. Conviene volver a él después del tercer capítulo, cuando dispongamos de la construcción por supremos y del teorema de unicidad.

Sean $F,G$ cuerpos ordenados completos y $\varphi:F\to G$ el isomorfismo construido en las etapas de la prueba de unicidad. Explica por qué cualquier isomorfismo de cuerpos ordenados $\theta:F\to G$ coincide con $\varphi$. Escribe explícitamente qué se conserva en los racionales y por qué sus conjuntos de racionales inferiores determinan cada elemento.


**Solución razonada.** Sea $\theta:F\to G$ un isomorfismo de cuerpos ordenados. Por conservar el neutro multiplicativo y ambas operaciones, fija las copias de $1$, de los naturales (sumas repetidas de $1$), de los enteros (opuestos) y de los racionales (inversos de enteros no nulos). Por tanto $\theta(q_F)=q_G$ para cada $q\in\mathbb Q$. Además, como preserva y refleja el orden,

$$q_G<\theta(x)\iff\theta(q_F)<\theta(x)\iff q_F<x.$$

La construcción del isomorfismo mediante $\varphi$ establece precisamente $q_G<\varphi(x)\iff q_F<x$. Luego $\theta(x)$ y $\varphi(x)$ tienen los mismos racionales estrictamente inferiores. Si fueran distintos, la densidad racional en $G$ produciría un racional situado estrictamente entre ambos, perteneciente a uno de esos conjuntos inferiores y no al otro. Es imposible. Así $\theta(x)=\varphi(x)$ para todo $x\in F$. La unicidad no significa que los cuerpos tengan los mismos elementos como conjuntos, sino que hay una sola correspondencia que conserva su estructura de cuerpo ordenado.


# Construir un modelo a partir de los racionales

La aritmética racional ofrece un punto de partida concreto: $\mathbb Q$, con sus cuatro operaciones habituales y su orden. El conjunto de racionales no negativos cuyo cuadrado es menor que dos ya nos mostró una dificultad: su menor cota superior tendría que ocupar una posición que ninguna fracción representa. Vamos a describir esa posición mediante información racional y a construir, con el mismo procedimiento, todo un cuerpo ordenado completo.

Utilizaremos **cortaduras inferiores**: conjuntos de racionales que reúnen toda la información situada bajo una posición. La pertenencia a uno de esos conjuntos se decide mediante propiedades racionales; a partir de ella definiremos el orden y las operaciones. Al construir la suma, el opuesto y el producto tendremos que comprobar que sus resultados siguen perteneciendo a la misma familia y que cumplen las leyes exigidas a un cuerpo.

En las verificaciones extensas conviene seguir una misma pregunta: qué propiedad del objeto nuevo permite recuperar la regla de cálculo conocida. El cierre descendente permitirá reajustar testigos; la posibilidad de encontrar un elemento mayor dentro de cada corte dará margen para las desigualdades estrictas; la aproximación racional finita proporcionará los opuestos y los recíprocos.

Nos bastará la propiedad arquimediana de la aritmética racional, que se demuestra sin apelar a los reales. Si $p/q>0$ con $p,q$ enteros positivos, entonces $p/q\le p$ y existe un entero mayor que esa fracción. También podemos encontrar racionales positivos tan pequeños como se quiera: se tiene $1/n< p/q$ cuando $np>q$. Éstos son los instrumentos aritméticos con los que reduciremos las anchuras de nuestros intervalos. Una sucesión de intervalos puede sugerir una convergencia, pero la prueba que utilizaremos se detiene siempre después de un número finito de pasos calculado para la tolerancia elegida.

## De una definición a un problema de existencia

La imagen de una recta separada en dos partes sugiere reunir en un conjunto toda la información inferior. Para convertirla en una construcción necesitamos condiciones de pertenencia que se expresen enteramente con racionales. Esas condiciones serán las que utilicemos después en las pruebas.

La definición del capítulo anterior fija las condiciones de llegada. El problema de existencia consiste en elegir objetos y operaciones que permitan verificar cada una de ellas. La elección de los racionales como material inicial pone a nuestra disposición cálculos exactos y un orden total; la nueva construcción deberá proporcionar además la propiedad del supremo.

Ya contamos con un cuerpo ordenado conocido: los racionales. Su aritmética está disponible y sus elementos se comparan entre sí. El problema es la completitud. Una descripción intuitiva habla de huecos en la recta racional; el trabajo formal debe reemplazar esa imagen por objetos cuya existencia y propiedades podamos justificar sin recurrir a los reales.

Adoptamos $\mathbb Q$ como punto de partida y presuponemos su aritmética, el buen orden de los naturales y la teoría elemental de conjuntos. La construcción de naturales, enteros y racionales pertenece a una etapa fundacional anterior. Con esas herramientas examinaremos qué información necesita un número nuevo y cómo operar con ella.

La estrategia consiste en cambiar el tipo de objeto que llamaremos número. En vez de buscar una fracción que ocupe cada hueco, utilizaremos un conjunto de fracciones para describir una posición. Luego definiremos suma, producto y orden entre esos conjuntos.

## Cortaduras: información suficiente para identificar una posición

La primera operación que investigaremos será comparar estos conjuntos. El cierre descendente resultará decisivo para probar que dos cortaduras cualesquiera se ordenan por inclusión.

Una cortadura de Dedekind es un subconjunto $A$ de $\mathbb Q$ con un elemento interior y un elemento exterior, cerrado hacia abajo y con la propiedad de que cada uno de sus elementos es superado por otro elemento del mismo conjunto. El cierre hacia abajo significa que, junto con una fracción, el conjunto contiene todas las fracciones menores. La última propiedad proporciona margen para aumentar un testigo permaneciendo dentro de la cortadura.

El elemento interior proporciona información inferior y el exterior asegura que esa información está acotada en el orden racional. El cierre descendente reúne todas las fracciones menores que las ya admitidas. La posibilidad de aumentar cada elemento fija una convención uniforme para la frontera y hará posible transformar representaciones exactas en testigos estrictos.

Para un racional conocido, por ejemplo $2$, podemos formar

$$C_2=\{q\in\mathbb Q:q<2\}.$$

Este conjunto tiene una frontera racional, pero no incluye el propio $2$. Si $q<2$, el punto medio $(q+2)/2$ sigue siendo racional, está por encima de $q$ y queda por debajo de $2$. Por eso no hay un último elemento de $C_2$.

El dibujo de una recta partida en dos ayuda a comprender la intención. Sin embargo, si escribimos $\{q\in\mathbb Q:q<x\}$ con un real arbitrario $x$ para definir todas las cortaduras, ya estamos suponiendo el objeto que queremos construir. Conviene distinguir expresamente esa imagen intuitiva de la definición mediante propiedades de subconjuntos racionales.
Consideremos ahora $\{q\in\mathbb Q:q^2<2\}$ como ejemplo asociado a la raíz de dos. Esa expresión no satisface la definición: contiene $0$, pero no contiene $-2$, aunque $-2<0$. La reparación es incluir todo el lado negativo:

$$H=\{q\in\mathbb Q:q<0\ \text{o}\ q^2<2\}.$$

En la parte no negativa, elevar al cuadrado conserva el orden; por eso el segundo criterio describe correctamente la porción situada bajo la frontera buscada. En la parte negativa, usar sólo el cuadrado recortaría también el extremo izquierdo, justamente lo que una cortadura descendente no puede hacer.

No necesitamos conocer previamente $\sqrt2$ para definir $H$: sólo intervienen racionales, el orden y el número $2$. Más adelante comprobaremos que este conjunto satisface los cuatro axiomas de cortadura; cuando el producto esté construido, demostraremos además que $H^2=C_2$. Es entonces cuando podemos interpretar $H$ como una raíz cuadrada positiva.

### Cortaduras y separación de sus lados

Una cortadura es un conjunto $A\subseteq\mathbb Q$ tal que:

$$A\ne\varnothing,\quad A\ne\mathbb Q,$$
$$\forall r\in A\ \forall s\in\mathbb Q\quad(s<r\Rightarrow s\in A),$$
$$\forall r\in A\ \exists s\in A\quad r<s.$$

Denotamos por $D$ el conjunto de todas las cortaduras. Si $a\in A$ y $b\in\mathbb Q\setminus A$, necesariamente $a<b$: la igualdad contradice las pertenencias; si $b<a$, el cierre descendente obligaría a $b\in A$. En particular, todo racional exterior es una cota superior racional de $A$.

Para $r\in\mathbb Q$, ponemos

$$C_r=\{q\in\mathbb Q:q<r\}.$$

Es no vacío porque contiene $r-1$, propio porque no contiene $r$, descendente por transitividad y sin máximo porque $(q+r)/2$ pertenece a $C_r$ y supera a cualquier $q\in C_r$. Así $D$ existe como subconjunto no vacío de $\mathcal P(\mathbb Q)$.

Una descripción $A=\{q:q<x\}$ con un real preexistente $x$ no forma parte de esta definición. Será una interpretación legítima después de construir un modelo, o una representación dentro de otro cuerpo ordenado completo en el isomorfismo con las cortaduras.

### El ejemplo cuadrático corregido y una cortadura no racional

El primer conjunto que podríamos considerar,

$$T=\{q\in\mathbb Q:q^2<2\},$$

no es descendente: $0\in T$, $-2<0$ y $-2\notin T$. La corrección es

$$H=\{q\in\mathbb Q:q<0\ \text{o}\ q^2<2\}.$$

Contiene todos los negativos y es propio porque $2\notin H$. Si $r\in H$ y $s<r$, cuando $s<0$ ya pertenece; si $s\ge0$, también $r>0$ y $s^2<r^2<2$. El cierre descendente queda probado sin multiplicar desigualdades por negativos.

Si $r<0$, el racional $0$ pertenece a $H$ y lo supera. Si $r\ge0$ pertenece a $H$, elegimos

$$\delta=\min\left(1,\frac{2-r^2}{2(2r+1)}\right)>0.$$

Como $\delta\le1$,

$$(r+\delta)^2\le r^2+\delta(2r+1)\le r^2+\frac{2-r^2}{2}<2.$$

Por tanto $r+\delta\in H$ y no hay máximo. Esto prueba que $H\in D$.

La comprobación siguiente de $H^2=C_2$ utiliza el producto positivo, el refinamiento racional y la compatibilidad de la inclusión racional con el producto, desarrollados más adelante en este capítulo. Puede leerse al concluir esas construcciones. Para testigos positivos $a,b\in H$, $(ab)^2=a^2b^2<4$; como $ab>0$, esto fuerza $ab<2$. Luego $H\odot H\subseteq C_2$. A la inversa, para $0\le q<2$ refinamos el par admisible $[1,2]$ de $H$ con anchura menor que $(2-q)/8$. Obtenemos $1\le a<p\le2$, $a\in H$, $p\notin H$, por lo que $p^2\ge2$. Entonces

$$p^2-a^2=(p-a)(p+a)<4\frac{2-q}{8}=\frac{2-q}{2},$$

$$a^2>2-\frac{2-q}{2}>q.$$

Los testigos $a,a$ colocan $q$ en $H\odot H$. Los negativos están incluidos por definición. La cortadura $H$ es positiva, y ahora —sólo después de esta prueba— podemos llamarla $\sqrt{C_2}$ o $\sqrt2$ en el modelo construido.

No coincide con ninguna $C_r$. Si lo hiciera, la preservación del producto daría $C_{r^2}=C_2$, y la inyectividad de $\iota$ daría $r^2=2$. Pero no existe tal racional: escribir $r=m/n$ en términos reducidos con $n>0$ conduce a $m^2=2n^2$; $m$ es par, digamos $m=2k$, y entonces $n^2=2k^2$ fuerza a $n$ par, contradiciendo que la fracción esté reducida. Se usa el hecho elemental de que el cuadrado de un entero impar es impar, deducido de $(2k+1)^2=2(2k^2+2k)+1$.

Así la inclusión racional no es sobreyectiva. No se usó una raíz real preexistente para rellenar el hueco: se construyó un conjunto racional que, mediante las operaciones probadas, desempeña ese papel.

Aquí aparece el primero de los grandes cambios de perspectiva: una frontera que no podemos nombrar mediante un racional puede, sin embargo, quedar perfectamente determinada por los racionales que caen bajo ella. El ejemplo cuadrático muestra además por qué las condiciones de la definición no son ornamentales: omitir todos los negativos destruiría el cierre descendente. La construcción gana rigor precisamente cuando dejamos de confiar en la imagen de una recta y examinamos qué pertenece al conjunto.

## Ordenar conjuntos por inclusión

La inclusión de racionales en la estructura nueva exige distinguir dos niveles: la fracción original y el conjunto que la representa. La compatibilidad de las operaciones se demostrará, no se supondrá.

Sea $D$ el conjunto de todas las cortaduras. Definimos

$$A\le B\iff A\subseteq B.$$

El orden estricto significa inclusión estricta. La relación no compara el número de elementos de los conjuntos. Ambas cortaduras pueden ser infinitas; lo relevante es qué racionales admite cada una.

La inclusión es reflexiva porque todo elemento de $A$ está en $A$. Es antisimétrica porque si cada uno de los dos conjuntos está incluido en el otro tienen exactamente los mismos elementos. Es transitiva porque pertenecer a $A$, luego a $B$ y luego a $C$ asegura pertenecer a $C$.

Estas tres propiedades producen un orden parcial. Para que sea total falta comparabilidad. En un conjunto de subconjuntos arbitrarios, la inclusión no suele ser total: $\{0\}$ y $\{1\}$ no están incluidos uno en el otro. La comparabilidad aparece aquí por la propiedad descendente de las cortaduras.

Si dos cortaduras fueran incomparables, existiría un racional $r$ admitido por $A$ y rechazado por $B$, y otro $s$ admitido por $B$ y rechazado por $A$. Los racionales $r,s$ no son iguales. Si $r<s$, el descenso de $B$ obliga a admitir $r$; si $s<r$, el descenso de $A$ obliga a admitir $s$. Cualquiera de las dos posibilidades contradice las pertenencias elegidas. Esta contradicción demuestra que toda pareja de cortaduras es comparable.
La prueba de comparabilidad exige examinar ambos casos y precisar el alcance de la negación inicial. No se niega sólo una inclusión: para afirmar incomparabilidad deben fallar las dos. La total ordenación de los racionales basta para demostrar total ordenación de las cortaduras; no hay un argumento que utilice el orden de los reales como premisa.

### Orden total e inclusión de los racionales

Definimos $A\le B$ si $A\subseteq B$, y $A<B$ si la inclusión es estricta. La inclusión es reflexiva, antisimétrica y transitiva por las propiedades de pertenencia a conjuntos.

Para demostrar comparabilidad, supongamos que ninguna de las dos inclusiones $A\subseteq B$, $B\subseteq A$ se cumple. Existen entonces $r\in A\setminus B$ y $s\in B\setminus A$. No son iguales. Si $r<s$, el cierre descendente de $B$ implica $r\in B$; si $s<r$, el de $A$ implica $s\in A$. Ambos casos contradicen la elección. Por tanto las cortaduras están totalmente ordenadas. La prueba utiliza el orden total de $\mathbb Q$, no el de un cuerpo de reales aún inexistente.

La función $\iota:\mathbb Q\to D$, $\iota(r)=C_r$, satisface

$$r\le s\iff C_r\subseteq C_s.$$

La implicación directa es inmediata. Si $r>s$, el racional $s$ pertenece a $C_r$ y no a $C_s$, de modo que la inclusión inversa es imposible. Si $r<s$, el propio $r$ pertenece a $C_s\setminus C_r$, por lo que la inclusión es estricta. Esto prueba preservación y reflexión del orden, así como inyectividad.

Los elementos de $\mathbb Q$ son fracciones y los de $D$ son conjuntos de fracciones. Identificaremos $r$ con $C_r$ sólo cuando la inclusión de estructuras esté justificada. Hasta aquí tenemos una inclusión de conjuntos ordenados; aún falta probar que preserve las operaciones de cuerpo.

La inclusión compara la información racional que contienen dos cortaduras. El cierre descendente obliga a admitir cada fracción menor que una ya admitida; por eso dos cortaduras quedan siempre anidadas. Este orden será el que deban respetar la suma y el producto que construiremos a continuación.

## Incluir los racionales en la nueva estructura

Una frontera no tiene por qué ser racional, pero siempre podemos rodearla por dos racionales suficientemente próximos. Este refinamiento finito será el instrumento clave para demostrar la existencia de opuestos e inversos.

Los elementos de $\mathbb Q$ son fracciones; los de $D$ son subconjuntos. Que deseemos recuperar los racionales dentro del sistema nuevo no los convierte automáticamente en los mismos objetos. Se necesita una función que asocie a cada racional su cortadura correspondiente:

$$\iota:\mathbb Q\longrightarrow D,\qquad \iota(r)=C_r.$$

Debemos probar que esta aplicación es inyectiva y que preserva y refleja el orden. La segunda exigencia puede expresarse mediante una equivalencia: $r\le s$ si y sólo si $\iota(r)\le\iota(s)$.

La diferencia con la imagen intuitiva anterior es el dominio del parámetro: ahora $r$ es racional. Ya existe y podemos compararlo con otros racionales, de modo que la descripción de $C_r$ es una definición legítima.
Si $r<s$, el racional $r$ pertenece a $C_s$ y no a $C_r$. Esa única fracción basta para distinguir ambas cortaduras y mostrar que la inclusión es estricta. Si $r>s$, el racional $s$ prueba que $C_r$ no puede estar incluido en $C_s$. Así obtenemos las dos direcciones de la equivalencia y también la inyectividad.

Hasta este momento la función conserva el orden. Hablar de una inclusión de cuerpos requiere algo más: deben definirse las operaciones en $D$ y comprobarse

$$C_r+C_s=C_{r+s},\qquad C_rC_s=C_{rs}.$$

Las demostraciones de la compatibilidad aditiva y multiplicativa completan estas verificaciones. Sólo después de ellas es legítimo identificar a un racional con su representante dentro del cuerpo construido.

### Aproximación racional finita

Llamamos admisible a un par $[a,b]$ con $a\in A$, $b\notin A$. Para todo $\varepsilon\in\mathbb Q_{>0}$ existe un par admisible de anchura $b-a<\varepsilon$.

Partimos de cualquiera, disponible por la definición de cortaduras. Si $m=(a+b)/2$ pertenece a $A$, sustituimos $a$ por $m$; de lo contrario sustituimos $b$ por $m$. Cada paso conserva la admisibilidad y divide la anchura por dos. Tras $n$ pasos, ésta es $(b_0-a_0)/2^n$.

Existe un $n$ natural con esa anchura menor que $\varepsilon$. En efecto, los enteros positivos superan cualquier racional, como se comprueba escribiéndolo como cociente de enteros con denominador positivo. Además $2^n\ge n+1$ por inducción. Elegir $n+1>(b_0-a_0)/\varepsilon$ basta. Es un procedimiento finito; no se afirma convergencia de una sucesión de puntos ni se usa completitud.

El refinamiento puede mantenerse dentro de un par inicial. Lo usaremos también para conservar un extremo inferior positivo, sin cambiar de corte.

Cada bisección conserva un racional interior y otro exterior, y reduce a la mitad la anchura entre ellos. Una tolerancia racional determina cuántas repeticiones necesitamos: al terminar disponemos de dos testigos adecuados para una estimación concreta. Usaremos esa libertad al demostrar la existencia del opuesto y, con un extremo inferior positivo, la del recíproco.

## Sumar y tomar opuestos de cortaduras

El paso del orden a las operaciones aditivas ya está preparado. La suma y el opuesto deben respetar la forma de los cortes incluso cuando sus extremos no están incluidos.

La suma de cortaduras se define por testigos racionales:

$$A+B=\{q\in\mathbb Q:\exists a\in A\ \exists b\in B\quad q<a+b\}.$$

La comparación $q<a+b$ ocurre en $\mathbb Q$. El lado izquierdo nombra una operación nueva entre cortaduras; el lado derecho utiliza la suma racional ya conocida. Esta distinción de niveles permite construir una operación sin presuponerla.

El cero nuevo es $C_0=\{q\in\mathbb Q:q<0\}$. El opuesto se escribe

$$-A=\{q\in\mathbb Q:\exists p\in\mathbb Q\setminus A\quad q<-p\}.$$

Para visualizar la operación, tomamos el complemento de la cortadura y lo reflejamos. La desigualdad estricta bajo $-p$ realiza una parte decisiva del trabajo: si el complemento tiene un primer elemento, la reflexión literal tendría un máximo. La fórmula evita incluir esa frontera.
No basta que la suma se parezca a una cortadura: debemos probar que realmente lo es. Un elemento $a\in A$ y otro $b\in B$ proporcionan un testigo de no vacuidad. Racionales exteriores $u\notin A$, $v\notin B$ acotan todos los testigos por $u+v$ y garantizan que el resultado no es todo $\mathbb Q$. El descenso usa el mismo par de testigos; un punto medio bajo $a+b$ prueba ausencia de máximo. La demostración que sigue desarrolla, una por una, las cuatro condiciones de cortadura.

Ese apartado demuestra además una igualdad útil: la suma coincide con el conjunto de todas las sumas exactas $a+b$, con $a\in A$, $b\in B$. La ausencia de máximo permite superar una suma exacta con nuevos testigos; el cierre descendente permite reajustar un sumando cuando partimos de una desigualdad estricta. Esta igualdad reduce la asociatividad a la asociatividad racional, sin saltarse la buena definición.

El inverso aditivo tiene un paso más delicado. Es fácil ver que todo elemento de $A+(-A)$ es negativo: un elemento de $A$ queda estrictamente por debajo de todo racional exterior. Para probar que aparecen **todos** los negativos, necesitamos acercar un racional interior y uno exterior lo suficiente. El refinamiento racional utiliza bisección finita para lograr cualquier anchura racional prescrita; la estructura aditiva emplea esa anchura para encontrar un testigo de cada $q<0$.

La bisección produce, tras un número finito de pasos, el margen racional requerido por la prueba. Con ella queda probado $A+(-A)=C_0$ y, junto con asociatividad, conmutatividad y unidad, la estructura de grupo abeliano aditivo.

### Suma: buena definición, conmutatividad y asociatividad

Definimos la suma mediante testigos racionales:

$$A+B=\{q\in\mathbb Q:\exists a\in A\ \exists b\in B\quad q<a+b\}.$$

Es no vacío: dados $a\in A$, $b\in B$, contiene $a+b-1$. Es propio: dados $u\notin A$, $v\notin B$, todo testigo satisface $a<u$, $b<v$; por tanto todos sus elementos son menores que $u+v$, que queda fuera. Si $q<a+b$ y $t<q$, el mismo testigo incluye a $t$. Finalmente $(q+a+b)/2$ está entre $q$ y $a+b$ y pertenece a la suma. Se cumplen las cuatro condiciones de cortadura.

Una forma equivalente, útil para las leyes algebraicas, es

$$A+B=\{a+b:a\in A,\ b\in B\}.$$

Si $q<a+b$, tomamos $a'=q-b<a$, que pertenece a $A$, y obtenemos $q=a'+b$. A la inversa, si $q=a+b$, la ausencia de máximo permite $a'>a$ en $A$; entonces $q<a'+b$ y cumple la definición estricta. Esta equivalencia no se obtiene suprimiendo arbitrariamente un signo estricto: necesita el cierre descendente y la ausencia de máximo.

La conmutatividad sigue de $a+b=b+a$ en $\mathbb Q$. Usando la forma equivalente, los elementos de $(A+B)+C$ son exactamente las sumas $(a+b)+c$, y los de $A+(B+C)$ son $a+(b+c)$, con $a\in A$, $b\in B$, $c\in C$. La asociatividad racional prueba igualdad de conjuntos.

### Cero, opuesto y estructura aditiva

Ponemos $0_D=C_0$. Si $q\in A+C_0$, hay $a\in A$, $b<0$ con $q<a+b<a$, de modo que $q\in A$. Si $q\in A$, elegimos $a\in A$ con $q<a$ y $b=(q-a)/2<0$; entonces $q<a+b$. Esto prueba $A+C_0=A$.

El opuesto utiliza racionales exteriores a la cortadura:

$$-A=\{q\in\mathbb Q:\exists p\in\mathbb Q\setminus A\quad q<-p\}.$$

Es no vacío: para un $p\notin A$, contiene $-p-1$. Si $a\in A$, cualquier $p\notin A$ supera a $a$, por lo que $-p<-a$; así $-a\notin-A$ y el conjunto es propio. El cierre descendente y la ausencia de máximo siguen tomando el mismo testigo y un punto medio bajo $-p$.

Demostremos $A+(-A)=C_0$. Si $q$ pertenece a la suma, existen $a\in A$, $b\in-A$ y $p\notin A$ con $q<a+b$ y $b<-p$. Como $a<p$, resulta $q<a-p<0$.

Para la inclusión contraria, sea $q<0$. El refinamiento racional da $a\in A$, $p\notin A$ con $p-a<-q$, es decir, $q-a<-p$. Elegimos un racional $b$ estrictamente entre $q-a$ y $-p$. Entonces $b\in-A$ y $q<a+b$, como necesitábamos. No se empleó una traslación de desigualdades entre cortaduras ni un axioma de grupo sin demostrar.

Por la prueba de las leyes de la suma y esta identidad, $(D,+,C_0)$ es un grupo abeliano. Los inversos son únicos: si $A+B=C_0=A+C$, sumar $-A$ y usar asociatividad da $B=C$. En consecuencia $-(-A)=A$ y $-(A+B)=(-A)+(-B)$, pues la suma propuesta es un inverso de $A+B$.

El orden es compatible con traslación. De $A\subseteq B$, cada testigo de $A+Z$ es testigo de $B+Z$, así que $A+Z\subseteq B+Z$. Si $A<B$ y las sumas fueran iguales, cancelar $Z$ daría $A=B$. Por tanto

$$A<B\iff A+Z<B+Z.$$

La dirección inversa se obtiene trasladando por $-Z$. En particular,

$$A<B\iff C_0<B-A.$$

Esta equivalencia se deriva aquí de la buena definición explícita de la suma y de la cancelación ya probada; no se presupone antes.

Si $A>C_0$, hay un racional positivo en $A$: un elemento de $A\setminus C_0$ es no negativo y, si fuera cero, la ausencia de máximo proporciona uno mayor. Si $A<C_0$, trasladar por $-A$ da $-A>C_0$.

### Compatibilidad de la inclusión racional con la suma

Para $r,s\in\mathbb Q$,

$$C_r+C_s=C_{r+s},\qquad -C_r=C_{-r}.$$

En la primera igualdad, cualquier testigo $a<r$, $b<s$ implica $q<a+b<r+s$. Si $q<r+s$, ponemos $\delta=(r+s-q)/4$, $a=r-\delta$, $b=s-\delta$; son testigos y $a+b>q$.

En la segunda, $p\notin C_r$ equivale a $p\ge r$, así que $q<-p$ implica $q<-r$. Para todo $q<-r$ sirve el testigo $p=r$, exterior a $C_r$. Obsérvese por qué la desigualdad estricta es indispensable: la reflexión literal de todo el complemento incluiría la frontera $-r$ y produciría un conjunto con máximo.

La suma es una operación cerrada entre cortaduras, asociativa y conmutativa, con cero y opuestos, que respeta las traslaciones del orden. El argumento que relaciona testigos estrictos y sumas exactas reúne dos propiedades de nuestros objetos: el descenso reajusta un sumando y la posibilidad de aumentarlo recupera la holgura estricta. Esa misma combinación reaparecerá al comparar perfiles racionales en el capítulo de unicidad.

## Multiplicar: primero positivos, después signos

El producto presenta una dificultad adicional: no está permitido multiplicar desigualdades ignorando los signos. Por eso construiremos primero el producto de objetos no negativos, y sólo después extenderemos a todos.

El producto se define primero para cortaduras no negativas:

$$A\odot B=C_0\cup\{q\in\mathbb Q:\exists a\in A\ \exists b\in B\quad a>0,\ b>0,\ q<ab\}.$$

La inclusión explícita de todos los negativos garantiza un lado inferior completo. Las restricciones positivas sobre $a,b$ evitan que la multiplicación de testigos racionales negativos produzca valores enormes sin representar el producto buscado. Por ejemplo, si multiplicáramos arbitrariamente todos los negativos de dos cortaduras, obtendríamos productos positivos sin cota, incluso cuando ambas cortaduras representaran cantidades pequeñas.

Cuando uno de los factores es $C_0$, no tiene elementos positivos: la segunda parte de la definición queda vacía y el producto es justamente $C_0$. Cuando ambos factores son positivos, existen testigos cuyo producto es positivo, y el resultado supera estrictamente a cero.

La fórmula anterior define el producto **únicamente para factores no negativos**. Después de demostrar las leyes en ese dominio, extenderemos la operación a todos los signos: para dos factores negativos se multiplicarán sus opuestos positivos; para signos diferentes se tomará el opuesto del producto positivo. Habrá que comprobar que esa extensión está bien definida y que las leyes siguen siendo válidas. La unidad multiplicativa será $C_1$.

**Corrección del recíproco.** La fórmula que aparece para el inverso,

$$\{q\in\mathbb Q:\exists p\in\mathbb Q\setminus A,\ p>0,\ q<1/p\},$$

sirve cuando $A>C_0$. Si se aplica a una cortadura negativa, todo racional positivo queda fuera de $A$, y los testigos $p$ pueden aproximarse arbitrariamente a cero. El conjunto resultante sería todo $\mathbb Q$, no una cortadura. Por ello la corrección completa exige dos casos: el recíproco positivo $J_A$ para $A>C_0$ y $-J_{-A}$ para $A<C_0$. El cero se excluye.

La condición $p>0$ no es una justificación completa del dominio de $A$. Cambiarla por $p\ne0$ tampoco soluciona el caso negativo. En la construcción del recíproco se prueba la buena definición y la identidad $AA^{-1}=C_1$, y se explica el contraejemplo que obliga a introducir el caso de signo faltante.

Las fórmulas del producto aún no son suficientes para que las cortaduras constituyan un cuerpo. Debemos comprobar sus leyes de manera explícita. Primero se demuestra asociatividad y distributividad en el cono no negativo mediante testigos. La parte pedagógicamente decisiva de la distributividad consiste en reunir dos testigos distintos del mismo factor: si $a_1,a_2\in A$, su máximo sigue perteneciendo a $A$ y puede dominar ambos productos.

Después representamos una cortadura arbitraria como diferencia de dos no negativas. Una prueba de independencia de representación permite extender el producto; las leyes ya verificadas en el cono y las leyes del grupo aditivo producen las leyes en todo $D$. Esa construcción justifica los cuatro casos de signos de la multiplicación. No se da por cierta la distributividad general para demostrar esa misma distributividad.

Con los inversos no nulos y $C_0\ne C_1$ queda un cuerpo. Su multiplicación restringida a los elementos distintos de cero es un grupo abeliano; la multiplicación de todo el conjunto no lo es, porque cero no es invertible. La precisión evita convertir una abreviación textual en un axioma falso.

El orden también debe conectarse con las operaciones. La suma preserva inclusión por sus testigos; la cancelación vuelve estricta la traslación cuando la inclusión original es estricta. Un producto de positivos es positivo por la fórmula del cono. Si $A<B$ y $Z>0_D$, la diferencia $(B-A)Z$ es positiva y la distributividad da $BZ-AZ>0_D$, por lo que $AZ<BZ$. Sólo ahora queda justificado el término **cuerpo ordenado**.

### Producto de cortaduras no negativas

Para $A,B\ge C_0$, definimos, siguiendo la definición de producto positivo,

$$A\odot B=C_0\ \cup\ \{q\in\mathbb Q:\exists a\in A\ \exists b\in B\quad a>0,\ b>0,\ q<ab\}.$$

Es no vacío porque contiene $C_0$. Elegimos racionales positivos $u\notin A$, $v\notin B$: basta aumentar racionales exteriores hasta que sean positivos. Para cualquier testigo positivo, $a<u$, $b<v$, luego $ab<uv$ y $uv$ queda fuera. El cierre descendente vale en cada una de las dos partes y se conserva al unirlas. Si $q<0$, hay un racional entre $q$ y cero en $C_0$; si $q\ge0$ y $q<ab$, hay un racional entre $q$ y $ab$ incluido por ese testigo. Así el producto pertenece a $D$ y es no negativo.

Si uno de los factores es $C_0$, no tiene testigos positivos, por lo que $A\odot C_0=C_0$. Si ambos son estrictamente positivos, elegimos $a,b>0$ en ellos; el racional $ab/2>0$ pertenece al producto. Éste es entonces estrictamente positivo.

La conmutatividad sigue de la simetría de los testigos. También hay monotonía no estricta en cada factor no negativo: ampliar una cortadura no elimina testigos positivos. No usamos aún multiplicación de desigualdades en $D$.

Un detalle útil: si $a\in A$, $b\in B$ son positivos, el racional $ab$ mismo pertenece a $A\odot B$. Basta reemplazar $a$ por un $a'>a$ en $A$ y usar $ab<a'b$.

### Leyes algebraicas en el cono no negativo

**Asociatividad.** Si alguno de $A,B,C\ge C_0$ es cero, ambos productos iterados son cero por el producto positivo. Supongamos que los tres son positivos. Para un racional $q\ge0$, pertenecer a $(A\odot B)\odot C$ equivale a existir $a\in A$, $b\in B$, $c\in C$, todos positivos, con $q<abc$.

En efecto, de $q<pc$, con $p>0$ en $A\odot B$, obtenemos $p<ab$ y por tanto $q<abc$. A la inversa, dado $q<abc$, elegimos un racional $p$ con $q/c<p<ab$ y $p>0$; pertenece a $A\odot B$ y da $q<pc$. Los racionales negativos pertenecen a todas las cortaduras de producto no negativo por definición. El mismo criterio de triple testigo describe $A\odot(B\odot C)$, y la asociatividad racional prueba la igualdad.

**Unidad.** $1_D=C_1$ satisface $A\odot C_1=A$. Si $q\ge0$ pertenece al producto, sus testigos cumplen $0<b<1$ y $q<ab<a\in A$, así que $q\in A$. Si $q\ge0$ pertenece a $A$, elegimos $a\in A$ con $a>q$ y un racional $b$ con $q/a<b<1$ y $b>0$; entonces $q<ab$. Los racionales negativos pertenecen a ambos conjuntos. Para $A=C_0$ vale la identidad de cero anterior.

**Distributividad no negativa.** Para $A,B,C\ge C_0$,

$$A\odot(B+C)=(A\odot B)+(A\odot C).$$

Si cualquiera de los factores relevantes es cero, las identidades de cero y suma reducen la afirmación inmediatamente. Consideremos $A,B,C>C_0$. Ambas partes contienen $C_0$ por monotonía aditiva y el producto positivo.

Sea $q\ge0$ en la parte izquierda. Hay $a\in A$, $d\in B+C$ positivos con $q<ad$. La definición de suma proporciona $b\in B$, $c\in C$ con $d<b+c$. Como $B,C$ contienen racionales positivos, podemos escoger un racional positivo en cada corte. Sustituimos cada testigo anterior por el máximo entre él y el positivo correspondiente; el máximo sigue perteneciendo a la misma cortadura. Obtenemos así dos racionales positivos $b,c$ cuya suma no es menor que el testigo $d$. Puesto que el primer factor $a$ es positivo, se conserva la desigualdad estricta y resulta $q<a(b+c)=ab+ac$. El detalle final del producto positivo garantiza $ab\in A\odot B$ y $ac\in A\odot C$, así que $q$ pertenece a la parte derecha.

A la inversa, si $q\ge0$ pertenece a la suma derecha, hay $u\in A\odot B$, $v\in A\odot C$ con $q<u+v$. Para cada $u$ y $v$ podemos conseguir testigos positivos $a_1,b$ y $a_2,c$ con $u<a_1b$, $v<a_2c$. Si alguno de los racionales intermedios es negativo, no necesita un testigo especial: como los cortes factores son estrictamente positivos, **cualquier** par de testigos positivos produce un producto que supera a ese racional. Si el valor intermedio es no negativo, la definición de pertenencia al corte producto ofrece sus testigos. Reunimos finalmente las dos elecciones mediante $a=\max(a_1,a_2)\in A$. Entonces

$$q<u+v<a(b+c).$$

El racional positivo $b+c$ pertenece a $B+C$ por la forma equivalente de la suma. El máximo escogido no es intercambiable con el mínimo: necesitamos un elemento de $A$ que **supere simultáneamente** a los dos testigos iniciales para que ambas desigualdades puedan sumarse. Por ello $q$ pertenece al producto izquierdo. Esto prueba la igualdad para todos los racionales.

La afirmación de cero de este párrafo incluye también los casos $B=C=C_0$ o un solo sumando cero; si $A=C_0$, el producto de ambos lados se reduce a $C_0+C_0=C_0$. No queda ningún caso de frontera delegado a una regla de signos no probada.

### Extensión con signos y leyes en todo D

Partimos de una definición por cuatro casos. Para auditar sus leyes sin una enumeración opaca de signos, construiremos primero la misma operación de una forma equivalente.

Todo $X\in D$ se puede escribir $X=P-Q$ con $P,Q\ge C_0$: si $X\ge C_0$, usamos $(P,Q)=(X,C_0)$; si $X<C_0$, usamos $(P,Q)=(C_0,-X)$. Por ahora el signo menos es la operación de grupo aditivo ya demostrada.

Para $T\ge C_0$, definimos

$$h_T(P-Q)=(P\odot T)-(Q\odot T).$$

Está bien definida. Si $P-Q=P'-Q'$, la ley de grupo implica $P+Q'=P'+Q$. Multiplicando esta igualdad entre cortaduras no negativas por $T$ y usando exclusivamente las leyes del producto no negativo, obtenemos

$$(P\odot T)+(Q'\odot T)=(P'\odot T)+(Q\odot T).$$

La cancelación aditiva da igualdad de las dos diferencias que definen $h_T$. Obsérvese el orden lógico: en esta operación auxiliar solo multiplicamos cortaduras no negativas por un factor no negativo. La distributividad utilizada es precisamente la que ya hemos demostrado en ese cono; no estamos suponiendo una multiplicación general de diferencias.

Además $h_T$ es aditiva: para $X=P-Q$, $Y=R-S$, la representación $(P+R)-(Q+S)$ de $X+Y$, junto con distributividad no negativa, proporciona

$$h_T(X+Y)=h_T(X)+h_T(Y).$$

En particular $h_T(-X)=-h_T(X)$. Para $T,U\ge C_0$, la misma distributividad da $h_{T+U}(X)=h_T(X)+h_U(X)$.

Para $Y=R-S$ con $R,S\ge C_0$, definimos ahora

$$XY=h_R(X)-h_S(X).$$

Tampoco depende de la representación de $Y$. Si $R-S=R'-S'$, tenemos $R+S'=R'+S$. Aplicar la identidad de aditividad en el subíndice da $h_R(X)+h_{S'}(X)=h_{R'}(X)+h_S(X)$, que prueba independencia. Esta es una **segunda** comprobación: la primera controló cómo escribíamos $X$; la presente controla cómo escribimos $Y$. Ambas preceden a las reglas de signo y a la distributividad general. Al desarrollar ambas representaciones,

$$ (P-Q)(R-S)=\bigl(P\odot R+Q\odot S\bigr)-\bigl(P\odot S+Q\odot R\bigr).$$

Todo el lado derecho es una cortadura porque ya están bien definidas suma, opuesto y productos no negativos. Elegir las representaciones según el signo reduce esta fórmula exactamente a

$$
AB=\begin{cases}
A\odot B,&A\ge C_0,\ B\ge C_0,\\
-\bigl((-A)\odot B\bigr),&A<C_0,\ B\ge C_0,\\
-\bigl(A\odot(-B)\bigr),&A\ge C_0,\ B<C_0,\\
(-A)\odot(-B),&A<C_0,\ B<C_0.
\end{cases}
$$

La fórmula por diferencias recupera los cuatro casos de signo y abarca también los factores cero. No hemos propuesto una segunda multiplicación incompatible con la primera: hemos construido una operación bien definida y luego hemos demostrado que coincide con la regla por signos anunciada.

La fórmula simétrica prueba conmutatividad. La aditividad de cada $h_T$ prueba $X(Y+Z)=XY+XZ$ mediante independencia de representaciones; también $(X+Y)Z=XZ+YZ$. Más explícitamente, para $Y=R-S$, $Z=T-U$, usamos la representación $(R+T)-(S+U)$ de $Y+Z$ y la aditividad en el subíndice. No se multiplica una diferencia con reglas formales antes de justificarlas.

Para asociatividad, escribimos $X=P-Q$, $Y=R-S$, $Z=T-U$ con seis cortaduras no negativas. Expandir $(XY)Z$ por la definición y las leyes del producto no negativo da la diferencia entre

$$P\odot R\odot T+Q\odot S\odot T+P\odot S\odot U+Q\odot R\odot U$$

$$P\odot R\odot U+Q\odot S\odot U+P\odot S\odot T+Q\odot R\odot T.$$

Expandir $X(YZ)$ da las mismas cuatro sumas positivas y las mismas cuatro negativas, reordenadas. El número total de términos procede de elegir, en cada uno de los tres factores, la parte positiva o la parte que se resta. Los términos con un número par de elecciones negativas aparecen con signo positivo; los demás, con signo negativo. Conmutatividad y asociatividad de la suma, y asociatividad en el cono, prueban igualdad. Cada término involucra productos de cortaduras no negativas ya legitimados.

Por las leyes del producto no negativo, $XC_1=(P\odot C_1)-(Q\odot C_1)=P-Q=X$. También $XC_0=C_0$. Como $0\in C_1$ y $0\notin C_0$, las unidades son distintas. Disponemos de un anillo conmutativo no trivial; la existencia de inversos multiplicativos se demostrará ahora.

### El recíproco positivo y su extensión por signos

Para $A>C_0$ definimos

$$J_A=\{q\in\mathbb Q:\exists p\in\mathbb Q\setminus A\quad p>0,\ q<1/p\}.$$

Esta fórmula es válida **únicamente para el caso positivo**. Toda $p\notin A$ supera a cualquier $a_0>0$ en $A$. El conjunto $J_A$ es no vacío y positivo: para un $p>0$ exterior, contiene $1/(2p)>0$ y todos los negativos. Es propio: todos sus elementos son menores que $1/a_0$, que queda fuera. Cierre descendente y ausencia de máximo se prueban con el mismo testigo y un punto medio inferior a $1/p$. Por tanto $J_A\in D$.

Probemos $A\odot J_A=C_1$. Si $q\ge0$ pertenece al producto, hay $a>0$ en $A$, $b>0$ en $J_A$ y un $p\notin A$ con $b<1/p$, tales que $q<ab$. Como $a<p$, resulta $q<ab<a/p<1$. Los negativos también están en $C_1$.

Para la inclusión contraria, sea $0\le q<1$. Fijamos $a_0>0$ en $A$ y refinamos un par admisible inicial $[a_0,p_0]$ hasta obtener $a\in A$, $p\notin A$, $a\ge a_0$ y

$$p-a<(1-q)a_0.$$

Todos esos racionales son positivos, y

$$\frac ap=1-\frac{p-a}{p}>1-(1-q)=q,$$

porque $p>a\ge a_0$. Elegimos un racional $b$ entre $q/a$ y $1/p$, positivo incluso cuando $q=0$. Así $b\in J_A$ y $q<ab$. Los $q<0$ pertenecen al producto por definición. Se prueba la igualdad.

Para $A\ne C_0$, definimos finalmente

$$A^{-1}=\begin{cases}J_A,&A>C_0,\\-J_{-A},&A<C_0.\end{cases}$$

En el segundo caso, $-A>C_0$ por la estructura aditiva. El producto por signos de la extensión multiplicativa a todos los signos da

$$A\bigl(-J_{-A}\bigr)=(-A)\odot J_{-A}=C_1.$$

No definimos inverso para $C_0$, pues $C_0X=C_0\ne C_1$ para todo $X$. Los inversos no nulos son únicos por asociatividad y unidad. Así $D$ es un cuerpo.

La restricción es necesaria, no decorativa. Si $A=C_{-1}$ y aplicáramos la fórmula positiva sin restringir $A$, todos los $p>0$ quedarían fuera. Para cualquier $q\in\mathbb Q$ podríamos elegir un $p>0$ suficientemente pequeño con $q<1/p$; el resultado sería $\mathbb Q$, que ni siquiera es una cortadura. Lo mismo ocurre para $A=C_0$. Cambiar $p>0$ por $p\ne0$ no repara esa definición general: los $p>0$ siguen proporcionando todos los racionales.

### Cuerpo ordenado e inclusión de cuerpos

La compatibilidad con suma ya está demostrada en la estructura aditiva. Si $A<B$ y $Z>C_0$, entonces $B-A>C_0$. Por el producto positivo, $(B-A)Z>C_0$; por distributividad,

$$BZ-AZ=(B-A)Z>C_0.$$

Aplicar la equivalencia de la estructura aditiva da $AZ<BZ$. Esto prueba la compatibilidad con multiplicación por positivos sin presuponerla para justificar las operaciones.

Para completar la inclusión racional, sean $r,s\ge0$. Si uno es cero, $C_r\odot C_s=C_{rs}$ por el caso cero. Si ambos son positivos, todo testigo de producto es menor que $rs$, por lo que el producto queda incluido en $C_{rs}$. Para un $z\ge0$ con $z<rs$, escogemos

$$0<\eta\le\min\left(\frac r2,\frac s2,1,\frac{rs-z}{2(r+s+1)}\right).$$

Los racionales $a=r-\eta>0$, $b=s-\eta>0$ pertenecen a $C_r,C_s$, y

$$ab=rs-\eta(r+s)+\eta^2>z.$$

Los negativos están incluidos automáticamente. Por tanto $C_r\odot C_s=C_{rs}$. La compatibilidad de la inclusión racional con la suma y los casos de signo de la extensión multiplicativa a todos los signos extienden la identidad a todo $r,s\in\mathbb Q$. Quedan probadas preservación de suma, producto, opuesto, cero, uno y orden; para $r\ne0$, la unicidad del inverso implica $C_r^{-1}=C_{1/r}$.

La multiplicación no vuelve a todo $D$ un grupo: cero no tiene inverso. La estructura multiplicativa de grupo abeliano corresponde a $D\setminus\{C_0\}$; la aditiva sí corresponde a todo $D$.

El producto nos obligó a separar tres problemas que en la aritmética escolar suelen pasar inadvertidos: qué racionales sirven como testigos, cómo se extiende una operación inicialmente positiva a números de cualquier signo y dónde se permite tomar inversos. Controlar esas tres cuestiones evita fórmulas que producen todo $\mathbb Q$ en lugar de una cortadura. Ahora tenemos todas las leyes de cuerpo y la compatibilidad multiplicativa del orden: sólo resta comprobar la propiedad que faltaba en los racionales originales.

## El supremo como unión

Las cortaduras forman ya un cuerpo ordenado. La propiedad que motivó ampliar los racionales requiere todavía una prueba: dada una familia con elementos y una cota superior común, debemos producir su menor cota superior. El orden por inclusión sugiere reunir toda la información racional que aporta cada miembro de la familia.

Un cuerpo aún no es necesariamente completo. Debemos mostrar que toda familia no vacía de cortaduras que admita una cota superior tiene una menor cota superior *dentro del conjunto de cortaduras*.

**Teorema de completitud.** Sea $V$ una familia no vacía de cortaduras que tiene una cota superior $U\in D$. La candidata a supremo es

$$S=\bigcup_{A\in V}A.$$

Hay tres niveles distintos: $V$ es un conjunto de cortaduras; cada $A\in V$ es un conjunto de racionales; $S$ es el conjunto de racionales que aparecen en al menos una de ellas. No se unen números reales preexistentes ni se toma el supremo racional de una frontera aún desconocida.

Antes de demostrar minimalidad, debemos asegurar que la candidata es una cortadura. Elegir una $A_0\in V$ y un racional suyo prueba no vacuidad. La cota común implica $A\subseteq U$ para cada miembro; al unirlos, $S\subseteq U\ne\mathbb Q$, lo que prueba que la unión sigue siendo propia. Para descenso y ausencia de máximo, un racional de $S$ se coloca primero en alguno de los cortes que lo contienen y se utiliza allí la propiedad correspondiente. Los testigos obtenidos vuelven a pertenecer a la unión.

La hipótesis de cota común no se puede omitir. Las cortaduras $C_n$ son todas propias, pero su unión cuando $n$ recorre los naturales contiene cada racional. Tampoco se puede omitir que la familia sea no vacía. Estos ejemplos aclaran por qué la afirmación correcta no es «toda unión de cortaduras es una cortadura».

Una vez probado $S\in D$, cada miembro de $V$ está incluido en $S$, así que $S$ es cota superior. Para cualquier otra cota superior $C\in D$, todos los miembros de $V$ están incluidos en $C$; por la propiedad de unión, también $S\subseteq C$. Eso es exactamente ser la menor cota superior. No hay que encontrar una fórmula para una frontera escalar: la operación de conjuntos produce directamente el objeto requerido.

La prueba de la unión no utiliza multiplicación. Esto ayuda a comprender la arquitectura del argumento: la completitud del orden puede verificarse independientemente, mientras que llamar a la estructura «cuerpo ordenado completo» exige haber saldado todas las obligaciones algebraicas anteriores. La demostración detallada que sigue precisará el dominio de las familias consideradas y justificará, una por una, las cuatro propiedades que su unión debe satisfacer para ser una cortadura.

### Comparación de las dos definiciones de suma sobre cortaduras

La **suma mediante testigos** que hemos construido,

$$A+B=\{q\in\mathbb Q:\exists a\in A\;\exists b\in B\quad q<a+b\},$$

coincide con la suma definida mediante recintos en el apéndice A: allí se unen los conjuntos $C_{a+b}$, donde $[a,u]$ y $[b,v]$ recorren intervalos racionales admisibles de $A$ y $B$. Cada par de racionales interiores puede completarse con extremos exteriores; inversamente, todo intervalo admisible aporta sus extremos inferiores como testigos. En cambio, **no inferimos sin demostración** que las expresiones de producto, en particular para signos diferentes, sean literalmente intercambiables. La coincidencia del producto y del recíproco exige una demostración independiente, presentada después de concluir ambas construcciones.

La construcción seguida aquí usa testigos racionales; la vía alternativa mediante recintos, presentada en el primer apéndice, define las operaciones de otra manera. Debemos probar la coincidencia de ambos procedimientos, no suponerla por la semejanza de sus expresiones.

### Completitud mediante unión

Sea $V\subseteq D$, $V\ne\varnothing$, y supongamos que existe $U\in D$ con $A\subseteq U$ para todo $A\in V$. Definimos

$$S=\bigcup_{A\in V}A.$$

**No vacío.** Elegimos $A_0\in V$ y luego $q\in A_0$, que existe porque $A_0$ es cortadura. Entonces $q\in S$. La no vacuidad de la familia es indispensable: una unión de una familia vacía sería vacía.

**Propio.** Todo $q\in S$ pertenece a algún $A\in V$, y por tanto a $U$. Así $S\subseteq U\ne\mathbb Q$. Un racional exterior a $U$ es también exterior a $S$. Que cada miembro sea propio, por separado, no bastaría: la unión de todos los $C_n$, con $n\in\mathbb N$, es $\mathbb Q$. La cota común es la hipótesis que evita ese problema.

**Descendente.** Si $p\in S$ y $q\in\mathbb Q$ satisface $q<p$, existe un $A\in V$ con $p\in A$. Por su cierre descendente, $q\in A\subseteq S$.

**Sin máximo.** Si $p\in S$, elegimos un $A\in V$ que lo contiene. Hay $q\in A$ con $p<q$, por lo que $q\in S$. No basta escribir que existe un racional mayor: el testigo debe pertenecer a $S$.

Por estas cuatro verificaciones, $S\in D$. Además, cada $A\in V$ está incluido en $S$, así que $S$ es cota superior. Si $C\in D$ es cualquier cota superior de $V$, entonces $A\subseteq C$ para todo $A\in V$ y, por la propiedad de unión, $S\subseteq C$. De ahí

$$S=\sup_D V.$$

Se obtiene un cuerpo ordenado completo. La demostración de la unión sólo necesitó el orden de inclusión y las condiciones de cortadura; el hecho de que sea un **cuerpo** completo utiliza además la buena definición de suma y producto, sus leyes algebraicas, la existencia de inversos y la compatibilidad con el orden. Podemos adoptar $D$ como modelo de $\mathbb R$. No fue necesario hablar de un isomorfismo con un cuerpo de reales supuesto de antemano para demostrar existencia.

La unión reúne exactamente los racionales admitidos por algún miembro de la familia. La cota común mantiene esa información dentro de una cortadura propia y la existencia de un miembro garantiza un elemento interior. Así obtenemos el supremo mediante una operación de conjuntos que sirve para toda familia del dominio del teorema.

## Qué se construyó y qué significa la conclusión

La existencia que acabamos de probar consiste en un objeto concreto con todas las propiedades exigidas. Queda pendiente, y ésa será la pregunta siguiente, si cualquier otro objeto con los mismos axiomas tiene exactamente la misma estructura.

**Conclusión de existencia.** El conjunto $D$ de cortaduras, dotado de las operaciones que acabamos de construir y del orden por inclusión, es un cuerpo ordenado completo. Hemos exhibido un modelo de los números reales sin suponer que existiera de antemano un sistema real. La construcción de $D$ prueba así la existencia. Esta distinción importa: la construcción ha resuelto el problema de **existencia**, mientras que la cuestión de si cualquier otra realización posee la misma estructura exige el teorema de unicidad del capítulo siguiente.

Si se usa el símbolo $\mathbb R$ para otro cuerpo ordenado completo ya elegido, la afirmación de isomorfismo necesita un teorema de unicidad. Demostraremos esta identificación por medio de un isomorfismo: a cada elemento de ese cuerpo le asocia el conjunto de racionales que quedan por debajo; la completitud permite recuperar cada cortadura como un supremo y muestra que la correspondencia conserva las operaciones. Esa comparación se realiza **después** de la construcción. Su justificación completa exigirá un argumento distinto del utilizado para demostrar la existencia.

El aprendizaje central consiste en reconocer cuándo una fórmula describe un objeto legítimo y cuándo sólo sugiere una interpretación. Las imágenes de una recta cortada sirven para orientar, pero las propiedades de conjuntos y las operaciones racionales sostienen la prueba. La construcción convierte esa diferencia en una herramienta: cada número nuevo queda determinado por la información racional situada bajo él, y la unión de esa información proporciona los supremos que faltaban.

## Problemas y soluciones del capítulo

### Ejercicio 1

Demuestra desde sus cuatro axiomas que $C_r$ es cortadura para cualquier $r\in\mathbb Q$. Determina si $r$ pertenece a $C_r$ y explica por qué importa ese detalle.

**Solución razonada.** $C_r$ contiene $r-1$ y no contiene $r$; así es no vacío y propio. Si $q<r$ y $p<q$, por transitividad $p<r$, luego $p\in C_r$. Si $q\in C_r$, el racional $t=(q+r)/2$ satisface $q<t<r$; de ahí que $C_r$ no tenga máximo. El propio $r$ queda excluido. Esto permite usar una convención única para las fronteras racionales: dos cortaduras principales quedan determinadas por sus cotas racionales sin que el elemento frontera pueda convertirse en el máximo del lado inferior.

### Ejercicio 2

Sea $A\subseteq\mathbb Q$ no vacío, propio y descendente. ¿La ausencia de máximo se deduce de las otras tres condiciones? Da un contraejemplo y repara el conjunto para que sea una cortadura.

**Solución razonada.** No se deduce. El conjunto $A=\{q\in\mathbb Q:q\le0\}$ contiene $-1$, es propio y es descendente, pero tiene máximo $0$. La reparación es $C_0=\{q:q<0\}$: en él, para cualquier $q<0$, el punto medio $q/2$ es racional, supera $q$ y sigue siendo negativo. Por ello la cuarta condición es lógicamente independiente de las otras tres.

### Ejercicio 3

Analiza $T=\{q\in\mathbb Q:q^2<2\}$: identifica el axioma de cortadura que falla. Prueba que $H=\{q\in\mathbb Q:q<0\ \mathrm{o}\ q^2<2\}$ es una cortadura sin utilizar $\sqrt2$ real.

**Solución razonada.** $0\in T$ porque $0^2<2$, pero $-2<0$ y $(-2)^2=4>2$, así que $-2\notin T$. El cierre descendente falla. Para $H$, todos los racionales negativos pertenecen al conjunto, y $2\notin H$, de manera que $H$ es no vacío y propio. Si $r\in H$ y $s<r$, el caso $s<0$ es inmediato. Si $s\ge0$, entonces $r>0$, $r^2<2$ y $s^2<r^2<2$; también $s\in H$. Para el axioma sin máximo, si $r<0$, sirve $0\in H$. Si $r\ge0$ y $r^2<2$, fijamos

$$\delta=\min\left(1,\frac{2-r^2}{2(2r+1)}\right)>0.$$

Como $\delta\le1$, obtenemos $(r+\delta)^2\le r^2+(2r+1)\delta\le r^2+(2-r^2)/2<2$, por lo que $r+\delta\in H$ supera a $r$. Sólo se empleó aritmética racional.

### Ejercicio 4

Demuestra que la inclusión entre cortaduras es total. A continuación prueba que $r<s\iff C_r\subsetneq C_s$ para racionales.

**Solución razonada.** La inclusión es un orden parcial no estricto. Si dos cortaduras $A,B$ fueran incomparables, existirían $r\in A\setminus B$ y $s\in B\setminus A$. Como $r\ne s$, o bien $r<s$, y el cierre descendente de $B$ obliga a $r\in B$, o bien $s<r$, y el de $A$ obliga a $s\in A$. Ambas alternativas contradicen los testigos. La relación es total. Si $r<s$, entonces $C_r\subseteq C_s$ y $r\in C_s\setminus C_r$, así que la inclusión es estricta. Si $C_r\subsetneq C_s$ no es posible $s\le r$, pues implicaría $C_s\subseteq C_r$. Luego $r<s$.

### Ejercicio 5

Justifica que para cualquier cortadura $A$, un par admisible $[a,b]$ y un racional $\varepsilon>0$ existe un par admisible $[u,v]\subseteq[a,b]$ con $v-u<\varepsilon$. No invoques límites ni completitud de $D$.

**Solución razonada.** Partimos de $[a_0,b_0]=[a,b]$ admisible. En cada etapa usamos el punto medio racional $m=(a_n+b_n)/2$: si $m\in A$, tomamos $[m,b_n]$; si $m\notin A$, tomamos $[a_n,m]$. Los extremos conservan las pertenencias y la anchura al cabo de $n$ pasos es $(b-a)/2^n$. Puesto que $2^n\ge n+1$, elegimos natural $n$ con $n+1>(b-a)/\varepsilon$, posible por la propiedad arquimediana de $\mathbb Q$. Entonces $(b-a)/2^n<\varepsilon$. Todas las operaciones son finitas; en particular, no se ha usado que los racionales tengan supremos.

### Ejercicio 6

Compara los conjuntos $\{q:\exists a\in A,b\in B\ q<a+b\}$ y $\{a+b:a\in A,b\in B\}$. Demuestra su igualdad indicando dónde se usan la ausencia de máximo y el cierre descendente.

**Solución razonada.** Si $q<a+b$, definimos $a'=q-b$. Como $a'<a$ y $a\in A$, el cierre descendente da $a'\in A$, y $q=a'+b$ es una suma exacta. Recíprocamente, si $q=a+b$ con $a\in A$, $b\in B$, la ausencia de máximo de $A$ proporciona $a'\in A$ con $a'>a$; entonces $q<a'+b$. El primer sentido usa descendencia y el segundo usa ausencia de máximo. Sin esas hipótesis no se justifica retirar la desigualdad estricta.

### Ejercicio 7

Demuestra $C_r+C_s=C_{r+s}$ y $-C_r=C_{-r}$ para racionales. Identifica por qué en el opuesto la desigualdad debe ser estricta.

**Solución razonada.** Si $q\in C_r+C_s$, hay $a<r$, $b<s$ con $q<a+b<r+s$, por lo que $q\in C_{r+s}$. Si $q<r+s$, sea $\delta=(r+s-q)/4>0$ y elijamos $a=r-\delta\in C_r$, $b=s-\delta\in C_s$. Entonces $a+b=r+s-2\delta>q$, así que $q\in C_r+C_s$. Para el opuesto, $p\notin C_r$ significa $p\ge r$. Por eso $q<-p$ implica $q<-r$, y se tiene $-C_r\subseteq C_{-r}$. Si $q<-r$, vale el testigo exterior $p=r$, de modo que se obtiene la otra inclusión. Si usáramos $q\le-p$, con $p=r$ incluiríamos $-r$, que sería máximo del conjunto resultante.

### Ejercicio 8

Partiendo de la fórmula de $-A$ y del refinamiento finito, prueba $A+(-A)=C_0$. Señala qué parte de la prueba necesitaría la aproximación arbitrariamente fina.

**Solución razonada.** Si $q\in A+(-A)$, existen $a\in A$, $b\in-A$ y un racional $p\notin A$ con $q<a+b$ y $b<-p$. Como $a<p$, resulta $q<a-p<0$; esto da $A+(-A)\subseteq C_0$. Para la inclusión contraria, dado $q<0$, el refinamiento del ejercicio 5 produce $a\in A$ y $p\notin A$ con $0<p-a<-q$. De ahí $q-a<-p$. Elegimos un racional $b$ estrictamente entre ambos. Cumple $b<-p$, luego $b\in-A$, y $q<a+b$. Así $q\in A+(-A)$. La segunda inclusión necesita encontrar el par interior–exterior con anchura menor que $-q$; ahí se utiliza la precisión arbitraria del refinamiento.

### Ejercicio 9

Justifica la equivalencia $A<B\iff A+Z<B+Z$ desde la inclusión y la estructura aditiva, sin suponer previamente la compatibilidad del producto.

**Solución razonada.** Si $A\subseteq B$, cualquier par de testigos $a\in A$, $z\in Z$ de $A+Z$ también sirve en $B+Z$; por tanto $A+Z\subseteq B+Z$. Si $A\subsetneq B$ y las sumas fueran iguales, adicionar $-Z$ a ambos lados y usar asociatividad y neutralidad probadas en las leyes de asociatividad, unidad y opuesto aditivo daría $A=B$, contradicción. La inclusión trasladada es entonces estricta. A la inversa, si $A+Z<B+Z$, trasladamos por $-Z$ y recuperamos $A<B$. No se empleó la regla multiplicativa del orden ni se supuso que $D$ fuese ya un cuerpo.

### Ejercicio 10

Explica por qué $\{q:\exists a\in A,b\in B,\ q<ab\}$ no define correctamente el producto positivo de cortaduras cualesquiera. Examina $A=B=C_0$ y describe el problema de tomar testigos negativos arbitrariamente pequeños.

**Solución razonada.** En $C_0$ se encuentran todos los racionales negativos. Si $q>0$ es cualquier racional, escogemos $a=b=-N$ con $N\in\mathbb N$ y $N^2>q$; entonces $q<ab=N^2$, de modo que $q$ pertenece al conjunto candidato. Los racionales no positivos también pertenecen: tomando $N$ mayor se satisface la desigualdad. La expresión sería $\mathbb Q$, no una cortadura. Además, la frase «testigos negativos arbitrariamente pequeños» puede inducir a confusión: el fenómeno defectuoso utiliza testigos negativos de **módulo arbitrariamente grande**. La fórmula correcta para factores no negativos se restringe a $a,b>0$ y agrega todos los negativos mediante $C_0$.

### Ejercicio 11

Dados $A,B>C_0$, prueba que el producto $A\odot B$ definido con testigos positivos es una cortadura positiva. Determina $A\odot C_0$.

**Solución razonada.** Tomamos $A,B>C_0$ y definimos $P=C_0\cup\{q:\exists a\in A,b\in B,\ a,b>0,\ q<ab\}$. Contiene $C_0$ y es no vacío. Elegimos racionales exteriores positivos $u\notin A$, $v\notin B$: como cada cortadura es propia, tomamos exteriores y los aumentamos hasta hacerlos positivos. Todo testigo positivo satisface $a<u$, $b<v$, luego $ab<uv$; así $uv\notin P$, y el conjunto es propio. Descendencia se hereda de las desigualdades estrictas. Si $q<0$, existe $t\in C_0$ entre $q$ y $0$; si $q\ge0$ y $q<ab$, existe $t=(q+ab)/2$ entre $q$ y $ab$ que también está en $P$. Por tanto no hay máximo. Dados $a>0$ en $A$ y $b>0$ en $B$, el racional $ab/2>0$ pertenece a $P$, de modo que $P>C_0$. Para $B=C_0$ no hay $b>0$, así que por definición $A\odot C_0=C_0$.

### Ejercicio 12

Al demostrar $A\odot(B+C)=(A\odot B)+(A\odot C)$ con $A,B,C>C_0$, se obtienen dos testigos posiblemente diferentes $a_1,a_2\in A$. Explica rigurosamente cómo elegir uno solo y concluir la inclusión no trivial.

**Solución razonada.** Para la inclusión $(A\odot B)+(A\odot C)\subseteq A\odot(B+C)$ consideramos primero $q\ge0$ del lado izquierdo. Existen $u\in A\odot B$, $v\in A\odot C$ con $q<u+v$. Como los factores originales son positivos, incluso si $u$ o $v$ es negativo podemos escoger testigos positivos $a_1\in A,b\in B$ y $a_2\in A,c\in C$ que satisfacen $u<a_1b$ y $v<a_2c$. Tomamos $a=\max(a_1,a_2)\in A$. La positividad racional permite

$$q<u+v<a_1b+a_2c\le a(b+c).$$

La caracterización de la suma mediante sumas exactas, ya demostrada, asegura $b+c\in B+C$, por lo cual $q\in A\odot(B+C)$. Los racionales negativos pertenecen automáticamente a ambos conjuntos. La elección $a=\max(a_1,a_2)$ es el paso que permite usar **un solo testigo de $A$** en el producto izquierdo. La otra inclusión se obtiene descomponiendo un testigo positivo $d\in B+C$ como suma de racionales de $B,C$, elevándolos a positivos si fuese necesario; con $q<ad$ se obtiene $q<ab+ac$ y los dos productos racionales exactos pertenecen respectivamente a $A\odot B$, $A\odot C$. No se invoca distributividad entre cortaduras antes de demostrarla.

### Ejercicio 13

Considera $A=C_{-1}$. Prueba que la expresión $\{q:\exists p\notin A,\ p>0,\ q<1/p\}$ es todo $\mathbb Q$. Formula el recíproco correcto de una cortadura negativa.

**Solución razonada.** Para $A=C_{-1}=\{q:q<-1\}$ todo $p>0$ está fuera de $A$. Sea $q\in\mathbb Q$ cualquiera. Elegimos $p\in\mathbb Q$ con $p>0$ y $p<1/(|q|+1)$. Entonces $1/p>|q|+1>q$, así que la fórmula incluye a $q$. Produce $\mathbb Q$ y no es una cortadura. La definición correcta es: si $A>C_0$, usamos $J_A=\{q:\exists p\notin A,\ p>0,\ q<1/p\}$; si $A<C_0$, definimos $A^{-1}=-J_{-A}$. No se define recíproco para $A=C_0$. El segundo caso funciona porque $-A>C_0$, resultado ya demostrado por las leyes del grupo aditivo y del orden.

### Ejercicio 14

Para $A>C_0$, demuestra $A\odot J_A=C_1$, donde $J_A$ es la cortadura definida por los recíprocos de racionales positivos exteriores a $A$. Debes probar las dos inclusiones y controlar los denominadores.

**Solución razonada.** Para $A>C_0$, existe $a_0>0$ con $a_0\in A$. Toda cota exterior racional $p\notin A$ cumple $p>a_0>0$. El conjunto $J_A$ es cortadura: para uno de esos $p$, contiene $1/(2p)>0$; es propio porque todos sus elementos son menores que $1/a_0$; cerradura descendente y ausencia de máximo proceden del mismo testigo $q<1/p$ y del punto medio. Sean $q\ge0$ y $q\in A\odot J_A$. Hay $a>0$ en $A$, $b>0$ en $J_A$ y $p\notin A$ con $q<ab$ y $b<1/p$. Como $a<p$, se sigue $q<ab<a/p<1$; los negativos también pertenecen a $C_1$. Para la otra inclusión, dado $0\le q<1$ refinamos dentro de un intervalo admisible $[a_0,p_0]$ hasta conseguir $a\in A$, $p\notin A$ con $a\ge a_0$ y $p-a<(1-q)a_0$. Entonces

$$\frac ap=1-\frac{p-a}{p}>q.$$

Se puede elegir racional $b$ con $\max(0,q/a)<b<1/p$, pues $q/a<1/p$ y $p>0$. Por construcción $b\in J_A$ y $q<ab$. Se concluye $A\odot J_A=C_1$, con todos los denominadores estrictamente positivos. El caso negativo se reduce al positivo y a la regla de signos demostrada en la extensión multiplicativa a todos los signos.

### Ejercicio 15

Sea $V\subseteq D$ no vacío y acotado superiormente. Prueba que $\bigcup V$ es cortadura y su supremo. Explica con un contraejemplo por qué «acotado superiormente» no puede omitirse.

**Solución razonada.** Sea $S=\bigcup_{A\in V}A$. Elegimos $A_0\in V$ y $q\in A_0$, obteniendo $q\in S$. La cota superior $U\in D$ satisface $A\subseteq U$ para todo $A\in V$, por lo que $S\subseteq U\ne\mathbb Q$; así $S$ es propio. Si $p\in S$ y $q<p$, hay $A\in V$ con $p\in A$, y la descendencia de ese $A$ proporciona $q\in S$. Si $p\in S$, un $A\in V$ que lo contiene ofrece $r\in A$ con $r>p$; el testigo pertenece a $S$ y demuestra ausencia de máximo. Por tanto $S\in D$. Cada $A\in V$ está contenido en $S$, de modo que $S$ es cota superior; si $T\in D$ es otra, entonces contiene todas las $A$ y por consiguiente $S\subseteq T$. Esto demuestra minimalidad y $S=\sup_D V$. Sin cota común, la familia $\{C_n:n\in\mathbb N\}$ tiene unión $\mathbb Q$, ya que dado $q\in\mathbb Q$ existe natural $n>q$. Por eso la cota común no es una condición ornamental.

### Ejercicio 16

Prueba, dentro de $D$, que la cortadura $H$ del ejercicio 3 satisface $H^2=C_2$ y que no es de la forma $C_r$ para ningún racional $r$.

**Solución razonada.** Del ejercicio 3 sabemos que $H\in D$; además $H>C_0$ porque $0\in H$. Si $a,b>0$ están en $H$, entonces $a^2,b^2<2$, por lo que $(ab)^2<4$ y $ab<2$. Cada testigo del producto pertenece a $C_2$: se obtiene $H\odot H\subseteq C_2$. Para la otra inclusión basta tratar $0\le q<2$, porque los negativos pertenecen por definición. Partimos del intervalo admisible $[1,2]$ de $H$ y refinamos hasta conseguir $a\in H$, $p\notin H$, $1\le a<p\le2$ y $p-a<(2-q)/8$. Como $p^2\ge2$,

$$p^2-a^2=(p-a)(p+a)<4\frac{2-q}{8}=\frac{2-q}{2},$$

así $a^2>2-(2-q)/2>q$. Los testigos positivos $a,a$ muestran que $q\in H\odot H$ y se concluye $H^2=C_2$. Si $H=C_r$ para algún racional, la preservación del producto implicaría $C_{r^2}=C_2$ y, por inyectividad, $r^2=2$. Pero si $r=m/n$ fuese una fracción reducida con $n>0$, $m^2=2n^2$ obliga a que $m$ sea par y, después de escribir $m=2k$, a que $n$ también lo sea. Contradicción. Por ello $H$ no representa ningún racional.

### Ejercicio 17 — Profundización

Esta actividad anticipa la identificación de un cuerpo completo con sus cortaduras, que más adelante justificaremos en su totalidad. Su solución incluye los argumentos necesarios para intentarla desde aquí.

Sea $F$ un cuerpo ordenado completo. Para $x\in F$ define $A_x=\{r\in\mathbb Q:r_F<x\}$. Demuestra que esta función es inyectiva y sobreyectiva sobre $D$, indicando en qué pasos usas la propiedad arquimediana, densidad y completitud.

**Solución razonada.** La propiedad arquimediana se obtiene de la completitud de $F$: si los naturales $n_F$ tuvieran una cota superior, su supremo $u$ permitiría encontrar $n_F>u-1_F$, y entonces $(n+1)_F>u$, contradicción. En consecuencia hay enteros por debajo y encima de cada $x\in F$. La densidad racional se obtiene escalando cualquier intervalo $x<y$ por un natural $n$ tal que $n_F(y-x)>1_F$ y escogiendo el primer entero $m_F$ mayor que $n_Fx$; entonces $x<(m/n)_F<y$. Para cada $x$, el conjunto $A_x=\{r:r_F<x\}$ es cortadura: es no vacío y propio por cotas enteras, descendente por el orden y sin máximo por densidad. Si $x<y$, la densidad proporciona un racional entre ambos, que está en $A_y$ pero no en $A_x$; de ahí la inyectividad. Si $A\in D$, el conjunto $E=\{r_F:r\in A\}$ es no vacío y está acotado superiormente por $p_F$ para cualquier $p\notin A$. La completitud permite tomar $x=\sup_FE$. Si $r\in A$, un $s\in A$ mayor que $r$ satisface $r_F<s_F\le x$, luego $r\in A_x$. Recíprocamente, si $r_F<x$, $r_F$ no es cota superior de $E$, de modo que existe $s\in A$ con $r_F<s_F$ y por descendencia $r\in A$. Se obtiene $A=A_x$. Se ha probado biyección; la preservación de operaciones requiere las pruebas adicionales del isomorfismo con las cortaduras y no se deduce de la mera biyección ordenada.

### Ejercicio 18 — Exploración de una construcción alternativa

Este problema adelanta la suma mediante recintos, que se construirá cuidadosamente en el primer apéndice. Para abordarlo ahora basta saber que esa suma reúne todos los racionales estrictamente menores que las sumas de los extremos inferiores de intervalos admisibles de ambas cortaduras.

Prueba directamente que la suma de cortaduras definida en la construcción por recintos mediante recintos racionales admisibles es idéntica a la suma por testigos de la construcción por testigos. Explica qué sí y qué no demuestra esta comparación.


**Solución razonada.** La suma por testigos es

$$A+_{\mathrm{test}}B=\{q:\exists a\in A,\,b\in B,\ q<a+b\}.$$

La suma por recintos de la construcción por recintos une los conjuntos $C_{a+b}$ cuando $a$ y $b$ son los extremos inferiores de intervalos racionales admisibles de $A$ y $B$. Cada $a\in A$ se puede completar con un exterior $u\notin A$ y cada $b\in B$ con $v\notin B$; se tienen entonces los intervalos admisibles $[a,u]$, $[b,v]$. A la inversa, cualquier intervalo admisible proporciona extremos inferiores pertenecientes a las cortaduras. Luego ambos procedimientos recorren exactamente los mismos pares de testigos y producen

$$\bigcup_{a\in A,b\in B} C_{a+b}=A+_{\mathrm{test}}B.$$

Esta igualdad prueba que **las sumas** coinciden. No verifica por sí misma los axiomas de cuerpo de ninguno de los dos procedimientos ni identifica automáticamente las fórmulas para producto y recíproco. La coincidencia de los productos y los recíprocos se justificará en el tercer apéndice, una vez construidas por separado ambas estructuras de cuerpo ordenado completo. Esa comparación posterior no puede emplearse como premisa de ninguna de las construcciones.


# ¿Qué significa que los reales sean únicos?

La construcción anterior exhibe un cuerpo ordenado completo. Otro modelo podría estar formado por clases de sucesiones o por objetos abstractos con operaciones y orden. La comparación pertinente consiste en construir una correspondencia biyectiva que preserve suma, producto, unidad y orden. El teorema que buscaremos afirma, además, que esa identificación ordenada queda determinada de manera única.

Sean $F$ y $G$ dos cuerpos ordenados completos cualesquiera. La unidad de cada uno genera una copia de los racionales, que nos dará un lenguaje común. Para cada $x\in F$ reuniremos los racionales que quedan por debajo de él, transportaremos sus copias a $G$ y tomaremos allí el supremo. Construir la función exige comprobar que cada conjunto tiene elementos y una cota; demostrar que es un isomorfismo exigirá después transportar las operaciones y el orden.

El momento más delicado será la multiplicación: necesitaremos distinguir un corte completo, su parte positiva y los productos exactos de testigos racionales. La distinción no es una sutileza verbal: de ella depende que las igualdades de conjuntos sean verdaderas.

Fijamos algunas convenciones antes de comenzar. En las demostraciones de este capítulo escribiremos $\mathbb N=\{0,1,2,\ldots\}$ y $\mathbb N_{>0}=\{1,2,\ldots\}$; el denominador natural de una fracción siempre pertenece a este segundo conjunto. Para cualquier cuerpo ordenado $H$ suponemos $0_H\ne1_H$. Esta distinción asegura que el cuerpo no se reduce al objeto de un solo elemento y que las copias positivas de los enteros son no nulas.

## Qué clase de unicidad buscamos

La unicidad buscada se refiere a una identificación que conserva todas las operaciones y el orden. Empezaremos precisando las propiedades de esa función para reconocer qué debemos demostrar sobre la candidata construida mediante supremos.

Un modelo concreto resuelve la existencia. Compararlo con otro modelo exige seguir sus operaciones y su orden a través de una función: los elementos pueden tener presentaciones distintas y, aun así, corresponderse de una manera que respete toda la estructura.

Consideremos dos cuerpos $F,G$ con la propiedad del supremo y busquemos un isomorfismo $\varphi:F\to G$. La analogía con dos tableros de ajedrez expresa la idea: cambiar el material y la apariencia de las piezas no cambia las reglas del juego. La comparación es estructural, aunque una analogía no prueba que dos objetos matemáticos sean isomorfos.

Para precisar la meta hay que demostrar dos cosas. La función será **biyectiva**, de manera que cada elemento de un modelo tenga exactamente un correspondiente en el otro; y preservará suma, producto, unidad y orden. Una correspondencia que olvide cualquiera de estas condiciones podría conservar sólo una parte de la información.
Hay que distinguir la existencia de alguna biyección de la invertibilidad de la función concreta que estamos construyendo. Que dos conjuntos tengan la misma cardinalidad significa que existe al menos una biyección entre ellos, pero no garantiza que nuestra función sea esa biyección. El mapa constante de los naturales en los naturales tiene conjuntos del mismo tamaño y no es invertible. Por eso se comprobará la inyectividad y la sobreyectividad de la aplicación concreta.

## Homomorfismo de cuerpos y orden

Las tres condiciones algebraicas que se escriben son

$$\varphi(a+b)=\varphi(a)+\varphi(b),\qquad \varphi(ab)=\varphi(a)\varphi(b),\qquad \varphi(1_F)=1_G.$$

Las dos primeras deben valer para **todos** $a,b\in F$. Conviene explicar por qué la preservación de la unidad figura como requisito separado. Una función que preserve producto sólo obliga a que su valor en $1_F$ sea idempotente: $e=e^2$. En un cuerpo eso deja dos alternativas, cero y uno. La condición de unidad excluye el mapa que colapsa todo a cero.

En cambio, preservar suma ya fuerza preservar cero: de $0_F+0_F=0_F$ se deduce que $\varphi(0_F)+\varphi(0_F)=\varphi(0_F)$; cancelar en $G$ da $\varphi(0_F)=0_G$. Esta consecuencia de la aditividad se obtiene antes de examinar la multiplicación: no constituye una hipótesis adicional.

El orden también se debe respetar:

$$x<y\iff\varphi(x)<\varphi(y).$$

No se mezclan los elementos de $F$ con los de $G$ en una misma comparación. Cada lado vive en su propio cuerpo. La función es precisamente el medio para relacionarlos.

La prueba completa de que los idempotentes de un cuerpo son sólo cero y uno utiliza $e(e-1)=0$ y la inexistencia de divisores de cero. También se demuestra que un homomorfismo unitario de cuerpos es automáticamente inyectivo. Esto no evita comprobar que nuestra candidata realmente sea tal homomorfismo; anticipar esa conclusión para justificar sus propiedades sería circular.

### Homomorfismos, cero, signos e idempotentes

Un homomorfismo de cuerpos unitario $h:F\to G$ cumple, para todos $a,b\in F$,

$$h(a+b)=h(a)+h(b),\quad h(ab)=h(a)h(b),\quad h(1_F)=1_G.$$

La primera identidad implica $h(0_F)=h(0_F)+h(0_F)$; cancelar en $G$ da $h(0_F)=0_G$. Entonces $h(a)+h(-a)=h(0_F)=0_G$, así que $h(-a)=-h(a)$. Si $a\ne0_F$, $h(a)h(a^{-1})=1_G$, de donde $h(a)\ne0_G$ y $h(a^{-1})=h(a)^{-1}$. Si $h(a)=h(b)$, la aditividad da $h(a-b)=0_G$; cuando $a-b\ne0_F$ la identidad del inverso lo prohíbe. Luego todo homomorfismo unitario entre cuerpos es inyectivo. Esto no necesita completitud ni orden.

Si sólo se suponen suma y producto, $e=h(1_F)$ satisface $e=e^2$. En un cuerpo, $e(e-1_G)=0_G$ implica $e=0_G$ o $e=1_G$: si el primer factor no es cero, multiplicar por su inverso fuerza el segundo a cero. Si $e=0_G$, entonces $h(a)=h(a1_F)=h(a)e=0_G$ para todo $a$. La alternativa es, por tanto, el mapa cero. Exigir unidad excluye esa alternativa. La cancelación multiplicativa se usa sólo con factor no nulo.

Una biyección es una función inyectiva y sobreyectiva; equivale a tener una inversa bilateral. Que dos conjuntos tengan la misma cardinalidad garantiza la **existencia** de alguna biyección, pero no convierte en biyectiva una función dada. Por ejemplo, $f:\mathbb N\to\mathbb N$, $f(n)=0$, tiene dominio y codominio del mismo tamaño y no es biyectiva.

Preservar suma y producto no basta si una aplicación pudiera enviar la unidad a cero: el mapa nulo también respeta ambas operaciones. El análisis de los idempotentes nos muestra por qué la condición $\varphi(1)=1$ es parte de la definición de homomorfismo unitario. La función que construiremos deberá satisfacerla mediante una prueba, no porque decidamos imponerla al resultado.

## Un lenguaje racional común

El siguiente paso consiste en introducir copias de los naturales, enteros y racionales en ambos cuerpos. En cada $H\in\{F,G\}$, el natural $n$ corresponde a sumar $1_H$ consigo mismo $n$ veces. El cero corresponde a $0_H$ y un entero negativo al opuesto del entero positivo correspondiente. Finalmente,

$$\iota_H(m/n)=m_H(n_H)^{-1},\qquad m\in\mathbb Z,\quad n\in\mathbb N_{>0}.$$

El denominador positivo no restringe las fracciones posibles: el signo negativo puede trasladarse al numerador. Pero aún hay una obligación decisiva. Las expresiones $1/2$ y $2/4$ representan el mismo racional; la fórmula debe darles el mismo elemento de $H$. Esa es la buena definición de la aplicación sobre racionales, y comprobarla será esencial para que la aplicación esté bien definida.

**Cómo se justifica la copia racional.** La demostración siguiente establecerá que el cuerpo tiene característica cero, verificará la independencia de la representación fraccionaria y comprobará la compatibilidad con suma, producto y orden. No basta suponer que la repetición de $1_H$ nunca se anule: se demuestra que $1_H>0_H$ y, por tanto, que cada suma positiva lo es.

Además, $\mathbb N$ y $\mathbb Z$ no son cuerpos. En esas etapas se habla respectivamente de una inclusión de semianillos y de anillos, con orden; sólo la etapa racional es un homomorfismo de cuerpos. Esta precisión evita exigir a los naturales un inverso aditivo que no tienen o a los enteros un inverso multiplicativo para cualquier no nulo.

Conservar los símbolos $q$, $q_F$ y $q_G$ sirve para pensar con claridad. El primero es una fracción; los otros dos son sus versiones en modelos diferentes. Que representen la misma cantidad racional no significa que sean literalmente el mismo objeto.

### Construcción completa de las copias racionales

Para un cuerpo ordenado $H$, primero $1_H>0_H$. En efecto, el cuadrado de cualquier elemento no nulo es positivo: si $a>0$, multiplicar $a>0$ por $a$ da $a^2>0$; si $a<0$, $-a>0$ y $a^2=(-a)^2>0$. Aplicar esto a $1_H\ne0_H$ da la afirmación.

Definimos $0_H$ como suma vacía y, para $n>0$, $n_H$ como suma de $n$ copias de $1_H$. Por asociatividad, concatenar sumas da $(m+n)_H=m_H+n_H$ para naturales. Distributividad repetida da $(mn)_H=m_Hn_H$. Si $n>0$, sumar positivos muestra $n_H>0_H$, por lo que no puede anularse. El cuerpo tiene característica cero.

Para un entero negativo $n=-k$, ponemos $n_H=-k_H$. La ley aditiva se extiende a todos los enteros: dados $m,n\in\mathbb Z$, elegir naturales $u,v$ con $m+u,n+v\ge0$. La identidad $m_H+u_H=(m+u)_H$ se obtiene cancelando sumas naturales si $m<0$, y por concatenación si $m\ge0$. Para evitar presuponer la identidad que deseamos demostrar, **comparamos por separado** $(m+n)_H+u_H+v_H$ y $(m_H+n_H)+u_H+v_H$. La primera es $(m+n+u+v)_H$ por la identidad ya establecida entre cualquier entero y un natural que lo deja no negativo; la segunda es $(m+u)_H+(n+v)_H=(m+n+u+v)_H$ por la ley de los naturales. Cancelar $u_H+v_H$ demuestra $(m+n)_H=m_H+n_H$. Para producto, la fórmula de naturales se extiende con $(-a)b=-(ab)$ y $(-a)(-b)=ab$, deducidas por distributividad en el cuerpo: $ab+(-a)b=(a-a)b=0$. De ahí $(mn)_H=m_Hn_H$ para todos los enteros.

Si $m<n$, $(n-m)_H>0$ y $n_H-m_H=(n-m)_H$; por tanto la inclusión de enteros preserva estrictamente el orden y es inyectiva. Reflexiona el orden porque, si $m\ge n$, las alternativas igualdad o desigualdad inversa impiden $m_H<n_H$.

Para $m\in\mathbb Z$, $n\in\mathbb N_{>0}$, definimos

$$\iota_H(m/n)=m_H(n_H)^{-1}.$$

El denominador es positivo y no nulo. Si $m/n=a/b$, con $n,b>0$, entonces $mb=an$. La inclusión entera convierte esto en $m_Hb_H=a_Hn_H$; dividir por $n_Hb_H\ne0$ da la misma imagen racional. Ésta es la buena definición que no se obtiene únicamente escribiendo una fórmula sobre fracciones.

Las operaciones se preservan explícitamente:

$$\iota_H(m/n)+\iota_H(a/b)=\frac{m_Hb_H+a_Hn_H}{n_Hb_H}=\iota_H\bigl((mb+an)/(nb)\bigr),$$
$$\iota_H(m/n)\iota_H(a/b)=\frac{m_Ha_H}{n_Hb_H}=\iota_H(ma/(nb)).$$

La unidad se preserva porque $\iota_H(1)=1_H$. El orden se preserva y refleja multiplicando por los denominadores positivos: $m/n<a/b$ equivale a $mb<an$, que equivale a $m_Hb_H<a_Hn_H$. Esto prueba también inyectividad. Los naturales forman aquí una copia de semianillo ordenado y los enteros de anillo ordenado; **no son cuerpos**. Sólo en $\mathbb Q$ corresponde literalmente hablar de homomorfismo de cuerpos. Escribiremos $q_H=\iota_H(q)$, manteniendo el tipo: $q$ es racional, $q_H$ pertenece a $H$.

Los racionales aparecen como el esqueleto algebraico común a todos los cuerpos ordenados. Para llegar a ellos fue necesario comprobar que la elección de una fracción no altera la imagen; una mera expresión $m_H/n_H$ no constituye una función hasta que se demuestra la independencia de representación. Esta buena definición es el fundamento sobre el que podremos comparar racionales situados en dos cuerpos que, de partida, no comparten elementos.

## La candidata se obtiene por un supremo

La completitud es decisiva en este punto: primero hace arquimedianos a los dos cuerpos y después permite colocar racionales tan cerca como necesitemos de cualquier elemento.

Para $x\in F$, definimos

$$A_x=\{q\in\mathbb Q:q_F<x\}.$$

Este conjunto registra qué racionales quedan por debajo de $x$ en $F$. Sus elementos siguen siendo racionales, no elementos de $F$. Después se transportan esos racionales a $G$ y se toma su supremo:

$$\varphi(x)=\sup_G\{q_G:q\in A_x\}.$$

Aquí están las tres capas del procedimiento: un elemento de $F$ produce un conjunto racional; el conjunto racional produce un subconjunto de $G$; el supremo en $G$ produce un único elemento de llegada. La copia racional funciona como puente entre modelos que inicialmente no tenían ninguna identificación dada.

Para utilizar $A_x$ necesitamos demostrar sus cuatro propiedades de cortadura. También hemos de comprobar que su imagen en $G$ es no vacía y está acotada superiormente. La intuición geométrica no sustituye ninguna de estas verificaciones.

La completitud implica primero que los naturales del cuerpo no están acotados: si tuvieran supremo $u$, alguno superaría $u-1$, y su sucesor superaría $u$. De esta propiedad arquimediana se deriva la densidad racional. Sólo entonces se demuestra que $A_x$ es no vacío, propio, descendente y sin máximo.

Un racional exterior a una cortadura supera a todos sus elementos; su imagen en $G$ proporciona una cota de la imagen. Esto permite tomar el supremo sin afirmar que el conjunto racional tenga supremo en $\mathbb Q$. La completitud aplicada es la de $G$.

Al considerar una expresión como $x+1_F$, debemos respetar el tipo de objeto: tal elemento pertenece a $F$, no necesariamente a la copia racional. Se elige una cota **racional** mediante la propiedad arquimediana; no se llama racional a cualquier expresión de un cuerpo abstracto.

La buena definición incluye existencia para cada entrada, unicidad del supremo y que entradas iguales den salidas iguales. Comprobar sólo esta última condición no bastaría si la expresión no existiera para alguna entrada.

### Completitud implica propiedad arquimediana

Sea $H$ completo. Si $\{n_H:n\in\mathbb N\}$ estuviera acotado superiormente, tendría un supremo $u$. Como $u-1_H<u$, $u-1_H$ no sería cota superior; existe $n$ con $u-1_H<n_H$. Sumar $1_H$ da $u<(n+1)_H$, contradiciendo que $u$ sea cota. Por tanto, para todo $x\in H$ existe $n\in\mathbb N$ con $x<n_H$.

En particular, para todo $\varepsilon>0_H$ existe $n>0$ con $n_H>\varepsilon^{-1}$, y al dividir por positivos se obtiene $0_H<(1/n)_H<\varepsilon$. Esto usa la completitud del cuerpo considerado; no la atribuye a $\mathbb Q$.

### Densidad de la copia racional

Sean $x<y$ en $H$ completo. Por la propiedad arquimediana, existe $n\in\mathbb N_{>0}$ con $1_H<n_H(y-x)$. El conjunto de enteros $m$ tales que $n_Hx<m_H$ es no vacío y está acotado inferiormente: la propiedad arquimediana aplicada a $n_Hx$ y a $-n_Hx$ suministra ambas cotas enteras. Tras trasladarlo por un entero se convierte en un subconjunto no vacío de naturales; el buen orden da un elemento mínimo $m$.

Su minimalidad significa $(m-1)_H\le n_Hx<m_H$. Dividir por $n_H>0$ da

$$x<(m/n)_H\le x+(1/n)_H<y.$$

Así hay un racional $q$ con $x<q_H<y$. También existen racionales estrictamente menores y mayores que cualquier $x$, por la propiedad arquimediana; por ejemplo, si $n_H>|x|+1_H$, sirven $-n$ y $n$. El símbolo $|x|$ significa $\max(x,-x)$ en el orden de $H$. No se intercambian $q\in\mathbb Q$ y $q_H\in H$.

### Cortes y transporte de conjuntos

Para $x\in F$ definimos

$$A_x=\{q\in\mathbb Q:q_F<x\}.$$

Tiene las cuatro propiedades de cortadura inferior. Hay un racional $a$ con $a_F<x$, así que no es vacío; hay un $b$ con $x<b_F$, así que es propio. Si $q\in A_x$ y $r<q$, el orden de la inclusión racional da $r_F<q_F<x$, luego $r\in A_x$. Si $q\in A_x$, la densidad proporciona $r$ con $q_F<r_F<x$; por reflexión del orden $q<r$, y $r\in A_x$. No tiene máximo.

Para cualquier cortadura $A\subseteq\mathbb Q$, si $a\in A$ y $b\notin A$, entonces $a<b$. Igualdad contradice pertenencia; si $b<a$, descenso obligaría a $b\in A$. Por tanto $\iota_G[A]=\{q_G:q\in A\}$ es no vacío y está acotado por $b_G$. No es necesario que $A$ tenga supremo en $\mathbb Q$. Que un subconjunto racional sea **propio**, sin descenso, no implica que esté acotado: los naturales son un contraejemplo. La conclusión utiliza las propiedades de cortadura.

La imagen tampoco tiene máximo: si $q_G$ está en ella, tomar $r>q$ en $A$ da otro elemento $r_G>q_G$. En consecuencia cada elemento de la imagen es estrictamente menor que su supremo en $G$: $q_G<r_G\le\sup_G\iota_G[A]$. Esta es la justificación que permite fortalecer una comparación con un supremo; no vale para cualquier conjunto arbitrario.

### Definición y buena definición de la aplicación

Ponemos

$$\varphi:F\longrightarrow G,\qquad \varphi(x)=\sup_G\iota_G[A_x].$$

La construcción de los perfiles racionales demuestra para **todo** $x\in F$ las dos hipótesis que permiten aplicar la completitud de $G$. El supremo es único: si $u,v$ son ambos mínimos entre las cotas superiores del mismo conjunto, $u\le v$ y $v\le u$, por lo que $u=v$. Así la expresión da exactamente un elemento de $G$ por cada entrada.

Si $x=y$, las condiciones $q_F<x$ y $q_F<y$ son idénticas; luego $A_x=A_y$, sus imágenes coinciden y sus supremos coinciden. Esta comprobación es correcta, pero por sí sola no supliría demostrar existencia del supremo para toda entrada. Se han verificado ambas cosas, sin presuponer que $\varphi$ sea homomorfismo.

### Aproximación al supremo y eliminación de epsilon

Sea $S\subseteq H$ no vacío, acotado superiormente, con supremo $s$. Para cada $\varepsilon>0_H$, $s-\varepsilon<s$ no es cota superior; existe $t\in S$ con

$$s-\varepsilon<t\le s.$$

La última desigualdad puede ser igualdad si el supremo pertenece a $S$. Sólo puede sustituirse por $t<s$ cuando se ha probado que $S$ no tiene máximo, como en los perfiles racionales.

Si $u,v\in H$ satisfacen $u-\varepsilon<v$ para **todo** $\varepsilon>0_H$, entonces $u\le v$. Si $u>v$, elegir $\varepsilon=(u-v)/2>0_H$ daría $u-\varepsilon=(u+v)/2>v$, contradicción. No se sustituye $\varepsilon=0$ en una proposición cuyo dominio exige positividad; se demuestra la conclusión por orden y contradicción. Ninguna de estas dos afirmaciones necesita una teoría de límites.

En esta cadena de resultados, la completitud se usa de manera local y precisa: en cada cuerpo por separado se obtiene primero la propiedad arquimediana y luego la densidad racional. Sólo después se forma el perfil $A_x$ y se transporta a $G$. El supremo que define $\varphi(x)$ existe porque su conjunto de entrada es no vacío y posee una cota superior en $G$; no utilizamos en ningún momento la completitud de $\mathbb Q$, que sabemos falsa. La distinción entre pertenencia, cota y supremo prepara todos los argumentos siguientes.

## El orden identifica posiciones diferentes

Supongamos $x<y$ en $F$. La densidad da un racional $q$ con $x<q_F<y$. Todo racional $p$ de $A_x$ satisface $p_F<x<q_F$; las inclusiones racionales permiten pasar de esa comparación a $p<q$ y después a $p_G<q_G$. Por tanto $q_G$ es una cota de la imagen que define $\varphi(x)$, y

$$\varphi(x)\le q_G.$$

Pero $q\in A_y$. Como $A_y$ no tiene máximo, existe $r\in A_y$ con $q<r$. Al transportarlo,

$$q_G<r_G\le\varphi(y).$$

Combinar las cadenas da $\varphi(x)<\varphi(y)$. La desigualdad estricta no aparece simplemente por tomar supremos: procede del espacio entre $q_G$ y $r_G$.
Un elemento de un conjunto puede ser igual a su supremo si es máximo. En los conjuntos transportados de una cortadura no ocurre, por ausencia de máximo, pero esa propiedad debe haberse establecido. El desarrollo utiliza la comparación no estricta final, que ya basta, y demuestra cuándo puede fortalecerse.

La preservación estricta también permite obtener inyectividad y reflexión del orden por tricotomía. Si las imágenes fueran iguales y las entradas diferentes, una de las entradas sería menor y produciría imágenes estrictamente ordenadas. No hace falta esperar a la sobreyectividad para resolver esta parte.

### Preservación estricta y reflexión del orden

Sean $x<y$ en $F$. Por densidad, elegir $q\in\mathbb Q$ con $x<q_F<y$. Todo $p\in A_x$ cumple $p_F<x<q_F$, luego $p<q$ y $p_G<q_G$. Por tanto $q_G$ es cota superior de $\iota_G[A_x]$ y $\varphi(x)\le q_G$.

Por otro lado, $q\in A_y$, y la ausencia de máximo da un $r\in A_y$ con $q<r$. Entonces

$$\varphi(x)\le q_G<r_G\le\varphi(y),$$

lo que demuestra $\varphi(x)<\varphi(y)$. La desigualdad final no estricta es suficiente. Incluso podría fortalecerse a $r_G<\varphi(y)$ porque el conjunto de racionales que define ese supremo carece de máximo.

Si $\varphi(x)<\varphi(y)$, no puede ser $x=y$, porque las imágenes serían iguales; tampoco $y<x$, porque lo demostrado daría la desigualdad inversa. La totalidad del orden obliga a $x<y$. Así se obtiene ambas direcciones sin esperar a demostrar sobreyectividad. Si $\varphi(x)=\varphi(y)$, $x<y$ o $y<x$ darían imágenes distintas; por tanto $x=y$ y la función es inyectiva.

Dos posiciones distintas en un cuerpo completo pueden separarse mediante un racional. La función que hemos definido conserva esa separación, de modo que no puede identificar dos entradas diferentes. Ésta es una prueba auténtica de inyectividad, independiente de la sobreyectividad que todavía no conocemos. Además muestra por qué el orden no es un adorno de la estructura: es el mecanismo que impide que dos elementos se confundan bajo la correspondencia.

## Primero sumar cortes

Para demostrar aditividad se comienza en el nivel racional. La suma de dos conjuntos se define mediante sumas de sus elementos:

$$A_x+A_y=\{p+r:p\in A_x,r\in A_y\}.$$

El objetivo intermedio es $A_{x+y}=A_x+A_y$. Una suma $p+r$ del lado derecho cumple $(p+r)_F=p_F+r_F<x+y$, así que pertenece al lado izquierdo.

Para la dirección difícil, tomar $q_F<x+y$ y medir la holgura exacta

$$\varepsilon=x+y-q_F>0_F.$$

La densidad permite elegir $p_F$ entre $x-\varepsilon/2$ y $x$, y $r_F$ entre $y-\varepsilon/2$ y $y$. Al sumar se obtiene $q_F<p_F+r_F$, luego $q<p+r$.
Como la suma se definió por representaciones exactas, falta explicar por qué esa desigualdad incorpora a $q$. El descenso de $A_x$ da $q-r<p\in A_x$, por lo que $q-r\in A_x$; ahora $q=(q-r)+r$ es una representación exacta. Esta comprobación hace explícita la equivalencia entre suma de Minkowski y suma por testigos estrictos. Se demuestra también que la suma de dos cortaduras sigue siendo cortadura.

Pensar la estrategia consiste en repartir una holgura, no en adivinar los racionales exactos. Las dos elecciones usan la misma cantidad positiva $\varepsilon/2$ y cada testigo conserva la condición de pertenencia a su propio corte.

### Suma de cortes: igualdad y cierre

Para dos cortaduras $A,B$ definimos la suma de Minkowski

$$A+B=\{a+b:a\in A,\ b\in B\}.$$

Es no vacía por elegir un elemento de cada conjunto. Si $u\notin A$, $v\notin B$, toda suma $a+b$ es menor que $u+v$, que por ello no está en la suma; ésta es propia. Si $t<a+b$, entonces $t-b<a$, por descenso $t-b\in A$ y $t=(t-b)+b$ está en la suma. Si $a+b$ está en ella, elegir $a'>a$ en $A$ proporciona $a'+b>a+b$ en la misma suma. Se cumplen las cuatro condiciones, incluida la ausencia de máximo.

Además,

$$A+B=\{q\in\mathbb Q:\exists a\in A\ \exists b\in B\quad q<a+b\}.$$

Para $q<a+b$, el descenso prueba $q-b\in A$ y da una representación exacta de $q$. Para $q=a+b$, aumentar $a$ dentro de $A$ proporciona un testigo estricto. Esto explica la equivalencia entre la forma por testigos y la suma de Minkowski. Pasar de una desigualdad estricta a una representación exacta requiere precisamente esa equivalencia; ninguna notación permite omitir la justificación.

Para $x,y\in F$, cada $a\in A_x$, $b\in A_y$ satisface $a_F+b_F<x+y$, así que $A_x+A_y\subseteq A_{x+y}$. A la inversa, si $q\in A_{x+y}$, definir en $F$ $\varepsilon=x+y-q_F>0_F$. Por densidad elegir racionales $a,b$ con

$$x-\varepsilon/2<a_F<x,\qquad y-\varepsilon/2<b_F<y.$$

Sumar da $q_F<a_F+b_F<x+y$, y reflexión del orden racional da $q<a+b$. La equivalencia anterior coloca $q$ en la suma. Se prueba

$$A_{x+y}=A_x+A_y.$$

Las cotas estrictas de cada testigo, no la sola cota de su suma, garantizan pertenencia individual.

La igualdad de los cortes de una suma es una afirmación sobre conjuntos de racionales, no sobre supremos. La hemos justificado repartiendo una holgura positiva entre dos elecciones racionales y corrigiendo después una desigualdad estricta hasta obtener una representación exacta. Se necesitará todavía otra prueba para transportar esa identidad a la suma de sus supremos. Separar ambos pasos impide que un salto notacional esconda la verdadera dificultad.

## Después sumar supremos

La identidad racional anterior debe pasar al nivel de $G$. Para conjuntos no vacíos acotados $S,T$, se demuestra

$$\sup(S+T)=\sup S+\sup T.$$

La suma de los supremos es cota de todas las sumas de elementos. Para demostrar que es la menor, se buscan elementos a menos de $\varepsilon/2$ de cada supremo, por debajo. Su suma queda por encima de $\sup S+\sup T-\varepsilon$. Como esto vale para todo $\varepsilon>0$, el supremo de las sumas no puede ser menor que la suma de los supremos.

El paso final no consiste en sustituir $\varepsilon=0$, pues la hipótesis sólo vale para epsilon positivo. Si $u-\varepsilon<v$ para todo epsilon positivo y fuera $u>v$, elegir $(u-v)/2$ contradice la desigualdad. Esa prueba es válida en el cuerpo ordenado y no necesita introducir un límite.

Aplicando la identidad a las imágenes de $A_x,A_y$, y usando que la inclusión racional preserva suma, se concluye

$$\varphi(x+y)=\varphi(x)+\varphi(y).$$

Aquí se distinguen tres identidades: igualdad de cortes, igualdad de imágenes de sumas y fórmula del supremo. Omitir una de ellas puede hacer que una cadena correcta parezca una sustitución meramente simbólica. La aditividad permite ya deducir $\varphi(0)=0$ y $\varphi(-x)=-\varphi(x)$, que se necesitarán para tratar los signos del producto.

### Supremo de una suma de conjuntos

Sean $S,T\subseteq H$ no vacíos y acotados superiormente, con $s=\sup S$, $t=\sup T$. El conjunto $S+T=\{a+b:a\in S,b\in T\}$ es no vacío; $s+t$ es una cota, porque $a\le s$, $b\le t$. Su supremo $u$ existe y $u\le s+t$.

Para cualquier $\varepsilon>0_H$, el lema de aproximación al supremo da $a>s-\varepsilon/2$ y $b>t-\varepsilon/2$, con $a\in S,b\in T$. Por tanto $s+t-\varepsilon<a+b\le u$. La conclusión para **toda** tolerancia positiva excluye que $s+t$ supere a $u$: si así fuera, elegir la mitad de su diferencia positiva contradice la desigualdad anterior. Por tanto $s+t\le u$. Ambas desigualdades prueban

$$\sup_H(S+T)=\sup_H S+\sup_H T.$$

La existencia de testigos simultáneos se obtiene aplicando por separado el mismo epsilon positivo a ambos conjuntos. No se supone que alguno alcance su supremo, ni se requiere positividad de $s,t$.

### Aditividad, cero y opuestos de phi

La inclusión racional de $G$ preserva suma, de modo que

$$\iota_G[A_x+A_y]=\iota_G[A_x]+\iota_G[A_y].$$

Esto es igualdad de conjuntos: una representación $q=a+b$ da $q_G=a_G+b_G$, y cada suma de dos imágenes procede de esa representación. Aplicando la suma de cortes y la identidad del supremo de una suma,

$$\varphi(x+y)=\sup_G\iota_G[A_{x+y}]=\sup_G\bigl(\iota_G[A_x]+\iota_G[A_y]\bigr)=\varphi(x)+\varphi(y).$$

En particular, $\varphi(0_F)=\varphi(0_F)+\varphi(0_F)$ y cancelar da $\varphi(0_F)=0_G$. De $x+(-x)=0_F$ se deduce $\varphi(-x)=-\varphi(x)$. Estos hechos se usan luego para extender el producto a otros signos; no dependen de que ya se haya demostrado multiplicatividad.

El supremo de un conjunto de sumas es la suma de los supremos aunque ninguno de los conjuntos alcance su propia cota mínima. El argumento trabaja con dos aproximaciones simultáneas y elimina la tolerancia positiva mediante contradicción; no la sustituye fraudulentamente por cero. La aplicación $\varphi$ es ya aditiva, lo que nos permite conocer sus valores en cero y en los opuestos antes de abordar el producto con signos arbitrarios.

## La parte positiva exige cambiar de dominio

Hemos terminado la prueba de aditividad en dos etapas: primero identificamos el corte de una suma y después transportamos esa identidad mediante el supremo. El producto exige una nueva preparación. Ahora importan los signos de los factores y el dominio de los racionales que utilizaremos como testigos.

Para el producto se empieza con $x,y>0_F$ y se consideran

$$A_x^+=\{q\in A_x:q>0\},\qquad A_y^+=\{q\in A_y:q>0\}.$$

Eliminar los elementos no positivos no cambia los supremos de sus imágenes: hay elementos positivos en cada conjunto, y cualquier cota de esos elementos positivos también supera a todos los no positivos. La parte positiva simplifica los multiplicadores sin perder la información que se busca.
Estas partes positivas no son cortaduras inferiores de todo $\mathbb Q$: no contienen negativos que están por debajo de cualquiera de sus elementos. Para usar completitud sólo hace falta demostrar que sus imágenes son no vacías y acotadas.

Además deben distinguirse el conjunto $U$ de **todos** los racionales menores que algún producto $pr$ y su parte positiva $P=U\cap\mathbb Q_{>0}$. Si la fórmula escrita permite $q\in\mathbb Q$, incluye negativos y cero; no puede ser igual a $A_{xy}^+$, que contiene sólo positivos. La distinción de dominios evita identificar el corte completo de un producto con su parte estrictamente positiva.

### Partes positivas y conservación de las cotas

Para $x>0_F$, ponemos

$$A_x^+=\{q\in A_x:q>0\},\qquad S_x=\iota_G[A_x^+].$$

La densidad entre $0_F$ y $x$ garantiza que $A_x^+$ y $S_x$ sean no vacíos. Están acotados porque son subconjuntos de $A_x$ y de su imagen. Todos los elementos de $S_x$ son positivos. Si $u$ es cota superior de $S_x$, elegir un $s_0\in S_x$ da $u\ge s_0>0_G$; así $u$ también supera a todos los elementos no positivos de $\iota_G[A_x]$. Por tanto los dos conjuntos tienen exactamente las mismas cotas superiores y

$$\sup_G S_x=\sup_G\iota_G[A_x]=\varphi(x)>0_G.$$

La positividad también puede deducirse del orden estricto ya demostrado y de la aditividad de la **aplicación todavía en construcción**; la prueba directa mediante un testigo resulta útil porque no necesita invocar esas propiedades para justificar los lemas del producto.

**El dominio de la parte positiva.** Si $q>0$ pertenece a $A_x^+$, entonces $-1<q$ pero $-1\notin A_x^+$. Falla el cierre descendente en todo $\mathbb Q$. Puede ser descendente **dentro de los positivos**; ése es otro dominio. No hace falta llamarla cortadura para que su imagen tenga supremo: bastan no vacuidad y cota.

La positividad nos da libertad para multiplicar desigualdades sin invertir su sentido, pero exige una precisión sobre el dominio: $A_x^+$ no es una cortadura descendente de todos los racionales. La construcción no la necesita como tal. Basta que su imagen tenga supremo y comparta sus cotas con el corte completo. Este es el primer puente del producto, y no debemos confundirlo con la multiplicatividad que todavía vamos a demostrar.

## Escalar y aplanar supremos

Para relacionar $S_x=\iota_G[A_x^+]$ y $S_y=\iota_G[A_y^+]$ con el supremo de sus productos, demostraremos primero el lema

$$c\sup S=\sup(cS),\qquad c>0.$$

La prueba completa del lema aparece a continuación. Su importancia es que permite reescribir $\varphi(x)\varphi(y)$ como un supremo de productos de elementos de $S_x,S_y$, sin presuponer la multiplicatividad de la función que buscamos demostrar.

El lema puede leerse examinando una cota superior arbitraria. Si $u$ acota todos los $cs$, dividir por $c>0$ muestra que $u/c$ acota $S$; la minimalidad de $\sup S$ implica $c\sup S\le u$. Este paso utiliza simultáneamente la existencia del inverso del factor positivo y la conservación del orden; su prueba completa y sistemática se presenta a continuación.

Aplicamos el lema dos veces y obtenemos supremos anidados. Para eliminar la anidación hay otra obligación: la unión de una familia de conjuntos y el conjunto de sus supremos tienen las mismas cotas cuando todos los conjuntos son no vacíos y comparten una cota. Se demuestra ese hecho antes de escribir el supremo del conjunto de todos los productos.

Así se obtiene

$$\varphi(x)\varphi(y)=\sup_G\{p_Gr_G:p\in A_x^+,r\in A_y^+\}.$$

Esta igualdad sólo usa el orden y las operaciones ya existentes en $G$; no anticipa que phi preserve productos. Los factores de cada aplicación del lema son positivos, porque proceden de las partes positivas o de sus supremos no vacíos.

### Escalamiento del supremo

Sean $c>0_H$ y $S\subseteq H$ no vacío, acotado superiormente. Si $s=\sup S$, todo $a\in S$ satisface $ca\le cs$, así que $cs$ es cota de $cS=\{ca:a\in S\}$. Si $u$ es cualquier cota de $cS$, $ca\le u$ para todo $a\in S$; dividir por $c>0$ da $a\le u/c$. Como $s$ es mínima cota, $s\le u/c$ y $cs\le u$. Esto prueba

$$\sup(cS)=c\sup S.$$

No se supone previamente continuidad de la multiplicación. La división y la conservación del sentido de la desigualdad se justifican por $c>0$. Para $c=0$, $cS=\{0\}$ y la identidad vale por comprobación directa, pero no por la prueba que divide por $c$. Para $c<0$, no vale en general: $S=\{0,1\}$, $c=-1$ da $c\sup S=-1$ y $\sup(cS)=0$. El cambio de signo intercambia cotas superiores e inferiores, no conserva supremos indiscriminadamente.

### Supremos anidados y producto de conjuntos positivos

Sea una familia no vacía $(E_t)_{t\in T}$ de subconjuntos no vacíos de $H$, cuya unión $E$ tenga una cota común $M$. Cada $e_t=\sup E_t$ existe y $e_t\le M$. Una cantidad $u\in H$ es cota de $E$ si y sólo si lo es de todos los $E_t$, si y sólo si $e_t\le u$ para todo $t$. Las cotas de $E$ coinciden con las del conjunto $\{e_t:t\in T\}$. Ambos son no vacíos y acotados, de modo que

$$\sup_{t\in T}\sup E_t=\sup\bigcup_{t\in T}E_t.$$

Esto es una prueba de igualdad de supremos, **no** de igualdad entre la colección de supremos y la unión de todos los conjuntos.

Ahora sean $S,T\subseteq H_{>0}$ no vacíos, acotados, y $s=\sup S>0$, $t=\sup T>0$. Cada producto $ab$ con $a\in S,b\in T$ satisface $0<ab\le st$, por multiplicación de desigualdades por positivos. Por el lema del escalamiento positivo,

$$st=\sup(sT)=\sup_{b\in T}(sb)=\sup_{b\in T}\sup(bS).$$

La unión de $bS$ está no vacía y acotada por $st$. El resultado anterior prueba

$$st=\sup\{ab:a\in S,b\in T\}.$$

Cada aplicación de escalamiento tiene coeficiente positivo: primero $s>0$, después cada $b>0$. No se utiliza la fórmula del producto de phi para demostrar esta identidad: sólo los axiomas de $H$ y el lema ya probado.

Al multiplicar supremos no estamos aplicando una presunta continuidad del producto. Hemos probado directamente la compatibilidad de los supremos con el escalamiento por positivos y hemos justificado cómo reunir una familia de supremos anidados. Con esos resultados, el producto de las imágenes queda reducido al supremo de productos racionales positivos. Falta identificar esos productos con el corte que corresponde a $xy$.

## El producto exige dos puentes

Las dos identidades que siguen responden a preguntas distintas. La primera describe **qué racionales** pertenecen al corte asociado a $xy$; la segunda demuestra que los racionales estrictamente inferiores a productos y los productos racionales exactos determinan el mismo supremo en $G$. Una descripción de pertenencia no sustituye automáticamente una igualdad de supremos, por lo que probaremos ambas.

La demostración del producto merece una precaución extra. Los racionales negativos pertenecen al corte completo, pero no a su parte positiva; la distinción cambiará el dominio de algunas igualdades.

Se quiere relacionar las partes positivas de los cortes con el corte de $xy$. Si $0<q<pr$, con $p_F<x$, $r_F<y$ y ambos testigos positivos, entonces $0<q_F<xy$. Esta dirección utiliza multiplicación de desigualdades únicamente por positivos.

Para la dirección inversa, de $0<q_F<xy$ se divide primero por $x>0$. Entre $q_F/x$ e $y$ se elige un racional transportado $r_F$. Después se divide por $r_F>0$ y se elige $p_F$ entre $q_F/r_F$ y $x$. El resultado es $q_F<p_Fr_F$, o $q<pr$. Los dos denominadores están controlados antes de usarlos; no hace falta suponer $x<y$.

Esto demuestra, con dominio positivo explícito,

$$A_{xy}^+=\{q\in\mathbb Q_{>0}:\exists p\in A_x^+\ \exists r\in A_y^+\ q<pr\}.$$

Todavía hay un segundo puente. La expresión anterior contiene racionales **menores que** productos, mientras el supremo obtenido en el tramo previo utiliza los productos mismos. Identificar ambas definiciones sin prueba deja un hueco.

Si una cantidad acota los productos, acota también todos los racionales inferiores transportados. Para la otra dirección, si una cota de esos racionales fuera menor que algún producto positivo, la densidad racional en $G$ permitiría encontrar un racional positivo entre la cota y el producto. Ese racional pertenece al conjunto de cotas estrictas y contradice que la cantidad lo acote. Por tanto los dos conjuntos tienen las mismas cotas y el mismo supremo.

Combinar los dos puentes da

$$\varphi(xy)=\varphi(x)\varphi(y)\qquad(x,y>0_F).$$

Una vez demostrado el producto para factores positivos, debemos extenderlo a todos los signos, incluido el cero. Un factor cero da cero en ambos lados. Un factor negativo se escribe como opuesto de uno positivo y se usa la preservación del opuesto, deducida de la aditividad. Dos factores negativos dan producto positivo; la regla de signos en los cuerpos reduce el caso al ya demostrado. No se aplica a negativos el lema de escalamiento positivo.

### Producto racional: conjunto completo y parte positiva

Para $x,y>0_F$, conviene distinguir

$$U=\{q\in\mathbb Q:\exists a\in A_x^+\ \exists b\in A_y^+\quad q<ab\},$$
$$P=U\cap\mathbb Q_{>0}.$$

El primero contiene todos los negativos y cero; el segundo no contiene ninguno. No pueden confundirse. Probaremos $U=A_{xy}$ y $P=A_{xy}^+$.

Si $q<ab$, las imágenes de los testigos cumplen $0<a_F<x$ y $0<b_F<y$. Multiplicar sólo por positivos da $a_Fb_F<xy$, luego $q_F<xy$ y $q\in A_{xy}$. Para $q\le0$, la pertenencia a $U$ se obtiene eligiendo cualquier par de testigos positivos, disponible por el análisis de partes positivas; su producto es positivo y supera $q$.

Si $0<q_F<xy$, dividir por $x>0_F$ da $0<q_F/x<y$. La densidad permite elegir $b\in\mathbb Q$ con

$$0<q_F/x<b_F<y.$$

Entonces $b>0$ y $b\in A_y^+$. De $q_F<xb_F$, dividir por $b_F>0$ da $0<q_F/b_F<x$. Elegir ahora $a\in\mathbb Q$ con

$$0<q_F/b_F<a_F<x$$

da $a\in A_x^+$ y $q_F<a_Fb_F=(ab)_F$. Reflexionar el orden racional da $q<ab$. Así todos los positivos de $A_{xy}$ pertenecen a $P$. Los otros racionales de $A_{xy}$ son no positivos y ya se trataron; se prueban ambas igualdades.

Por los perfiles racionales, $U$ es una cortadura, pues es $A_{xy}$. $P$ no lo es en todo $\mathbb Q$, pero su imagen es no vacía y acotada, y tiene el mismo supremo que la de $U$. La condición $q>0$ es indispensable cuando el objetivo es $A_{xy}^+$; sin ella la fórmula representa el corte completo $A_{xy}$. El argumento anterior obtiene los testigos mediante dos divisiones positivas y justifica cada paso.

### Productos exactos y cotas estrictas: multiplicatividad positiva

El conjunto de productos exactos en $G$ es

$$V=\{a_Gb_G:a\in A_x^+,b\in A_y^+\}.$$

Por el producto de supremos positivos, $\sup V=\varphi(x)\varphi(y)$. En cambio, $\iota_G[P]$ está formado por imágenes de racionales **estrictamente menores** que algún $ab$. Los conjuntos no son por definición iguales. Demostremos que tienen las mismas cotas.

Si $u$ es cota de $V$ y $q\in P$, hay $a,b$ con $q<ab$; entonces $q_G<a_Gb_G\le u$, por lo que $u$ es cota de $\iota_G[P]$.

Si $u$ es cota de $\iota_G[P]$ y existiera $v=a_Gb_G\in V$ con $u<v$, como $v>0_G$ tendríamos $\max(u,0_G)<v$. La densidad en $G$ daría un racional $q$ con

$$\max(u,0_G)<q_G<v=(ab)_G.$$

Reflexionar el orden racional prueba $0<q<ab$, luego $q\in P$, contradiciendo $q_G>u$. Por tanto $u$ es cota de $V$. Ambos conjuntos son no vacíos y acotados; sus supremos coinciden.

También se puede demostrar la igualdad de conjuntos una vez corregido el dominio positivo. Si $q\in P$ y $q<ab$, poner $a'=q/b$ da un racional positivo menor que $a$; el descenso de $A_x$ implica $a'\in A_x^+$ y $q=a' b$. Por tanto $q_G\in V$. Si $a_Gb_G\in V$, la ausencia de máximo de $A_x$ permite $a'>a$ todavía en $A_x^+$; como $b>0$, $ab<a' b$ y $ab\in P$. Luego $V=\iota_G[P]$. La igualdad de conjuntos queda ahora justificada por la equivalencia de testigos, no por una identificación intuitiva de expresiones diferentes. La prueba por cotas anterior ofrece otra justificación completa.

El análisis de partes positivas y el corte de productos racionales dan ahora

$$\varphi(xy)=\sup_G\iota_G[A_{xy}^+]=\sup_G\iota_G[P]=\sup_G V=\varphi(x)\varphi(y)\quad(x,y>0_F).$$

El tránsito por supremos queda así completo. La igualdad de supremos entre productos y sus cotas estrictas es un paso adicional indispensable, no una identificación automática de elementos.

### Extensión a cero y a todos los signos

La aditividad ya probada da $\varphi(0_F)=0_G$ y $\varphi(-x)=-\varphi(x)$. Si uno de $x,y$ es cero, ambos lados de $\varphi(xy)=\varphi(x)\varphi(y)$ son cero por los axiomas de cuerpo.

Si $x<0<y$, poner $a=-x>0$, $b=y>0$. Entonces $xy=-(ab)$ y

$$\varphi(xy)=-\varphi(ab)=-\varphi(a)\varphi(b)=\varphi(x)\varphi(y).$$

Si $y<0<x$, intercambiar los factores, usando conmutatividad en $F$ y en $G$. Si ambos son negativos, poner $a=-x>0$, $b=-y>0$; $xy=ab$ y

$$\varphi(xy)=\varphi(a)\varphi(b)=(-\varphi(x))(-\varphi(y))=\varphi(x)\varphi(y).$$

Si ambos son positivos se aplica la multiplicatividad positiva. La tricotomía de cada factor cubre todos los casos. No se usa preservación del producto con negativos para demostrar previamente preservación del opuesto.

La multiplicación requería dos puentes distintos. El primero identifica cuáles racionales positivos están estrictamente bajo un producto; el segundo compara esos racionales con los productos exactos de testigos, sin tratarlos como iguales por definición. Las dos inclusiones se han demostrado y todas las divisiones tienen denominadores positivos. Solo entonces es legítimo concluir que la función conserva el producto; los casos de cero y signo diferente se reducen, gracias a la aditividad, al positivo.

## La unidad y el homomorfismo

La multiplicatividad, que ya incluye el caso $1_F\cdot1_F$, implica que $\varphi(1_F)$ es idempotente. Sólo puede ser cero o uno. Como se ha demostrado aditividad, $\varphi(0_F)=0_G$. La preservación estricta del orden da

$$0_G=\varphi(0_F)<\varphi(1_F).$$

Queda excluido cero y se concluye $\varphi(1_F)=1_G$. Phi es ahora un homomorfismo unitario que preserva y refleja orden.

La condición de unidad no se impuso arbitrariamente a la fórmula del supremo. Se obtuvo de sus propiedades. El orden de la prueba importa: aditividad permite conocer el cero; producto permite conocer idempotencia; orden permite elegir la alternativa correcta.

### Unidad, homomorfismo y racionales fijos

Como $1_F>0_F$, la multiplicatividad positiva, o la ya extendida, da $e=\varphi(1_F)=\varphi(1_F)^2$. La caracterización de los idempotentes, demostrada al comienzo del capítulo, muestra que $e$ es cero o uno en $G$. La preservación estricta del orden y la aditividad de $\varphi$, obtenidas antes de tratar la unidad, dan

$$0_G=\varphi(0_F)<\varphi(1_F)=e.$$

La alternativa cero queda excluida, de modo que $\varphi(1_F)=1_G$. Junto con aditividad y multiplicatividad, $\varphi$ es un homomorfismo de cuerpos unitario, que además preserva y refleja el orden. La preservación de la unidad queda así deducida, no añadida como requisito arbitrario.

Cualquier homomorfismo unitario $h:F\to G$ fija las copias racionales: preservar $1$ y sumar repetidamente da $h(n_F)=n_G$; preservar cero y opuestos extiende a enteros; preservar inversos no nulos da

$$h((m/n)_F)=m_G(n_G)^{-1}=(m/n)_G.$$

El denominador nunca es cero por característica cero. No se identifica literalmente una fracción con los elementos abstractos de ambos cuerpos.

El valor de la unidad no es un detalle menor. Una aplicación aditiva y multiplicativa podría seguir siendo la aplicación nula; el orden descarta esa posibilidad porque la imagen de uno es estrictamente positiva. Así tenemos un homomorfismo unitario, además de una función inyectiva y estrictamente creciente. Para obtener un isomorfismo todavía debemos probar que todos los elementos de $G$ se alcanzan.

## Cada elemento de G tiene una preimagen

Al conocer la unidad y el orden, queda una última obligación: demostrar que ningún elemento del cuerpo de llegada ha quedado fuera de la imagen.

La inyectividad se deduce de la preservación estricta del orden. Para la sobreyectividad, dado $y\in G$, se construye el corte inverso

$$B_y=\{q\in\mathbb Q:q_G<y\},\qquad x=\sup_F\{q_F:q\in B_y\}.$$

Las mismas comprobaciones de cortadura y de cota permiten tomar este supremo en $F$. El objetivo intermedio es $A_x=B_y$.

Si $q\in B_y$, escoger $r>q$ también en $B_y$ da $q_F<r_F\le x$, luego $q\in A_x$. Para la inclusión contraria, usamos la contraposición: si $q\notin B_y$, todos los racionales $r\in B_y$ son menores que $q$, así que $q_F$ acota sus imágenes y $x\le q_F$. Por tanto $q\notin A_x$. Las dos inclusiones prueban igualdad.

Entonces

$$\varphi(x)=\sup_G\iota_G[A_x]=\sup_G\iota_G[B_y]=y.$$
La última igualdad requiere densidad. Que todos los elementos de un conjunto estén por debajo de $y$ sólo muestra que $y$ es cota, no que sea mínima. Pero cualquier $z<y$ deja, por densidad, un $q_G$ entre ambos; ese elemento pertenece a la imagen y supera $z$. Ningún valor menor que $y$ puede acotar el conjunto. Por eso $y$ es el supremo.

Cada $y$ tiene preimagen, y la inyectividad garantiza que es única. Phi es una biyección y un homomorfismo ordenado: es el isomorfismo buscado.

### Sobreyectividad mediante el corte inverso

Dado $y\in G$, definimos

$$B_y=\{q\in\mathbb Q:q_G<y\},\qquad x=\sup_F\iota_F[B_y].$$

Aplicar los perfiles racionales intercambiando $F,G$ demuestra que $B_y$ es cortadura y su imagen en $F$ es no vacía y acotada; el supremo $x$ existe. Probaremos $A_x=B_y$.

Si $q\in B_y$, la ausencia de máximo permite $r\in B_y$ con $q<r$. Entonces $q_F<r_F\le x$, así que $q\in A_x$.

Para la otra inclusión usamos la contraposición, con dominio $q\in\mathbb Q$. Si $q\notin B_y$, $q_G\ge y$. Para todo $r\in B_y$, $r_G<y\le q_G$, por reflexión del orden $r<q$. Así $q_F$ es cota superior de $\iota_F[B_y]$, y $x\le q_F$. No se cumple $q_F<x$, luego $q\notin A_x$. Esta contraposición prueba $A_x\subseteq B_y$.

Por tanto

$$\varphi(x)=\sup_G\iota_G[A_x]=\sup_G\iota_G[B_y].$$

El último supremo es $y$, pero **no** basta decir que todos sus elementos sean menores que $y$. $y$ es cota. Si $z<y$, la densidad da un racional $q$ con $z<q_G<y$, que pertenece a la imagen; luego $z$ no es cota. Por totalidad del orden, ninguna cota puede ser menor que $y$, y $y$ es la mínima. Así $\varphi(x)=y$.

Hemos producido una preimagen para **cada** $y\in G$. La función es sobreyectiva e inyectiva por la preservación del orden, por tanto biyectiva; junto con la conservación de la unidad es un isomorfismo de cuerpos ordenados. Su inversa es el mismo procedimiento en sentido contrario: $y\mapsto\sup_F\iota_F[B_y]$. Las dos identidades de inversa se deducen de que produce una preimagen y de la inyectividad.

El perfil racional inverso proporciona una entrada para cada elemento del cuerpo de llegada. Para cada $y$ del cuerpo de llegada producimos una entrada $x$ tomando ahora un supremo en $F$; la igualdad de perfiles demuestra que $\varphi(x)=y$. Esto da sobreyectividad. La función queda caracterizada por la totalidad de sus racionales inferiores; por eso puede demostrarse, como resultado adicional, la unicidad de la identificación ordenada.

## Por qué la identificación ordenada es única

Dos cuerpos ordenados completos tienen la misma estructura hasta isomorfismo. Esto se combina con la existencia obtenida al construir las cortaduras para justificar la caracterización axiomática de los números reales. La prueba de unicidad no vuelve a definir las operaciones sobre cortaduras: trabaja directamente con las operaciones ya dadas en $F$ y $G$.

Se puede demostrar además que la identificación ordenada es única. Cualquier isomorfismo unitario fija los racionales: preserva uno, sus sumas enteras y sus cocientes no nulos. Si también preserva y refleja orden, un elemento $x$ y su imagen tienen exactamente los mismos racionales por debajo. La densidad hace que ese conjunto determine un único elemento en $G$. Por eso cualquier identificación ordenada coincide con la aplicación del supremo construida por supremos.

Ahora podemos distinguir dos afirmaciones. Haber construido un isomorfismo demuestra que los dos cuerpos comparten estructura; demostrar que no existe otro isomorfismo ordenado compatible con las operaciones refuerza esa conclusión. La segunda cuestión se resolverá comparando perfiles racionales inferiores.

### El perfil racional determina la identificación

Hemos probado que dos cuerpos ordenados completos son isomorfos. Esto expresa unicidad **hasta isomorfismo**, no igualdad literal de conjuntos. La existencia de un modelo proviene de la construcción previa; aquí se parte de dos modelos cualesquiera que satisfacen los axiomas y se demuestra que su estructura es la misma.

Podemos demostrar algo más: el isomorfismo **ordenado** es único. Si $h:F\to G$ es otro isomorfismo que preserva y refleja orden, la conservación de la unidad demuestra que fija las copias racionales. Para cada $x\in F$ y cada racional $q$,

$$q_F<x\iff h(q_F)<h(x)\iff q_G<h(x).$$

Así $A_x=B_{h(x)}$. Por la caracterización de la sobreyectividad por el corte inverso, $\sup_G\iota_G[B_{h(x)}]=h(x)$; por definición de $\varphi$, la misma expresión es $\varphi(x)$. Luego $h(x)=\varphi(x)$ para todo $x$, y $h=\varphi$.

La demostración no presupuso un isomorfismo para transportar supremos, no usó la multiplicatividad de phi para demostrar la densidad, y no convirtió la completitud de $F$ o $G$ en completitud de $\mathbb Q$. La propiedad arquimediana y la densidad racional se deducen de los axiomas de cada cuerpo completo antes de construir los cortes. El supremo en $G$ se usa al construir phi; el supremo en $F$ se usa al construir la preimagen. Esta dependencia explica exactamente por qué se requieren completos **ambos** cuerpos.

Hay que distinguir dos tesis. Que dos cuerpos completos sean isomorfos garantiza la existencia de una identificación estructural; que el isomorfismo ordenado sea único dice además que no tenemos libertad para emparejar sus elementos de otra manera si queremos conservar las operaciones, la unidad y el orden. El perfil racional inferior fuerza cada correspondencia individual. Esta conclusión cierra el problema abierto por la definición axiomática del primer capítulo.

## Problemas y soluciones del capítulo

### Ejercicio 1

Sea $h:F\to G$ una aplicación que preserva suma y producto, pero no suponemos $h(1_F)=1_G$. Demuestra que $h$ es la función cero o es un homomorfismo unitario inyectivo. ¿Dónde se utiliza que $G$ sea un cuerpo?

**Solución razonada.** La preservación aditiva implica $h(0_F)=h(0_F)+h(0_F)$; cancelar da $h(0_F)=0_G$. Poniendo $e=h(1_F)$, la preservación del producto produce $e^2=e$, es decir, $e(e-1_G)=0_G$. Como $G$ es cuerpo, no tiene divisores de cero: o $e=0_G$ o $e=1_G$. Si $e=0_G$, para todo $a\in F$ se tiene $h(a)=h(a1_F)=h(a)e=0_G$; $h$ es cero. Si $e=1_G$, $h$ es unitario. Si $h(a)=h(b)$, entonces $h(a-b)=0_G$. Para $a\ne b$, el elemento $a-b$ es no nulo, y la igualdad $h(a-b)h((a-b)^{-1})=1_G$ contradice $h(a-b)=0_G$. Luego $a=b$. **Mecanismo:** la cancelación descarta la imagen nula de un invertible. No utilizamos orden ni completitud.

### Ejercicio 2

Explica por qué la igualdad de cardinalidad de $F$ y $G$ no demuestra que una aplicación propuesta $h:F\to G$ sea biyectiva. Produce un ejemplo entre dos conjuntos infinitos del mismo tamaño que falle tanto en inyectividad como en sobreyectividad.

**Solución razonada.** Los conjuntos $\mathbb N$ y $\mathbb N$ son ciertamente equipotentes: la identidad es biyectiva. Sin embargo, la aplicación $f:\mathbb N\to\mathbb N$ definida por $f(n)=0$ tiene $f(0)=f(1)$ y no alcanza $1$, de modo que no es ni inyectiva ni sobreyectiva. La frase «existe alguna biyección entre dominio y codominio» tiene un cuantificador existencial sobre **funciones**, mientras «$f$ es biyectiva» predica una propiedad de **esta función**. En el teorema de unicidad se verifica la aplicación $\varphi$ particular; no es suficiente comparar tamaños de cuerpos.

### Ejercicio 3

En un cuerpo ordenado $H$, explica cómo se construye $q_H$ cuando $q=m/n$, con $m\in\mathbb Z$ y $n>0$. Prueba que las fracciones $m/n$ y $km/kn$, con $k>0$ entero, tienen la misma imagen. Demuestra además la identidad general para cualesquiera dos representaciones de un mismo racional.

**Solución razonada.** Primero $1_H>0_H$, luego $n_H>0_H$ para todo natural positivo $n$ por suma repetida. Ningún denominador $n_H$ se anula. Definimos $m_H$ para los enteros mediante sumas de $1_H$ y opuestos, y $\iota_H(m/n)=m_H(n_H)^{-1}$. Si $k>0$, las leyes de suma y producto enteros en $H$ dan $(km)_H=k_Hm_H$, $(kn)_H=k_Hn_H$ y $k_H\ne0_H$, por lo cual $(km)_H/(kn)_H=m_H/n_H$. Para dos fracciones generales $m/n=a/b$, con $n,b>0$, se cumple $mb=an$ en los enteros. Transportar esta identidad da $m_Hb_H=a_Hn_H$. Como $n_Hb_H>0_H$, dividir por él demuestra $m_H/n_H=a_H/b_H$. Ésta es la independencia de representación; la igualdad de símbolos fraccionarios por sí sola no bastaría para definir una función.

### Ejercicio 4

Deriva la propiedad arquimediana de un cuerpo ordenado completo usando la propiedad del supremo. Indica en qué punto el argumento dejaría de ser válido para un cuerpo ordenado no necesariamente completo.

**Solución razonada.** Los naturales insertados $n_H$ crecen estrictamente porque $1_H>0_H$. Supongamos que el conjunto $N_H=\{n_H:n\in\mathbb N\}$ tiene una cota. Si $H$ es completo, posee $u=\sup_H N_H$. El elemento $u-1_H<u$ no es cota superior; algún $n_H$ satisface $u-1_H<n_H$. Sumar $1_H$ produce $u<(n+1)_H$, en contradicción con que $u$ acote todos los naturales. Por tanto $N_H$ no está acotado. En un cuerpo no completo, aunque estuviese acotado el conjunto de naturales, puede **no existir el supremo** requerido para hacer el argumento; ése es el paso exacto donde se usa completitud.

### Ejercicio 5

Demuestra que, en un cuerpo ordenado completo $H$, dados $x<y$ existe $q\in\mathbb Q$ con $x<q_H<y$. No utilices una función piso no construida ni presupongas densidad.

**Solución razonada.** Sea $d=y-x>0_H$. Por arquimedianidad elige $n\ge1$ con $n_H>1_H/d$, de donde $n_Hd>1_H$. Entre los enteros insertados hay uno estrictamente mayor que $n_Hx$; por arquimedianidad también los hay estrictamente menores. Elige el **menor entero** $m$ que supera $n_Hx$, usando buen orden después de trasladar a los naturales. La minimalidad da $(m-1)_H\le n_Hx<m_H$. De ahí $n_Hx<m_H\le n_Hx+1_H<n_Hy$. Dividir por $n_H>0_H$ produce $x<(m/n)_H<y$. El uso de un entero mínimo ha sido justificado; no se supuso previamente un operador piso ni densidad racional.

### Ejercicio 6

El conjunto $\mathbb N\subset\mathbb Q$ es no vacío y propio. ¿Por qué no puede utilizarse sólo esa información para asegurar que $\{q_G:q\in\mathbb N\}$ está acotado superiormente en un cuerpo completo $G$? Explica el papel adicional del cierre descendente cuando $A$ es una cortadura.

**Solución razonada.** El conjunto $\mathbb N$ no es todo $\mathbb Q$ y contiene racionales; pese a ello no está acotado superiormente en ningún cuerpo ordenado completo, por el ejercicio 4. En cambio, si $A$ es una cortadura, existe un racional exterior $b\notin A$ porque $A\ne\mathbb Q$. Para todo $a\in A$, necesariamente $a<b$: si $b<a$, el cierre descendente obligaría $b\in A$, y la igualdad contradice la pertenencia. Entonces $b_G$ acota $\{a_G:a\in A\}$. El par «propio + descenso» es la razón de la acotación; la propiedad de no tener máximo interviene luego al fortalecer desigualdades estrictas bajo supremos.

### Ejercicio 7

Para un $x\in F$ demuestra las cuatro condiciones de cortadura del conjunto $A_x=\{q\in\mathbb Q:q_F<x\}$. Explica por qué $\{q_G:q\in A_x\}$ posee supremo en $G$ sin suponer un supremo de $A_x$ en $\mathbb Q$.

**Solución razonada.** La propiedad arquimediana proporciona racionales $a,b$ con $a_F<x<b_F$. Así $a\in A_x$ y $b\notin A_x$. Si $r<q$ en $\mathbb Q$ y $q\in A_x$, entonces $r_F<q_F<x$, por lo que $r\in A_x$. Si $q\in A_x$, la densidad proporciona $r\in\mathbb Q$ con $q_F<r_F<x$, y $q<r$, $r\in A_x$. Por tanto $A_x$ es no vacío, propio, descendente y sin máximo. Como en el ejercicio 6, cualquier exterior racional $b$ acota su imagen en $G$. Es no vacía por $a_G$. La completitud de $G$ permite definir $\varphi(x)$ como su supremo. No se tomó un supremo de $A_x$ en $\mathbb Q$, donde la propiedad del supremo no vale en general.

### Ejercicio 8

Prueba, para todo $x\in F$ y $q\in\mathbb Q$, la equivalencia

$$q_G<\varphi(x)\iff q_F<x.$$

¿Por qué el carácter *sin máximo* de $A_x$ es decisivo para la dirección directa desde $q_F<x$?

**Solución razonada.** Supongamos $q_F<x$. Entonces $q\in A_x$. Como la cortadura no tiene máximo, hay $r\in A_x$ con $q<r$. Se sigue $q_G<r_G\le\varphi(x)$, luego $q_G<\varphi(x)$. Inversamente, si $q_F\ge x$, todo $r\in A_x$ satisface $r_F<x\le q_F$, así $r<q$ y $r_G<q_G$. Por tanto $q_G$ es cota superior de la imagen, y $\varphi(x)\le q_G$, negando la desigualdad estricta. Ambas direcciones están probadas. El argumento ilustra por qué «elemento de un conjunto menor o igual que su supremo» no puede fortalecerse siempre a una desigualdad estricta: aquí funciona porque podemos encontrar un miembro **aún mayor** del mismo corte.

### Ejercicio 9

Usando densidad, demuestra $x<y\Rightarrow\varphi(x)<\varphi(y)$. Demuestra después la recíproca y la inyectividad por tricotomía, sin invocar la sobreyectividad.

**Solución razonada.** Sean $x<y$ en $F$. Por densidad elige $q$ con $x<q_F<y$. Para todo $p\in A_x$, tenemos $p_F<x<q_F$, luego $p_G<q_G$, por lo que $\varphi(x)\le q_G$. Como $q\in A_y$ y $A_y$ no tiene máximo, hay $r\in A_y$ con $q<r$, y así $q_G<r_G\le\varphi(y)$. En conjunto $\varphi(x)<\varphi(y)$. Si $\varphi(x)<\varphi(y)$, la tricotomía impide $x=y$ y $y<x$ (esta última daría $\varphi(y)<\varphi(x)$). Luego $x<y$. Finalmente, si $\varphi(x)=\varphi(y)$ y $x\ne y$, una de las dos desigualdades estrictas entre entradas conduciría a desigualdad estricta entre imágenes: contradicción. Por tanto $\varphi$ es inyectiva.

### Ejercicio 10

Prueba $A_{x+y}=A_x+A_y$, donde la suma del lado derecho es el conjunto de **sumas exactas** $a+b$ con $a\in A_x,b\in A_y$. Localiza y repara el error en el intento: «de $q<a+b$ se deduce inmediatamente que $q=a+b$».

**Solución razonada.** Si $a\in A_x$ y $b\in A_y$, entonces $a_F+b_F<x+y$; así $A_x+A_y\subseteq A_{x+y}$. Para la inclusión recíproca, fija $q\in A_{x+y}$ y $\varepsilon=x+y-q_F>0_F$. La densidad proporciona $a,b\in\mathbb Q$ con $x-\varepsilon/2<a_F<x$ y $y-\varepsilon/2<b_F<y$. Entonces $q_F<a_F+b_F$, por lo que $q<a+b$. No es correcto afirmar que esto **significa** $q=a+b$. Hay que reajustar el testigo: como $q-b<a$ y $a\in A_x$, el descenso da $q-b\in A_x$; ya sabemos $b\in A_y$, y por tanto $q=(q-b)+b$ es una suma exacta. Esto prueba $A_{x+y}\subseteq A_x+A_y$. La técnica transferible consiste en distribuir la holgura primero y usar la propiedad descendente después.

### Ejercicio 11

Sean $S,T\subseteq H$ no vacíos y acotados superiormente. Demuestra

$$\sup_H(S+T)=\sup_H S+\sup_H T.$$

En el paso final, no sustituir $\varepsilon=0$ en una hipótesis formulada solamente para $\varepsilon>0$.

**Solución razonada.** Pongamos $s=\sup S$, $t=\sup T$ y $u=\sup(S+T)$. Este último existe: la suma no es vacía y $s+t$ la acota. Todo $a+b$ cumple $a+b\le s+t$, así que $u\le s+t$. Para $\varepsilon>0_H$, como $s-\varepsilon/2$ no es cota de $S$, existe $a\in S$ con $s-\varepsilon/2<a\le s$. Análogamente $b\in T$ satisface $t-\varepsilon/2<b\le t$. Sumando, $s+t-\varepsilon<a+b\le u$. Si fuese $s+t>u$, escoger $\varepsilon=(s+t-u)/2$ contradiría esta desigualdad universal. Por tanto $s+t\le u$ y hay igualdad. **No** se evaluó el caso $\varepsilon=0$, prohibido por la hipótesis de aproximación.

### Ejercicio 12

Si $x>0_F$, demuestra que $A_x^+=A_x\cap\mathbb Q_{>0}$ no es una cortadura inferior de $\mathbb Q$, pero que su imagen en $G$ y la imagen de $A_x$ tienen el **mismo supremo**.

**Solución razonada.** Como $0_F<x$, por densidad hay un racional $q$ con $0_F<q_F<x$; entonces $q\in A_x^+$. Pero para cualquier $q>0$ en $A_x^+$ el racional $-1$ es menor que $q$ y no pertenece a $A_x^+$. Falla el cierre descendente en todo $\mathbb Q$. El conjunto imagen $S=\{q_G:q\in A_x^+\}$ sigue siendo no vacío y acotado superiormente. Si $u$ acota $S$, debe superar un elemento positivo $s_0\in S$, luego $u>0_G$, y por ello también supera todos los racionales no positivos de la imagen total $\{q_G:q\in A_x\}$. Como los racionales positivos restantes ya están en $S$, $u$ acota la imagen total. La recíproca es inmediata por inclusión. Los conjuntos tienen exactamente las mismas cotas superiores y el mismo supremo, pese a no ser ambos cortaduras.

### Ejercicio 13

Demuestra que, una vez establecida la aditividad de $\varphi$, necesariamente $\varphi(0_F)=0_G$ y $\varphi(-x)=-\varphi(x)$ para cualquier $x\in F$. No utilices multiplicatividad.

**Solución razonada.** Aplicando la aditividad a $0_F=0_F+0_F$ resulta $\varphi(0_F)=\varphi(0_F)+\varphi(0_F)$; cancelar en el grupo aditivo de $G$ da $\varphi(0_F)=0_G$. Para cualquier $x$, tenemos $0_F=x+(-x)$, así que $0_G=\varphi(x)+\varphi(-x)$. Por unicidad del inverso aditivo, $\varphi(-x)=-\varphi(x)$. No se usó producto. Esta separación es necesaria cuando posteriormente se desea derivar la multiplicatividad con factores negativos a partir de la ya probada con factores positivos.

### Ejercicio 14

Sea $S\subseteq H$ no vacío y acotado superiormente. Demuestra $\sup(cS)=c\sup S$ para $c>0$. Analiza separadamente $c=0$ y $c<0$; en el segundo caso formula una identidad correcta bajo las hipótesis de existencia pertinentes.

**Solución razonada.** Si $c>0_H$ y $s=\sup S$, entonces $cs$ acota $cS$. Si $u$ es cualquier otra cota de $cS$, cada $ca\le u$ permite dividir por $c>0_H$ y concluir $a\le u/c$; la minimalidad de $s$ implica $s\le u/c$, luego $cs\le u$. Así $\sup(cS)=cs$. Si $c=0$, $cS=\{0_H\}$ porque $S$ es no vacío, y ambas expresiones son cero. Si $c<0$, el producto invierte el orden: **cuando $S$ también está acotado inferiormente**, su ínfimo $m$ existe y $cm$ acota superiormente $cS$. Si $u$ acota $cS$, de $ca\le u$ se obtiene $u/c\le a$ para todos los $a\in S$; por maximalidad de $m$, $u/c\le m$. Multiplicar por $c<0$ invierte el sentido y da $cm\le u$. Por tanto $\sup(cS)=c\inf S$ para $c<0$ y $S$ acotado inferiormente. Sin esa segunda acotación $cS$ puede carecer de cota superior.

### Ejercicio 15

Sean $x,y>0_F$ y $U=\{q\in\mathbb Q:\exists a\in A_x^+,b\in A_y^+,\ q<ab\}$. Demuestra $U=A_{xy}$, con una secuencia explícita de elecciones racionales y sin usar previamente que $\varphi$ preserve el producto.

**Solución razonada.** Si $q\in U$, hay $a\in A_x^+$ y $b\in A_y^+$ con $q<ab$. Por positividad $a_Fb_F<xy$, luego $q_F<xy$ y $q\in A_{xy}$. Para la otra inclusión, como $x,y>0_F$, también $xy>0_F$. Si $q\le0$ es racional, cualquier par de racionales positivos $a\in A_x^+$ y $b\in A_y^+$ cumple $q<ab$, por lo que $q\in U$. Si $q>0$ y $q_F<xy$, dividir por $x>0_F$ da $0<q_F/x<y$. Por densidad elige $b\in\mathbb Q$ con $q_F/x<b_F<y$ (es automáticamente positivo). Así $q_F<xb_F$, y dividir ahora por $b_F>0_F$ da $0<q_F/b_F<x$. Elige $a\in\mathbb Q$ con $q_F/b_F<a_F<x$. Ambos testigos son positivos, están en sus cortes respectivos y cumplen $q<ab$ por reflexión de la inclusión racional. Por tanto $A_{xy}\subseteq U$. Las dos divisiones se efectuaron sólo después de justificar la positividad de sus denominadores.

### Ejercicio 16

Sea $P=U\cap\mathbb Q_{>0}$, con $U$ como en el ejercicio 15, y $V=\{a_Gb_G:a\in A_x^+,b\in A_y^+\}$. ¿Son iguales $\{q_G:q\in P\}$ y $V$? Demuéstralo verificando las dos inclusiones. Explica por qué la igualdad falla si se reemplaza $P$ por el conjunto completo $U$.

**Solución razonada.** Como $q\in P$ equivale a $q>0$ y $q<ab$ para ciertos racionales positivos $a\in A_x^+$ y $b\in A_y^+$, elegimos $a'=q/b$. Es racional, positivo y cumple $a'<a$, de modo que $a'\in A_x^+$ por descenso. Además, $q=a'b$ y por tanto $q_G=a'_Gb_G\in V$. Recíprocamente, si $a_Gb_G\in V$, la ausencia de máximo de $A_x$ proporciona $a'>a$ en $A_x$ (también positivo); de $ab<a'b$ resulta $ab\in P$, y su imagen es $a_Gb_G$. Las dos inclusiones prueban $\iota_G[P]=V$. Si se usa el conjunto completo $U$, éste contiene racionales negativos, mientras $V$ contiene sólo productos positivos; las imágenes no pueden ser iguales. Ésta es la razón precisa por la cual corregir el **dominio de $q$** evita un fallo de tipo en la prueba multiplicativa.

### Ejercicio 17

Supón que $\varphi$ es aditiva, multiplicativa y preserva estrictamente el orden. Deduce $\varphi(1_F)=1_G$ a partir de un idempotente. Explica cómo se deduce luego $\varphi(q_F)=q_G$ para cada racional $q$.

**Solución razonada.** La multiplicatividad da $e=\varphi(1_F)=\varphi(1_F1_F)=e^2$. De $e(e-1_G)=0_G$ se sigue $e\in\{0_G,1_G\}$. La aditividad da $\varphi(0_F)=0_G$ (el ejercicio 13) y, como $0_F<1_F$, el orden estricto produce $0_G<e$. Por tanto $e=1_G$. Como $\varphi$ conserva $1$, suma y opuestos, preserva los enteros: $\varphi(m_F)=m_G$. Si $n>0$, su imagen es no nula; de $\varphi(n_F)\varphi(n_F^{-1})=\varphi(1_F)=1_G$ se deduce $\varphi(n_F^{-1})=n_G^{-1}$. Para cada fracción $m/n$ obtenemos $\varphi((m/n)_F)=m_Gn_G^{-1}=(m/n)_G$. La buena definición de estas copias se fundamentó previamente; no son elementos literalmente iguales de distintos cuerpos.

### Ejercicio 18

Demuestra la sobreyectividad de $\varphi$ construyendo para cada $y\in G$ la cortadura $B_y=\{q\in\mathbb Q:q_G<y\}$ y el elemento $x=\sup_F\{q_F:q\in B_y\}$. Después prueba que cualquier isomorfismo de cuerpos ordenados $h:F\to G$ es igual a $\varphi$. Distingue la existencia de un isomorfismo de la unicidad de esa función.


**Solución razonada.** Fijado $y\in G$, sea $B_y=\{q\in\mathbb Q:q_G<y\}$. Por las mismas propiedades de la imagen racional inferior que en el ejercicio 7, $B_y$ es cortadura y su imagen en $F$ es no vacía y acotada. Sea $x=\sup_F\{q_F:q\in B_y\}$. Si $q\in B_y$, hay $r\in B_y$ con $q<r$, y $q_F<r_F\le x$; luego $q\in A_x$. Para la otra dirección, si $q\notin B_y$, entonces $q_G\ge y$; todo $r\in B_y$ cumple $r<q$, de modo que $q_F$ es cota de los racionales transportados y $x\le q_F$. Por tanto $q\notin A_x$. Queda $A_x=B_y$. Por definición $\varphi(x)=\sup_G\{q_G:q_G<y\}$. El elemento $y$ es cota, y si $z<y$, la densidad racional en $G$ proporciona $q_G$ con $z<q_G<y$, por lo que $z$ no es cota; luego $\varphi(x)=y$. Así $\varphi$ es sobreyectiva.

Para la unicidad, sea $h:F\to G$ otro isomorfismo de cuerpos ordenados. Como preserva unidad y operaciones, fija cada copia racional (el ejercicio 17). Por reflexión de orden, para todo $q\in\mathbb Q$ tenemos $q_F<x\iff q_G<h(x)$. Es decir, $A_x=B_{h(x)}$. Aplicando la caracterización del supremo racional recién probada, $\varphi(x)=\sup_G\iota_G[A_x]=h(x)$. Como vale para todo $x$, $h=\varphi$. Hemos demostrado primero la **existencia de un isomorfismo** y después, como ampliación, la **unicidad del isomorfismo ordenado**; ninguna afirmación identifica literalmente a $F$ con $G$ como conjuntos.


# Medir una suma y controlar un error

Una aproximación adquiere utilidad cuando podemos controlar su error. Si sumamos dos cantidades aproximadas, la desigualdad triangular permite repartir una tolerancia entre los dos errores y obtener una cota para el resultado. Partiremos del valor absoluto y demostraremos la estimación que sostiene ese procedimiento:

$$|a+b|\le |a|+|b|.$$

El resultado asegura que sumar errores no puede producir una magnitud mayor que la suma de sus magnitudes individuales. Es una afirmación simple de recordar y sorprendentemente fértil: controla la diferencia entre dos valores absolutos, explica una propiedad geométrica de los triángulos y permite demostrar que la suma de sucesiones convergentes también converge.

Debemos, sin embargo, distinguir contextos. La desigualdad escalar vale en **todo cuerpo ordenado**, incluso uno en el que no existan raíces de todos los positivos. La longitud euclídea de vectores necesita otras pruebas, y una norma general tiene sus propios axiomas. Al separar estos niveles veremos cómo un razonamiento algebraico elemental llega a convertirse en una herramienta del análisis.

Como preliminar algebraico, recordemos que en un cuerpo ordenado los elementos $2,4$ son positivos y no nulos. El cuadrado de un elemento negativo también es positivo, pues $(-x)^2=x^2>0$ si $x\ne0$; por consiguiente $x^2=0$ implica $x=0$. Usaremos estas propiedades sin suponer todavía la existencia de raíces cuadradas para todos los elementos positivos.

## Una suma puede cancelar parte de sus términos

Para $a=3$ y $b=2$, sumar conserva toda la magnitud: $|a+b|=5=|a|+|b|$. Para $a=3$ y $b=-2$, la suma vale $1$, aunque las magnitudes individuales siguen sumando $5$. Cuando los signos se oponen, una parte se cancela. La desigualdad triangular expresa la cota que funciona en todos los casos:

$$
\forall a,b\in\mathbb R,\qquad |a+b|\le|a|+|b|.
$$

El miembro izquierdo mide el resultado de sumar; el derecho mide cada término antes de sumarlos. El signo $\le$ admite tanto igualdad como cancelación. Por ejemplo, para $a=4,b=-4$, el miembro izquierdo es cero y el derecho es ocho. El nombre geométrico se comprenderá después; empezaremos por el caso escalar, que es anterior a cualquier construcción de normas vectoriales.

Para leer la fórmula necesitamos precisar el valor absoluto. Si $x\ge0$, $|x|=x$; si $x<0$, $|x|=-x$. El resultado es siempre no negativo, y sólo es cero cuando $x=0$. Por eso «hacer positivo» debe entenderse con atención al cero. La distancia de $-3$ al origen es $3$, y la de $0$ al origen es $0$.

Una observación elemental es $x\le|x|$. Para $x\ge0$ hay igualdad; para $x<0$, el miembro izquierdo es negativo y el derecho positivo. También $-x\le|x|$, lo que produce una cota por ambos lados: $-|x|\le x\le|x|$.

## La desigualdad triangular por cuadrados y raíces

La prueba por cuadrados compara dos cantidades que podremos desarrollar con la distributividad. El paso de regreso a sus magnitudes exige usar que el cuadrado es estrictamente creciente entre elementos no negativos. Esta propiedad de orden permitirá comprender exactamente qué hace la notación de raíz.

Para demostrar la desigualdad, comparemos dos expansiones cuadráticas. Al desarrollar $(a+b)^2$, el término cuyo signo cambia es $2ab$. Los cuadrados $a^2$ y $b^2$ son no negativos. Si reemplazamos $ab$ por $|a||b|$, ese término no disminuye.
La identidad $|ab|=|a||b|$ se demuestra atendiendo a los signos: con dos factores positivos o dos negativos, el producto es positivo y las magnitudes multiplicadas valen $ab$; con signos opuestos valen $-ab$; si hay un cero, todos esos productos se anulan. Aplicando $x\le|x|$ a $x=ab$, obtenemos $ab\le|a||b|$. Este razonamiento no requiere multiplicar desigualdades por factores de signo desconocido.

Como $2>0$, podemos duplicar esa desigualdad y sumar los cuadrados:

$$
\begin{aligned}
(a+b)^2&=a^2+2ab+b^2\\
&\le |a|^2+2|a||b|+|b|^2\\
&=(|a|+|b|)^2.
\end{aligned}
$$

Podemos comparar ahora las raíces no negativas de ambos miembros; este paso exige dos justificaciones. La primera es que $\sqrt{z^2}=|z|$: $|z|$ es no negativo, su cuadrado es $z^2$ y ninguna otra raíz no negativa puede tener el mismo cuadrado. La segunda es que, entre números no negativos, el orden de los cuadrados conserva el orden original. Si $0\le u<v$, entonces $v^2-u^2=(v-u)(v+u)>0$; por tanto, $u^2\le v^2$ impide $u>v$.

Aplicando esas razones a los cuadrados que ya tenemos,

$$
|a+b|\le\bigl||a|+|b|\bigr|=|a|+|b|.
$$

La última igualdad usa que la suma de dos números no negativos es no negativa. Permanece válida si ambos son cero. Tomar raíces de cuadrados no exige que todo positivo de un cuerpo ordenado tenga raíz: aquí los radicandos ya son cuadrados. La existencia de raíces para reales no negativos en general se demuestra por supremos en la demostración complementaria, como una ampliación distinta.

**Cuándo hay igualdad.** La diferencia de los cuadrados de ambos miembros de la triangular es $2(|a||b|-ab)$. Se anula exactamente cuando $ab\ge0$. En la recta hay igualdad si los signos coinciden o si uno de los números es cero; con signos opuestos y ambos no nulos hay desigualdad estricta. Por ejemplo, $a=-3,b=-2$ también da igualdad, aunque ambos números sean negativos.

Una segunda demostración, que encontraremos entre las variantes matemáticas, suma las cotas $-|a|\le a\le|a|$ y $-|b|\le b\le|b|$. Su interés es mostrar la triangular como una afirmación sobre cotas dobles. Esta alternativa ilumina el argumento de orden sin sustituir el camino por cuadrados seguido antes.

### Valor absoluto y casos de signo

Para $x$ en un cuerpo ordenado $F$, definimos $|x|=x$ si $x\ge0$ y $|x|=-x$ si $x<0$. Los dos casos son exhaustivos y disjuntos por totalidad del orden; la regla asigna un único elemento. De ella se deducen $|x|\ge0$, $|x|=0\iff x=0$, $|-x|=|x|$, $|x|^2=x^2$ y $-|x|\le x\le|x|$.

Si $x\ge0$, las primeras afirmaciones se reducen a $x\ge0$, y $-x\le x$ porque $2x\ge0$. Si $x<0$, $-x>0$, $x=-|x|<|x|$ y $(-x)^2=x^2$. Para la simetría, si $x>0$ se tiene $|-x|=-(-x)=x$; si $x<0$, $-x>0$ da $|-x|=-x$; para $x=0$ ambos lados son cero. La igualdad $|x|=0$ en cada rama exige $x=0$. Estas verificaciones cubren también los casos de borde que la expresión informal «hacer positivo» puede ocultar.

### Producto y control de signos

Para todo $a,b\in F$, $|ab|=|a||b|$ y $ab\le|a||b|$. Si alguno es cero, ambos productos de la igualdad son cero. Si ambos son positivos, $ab>0$ y los dos lados valen $ab$. Si ambos son negativos, $ab=(-a)(-b)>0$ y $|a||b|=(-a)(-b)=ab$. Si tienen signos opuestos, $ab<0$ y $|a||b|=-ab=|ab|$. La desigualdad resulta de aplicar el valor absoluto a $x=ab$.

No se multiplica $a\le|a|$ por un $b$ de signo desconocido. Multiplicar una desigualdad por un negativo invierte su sentido; el análisis de signos evita esa inferencia ilegítima.

### Cotas dobles y equivalencias

Para $c\ge0$ y $t\in F$,

$$
|t|\le c\iff -c\le t\le c.
$$

La dirección directa usa $-|t|\le t\le|t|$ y $-|t|\ge-c$. Para la recíproca, si $t\ge0$, $|t|=t\le c$; si $t<0$, $t\ge-c$ equivale, al negar ambos miembros, a $-t\le c$, y $|t|=-t$. Para $c>0$, el mismo razonamiento con desigualdades estrictas demuestra

$$
|t|<c\iff -c<t<c.
$$

Con $c=0$, la versión no estricta exige $t=0$; la estricta tiene ambos miembros falsos. No se convierte una cadena no estricta en una estricta.

### Cuadrados y raíces de cuadrados

Para $0\le u<v$, $v^2-u^2=(v-u)(v+u)>0$ porque ambos factores son positivos. Por consiguiente, para $u,v\ge0$,

$$
u\le v\iff u^2\le v^2.
$$

La dirección directa incluye el caso $u=v$; la recíproca excluye $u>v$ por el resultado estricto. Todo cuadrado $z^2$ posee una raíz no negativa, $|z|$, por las propiedades elementales del valor absoluto. Si $r\ge0$ y $r^2=z^2=|z|^2$, la equivalencia anterior en ambas direcciones da $r=|z|$. Es legítimo escribir $\sqrt{z^2}=|z|$, incluso si $F$ no posee raíces de todos sus positivos. Además, si dos cuadrados están ordenados, sus raíces no negativas conservan el orden. Esta comparación basta para el argumento escalar y no usa completitud.

### La desigualdad triangular mediante cuadrados

Sean $a,b\in F$. Por la identidad $|ab|=|a||b|$, $ab\le|a||b|$; multiplicamos por $2>0$ y sumamos $a^2=|a|^2$ y $b^2=|b|^2$. Las expansiones distributivas dan

$$
(a+b)^2=a^2+2ab+b^2
\le |a|^2+2|a||b|+|b|^2=(|a|+|b|)^2.
$$

Cada miembro es el cuadrado de un elemento no negativo explícito. La monotonía estricta del cuadrado en ese dominio permite comparar esos elementos y garantiza que son las raíces no negativas correspondientes. Aplicamos esa propiedad para obtener:

$$
|a+b|=\sqrt{(a+b)^2}
\le\sqrt{(|a|+|b|)^2}=\bigl||a|+|b|\bigr|=|a|+|b|.
$$

La última igualdad usa $|a|+|b|\ge0$, incluyendo $a=b=0$. Las palabras «positivo» o «estrictamente positivo» no justifican excluir ese caso. La demostración funciona en cualquier cuerpo ordenado: no depende de la completitud ni de haber construido raíces cuadradas para todos los positivos.

### Igualdad en la recta

Para $a,b\in F$,

$$
|a+b|=|a|+|b|\iff ab\ge0.
$$

La diferencia de los cuadrados de ambos miembros es $2(|a||b|-ab)$. Ambos miembros son no negativos; por la monotonía del cuadrado entre elementos no negativos, su igualdad equivale a $|a||b|=ab$. Por la identidad $|ab|=|a||b|$, esto equivale a $|ab|=ab$, es decir, a $ab\ge0$. Incluye los ceros y los signos iguales.

La desigualdad triangular aparece aquí sin recurrir a la completitud. La notación de raíz no debe engañarnos: al pasar de $(a+b)^2$ a $|a+b|$ sólo tomamos la raíz no negativa de un cuadrado que ya existe. Por otra parte, el caso de igualdad revela el papel de los signos: dos sumandos pueden reforzarse o cancelarse. La prueba por cotas del apéndice proporciona otro camino al mismo resultado, pero no reemplaza la vía por cuadrados que hemos seguido.

## La desigualdad inversa mide cuánto pueden cambiar las magnitudes

Si dos números están próximos, sus valores absolutos no pueden estar más lejos que ellos. La afirmación precisa es

$$
\bigl||a|-|b|\bigr|\le|a-b|.
$$

Hay dos niveles de barras: primero se calculan $|a|$ y $|b|$; luego se toma la magnitud de su diferencia. Por ejemplo, $a=3,b=7$ produce $|3-7|=4$ en ambos miembros. Para $a=3,b=-7$, las magnitudes difieren en cuatro, pero los números distan diez.

La desigualdad triangular inversa se deduce directamente de la desigualdad que acabamos de probar. Escribimos $a=(a-b)+b$ y aplicamos la cota ya demostrada:

$$
|a|\le|a-b|+|b|,\qquad |a|-|b|\le|a-b|.
$$

Todavía falta controlar cuánto puede ser negativo $|a|-|b|$. Intercambiar $a$ y $b$ proporciona $|b|-|a|\le|b-a|$. Como $b-a=-(a-b)$ y el valor absoluto no cambia al negar su argumento, $|b-a|=|a-b|$. Negando la desigualdad intercambiada queda

$$
-|a-b|\le|a|-|b|\le|a-b|.
$$

Para terminar necesitamos interpretar una cota simétrica. Si $c\ge0$, las condiciones $-c\le t\le c$ y $|t|\le c$ son equivalentes. Si $t\ge0$, basta su cota superior; si $t<0$, su cota inferior equivale a $-t\le c$, y $-t=|t|$. La dirección contraria usa $-|t|\le t\le|t|$. Tomando $t=|a|-|b|$ y $c=|a-b|$, obtenemos la desigualdad inversa.

### Desigualdad triangular inversa

Para $a,b\in F$, escribimos $a=(a-b)+b$. Por la desigualdad triangular,

$$
|a|\le|a-b|+|b|,\qquad |a|-|b|\le|a-b|.
$$

Intercambiando $a,b$, $|b|-|a|\le|b-a|=|a-b|$, donde la igualdad se deduce de la simetría del valor absoluto, y no únicamente del ejemplo $a=3,b=7$. Negar la última desigualdad produce $-|a-b|\le|a|-|b|$. En conjunto,

$$
-|a-b|\le|a|-|b|\le|a-b|.
$$

Aplicamos la equivalencia entre valor absoluto y cotas dobles con $t=|a|-|b|$ y $c=|a-b|\ge0$ para concluir $\bigl||a|-|b|\bigr|\le|a-b|$. No se usa la desigualdad inversa para demostrar la triangular.

### Sumas finitas

Para $m\ge1$ y $x_1,\ldots,x_m\in F$, $|\sum_{j=1}^m x_j|\le\sum_{j=1}^m|x_j|$. Para $m=1$ hay igualdad. Si vale para $m$, la desigualdad triangular aplicada a $\sum_{j=1}^m x_j$ y $x_{m+1}$ da la cota para $m+1$, tras sustituir la hipótesis inductiva. La suma vacía vale cero y satisface también la cota.

La desigualdad triangular inversa permite controlar un error después de aplicar el valor absoluto. Si dos cantidades distan poco, sus magnitudes también distan poco: $\bigl||a|-|b|\bigr|\le |a-b|$. El punto de la prueba fue obtener las dos desigualdades en sentidos opuestos, no elegir arbitrariamente cuál de los dos valores absolutos era mayor. La misma técnica sirve para estimar sumas finitas.

## Por qué aparecen triángulos

La prueba escalar anterior utilizó únicamente sumas, productos y el orden de un cuerpo. Cuando se pasa a vectores, la palabra «longitud» introduce un objeto nuevo: una función que asigna a cada vector un número no negativo. Antes de transportar la desigualdad debemos construir esa función y comprobar las propiedades que necesitamos de ella. Esta etapa muestra por qué una analogía geométrica puede orientar una demostración sin reemplazarla.

La geometría es una aplicación, no una sustitución literal de letras. Entre la magnitud escalar y la longitud de un vector tendremos que construir las raíces necesarias y probar Cauchy–Schwarz.

Imaginemos dos vectores del plano colocados uno a continuación del otro. El primero lleva del punto $A$ al punto $C$, y el segundo de $C$ a $B$. Su suma lleva de $A$ a $B$. Los tres segmentos delimitan un triángulo cuando los puntos no son colineales. Si usamos la longitud euclídea,

$$
\|u+v\|_2\le\|u\|_2+\|v\|_2,
$$

el segmento directo no supera la suma de los otros dos. La afirmación vale para cualquiera de los lados del triángulo al nombrar de nuevo los puntos. La longitud de $u+v$ no tiene que ser siempre la mayor de las tres: en el dibujo particular puede serlo, pero por ejemplo $u=(2,0),v=(-1,0)$ da longitudes $1,2,1$.
La prueba escalar anterior cuantifica sobre números; introducir vectores en su fórmula no demuestra una nueva desigualdad. Para el plano definimos $\|u\|_2=\sqrt{u_1^2+u_2^2}$ y el producto escalar $u\cdot v=u_1v_1+u_2v_2$. La identidad

$$
\|u\|_2^2\|v\|_2^2-(u\cdot v)^2=(u_1v_2-u_2v_1)^2\ge0
$$

demuestra $u\cdot v\le\|u\|_2\|v\|_2$. Al expandir el cuadrado de la longitud de la suma, obtenemos

$$
\|u+v\|_2^2\le(\|u\|_2+\|v\|_2)^2.
$$

La comparación entre números no negativos permite tomar raíces y concluir la triangular vectorial. Este razonamiento demuestra la desigualdad vectorial mediante Cauchy–Schwarz, sin pretender deducirla de la versión escalar por un mero cambio de símbolos.

Vale la pena preguntarse cuándo hay igualdad. En la geometría euclídea, si ambos vectores son no nulos, deben tener la misma dirección y el mismo sentido. Se admite también un vector nulo. Que el triángulo tenga área cero no caracteriza por sí solo esa igualdad: con $u=(1,0)$ y $v=(-1,0)$, la suma tiene longitud cero y las longitudes individuales suman dos. La orientación decide si el recorrido intermedio avanza hacia el destino o retrocede.

Si se define una métrica $d$, la triangular se escribe $d(A,B)\le d(A,C)+d(C,B)$. Esta formulación compara tres distancias sin presuponer rectas, flechas o caminos mínimos. En el plano euclídeo coincide con la intuición del recorrido directo; la sola definición de métrica no garantiza que existan curvas que alcancen una distancia mínima.

### Raíz de un real no negativo

Para todo $c\in\mathbb R$, $c\ge0$, existe un único $s\ge0$ con $s^2=c$. Para $c=0$, $s=0$ y su unicidad procede de la estricta monotonía del cuadrado entre elementos no negativos. Sea $c>0$. El conjunto $S=\{x\in\mathbb R:x\ge0,\ x^2\le c\}$ contiene cero. Es acotado superiormente por $c+1$, pues $(c+1)^2>c$ y la monotonía del cuadrado excluye de $S$ cualquier $x>c+1$. Sea $s=\sup S$. Es positivo: $x=c/(c+1)>0$ pertenece a $S$, puesto que $c<(c+1)^2$ implica $x^2<c$; el denominador es positivo.

Si $s^2<c$, sea $d=c-s^2>0$ y elijamos $h=\min\{1,d/[2(2s+1)]\}>0$. Todos los denominadores son positivos. Como $h\le1$,

$$
(s+h)^2-s^2=2sh+h^2\le(2s+1)h\le d/2<d.
$$

Así, $s+h\in S$ y $s+h>s$, contradicción. Si $s^2>c$, sea $d=s^2-c>0$ y $h=\min\{s/2,d/(4s)\}>0$. Entonces $s-h\ge s/2>0$ y

$$
(s-h)^2=s^2-2sh+h^2\ge s^2-d/2>c.
$$

Todo $x\in S$ debe cumplir $x\le s-h$: si $x>s-h$, la monotonía estricta de cuadrados daría $x^2>(s-h)^2>c$. Por tanto $s-h$ sería una cota superior menor que $s$, otra contradicción. Queda $s^2=c$. Dos raíces no negativas son iguales por la monotonía del cuadrado entre elementos no negativos. La función $c\mapsto\sqrt c$ preserva el orden, nuevamente por la monotonía del cuadrado entre elementos no negativos. No usa continuidad, límites, triangular, inversa ni Cauchy–Schwarz.

### Cauchy–Schwarz en el plano

Para $u=(u_1,u_2),v=(v_1,v_2)\in\mathbb R^2$, definimos $u\cdot v=u_1v_1+u_2v_2$ y $\|u\|_2=\sqrt{u_1^2+u_2^2}$. El radicando es no negativo y el teorema de existencia y unicidad de raíces no negativas, demostrado antes en este capítulo, legitima la definición. Sean $U=\|u\|_2$ y $V=\|v\|_2$. La expansión algebraica verifica

$$
U^2V^2-(u\cdot v)^2=(u_1v_2-u_2v_1)^2\ge0.
$$

Como $|u\cdot v|$ y $UV$ son no negativos, la monotonía del cuadrado implica $|u\cdot v|\le UV$; en particular $u\cdot v\le UV$. La igualdad en la versión absoluta equivale a $u_1v_2-u_2v_1=0$. Si $u\ne0$, eligiendo una coordenada $u_i\ne0$ y poniendo $\lambda=v_i/u_i$, la identidad de determinante cero fuerza la otra coordenada $v_j=\lambda u_j$. Para $u=0$ el determinante se anula para cualquier $v$. No presupone la desigualdad triangular vectorial.

### Triangular euclídea e igualdad

Para $u,v\in\mathbb R^2$, la expansión del cuadrado y la desigualdad de Cauchy--Schwarz recién demostrada dan

$$
\|u+v\|_2^2=U^2+2u\cdot v+V^2\le U^2+2UV+V^2=(U+V)^2.
$$

Por la monotonía del cuadrado entre elementos no negativos, $\|u+v\|_2\le U+V$. Hay igualdad exactamente cuando $u\cdot v=UV$. Si alguno es cero, hay igualdad. Si ambos son no nulos, esta condición implica igualdad absoluta en el caso de igualdad de Cauchy–Schwarz, por lo que $v=\lambda u$; además $\lambda U^2=u\cdot v=UV>0$, y $\lambda>0$. Recíprocamente, para $\lambda>0$ se tiene $V=\lambda U$ porque ambos lados son no negativos y sus cuadrados coinciden. Entonces $u\cdot v=\lambda U^2=UV$ y hay igualdad.

La descripción exacta es: algún vector nulo, o vectores no nulos con la misma dirección y el mismo sentido. La mera área cero no basta: $u=(1,0)$ y $v=(-1,0)$ producen $\|u+v\|_2=0<2=U+V$. La caracterización tampoco vale para toda norma: en $\ell^1$ del plano, $u=(1,0)$ y $v=(0,1)$ tienen igualdad y no son paralelos.

Para comprobar que la longitud euclídea es realmente una norma, además de la triangular ya probada, verificamos las otras cláusulas. La raíz es no negativa por definición. Si $\|u\|_2=0$, entonces $u_1^2+u_2^2=0$; ambos sumandos no negativos deben ser cero, y cada coordenada es cero. La recíproca es inmediata por la definición. Para todo $\lambda\in\mathbb R$, los números $\|\lambda u\|_2$ y $|\lambda|\|u\|_2$ son no negativos y sus cuadrados valen $\lambda^2(u_1^2+u_2^2)$; por la monotonía del cuadrado entre elementos no negativos son iguales, incluso si $\lambda=0$. Se han verificado así las tres cláusulas antes de utilizar la longitud como ejemplo de norma.

Para pasar de una magnitud escalar a la longitud de un vector hubo que pagar dos deudas. La primera es justificar las raíces de todos los positivos con la propiedad del supremo; la segunda es demostrar la desigualdad de Cauchy--Schwarz mediante una identidad algebraica y deducir de ella la triangular euclídea. Este camino explica también por qué la condición de igualdad depende de la norma: no basta dibujar dos vectores colineales, hay que distinguir si tienen o no el mismo sentido.

## La suma de dos sucesiones convergentes

Al pasar a sucesiones no basta manipular símbolos de límites: fijada una tolerancia, deben elegirse índices que controlen simultáneamente los errores de ambos sumandos.

Volvamos a los números reales para estudiar una consecuencia analítica de la desigualdad. Una sucesión es una función de los naturales positivos en los reales. Sus primeros términos orientan la intuición, pero una lista finita no determina ni la sucesión ni su límite. Como ejemplo, definamos $a_n=3+10^{-n}$ y $b_n=2-10^{-n}$. La primera converge a tres, la segunda a dos y su suma es exactamente cinco en todo índice.

La definición precisa de $a_n\to a$ exige que para cada $\varepsilon>0$ exista un índice $N$ tal que todos los $n\ge N$ cumplan $|a_n-a|<\varepsilon$. La tolerancia se fija antes del índice. Un índice puede depender de la tolerancia; no puede depender del término concreto que después se examina. Para comprobar los ejemplos anteriores, $10^n\ge n$ para $n\ge1$ por inducción: vale en $n=1$ y $10^{n+1}\ge10n\ge n+1$. De modo que $10^{-n}\le1/n$. Por la propiedad arquimediana elegimos $N>1/\varepsilon$, y para todo $n\ge N$ ambos errores, $|a_n-3|$ y $|b_n-2|$, son menores que $\varepsilon$.

Si $a_n\to a$ y $b_n\to b$, queremos que el error de su suma sea pequeño. La identidad algebraica reagrupa ese error:

$$
|(a_n+b_n)-(a+b)|=|(a_n-a)+(b_n-b)|
\le|a_n-a|+|b_n-b|.
$$

Cada sumando de la derecha ya es controlable por una hipótesis de convergencia. Fijado $\varepsilon>0$, elegimos $N_a$ para que el primer error sea menor que $\varepsilon/2$, y $N_b$ para que el segundo sea menor que $\varepsilon/2$. A partir de $N=\max\{N_a,N_b\}$, ambos controles valen en el mismo índice. La suma de errores es menor que $\varepsilon$, y queda $a_n+b_n\to a+b$.

La partición en mitades responde a un presupuesto de error. También servirían $\varepsilon/3$ y $2\varepsilon/3$. En cambio, exigir a cada error solamente que sea menor que $\varepsilon$ produciría una cota $2\varepsilon$, insuficiente para cerrar esa prueba con la tolerancia ya fijada. El mecanismo transferible combina una reagrupación algebraica, una estimación triangular y un índice común.

La misma estimación reaparece cuando examinamos sucesiones de Cauchy. Demostraremos a continuación que la suma de dos sucesiones de Cauchy sigue siendo de Cauchy; la conclusión es distinta de afirmar que deba converger. Esto no implica que toda sucesión de Cauchy converja en cualquier espacio normado: la existencia del límite exige una hipótesis adicional de completitud.

### Suma de sucesiones convergentes

Para sucesiones $a_n,b_n:\mathbb N_{\ge1}\to\mathbb R$, escribimos $a_n\to a$ cuando para todo $\varepsilon>0$ existe $N\in\mathbb N_{\ge1}$ tal que para todo $n\ge N$ se cumple $|a_n-a|<\varepsilon$. Si $a_n\to a$ y $b_n\to b$, entonces $a_n+b_n\to a+b$.

Fijado $\varepsilon>0$, la primera convergencia proporciona $N_a$ para tolerancia $\varepsilon/2$, y la segunda $N_b$ para la misma tolerancia. Sea $N=\max\{N_a,N_b\}$. Para todo $n\ge N$, las dos estimaciones valen simultáneamente, y la reagrupación algebraica da

$$
|(a_n+b_n)-(a+b)|=|(a_n-a)+(b_n-b)|
\le|a_n-a|+|b_n-b|<\varepsilon/2+\varepsilon/2=\varepsilon.
$$

El índice depende de $\varepsilon$ y de ambas sucesiones; nunca se elige un índice distinto para cada sumando después de fijar $n$. La misma prueba en un espacio normado utiliza la desigualdad triangular de la norma en lugar de la desigualdad escalar. No usa completitud ni unicidad del cuerpo ordenado completo.

### Unicidad de límites y continuidad de la norma

Si una sucesión $x_n$ de un espacio normado converge a $x$ y a $y$, y $d=\|x-y\|>0$, elegimos índices para que ambas distancias a partir de un máximo común sean menores que $d/3$. Entonces

$$
d=\|(x-x_n)+(x_n-y)\|\le\|x-x_n\|+\|x_n-y\|<2d/3<d,
$$

contradicción. Queda $d=0$ y $x=y$. Si $x_n\to x$, la desigualdad triangular inversa para normas da $|\|x_n\|-\|x\||\le\|x_n-x\|$; para cada $\varepsilon>0$ el índice de la convergencia original hace el miembro derecho menor que $\varepsilon$. Luego $\|x_n\|\to\|x\|$. La unicidad de un límite dentro de un espacio no es la unicidad estructural del cuerpo del teorema de unicidad.

### Suma de sucesiones de Cauchy

En un espacio normado, $x_n$ es de Cauchy si $\forall\varepsilon>0\ \exists N\ \forall m,n\ge N$, $\|x_n-x_m\|<\varepsilon$. Si $x_n,y_n$ son de Cauchy, para cada $\varepsilon>0$ elegimos índices para $\varepsilon/2$ y su máximo común. Para $m,n$ mayores que ese máximo,

$$
\|(x_n+y_n)-(x_m+y_m)\|\le\|x_n-x_m\|+\|y_n-y_m\|<\varepsilon.
$$

No se afirma que esas sucesiones converjan en cualquier espacio normado; eso requeriría completitud del espacio.

El procedimiento vuelve a repartir una tolerancia y a reunir dos índices en uno común. La desigualdad triangular convierte entonces los controles individuales en un control sobre la suma. La misma idea prueba la estabilidad de la condición de Cauchy; la existencia de un límite para toda sucesión de Cauchy corresponde a la completitud del espacio.

## Una norma especifica qué entendemos por magnitud

Para un espacio vectorial real $V$, una norma es una función $\|\cdot\|:V\to\mathbb R$ que satisface, para todos los vectores $x,y$ y escalares reales $\lambda$,

$$
\|x\|\ge0,\quad \|x\|=0\iff x=0_V,\qquad
\|\lambda x\|=|\lambda|\|x\|,\qquad
\|x+y\|\le\|x\|+\|y\|.
$$

La primera cláusula distingue el vector cero. La segunda controla el cambio de escala y conserva la magnitud cuando se invierte el sentido. La tercera permite comparar una suma con sus términos. Equipar $V$ con una norma significa elegir una función que cumpla esas cláusulas; conocer sólo la estructura de espacio vectorial no determina una longitud única.

La segunda propiedad recibe el nombre de **homogeneidad absoluta**: el factor es $|\lambda|$, no $\lambda$. Una norma no es lineal en un espacio no trivial, pues para $x\ne0$ la norma de $-x$ coincide con la de $x$, mientras una aplicación lineal tendría que cambiar su signo.

En $\mathbb R^2$, tanto $\|(x,y)\|_2=\sqrt{x^2+y^2}$ como $\|(x,y)\|_1=|x|+|y|$ son normas. La segunda cumple la triangular sumando las dos desigualdades escalares por coordenadas. Bajo esa norma, $u=(1,0)$ y $v=(0,1)$ tienen igualdad: $\|u+v\|_1=2=\|u\|_1+\|v\|_1$, aunque no sean paralelos. La caracterización geométrica euclídea de la igualdad depende de la norma elegida.

Los espacios de matrices y funciones ofrecen otros ejemplos. Una matriz puede medirse sumando las magnitudes de sus entradas. Como ejemplo infinito dimensional concreto, las funciones $\mathbb N\to\mathbb R$ de soporte finito pueden medirse sumando las magnitudes de sus valores; sus funciones indicadoras de un único índice constituyen una familia linealmente independiente infinita. Hay asimismo espacios de funciones de dimensión finita, como el de las funciones constantes. Estos ejemplos separan el objeto vectorial de su dibujo como flecha y evitan identificar «función» con «dimensión infinita».

### Norma: definición y homogeneidad

Sea $V$ un espacio vectorial real. Una norma es una función $\|\cdot\|:V\to\mathbb R$ tal que, para todos $x,y\in V$ y $\lambda\in\mathbb R$, se cumplen:

1. $\|x\|\ge0$ y $\|x\|=0\iff x=0_V$;
2. $\|\lambda x\|=|\lambda|\|x\|$;
3. $\|x+y\|\le\|x\|+\|y\|$.

Se llama espacio normado al par $(V,\|\cdot\|)$. Las cláusulas son requisitos universales, no propiedades deducidas de llamar «longitud» a una función arbitraria. La segunda es homogeneidad absoluta. Una norma en un espacio no trivial no es una aplicación lineal $V\to\mathbb R$: para $x\ne0$, la homogeneidad con $\lambda=-1$ exige $\|-x\|=\|x\|>0$, mientras que la linealidad exigiría $\|-x\|=-\|x\|<0$. El valor absoluto en $\mathbb R$ satisface las tres cláusulas: la definitud se deduce de su definición, la homogeneidad del producto de valores absolutos y la cota de las sumas de la desigualdad triangular. No se pretende «demostrar» la tercera cláusula para cualquier función positiva y homogénea.

### Distancia y desigualdad inversa en una norma

Para un espacio normado, definimos $d(x,y)=\|x-y\|$. La positividad y definitud exigidas por la definición de norma dan $d(x,y)\ge0$ y $d(x,y)=0\iff x=y$. La homogeneidad con $-1$ da simetría. De $x-z=(x-y)+(y-z)$ y la tercera cláusula se obtiene $d(x,z)\le d(x,y)+d(y,z)$. Por tanto $d$ es una métrica.

Asimismo, $\|x\|\le\|x-y\|+\|y\|$ y $\|y\|\le\|y-x\|+\|x\|$. La simetría y las cotas dobles producen $|\|x\|-\|y\||\le\|x-y\|$. Esta prueba usa el axioma vectorial triangular, no sustituye vectores dentro de un teorema cuantificado sólo sobre números reales. En una métrica arbitraria se compara la distancia directa con la suma de dos distancias; la existencia de caminos minimizantes no se deduce de esos axiomas.

### Matrices, funciones y ejemplos de normas

En $\mathbb R^2$, $\|(x,y)\|_1=|x|+|y|$ es una norma: la no negatividad y definitud siguen de las propiedades del valor absoluto, la homogeneidad de la fórmula para $|ab|$, y la triangular se obtiene sumando las desigualdades escalares demostradas para cada coordenada. En matrices reales $r\times s$, con $r,s\ge1$ finitos, $\|A\|_1=\sum_{i,j}|a_{ij}|$ cumple las mismas propiedades entrada por entrada, con una suma finita.

Sea $c_{00}(\mathbb N)$ el espacio de funciones $f:\mathbb N\to\mathbb R$ de soporte finito. Está cerrado bajo suma y multiplicación escalar: el soporte de una suma está contenido en la unión de los dos soportes finitos y el de un múltiplo está contenido en el soporte original. Definimos $\|f\|_1=\sum_n|f(n)|$, suma finita independiente de añadir términos nulos. Si esta suma es cero, todos sus sumandos no negativos son cero, y $f=0$; la homogeneidad y triangular se prueban sobre la unión finita de los soportes. Las funciones $e_k(n)=1$ si $n=k$, y cero en otro caso, son linealmente independientes: evaluar una combinación finita en $k$ recupera su coeficiente. Este espacio es infinito dimensional. En cambio, las funciones constantes $\mathbb R\to\mathbb R$ forman un espacio de dimensión uno. Ser un espacio de funciones no obliga por sí solo a tener dimensión infinita.

Los ejemplos de normas en matrices y funciones amplían la intuición geométrica: un vector no tiene por qué ser una flecha dibujable. Pero ninguna función que se llame magnitud merece automáticamente el nombre de norma. Debe anularse sólo en cero, ser absolutamente homogénea y cumplir la triangular. Al demostrar estas propiedades separadamente aprendemos a reconocer cuáles argumentos dependen de la estructura vectorial y cuáles de la función concreta escogida.

## La desigualdad triangular y la estabilidad de los límites

Una pregunta más difícil aparece al retirar el axioma triangular: ¿sigue siendo estable la suma de sucesiones convergentes? Los dos ejemplos siguientes mostrarán que, sin ese axioma, la estabilidad puede fallar, pero también puede conservarse. Lo decisivo será identificar qué estimación adicional poseen las funciones consideradas.

Definamos $p(x,y)=|x|+|y|+x^2/|y|$ si $xy\ne0$, y $p(x,y)=|x|+|y|$ si $xy=0$. La segunda rama evita dividir por cero. La función es positiva fuera del origen y satisface $p(\lambda v)=|\lambda|p(v)$, pero $p(1,1)=3>2=p(1,0)+p(0,1)$.

Si definimos convergencia a $z$ mediante $p(z_n-z)\to0$, las sucesiones $u_n=(1/n,0)$ y $v_n=(0,1/n^2)$ convergen a cero. Para la suma, el término nuevo $x^2/|y|$ vale uno, y $p(u_n+v_n)=1+1/n+1/n^2$. Así, la suma no converge a cero. Tampoco tiene otro límite: como $p(x,y)\ge|x|+|y|$, cualquier límite para $p$ tendría que coincidir con los límites cero de ambas coordenadas. El desarrollo comprueba formalmente esa exclusión y todas las dependencias.

La ausencia de triangular no impone ese fallo en todos los casos. Por ejemplo, $q(x,y)=(\sqrt{|x|}+\sqrt{|y|})^2$ también es positiva y homogénea, y $q(1,1)=4>2=q(1,0)+q(0,1)$. Sin embargo,

$$
|x|+|y|\le q(x,y)\le2(|x|+|y|).
$$

Estas cotas hacen que converger para $q$ sea equivalente a converger en la norma $\ell^1$. La suma de límites se conserva en ese caso. La triangular garantiza directamente una estimación uniforme que permite sumar errores; si se retira, hay que buscar otro control o aceptar que esa operación puede fallar.

### Retirar la triangular puede destruir la suma de límites

En $\mathbb R^2$ definimos una función $p$ por

$$
p(x,y)=\begin{cases}
|x|+|y|+x^2/|y|,&xy\ne0,\\
|x|+|y|,&xy=0.
\end{cases}
$$

Es bien definida: en la primera rama $y\ne0$ y $|y|>0$; la segunda evita toda división por cero. Es no negativa y se anula exactamente en $(0,0)$ porque $p(x,y)\ge|x|+|y|$. Para $\lambda\ne0$, la condición $xy=0$ se conserva al multiplicar ambas coordenadas por $\lambda$. En la primera rama, $(\lambda x)^2/|\lambda y|=|\lambda|x^2/|y|$, usando $\lambda^2=|\lambda|^2$ y $|\lambda y|=|\lambda||y|$. Las dos ramas dan $p(\lambda v)=|\lambda|p(v)$; para $\lambda=0$ ambos miembros son cero. Sin embargo, $p(1,1)=3>2=p(1,0)+p(0,1)$, por lo que no es una norma.

Definimos expresamente la relación $z_n\to_p z$ por $p(z_n-z)\to0$, sin suponer que la función induzca una métrica. Sean $u_n=(1/n,0)$ y $v_n=(0,1/n^2)$. Entonces $p(u_n)=1/n\to0$ y $p(v_n)=1/n^2\to0$, mientras que

$$
p(u_n+v_n)=1/n+1/n^2+1>1.
$$

La suma no converge a cero. Tampoco converge a otro $w=(\alpha,\beta)$: si $p(u_n+v_n-w)\to0$, la cota $p\ge|x|+|y|$ implica $|1/n-\alpha|\to0$ y $|1/n^2-\beta|\to0$. Esas coordenadas ya convergen a cero; la unicidad de límites escalares, demostrada antes mediante la desigualdad triangular, obliga a $\alpha=\beta=0$, caso excluido. Aquí se usa la propiedad arquimediana de $\mathbb R$ para $1/n\to0$: dado $\varepsilon>0$, existe $N>1/\varepsilon$, y $n\ge N$ da $1/n<\varepsilon$; $1/n^2\le1/n$ para $n\ge1$.

La propiedad arquimediana utilizada aquí se deduce de la completitud del cuerpo ordenado: si $\mathbb N$ fuera acotado con supremo $s$, $s-1$ no sería cota superior, de modo que algún $n>s-1$ satisfaría $n+1>s$, contradicción.

### Ausencia de triangular sin pérdida de suma de límites

Definimos $q(x,y)=(\sqrt{|x|}+\sqrt{|y|})^2$, usando la existencia de raíces cuadradas no negativas en el cuerpo real completo. Es no negativa, definida y positiva fuera de cero. Es absolutamente homogénea: para $t=|\lambda|\ge0$, $\sqrt{t|x|}=\sqrt t\sqrt{|x|}$ porque el miembro derecho es no negativo y su cuadrado vale $t|x|$; la unicidad de raíz lo identifica. Al cuadrar la suma se obtiene $q(\lambda v)=|\lambda|q(v)$, incluyendo $\lambda=0$. Pero $q(1,1)=4>2=q(1,0)+q(0,1)$.

Para $A=\sqrt{|x|}$ y $B=\sqrt{|y|}$, $(A-B)^2\ge0$ implica $2AB\le A^2+B^2$. Por tanto,

$$
|x|+|y|\le q(x,y)=|x|+|y|+2\sqrt{|x||y|}\le2(|x|+|y|).
$$

Así, $z_n\to_q z$, definido mediante $q(z_n-z)\to0$, equivale a convergencia para la norma $\ell^1$: una dirección usa la primera cota y la otra usa la segunda con tolerancia $\varepsilon/2$. La suma de dos sucesiones convergentes para $q$ converge a la suma de sus límites por la estabilidad de límites bajo suma en $\ell^1$ y esta equivalencia. La ausencia de la triangular permite que falle la suma de límites, como en el contraejemplo anterior; no obliga a que falle en toda función positiva y homogénea.

### Segunda prueba escalar por cotas

Por las propiedades elementales del valor absoluto, $-|a|\le a\le|a|$ y $-|b|\le b\le|b|$. La compatibilidad del orden con la suma da $-(|a|+|b|)\le a+b\le|a|+|b|$. Por la equivalencia entre valor absoluto y cotas dobles, $|a+b|\le|a|+|b|$. Esta presentación deja visible la función de las cotas inferior y superior. No se utiliza ningún resultado que se pretende demostrar después.

Los dos ejemplos finales delimitan con exactitud el papel de la desigualdad triangular. Puede faltar y provocar el fracaso de la suma de límites, pero también puede faltar sin alterar las sucesiones convergentes cuando la función se compara por dos constantes con una norma auténtica. Esta diferencia evita convertir una posibilidad en una afirmación universal. La triangular no es solo una imagen geométrica agradable: es una hipótesis de estabilidad cuya presencia o ausencia debe examinarse en cada demostración.

## Problemas y soluciones del capítulo

### Ejercicio 1

Calcular $|a+b|$ y $|a|+|b|$ para $(a,b)=(3,2),(3,-2),(-3,-2),(4,-4),(0,0)$; describir cuándo hay igualdad.

**Solución razonada.** Los pares de valores son, respectivamente, $(5,5),(1,5),(5,5),(0,8),(0,0)$. En el primero, sumar positivos conserva magnitud. En el segundo y cuarto, los signos opuestos producen cancelación. En el tercero, la suma es $-5$, cuya magnitud es cinco. El último obliga a admitir el cero en «no negativo». La condición general de igualdad es $ab\ge0$, demostrada en el caso de igualdad escalar; no equivale a que ambos números sean positivos.

### Ejercicio 2

Auditar la pretendida prueba: «Como $a\le|a|$ y $b\le|b|$, multiplicamos las dos desigualdades y obtenemos $ab\le|a||b|$». Repararla.

**Solución razonada.** Multiplicar desigualdades miembro a miembro sin control de signos no es una regla válida. Por ejemplo, $-3\le1$ y $-2\le1$ son verdaderas, pero su producto sugeriría $6\le1$, falso. La reparación aplica $x\le|x|$ al único número $x=ab$, obteniendo $ab\le|ab|$. Se demuestra $|ab|=|a||b|$ por cuatro combinaciones de signos y el caso cero: dos signos iguales dan producto positivo; signos opuestos hacen que ambas expresiones de magnitud valgan $-ab$; un cero anula todo. Queda la cota requerida sin multiplicar por un factor de signo desconocido.

### Ejercicio 3

Decidir si $\sqrt{z^2}=z$ para todo real $z$, y si $u^2\le v^2$ implica $u\le v$ sin hipótesis adicionales.

**Solución razonada.** Para $z=-3$, la raíz no negativa de $z^2=9$ es tres, no menos tres. La identidad correcta es $\sqrt{z^2}=|z|$. Para $u=2,v=-3$, los cuadrados satisfacen $4\le9$, pero $2\le-3$ es falso. Si $u,v\ge0$, la inferencia sí vale: $u>v$ daría $u^2-v^2=(u-v)(u+v)>0$, contradiciendo la hipótesis. El signo de los números, no sólo el de sus cuadrados, controla esa recuperación del orden.

### Ejercicio 4

Resolver $|x-2|\le3$ y $|x-2|<3$. Explicar la diferencia en sus extremos.

**Solución razonada.** La primera condición equivale a $-3\le x-2\le3$, y al sumar dos a las tres partes queda $-1\le x\le5$. La segunda equivale a $-3<x-2<3$, por lo que $-1<x<5$. En $x=-1$ o $x=5$ el valor absoluto es tres: se incluyen en la primera solución y se excluyen en la segunda. Las equivalencias usan $3>0$ y los dos casos de signo del argumento, no una eliminación formal de barras.

### Ejercicio 5

Probar $||a|-|b||\le|a-b|$ a partir de la triangular, sin suponer $|a|\ge|b|$. Si $|a-b|<0.01$, obtener una cota para la diferencia de magnitudes.

**Solución razonada.** De $a=(a-b)+b$ y la triangular sale $|a|-|b|\le|a-b|$. Intercambiar variables da $|b|-|a|\le|b-a|=|a-b|$. Negando esta última desigualdad y combinando, $-|a-b|\le|a|-|b|\le|a-b|$. La equivalencia de cota doble y valor absoluto produce el resultado, sin decidir cuál magnitud es mayor. Por transitividad, la hipótesis numérica da $||a|-|b||<0.01$. Esta cota estricta final procede del dato estricto, aunque la inversa sea no estricta.

### Ejercicio 6

Para $u,v\in\mathbb R^2$ con longitud euclídea, determinar cuándo $\|u+v\|_2=\|u\|_2+\|v\|_2$. ¿Basta que los tres puntos del dibujo sean colineales?

**Solución razonada.** Si uno es cero, hay igualdad. Para ambos no nulos, comparar los cuadrados reduce la igualdad a $u\cdot v=\|u\|_2\|v\|_2>0$. La identidad $\|u\|_2^2\|v\|_2^2-(u\cdot v)^2=(u_1v_2-u_2v_1)^2$ fuerza determinante cero, por lo que $v=\lambda u$; se toma una coordenada $u_i\ne0$, se define $\lambda=v_i/u_i$ y la otra coordenada sigue de la identidad. El producto escalar positivo exige $\lambda>0$. Recíprocamente, $v=\lambda u$ con $\lambda>0$ hace $\|v\|_2=\lambda\|u\|_2$ y $\|u+v\|_2=(1+\lambda)\|u\|_2$, luego hay igualdad. La colinealidad sola permite sentido contrario: $u=(1,0),v=(-1,0)$ da cero en el miembro izquierdo y dos en el derecho. Los puntos son colineales, pero la igualdad falla.

### Ejercicio 7

En cualquier espacio normado, probar que para $m\ge1$ y $x_0,\ldots,x_m$, $\|x_m-x_0\|\le\sum_{j=1}^m\|x_j-x_{j-1}\|$.

**Solución razonada.** La identidad telescópica $x_m-x_0=\sum_{j=1}^m(x_j-x_{j-1})$ se verifica cancelando cada término intermedio. La cota para una suma finita se demuestra por inducción: para un sumando es igualdad; agregar uno más usa la triangular y luego la hipótesis inductiva. Aplicándola a los incrementos obtenemos la cota pedida. Este argumento sólo compara magnitudes de incrementos finitos; no presupone la existencia de una curva minimizante.

### Ejercicio 8

Dados $a_n\to a$ y $b_n\to b$, probar que $a_n+b_n\to a+b$ usando presupuestos $\varepsilon/3$ y $2\varepsilon/3$. Explicar por qué se necesita un máximo de índices.

**Solución razonada.** Fijado $\varepsilon>0$, la primera hipótesis entrega $N_a$ con $|a_n-a|<\varepsilon/3$ para $n\ge N_a$, y la segunda $N_b$ con $|b_n-b|<2\varepsilon/3$ para $n\ge N_b$. Definimos $N=\max(N_a,N_b)$. Para todo $n\ge N$, la triangular y la reagrupación de términos dan $|(a_n+b_n)-(a+b)|\le|a_n-a|+|b_n-b|<\varepsilon$. El máximo asegura que ambos controles estén activos para el mismo término; elegir sólo $N_a$ podría dejar el segundo error sin control. La construcción satisface el orden de cuantificadores: primero tolerancia, luego índice, después todos los índices mayores.

### Ejercicio 9

Mostrar que toda sucesión convergente en un espacio normado es de Cauchy. Señalar qué parte no demuestra que toda sucesión de Cauchy converja.

**Solución razonada.** Si $x_n\to x$, para cada $\varepsilon>0$ elegimos $N$ con $\|x_n-x\|<\varepsilon/2$ para todo $n\ge N$. Si $m,n\ge N$, $\|x_n-x_m\|\le\|x_n-x\|+\|x-x_m\|<\varepsilon$, usando simetría de la norma. Así cumple la definición de Cauchy. La prueba empezó con un límite $x$ ya existente; no construye uno a partir de la condición de Cauchy. La recíproca exige completitud del espacio y queda fuera de lo demostrado aquí.

### Ejercicio 10

Probar que $\|(x,y)\|_1=|x|+|y|$ es norma; hallar dos vectores no paralelos que tengan igualdad triangular en ella. Mostrar que $h(x,y)=|x|$ no es norma en $\mathbb R^2$.

**Solución razonada.** La suma es no negativa y sólo se anula si ambas coordenadas se anulan, porque sus sumandos son no negativos. La identidad del producto de valores absolutos da $\|\lambda(x,y)\|_1=|\lambda|(|x|+|y|)$. Para dos vectores, la triangular escalar aplicada a cada coordenada y sumada demuestra la tercera cláusula. Con $u=(1,0),v=(0,1)$, sus normas son uno y la de la suma es dos; no son paralelos. La función $h$ cumple no negatividad, homogeneidad absoluta y triangular, pero $h(0,1)=0$ para un vector no nulo, por lo que falla definitud. La caracterización de la igualdad geométrica del ejercicio 6 depende de que la norma sea euclídea.

### Ejercicio 11

Para la función $p$ del contraejemplo sin triangular, comprobar todas las propiedades que conserva y demostrar que la suma de $u_n=(1/n,0)$ y $v_n=(0,1/n^2)$ no converge para la relación $\to_p$ a ningún punto.

**Solución razonada.** La rama con $xy\ne0$ tiene denominador $|y|>0$; en los ejes la rama sin cociente evita el cero. La cota $p(x,y)\ge|x|+|y|$ da no negatividad y definitud. Si $\lambda\ne0$, preserva la pertenencia a los ejes y el cociente escala por $\lambda^2/|\lambda|=|\lambda|$, de modo que $p(\lambda v)=|\lambda|p(v)$ en ambas ramas; si $\lambda=0$, se verifica directamente. La triangular falla porque $p(1,1)=3$ y la suma de valores en los vectores coordenados es dos. Para las sucesiones, $p(u_n)=1/n$ y $p(v_n)=1/n^2$ tienden a cero, por la propiedad arquimediana. Pero $p(u_n+v_n)=1+1/n+1/n^2>1$, por lo que no convergen a cero. Si convergieran a $(\alpha,\beta)$ para $p$, su cota inferior obligaría a $1/n\to\alpha$ y $1/n^2\to\beta$. La unicidad de límites escalares, probada con la triangular escalar, obliga a $\alpha=\beta=0$, contradicción. No se usa una triangular para $p$ ni se llama métrica a $p(x-y)$.

### Ejercicio 12

Para $q(x,y)=(\sqrt{|x|}+\sqrt{|y|})^2$, verificar que no es norma y que, aun así, la suma de dos sucesiones convergentes para $q$ converge a la suma de sus límites.

**Solución razonada.** Las raíces no negativas existen para todos los reales no negativos por el teorema demostrado mediante la propiedad del supremo. La función es positiva fuera del origen. La unicidad de raíz muestra $\sqrt{|\lambda||x|}=\sqrt{|\lambda|}\sqrt{|x|}$, por lo que al cuadrar la suma $q(\lambda v)=|\lambda|q(v)$. Sin embargo, $q(1,1)=4>2=q(1,0)+q(0,1)$, y falla la triangular. Poniendo $A=\sqrt{|x|},B=\sqrt{|y|}$, de $(A-B)^2\ge0$ resulta $2AB\le A^2+B^2$, y obtenemos $\|v\|_1\le q(v)\le2\|v\|_1$. La primera cota convierte convergencia para $q$ en convergencia para $\ell^1$; la segunda convierte convergencia para $\ell^1$ en convergencia para $q$, usando tolerancia $\varepsilon/2$. Si $u_n\to_q u$ y $v_n\to_q v$, ambas convergen en $\ell^1$, su suma converge allí por la estabilidad de los límites bajo suma en espacios normados, y entonces converge para $q$. El ejemplo precedente muestra que la estabilidad puede fallar; éste demuestra que tal fallo no es inevitable para toda función sin desigualdad triangular.


### Ejercicio 13

En un cuerpo ordenado arbitrario $F$, demuestra $|a+b|\le |a|+|b|$ exclusivamente mediante cotas superiores e inferiores, sin elevar al cuadrado. Precisa dónde se usa la hipótesis de cuerpo ordenado y qué papel desempeña la completitud.

**Solución razonada.** Por definición de valor absoluto, $-|a|\le a\le |a|$ y $-|b|\le b\le |b|$. La invariancia del orden por traslaciones autoriza sumar las desigualdades correspondientes: $-(|a|+|b|)\le a+b\le |a|+|b|$. El extremo $|a|+|b|$ es no negativo, por lo que la equivalencia entre valor absoluto y cotas dobles da $|a+b|\le |a|+|b|$. Solo se utilizaron reglas de orden y adición de $F$; no existe ninguna aplicación del axioma del supremo. Esta prueba por cotas ofrece un segundo camino, independiente del argumento por cuadrados.

### Ejercicio 14

En los reales ya construidos, para $a,b\ge0$ demuestra $|\sqrt a-\sqrt b|\le\sqrt{|a-b|}$. Justifica la existencia de las raíces y todos los pasos de orden.

**Solución razonada.** El teorema de existencia de raíces cuadradas no negativas, obtenido mediante la propiedad del supremo, garantiza las raíces de $a,b,|a-b|$. Por simetría basta suponer $a\ge b$, de modo que $x=\sqrt a\ge y=\sqrt b\ge0$ por monotonía de la raíz. La identidad de diferencia de cuadrados da $a-b=(x-y)(x+y)$. Puesto que $x+y\ge x-y\ge0$, multiplicar por $x-y$ conserva el orden y produce $a-b\ge(x-y)^2$. Ambos lados son no negativos. La comparación de raíces del orden de los cuadrados concluye $\sqrt{a-b}\ge x-y=|\sqrt a-\sqrt b|$. Para $b\ge a$ se intercambian las letras. Este argumento no necesita continuidad previamente demostrada de la raíz: da una cota explícita que después permite demostrarla.

### Ejercicio 15

Utilizando únicamente reglas de cuerpo ordenado, desigualdad triangular y definición de límite, demuestra que si $a_n\to a$ y $b_n\to b$ entonces $a_nb_n\to ab$. No presupongas continuidad del producto.

**Solución razonada.** Sea $\varepsilon>0$ y definamos $\delta=\min\{1/2,\varepsilon/[2(|a|+|b|+2)]\}>0$. Elegimos índices $N_a,N_b$ para que, si $n\ge N=\max\{N_a,N_b\}$, se tenga $|a_n-a|<\delta$ y $|b_n-b|<\delta$. La triangular da $|a_n|\le |a|+|a_n-a|<|a|+1$. La identidad algebraica $a_nb_n-ab=a_n(b_n-b)+b(a_n-a)$ y $|xy|=|x||y|$ implican

$$|a_nb_n-ab|\le |a_n||b_n-b|+|b||a_n-a|<(|a|+1+|b|)\delta<\varepsilon.$$

La última desigualdad se deduce de la elección de $\delta$. Todas las multiplicaciones de cotas emplean cantidades no negativas; el índice $N$ sirve simultáneamente para las dos convergencias.

### Ejercicio 16

En $\mathbb R^2$ prueba $\|v\|_2\le\|v\|_1\le\sqrt2\|v\|_2$ y concluye que ambas normas definen las mismas sucesiones convergentes.

**Solución razonada.** Para $v=(x,y)$, ambas normas son no negativas. Como $2|x||y|\ge0$,

$$x^2+y^2\le (|x|+|y|)^2.$$

Además $(|x|-|y|)^2\ge0$ implica $2|x||y|\le x^2+y^2$, y por tanto

$$(|x|+|y|)^2\le2(x^2+y^2).$$

La existencia de raíces cuadradas no negativas, demostrada mediante supremos, y la monotonía de dichas raíces permiten pasar de las desigualdades entre cuadrados a las cotas propuestas. Si $\|v_n-v\|_1\to0$, la primera cota da $\|v_n-v\|_2\to0$. Recíprocamente, para una tolerancia $\varepsilon$ de la norma uno, basta pedir que el error euclídeo sea menor que $\varepsilon/\sqrt2$, pues $\sqrt2>0$. La equivalencia de convergencia se ha demostrado mediante constantes, sin identificación de las normas como funciones iguales.

### Ejercicio 17

Considera el espacio $c_{00}(\mathbb N)$ de sucesiones reales de soporte finito con $\|x\|_1=\sum_n|x(n)|$, definido en los ejemplos de normas. Prueba que $x^{(N)}=\sum_{k=1}^N2^{-k}e_k$ es de Cauchy, pero no converge en ese espacio.

**Solución razonada.** Si $M>N$, la diferencia tiene norma $\sum_{k=N+1}^M2^{-k}<2^{-N}$: se obtiene multiplicando la suma geométrica finita por dos y restando, o usando $\sum_{k=N+1}^M2^{-k}=2^{-N}-2^{-M}$. Por inducción $2^N\ge N+1$, y la arquimedianidad de $\mathbb R$ permite hacer $2^{-N}$ menor que cualquier tolerancia. Por tanto las diferencias de términos con índices suficientemente grandes son pequeñas y la sucesión es de Cauchy.

Supongamos que converge en $c_{00}$ a un $f$ de soporte finito. Elijamos $k$ fuera de su soporte. Para todo $N\ge k$, la coordenada $k$ de $x^{(N)}-f$ es $2^{-k}$; por la cota $\|z\|_1\ge|z(k)|$, tenemos $\|x^{(N)}-f\|_1\ge2^{-k}>0$. Esto contradice la convergencia a $f$. La completitud de los escalares reales no implica automáticamente la completitud de cualquier espacio normado de funciones.

### Ejercicio 18

Sea $p$ la función del contraejemplo sin triangular y $\|\cdot\|_1$ la norma usual. Demuestra que no existe una constante $C>0$ tal que $p(v)\le C\|v\|_1$ para todos los vectores $v$. Compara con la función $q$ del ejemplo homogéneo comparable a una norma.

**Solución razonada.** Tomemos $v_t=(t,t^2)$ con $t>0$. Ninguna coordenada es cero y

$$p(v_t)=t+t^2+\frac{t^2}{t^2}=t+t^2+1,\qquad\|v_t\|_1=t+t^2.$$

Cuando $t\to0^+$, la norma usual tiende a cero, pero $p(v_t)\ge1$. Si existiera tal $C$, escoger $0<t<\min(1,1/(4C))$ daría $C(t+t^2)<2Ct<1/2< p(v_t)$, contradicción. La función homogénea $q$, comparable con una norma, satisface en cambio $\|v\|_1\le q(v)\le2\|v\|_1$ para todo $v$. Por eso la convergencia inducida por $q$ coincide con la usual, mientras el fallo de estabilidad de $p$ puede explicarse por su falta de control uniforme en términos de una norma.

## Problemas de síntesis

### Problema de síntesis 1

Sea $D$ el conjunto de cortaduras racionales y $C_r=\{q\in\mathbb Q:q<r\}$. Prueba que, para toda $A\in D$ y todo $r\in\mathbb Q$,

$$r\in A\iff C_r\subsetneq A.$$

Determina si la demostración de esta equivalencia **necesita** que $A$ no tenga máximo, o si vale para cualquier subconjunto de $\mathbb Q$ cerrado hacia abajo (interpretando $\subsetneq$ como inclusión de conjuntos, sin exigir $A\in D$).

**Solución razonada.** Si $r\in A$, todo $q<r$ pertenece a $A$ por descenso, de modo que $C_r\subseteq A$. La inclusión es estricta porque el **propio $r$** pertenece a $A$ y no pertenece a $C_r$. Si $C_r\subsetneq A$, existe $s\in A\setminus C_r$, es decir, $s\ge r$. Si $s=r$, se tiene $r\in A$; si $s>r$, el descenso también da $r\in A$. No se utilizó la ausencia de máximo, la condición de conjunto propio, no vacuidad ni completitud. Para comprobarlo en un conjunto descendente con máximo, sea $A=\{q\in\mathbb Q:q\le0\}$. Tiene máximo $0$, y aun así la equivalencia vale para **cada** racional $r$. La ausencia de máximo es una condición necesaria para pertenecer a $D$, pero **no es hipótesis mínima de este lema**. La equivalencia se utilizará para demostrar la unicidad de la identificación entre un cuerpo completo y sus cortaduras.

### Problema de síntesis 2

Para $A=C_0$ examina el par $[0,1]$ como recinto y como intervalo admisible. Construye un intervalo admisible mediante ensanchamiento y prueba que su anchura se incrementa en $2\eta$ respecto del original.

**Solución razonada.** El par $[0,1]$ es un recinto porque $C_0\subseteq A=C_0\subseteq C_1$. No es admisible: el extremo inferior $0\notin A$. Para cualquier racional $\eta>0$, el intervalo $[-\eta,1+\eta]$ sí es admisible: $-\eta<0$, de modo que $-\eta\in C_0$, y $1+\eta\ge0$, por lo que $1+\eta\notin C_0$. La anchura inicial era $1$; la nueva es $(1+\eta)-(-\eta)=1+2\eta$. Si se necesita una anchura final menor que un objetivo $\rho$ y se escoge $2\eta<\rho$, debe elegirse el recinto inicial con anchura menor que $\rho-2\eta$; no basta con que el recinto inicial mida menos que $\rho$. Esta precaución es indispensable para transferir identidades por recintos sin perder el control de la anchura.

### Problema de síntesis 3

Demuestra directamente, sin utilizar el teorema de unicidad de los cuerpos ordenados completos, que la suma por recintos admisibles de la construcción por recintos coincide con la suma por testigos de la construcción por testigos. Explica por qué esta demostración no prueba automáticamente la coincidencia de productos.

**Solución razonada.** La suma por recintos se define como la unión de $C_{a+b}$ cuando $a\in A$ y $b\in B$ son extremos inferiores de intervalos admisibles. Cualquier $a\in A$ puede completarse con un $u\notin A$, y cualquier $b\in B$ con un $v\notin B$; las cuatro condiciones de cortadura garantizan $a<u$, $b<v$. Así **todos** los pares $(a,b)\in A\times B$ aparecen como extremos inferiores de alguna elección admisible. Recíprocamente, todo extremo inferior admisible pertenece al corte correspondiente. Por tanto la unión es exactamente

$$\bigcup_{a\in A,\ b\in B} C_{a+b}=\{q\in\mathbb Q:\exists a\in A,b\in B,\ q<a+b\},$$

la suma por testigos. El producto por recintos toma el **mínimo de cuatro productos de extremos**, mientras que el producto positivo por testigos controla signos y exige $a,b>0$; la identificación de estas fórmulas necesita pruebas adicionales. Una comparación global de ambas multiplicaciones se realiza *después* de terminar ambos cuerpos y disponer del isomorfismo del teorema de unicidad, como demuestra el teorema comparativo del tercer apéndice.

### Problema de síntesis 4

Sean $F,G$ cuerpos ordenados completos y $x,y>0_F$. Define $A_x^+$, $A_y^+$ como en el teorema de unicidad y

$$U=\{q\in\mathbb Q:\exists a\in A_x^+,b\in A_y^+,\ q<ab\},\qquad P=U\cap\mathbb Q_{>0}.$$

Prueba $U=A_{xy}$, $P=A_{xy}^+$ y que $P$ no es una cortadura de Dedekind en todo $\mathbb Q$.

**Solución razonada.** Si $q<ab$ con $a,b>0$ situados bajo $x,y$, multiplicar desigualdades por positivos da $q_F<(ab)_F<xy$, luego $U\subseteq A_{xy}$. Para la otra inclusión, como $xy>0$, todo racional no positivo $q$ es menor que el producto de **cualquier** par de testigos positivos, que existen por densidad racional. Si $q>0$ y $q_F<xy$, elegimos primero $b_F$ racional transportado con $q_F/x<b_F<y$, que es posible por densidad, y después $a_F$ racional transportado con $q_F/b_F<a_F<x$. Ambos denominadores $x$ y $b_F$ son positivos. Se sigue $q_F<a_Fb_F$ y, por reflexión del orden racional, $q<ab$: así $A_{xy}\subseteq U$. La igualdad de las partes positivas es ahora una intersección con $\mathbb Q_{>0}$. En cuanto $q>0$ pertenece a $P$, el racional $-1$ es menor que $q$ pero no pertenece a $P$. Falla descenso en $\mathbb Q$, por lo que $P$ no es una cortadura completa aunque su imagen tenga supremo en $G$.

### Problema de síntesis 5

Sea $F$ un cuerpo ordenado, quizá no completo. Demuestra $|a+b|\le|a|+|b|$ conservando la prueba por cuadrados; explica por qué es lícito escribir $\sqrt{(a+b)^2}$ sin asumir que toda cantidad positiva de $F$ tenga raíz.

**Solución razonada.** Por el análisis de signos, $|ab|=|a||b|$; también $ab\le|ab|$. Como $2>0$,

$$(a+b)^2=a^2+2ab+b^2\le |a|^2+2|a||b|+|b|^2=(|a|+|b|)^2.$$

Ambos números $u=|a+b|$ y $v=|a|+|b|$ son no negativos. Si $u>v$, entonces $u^2-v^2=(u-v)(u+v)>0$, contradiciendo la desigualdad cuadrática. Luego $u\le v$. La expresión $\sqrt{(a+b)^2}$ designa aquí **el elemento conocido** $|a+b|$, que ya pertenece a $F$, satisface el cuadrado indicado y es no negativo; su unicidad se sigue de la estricta monotonía de cuadrados no negativos. No se construyó $\sqrt c$ para un positivo arbitrario $c$. Por eso no se necesita completitud de $F$.

### Problema de síntesis 6

En $c_{00}(\mathbb N)$ con $\|x\|_1=\sum_k|x(k)|$, toma $x^{(N)}=\sum_{k=1}^N2^{-k}e_k$. Prueba que $(x^{(N)})_N$ es de Cauchy, que no converge dentro de $c_{00}$ y por qué no contradice la completitud de $\mathbb R$.

**Solución razonada.** Si $M>N$, la diferencia tiene norma $\sum_{k=N+1}^M2^{-k}=2^{-N}-2^{-M}<2^{-N}$. Dada $\varepsilon>0$, la propiedad arquimediana asegura algún $N_0$ con $2^{-N_0}<\varepsilon$, pues $2^N\ge N+1$. Para $M,N\ge N_0$, reordenamos los índices y aplicamos la cota desde el menor de ellos: la distancia es menor que $\varepsilon$. Se cumple Cauchy. Si existiera límite $f\in c_{00}$, su soporte sería finito; elegimos $k$ fuera de él. Para todo $N\ge k$ la diferencia coordenada $k$ vale $2^{-k}$ y $\|x^{(N)}-f\|_1\ge2^{-k}>0$, contradiciendo convergencia a $f$. Los escalares individuales pertenecen a un cuerpo completo, pero el supuesto límite natural tiene infinitas coordenadas no nulas y **no pertenece al espacio de soporte finito**. La propiedad de que toda sucesión de Cauchy converge se refiere al espacio normado completo, no solamente a su cuerpo base.


Los problemas de síntesis vuelven sobre una lección fundamental: los axiomas que hacen de un conjunto una cortadura no son siempre las hipótesis mínimas de cada propiedad que demostramos acerca de él. Distinguir ambas cuestiones permite construir pruebas más precisas y evita incorporar premisas que no se utilizan.

# Otra construcción de las operaciones mediante recintos racionales

En el capítulo II definimos las operaciones a partir de testigos racionales. Este apéndice vuelve al mismo problema con una información más simétrica: un intervalo racional que rodea la cortadura. Calcular con sus extremos produce recintos para la suma, el producto o el recíproco. Para obtener operaciones exactas tendremos que controlar la admisibilidad de esos extremos y demostrar que recintos arbitrariamente estrechos determinan una misma cortadura.

## Consecuencias del axioma del supremo

Los lemas de esta primera parte se aplican a cualquier cuerpo ordenado completo. No se utilizan como premisas para fabricar el cuerpo de cortaduras: allí sólo tendremos racionales y conjuntos de racionales. La distinción entre estudiar las consecuencias de una estructura y demostrar que dicha estructura existe será especialmente importante al comparar posteriormente los modelos.

### Propiedad arquimediana

Sea \(F\) un cuerpo ordenado completo. Los elementos \(n1_F\), \(n\in\mathbb N\), están estrictamente ordenados: \((n+1)1_F=n1_F+1_F>n1_F\). Si el conjunto de estos elementos estuviese acotado superiormente, tendría supremo \(s\). Como \(s-1<s\), existe un natural \(n\) tal que \(s-1<n1_F\). Entonces \(s<(n+1)1_F\), contradicción. Por tanto, para cada \(x\in F\) hay \(n\in\mathbb N\) con \(x<n1_F\).

**Lectura del argumento.** La propiedad arquimediana afirma que los naturales insertados en $F$ no pueden quedar todos por debajo de una cota. El movimiento decisivo de la prueba es tomar una supuesta cota mínima $s$ y observar que $s-1<s$; la caracterización del supremo proporciona un natural mayor que $s-1$. Al sumarle $1$ se produce otro natural mayor que $s$, lo que contradice la elección de $s$. Esta estrategia —desplazar una cota y usar el carácter mínimo del supremo— es distinta de probar directamente que cada elemento de $F$ está acotado por un entero.

### Copia canónica de los racionales

La función \(n\mapsto n1_F\) respeta la suma y el producto de naturales, por asociatividad y distributividad. Se extiende a enteros por inversos aditivos. Es inyectiva: si \(m<n\), entonces \((n-m)1_F>0\). Definimos

$$\iota_F(p/q)=(p1_F)(q1_F)^{-1},\qquad q\ne0.$$

Si \(p/q=p'/q'\), entonces \(pq'=p'q\) en \(\mathbb Z\); la misma identidad vale en \(F\), y multiplicar por los inversos de los denominadores prueba que las imágenes coinciden. Las fórmulas de suma y producto de fracciones muestran que \(\iota_F\) es homomorfismo; su inyectividad se deduce de la de los enteros. Usando denominadores positivos, la positividad de los inversos muestra que preserva y refleja el orden. Identificaremos cada racional con su imagen cuando el cuerpo esté claro.

**Verificación de buena definición.** La fórmula para $\iota_F(p/q)$ no debe depender de la fracción elegida para representar un racional. Si $p/q=r/s$, con $q,s\ne0$, entonces $ps=rq$. Después de pasar a $F$ y multiplicar por $(q_Fs_F)^{-1}$, se obtiene $p_Fq_F^{-1}=r_Fs_F^{-1}$. Los denominadores son no nulos porque la aplicación de los enteros es inyectiva. También se verifican explícitamente, por distributividad y conmutatividad,

$$\iota_F\left(\frac pq+\frac rs\right)
=\frac{p_Fs_F+r_Fq_F}{q_Fs_F}
=\iota_F(p/q)+\iota_F(r/s),$$

$$\iota_F\left(\frac pq\frac rs\right)=\frac{p_Fr_F}{q_Fs_F}
=\iota_F(p/q)\,\iota_F(r/s).$$

Estas igualdades, junto con $\iota_F(1)=1_F$, fundamentan por qué hablamos de una **copia racional canónica**, y no de una selección arbitraria de fracciones. No se recurre a la completitud para definir la copia.

### Localización entre enteros

Para \(t\in F\), tomemos \(N\in\mathbb N\) con \(N>|t|\), donde \(|t|=t\) si \(t\ge0\), y \(|t|=-t\) si \(t<0\). Hay naturales \(k\) con \(k-N>t\), por la prueba arquimediana. Sea \(k\) el menor. Como \(-N<t\), se tiene \(k\ge1\), y la minimalidad implica \((k-1)-N\le t\). Con \(m=k-N\in\mathbb Z\),

$$m-1\le t<m.$$

### Densidad racional

Sean \(x<y\) en \(F\). Por la prueba arquimediana hay \(n\in\mathbb N\), \(n>0\), tal que \(n>(y-x)^{-1}\). Así \(n(y-x)>1\). Por la localización de enteros existe \(m\in\mathbb Z\) tal que \(m-1\le nx<m\). Entonces

$$nx<m\le nx+1<ny.$$

Dividir por \(n>0\) da \(x<m/n<y\). La densidad no se ha supuesto: se ha deducido de la completitud.

### De la localización entera a la densidad racional

El procedimiento de localización entre enteros no presupone una función piso: ésta sería otra forma de expresar el resultado que se acaba de demostrar. La buena ordenación de los naturales selecciona el **primer** entero que supera $t$ después de trasladarlo por un entero $N$; la minimalidad de ese índice proporciona el extremo inferior.

En la densidad racional se amplía primero la diferencia $y-x>0$ mediante un entero positivo $n$ hasta que $n(y-x)>1$. Se localiza entonces un entero $m$ estrictamente entre $nx$ y $ny$, y se divide por $n>0$. El racional $m/n$ no se supuso denso de antemano: se construyó usando la propiedad arquimediana y la localización anterior. El orden lógico de estas dos pruebas es esencial para evitar circularidad.

## Operaciones por recintos mediante cortaduras racionales

### Cortaduras y orden por inclusión

Una cortadura es un subconjunto \(A\subset\mathbb Q\) con un elemento interior y otro exterior, cerrado hacia abajo y con un elemento mayor dentro del conjunto para cada elemento suyo. Es decir, \(a\in A\), \(r<a\) implican \(r\in A\), y para cada \(a\in A\) existe \(a'\in A\) con \(a<a'\). Denotamos por \(D\) el conjunto de todas las cortaduras. Es un conjunto, pues es un subconjunto del conjunto potencia de \(\mathbb Q\).

Para \(r\in\mathbb Q\), sea \(C_r=\{q\in\mathbb Q:q<r\}\). Es cortadura: contiene \(r-1\), excluye \(r\), está cerrada hacia abajo y, dado \(q<r\), contiene \((q+r)/2>q\). Se tiene \(C_r\subsetneq C_s\iff r<s\): una implicación se obtiene de la inclusión de intervalos; para la estricta, \(r\in C_s\setminus C_r\). La recíproca sigue por tricotomía.

Ordenamos \(D\) por inclusión estricta. Es un orden total: si \(A\not\subseteq B\), elijamos \(a\in A\setminus B\). Todo \(b\in B\) satisface \(b<a\), pues de \(a\le b\) y el cierre hacia abajo se seguiría \(a\in B\). Luego \(B\subseteq A\). Transitividad y tricotomía se deducen de la inclusión y la igualdad de conjuntos.

Un **intervalo racional admisible** para \(A\) es un par \([a,b]\) con \(a\in A\) y \(b\notin A\). Siempre \(a<b\), y

$$C_a\subseteq A\subseteq C_b.$$

Para la segunda inclusión, un elemento de \(A\) no puede ser mayor que \(b\) por cierre hacia abajo, ni igual por la elección de \(b\).

Existen intervalos admisibles de anchura menor que cualquier \(\varepsilon\in\mathbb Q\), \(\varepsilon>0\). Partimos de cualquiera y bisecamos: si el punto medio pertenece a \(A\), sustituimos el extremo inferior; si no, el superior. La anchura después de \(n\) pasos es \((b-a)/2^n\). Como \(2^n\ge n+1\), la arquimedianidad racional permite hacerla menor que \(\varepsilon\). Esto es un procedimiento finito; no se usa un límite real.

**Criterio de igualdad.** Si dos cortaduras admiten un mismo recinto \(C_l\subseteq A,B\subseteq C_u\) de anchura \(u-l\) arbitrariamente pequeña, son iguales. En efecto, si \(A\subsetneq B\), escojamos \(r\in B\setminus A\) y \(s\in B\), \(r<s\). De \(C_l\subseteq A\) resulta \(l\le r\), y de \(B\subseteq C_u\), \(s<u\). Por tanto, \(u-l>s-r>0\), imposible para anchuras arbitrariamente pequeñas. El otro orden se trata intercambiando las cortaduras.

**Distinción fundamental: recinto frente a intervalo admisible.** Un recinto de $H$ es un par racional $l<u$ que satisface $C_l\subseteq H\subseteq C_u$. En cambio, el intervalo $[a,b]$ es *admisible* cuando $a\in H$ y $b\notin H$. Todo intervalo admisible proporciona un recinto, pero la recíproca puede fallar: para $H=C_0$, el par $[0,1]$ satisface $C_0\subseteq H\subseteq C_1$, aunque $0\notin H$, de modo que no es admisible.

Esta diferencia determina qué extremos se pueden introducir en las operaciones definidas en la construcción mediante recintos. Si sólo se conoce un recinto $[l,u]$ de $H$, se obtiene un intervalo admisible **ensanchándolo** a $[l-\eta,u+\eta]$, donde $\eta>0$. Se tiene $l-\eta\in C_l\subseteq H$ y $u+\eta\notin C_u\supseteq H$. El precio es aumentar la anchura en $2\eta$, un efecto que debe entrar en todas las estimaciones posteriores.

### Operaciones mediante intervalos racionales

Para intervalos admisibles \([a,b]\) de \(A\) y \([c,d]\) de \(B\), asociamos los recintos:

$$[a+c,b+d],\qquad [-b,-a],$$
$$[L,U],\quad L=\min(ac,ad,bc,bd),\quad U=\max(ac,ad,bc,bd).$$

Para \(A\ne C_0\), usamos también intervalos admisibles que no contienen cero y el recinto \([1/b,1/a]\). Existen: si \(C_0\subsetneq A\), hay un racional positivo en \(A\) (si el primer testigo fuera cero, la ausencia de máximo proporciona uno positivo). Si \(A\subsetneq C_0\), hay un racional negativo fuera de \(A\): un testigo de \(C_0\setminus A\). Se escogen ambos extremos del mismo signo.

Definimos cada resultado como

$$\bigcup_{[L,U]}C_L,$$

donde se recorren los intervalos admisibles correspondientes. Así se definen \(A+B\), \(-A\), \(AB\) y \(A^{-1}\) para \(A\ne C_0\). Los neutros propuestos son \(C_0\) y \(C_1\).

**Justificación de que son cortaduras.** Dos intervalos admisibles de una misma cortadura tienen interior común: su mayor extremo inferior pertenece a la cortadura y su menor extremo superior no pertenece, por lo que el primero es estrictamente menor que el segundo. Escogiendo una entrada racional en ese interior para cada variable, su suma, opuesto, producto o recíproco pertenece a los dos recintos de salida. En el recíproco las entradas permanecen del mismo signo; intervalos positivos y negativos de una misma cortadura no pueden coexistir. Se sigue que cualquier extremo inferior de salida es menor o igual que cualquier extremo superior de salida, aun cuando procedan de elecciones diferentes.

La unión de los \(C_L\) es no vacía (contiene un racional menor que un \(L\) elegido), está cerrada hacia abajo y no tiene máximo, porque cada miembro de la unión pertenece a algún \(C_L\) sin máximo. Es propia: un extremo superior \(U_0\) elegido no está en ningún \(C_L\), ya que \(L\le U_0\). Además, para cada recinto de salida,

$$C_L\subseteq\text{resultado}\subseteq C_U.$$

**Justificación de los recintos y sus anchuras.** Para suma y opuesto es inmediata. Para producto, si \(a\le t\le b\), \(c\le v\le d\), escribimos \(t=(1-\lambda)a+\lambda b\), \(v=(1-\mu)c+\mu d\), con \(\lambda,\mu\in[0,1]\). La expansión de \(tv\) es una combinación de \(ac,ad,bc,bd\) con coeficientes no negativos que suman uno. Por tanto, pertenece a \([L,U]\). Este razonamiento es puramente racional.

Si los cuatro extremos tienen valor absoluto menor o igual que \(M\), cualesquiera dos productos de extremos difieren en valor absoluto a lo sumo

$$M((b-a)+(d-c)),$$

usando \(tv-t'v'=t(v-v')+v'(t-t')\). Así la anchura del recinto del producto obedece la misma cota. La del recinto de la suma es \((b-a)+(d-c)\); la del opuesto es \(b-a\). Para el recíproco, si los extremos tienen módulo al menos \(h>0\),

$$\frac1a-\frac1b=\frac{b-a}{ab}\le\frac{b-a}{h^2}.$$

Podemos refinar dentro de intervalos iniciales fijos; los módulos quedan acotados, y para el recíproco quedan además separados de cero. En consecuencia, las anchuras de salida pueden hacerse arbitrariamente pequeñas.

**Ejemplo orientador.** Para las cortaduras principales $C_1$ y $C_2$ se pueden escoger intervalos admisibles $[1-\delta,1+\delta]$ y $[2-\delta,2+\delta]$, con $\delta>0$ racional. El recinto de su suma es $[3-2\delta,3+2\delta]$. Como $\delta$ puede hacerse arbitrariamente pequeño, estos recintos permiten identificar el resultado con $C_3$ mediante el criterio de igualdad de la definición de las cortaduras. La igualdad algebraica exacta $C_1+C_2=C_3$ se fundamenta en el lema de transferencia, no en una intuición de aproximación decimal.

En las definiciones anteriores aparecen uniones de conjuntos, pero cada unión se forma a partir de **extremos racionales inferiores** de recintos producidos por operaciones racionales finitas. La cuestión crucial no es sólo que el resultado sea una cortadura, sino que distintos cálculos con las mismas entradas produzcan exactamente la misma cortadura. Para pasar de fórmulas racionales a identidades de $D$ necesitamos el lema siguiente.

### Transferencia de identidades racionales

El siguiente lema coordina las aproximaciones de todas las variables de una identidad; asigna tolerancias a cada operación y controla especialmente los denominadores antes de tomar recíprocos. Es necesario porque utilizar aproximaciones independientes de una misma variable podría invalidar la transferencia de identidades.

Demostramos el paso que permite verificar todos los axiomas, sin asumir previamente que \(D\) sea un cuerpo.

**Lema de aproximación simultánea.** Sean $E_1,\ldots,E_k$ expresiones finitas construidas con variables $X_1,\ldots,X_n$, constantes racionales, suma, opuesto, producto y recíproco. Sean $A_1,\ldots,A_n\in D$. Evaluamos las expresiones usando las operaciones definidas en la construcción mediante recintos y las constantes $C_r$. Suponemos que, en cada aparición de un recíproco, la cortadura que constituye su operando es distinta de $C_0$.

Para todo $\varepsilon\in\mathbb Q_{>0}$ podemos elegir para cada variable $A_i$ un intervalo admisible $I_i=[a_i,b_i]$ y una entrada racional $t_i\in(a_i,b_i)$, ambos comunes a todas sus apariciones, tales que cada expresión $E_j$ admite un recinto $[l_j,u_j]$ con

$$C_{l_j}\subseteq E_j(A_1,\ldots,A_n)\subseteq C_{u_j},\qquad u_j-l_j<\varepsilon,$$
$$l_j\le E_j(t_1,\ldots,t_n)\le u_j.$$

Las evaluaciones racionales están bien definidas: en cada recíproco su operando racional es no nulo. Para cada una de esas apariciones se puede fijar previamente una separación racional positiva respecto de cero que todas las elecciones finales respetarán.

**Prueba.** Se consideran simultáneamente los árboles finitos de las expresiones. Las apariciones repetidas de una variable son hojas distintas, pero todas tendrán el mismo intervalo y el mismo valor racional. Para cada nodo $v$, denotamos por $H_v$ su cortadura evaluada mediante la construcción mediante recintos. Esta evaluación existe por inducción sobre los árboles y por la hipótesis sobre los recíprocos; no requiere que $D$ sea ya un cuerpo.

**1. Cotas fijas.** Para cada $H_v$, escogemos un intervalo admisible fijo $[\alpha_v,\beta_v]$, disponible por la definición de las cortaduras. Sea $[l,u]$ cualquier recinto de $H_v$, es decir, $C_l\subseteq H_v\subseteq C_u$. Como $\alpha_v\in H_v$, tenemos $\alpha_v<u$. Como $\beta_v\notin H_v$, tenemos $l\le\beta_v$: si $\beta_v<l$, entonces $\beta_v\in C_l\subseteq H_v$, contradicción. Por tanto, si $u-l<1$,

$$\alpha_v-1<l\le u<\beta_v+1.$$

Un ensanchamiento de cada extremo menor que 1 queda dentro de $[\alpha_v-2,\beta_v+2]$. Al haber finitos nodos, elegimos un racional

$$M=2+\max_v\bigl\{|\alpha_v|,|\beta_v|\bigr\}.$$

Esta cota sirve para los módulos de todos los extremos ensanchados que usaremos. Depende de las cortaduras fijas y de los árboles, no de la precisión final. Se evita así utilizar una cota del producto que pudiera crecer al refinar.

**2. Separación de los operandos de recíprocos.** Para cada nodo cuyo operando es $H\ne C_0$, la definición de las cortaduras da exactamente uno de los casos $H>C_0$ o $H<C_0$, donde estos símbolos significan inclusión estricta.

Si $H>C_0$, escogemos $r\in H$ con $r>0$: si un primer testigo de $H\setminus C_0$ es cero, la ausencia de máximo proporciona uno positivo. Cualquier recinto $[l,u]$ de $H$ satisface $u>r$. Si $u-l<r/2$, entonces $l>r/2$. Al ensanchar menos que $r/4$ por cada lado, todo el intervalo permanece por encima de $r/4$.

Si $H<C_0$, escogemos $r\in C_0\setminus H$, de modo que $r<0$. Todo recinto tiene $l\le r$. Si $u-l<|r|/2$, entonces $u<r/2<0$. Al ensanchar menos que $|r|/4$, todo el intervalo permanece por debajo de $r/4<0$.

En ambos casos fijamos $g=|r|/4>0$. Los intervalos finales del operando del recíproco tendrán un solo signo y todos sus elementos módulo al menos $g$. Estas elecciones se hacen para cada aparición; si un mismo operando se repite, las restricciones finitas se satisfacen conjuntamente tomando las precisiones menores correspondientes.

**3. Asignación explícita de precisiones.** Asignamos a cada raíz una tolerancia racional $\rho=\min(\varepsilon,1/2)$. Propagamos tolerancias desde las raíces hacia las hojas. Si un nodo tiene tolerancia $\rho$, las tolerancias $\delta$ de sus hijos se escogen como sigue:

- Suma: ambos hijos reciben $\delta=\min(1/2,\rho/8)$.
- Opuesto: el hijo recibe $\delta=\min(1/2,\rho/4)$.
- Producto: ambos hijos reciben $\delta=\min(1/2,\rho/(8M))$.
- Recíproco: el hijo recibe $\delta=\min(1/2,|r|/2,\rho g^2/4)$, con el testigo $r$ y la separación $g$ del paso 2.

Todas estas cantidades son racionales positivas. El proceso termina porque los árboles son finitos. Las restricciones se asignan desde las raíces hasta las hojas y se reúnen por mínimos cuando una variable aparece repetida: así, una sola elección de intervalo satisface simultáneamente las exigencias de todas sus apariciones. Ninguna tolerancia depende de un límite ni de un resultado de completitud de $D$.

**4. Una elección por variable.** Para cada $A_i$ que aparezca en los árboles, tomamos el mínimo de las tolerancias de todas sus hojas. Para una variable que no aparezca, basta cualquier intervalo admisible de anchura menor que $\min(\varepsilon,1/2)$. Elegimos por la definición de las cortaduras un intervalo admisible $I_i=[a_i,b_i]$ de anchura menor que ese mínimo. Si se han fijado intervalos iniciales distintos para apariciones de la misma variable, podemos escogerlo dentro de su intersección: el máximo de sus extremos inferiores pertenece a $A_i$ y el mínimo de sus extremos superiores no pertenece, por lo que forman un intervalo admisible. La bisección finita de la definición de las cortaduras refina dentro de él.

Fijamos una sola vez $t_i=(a_i+b_i)/2\in\mathbb Q$. Este mismo $t_i$ se usa en todas las apariciones de $X_i$, tanto en expresiones diferentes como en lados distintos de una identidad. No se exige $t_i\in A_i$: se exige que esté dentro del intervalo racional admisible elegido. Para una hoja constante $C_r$ con tolerancia $\rho$, elegimos $0<\gamma<\rho/2$ y usamos $[r-\gamma,r+\gamma]$, con valor racional exactamente $r$.

**5. Evaluación desde las hojas.** Por inducción, cada hijo de un nodo tiene un recinto $[l,u]$ de anchura menor que su tolerancia $\delta$, y su valor racional pertenece a ese recinto. Para aplicar la construcción mediante recintos al padre, escogemos racional $0<\eta<\delta/2$ y reemplazamos el recinto por

$$[a,b]=[l-\eta,u+\eta].$$

Este intervalo es admisible para $H$: $a\in C_l\subseteq H$ y $b\notin C_u\supseteq H$. Conserva dentro el valor racional del hijo y tiene anchura menor que $2\delta$. Como $\delta\le1/2$ y $\eta<1$, todos sus extremos tienen módulo a lo sumo $M$, por el paso 1.

En una suma, la construcción mediante recintos da anchura de salida menor que $4\delta\le\rho/2<\rho$. En un opuesto, la anchura es menor que $2\delta\le\rho/2<\rho$. En un producto, la construcción mediante recintos da anchura menor que $4M\delta\le\rho/2<\rho$. En cada caso, el valor racional del padre está en el recinto de salida por las propiedades racionales de los recintos demostradas en la construcción mediante recintos.

En un recíproco, la elección $\delta\le|r|/2$ y $\eta<\delta/2\le|r|/4$ activa el paso 2. Los extremos $a,b$ y el valor racional del hijo son del mismo signo y tienen módulo al menos $g>0$. Por tanto $ab\ge g^2>0$, el denominador racional del recíproco es no nulo y la construcción mediante recintos permite el recinto $[1/b,1/a]$. Su anchura cumple

$$\frac1a-\frac1b=\frac{b-a}{ab}<\frac{2\delta}{g^2}\le\frac\rho2<\rho.$$

El valor racional del recíproco queda en ese recinto por la monotonía racional de $t\mapsto1/t$ en cada semieje. No se divide por una cortadura ni se emplean reglas de orden de $D$ todavía no demostradas.

La inducción llega a todas las raíces con anchuras menores que $\varepsilon$. Los valores racionales usan las entradas compartidas del paso 4; todos los denominadores se han controlado en sus propios nodos. Esto prueba el lema. $\square$

Si dos expresiones racionalmente idénticas satisfacen las condiciones del lema, sus resultados en cortaduras son iguales. En efecto, sus recintos contienen un mismo valor racional \(v\) y tienen anchuras menores que \(\varepsilon\). Ambos recintos están dentro de \([v-\varepsilon,v+\varepsilon]\). Las dos cortaduras tienen, pues, un recinto común de anchura \(2\varepsilon\). El criterio de igualdad de cortaduras demuestra su coincidencia.

Aplicamos esto a las identidades racionales

$$A+B=B+A,\quad (A+B)+C=A+(B+C),\quad A+C_0=A,$$
$$A+(-A)=C_0,$$
$$AB=BA,\quad (AB)C=A(BC),\quad AC_1=A,$$
$$A(B+C)=AB+AC.$$

También \(AA^{-1}=C_1\) para \(A\ne C_0\): el lema asegura entradas racionales no nulas y utiliza \(t(1/t)=1\). No hay que asumir invertibilidad de la cortadura para construir el recíproco: se definió en la construcción por recintos mediante intervalos admisibles. Las mismas identidades muestran que \(C_r+C_s=C_{r+s}\), \(C_rC_s=C_{rs}\), \(-C_r=C_{-r}\) y \(C_r^{-1}=C_{1/r}\) si \(r\ne0\). Finalmente, \(C_0\ne C_1\), pues \(0\in C_1\setminus C_0\). Por tanto, \(D\) es un cuerpo.

**Cómo leer el lema de transferencia.** Una identidad como $X-X=0$ sólo puede transferirse si cada aparición de $X$ se evalúa usando **el mismo racional de entrada**. El lema garantiza simultáneamente esa elección y recintos arbitrariamente estrechos para todas las expresiones que se comparan.

La construcción tiene dos direcciones complementarias. Primero se asignan tolerancias **desde las raíces hacia las hojas** de los árboles finitos, en función de la precisión deseada y de las cotas para las operaciones. Después se evalúan las expresiones **desde las hojas hacia las raíces**. Al encontrar un recíproco, la precisión de su argumento debe asegurar que los valores racionales permanezcan separados de cero. En ningún momento se invoca una continuidad real que todavía no hemos construido.

La conclusión es una regla de igualdad exacta: si dos expresiones coinciden como identidades racionales para las entradas permitidas, sus cortaduras quedan atrapadas en recintos comunes de anchura arbitrariamente pequeña y, por la definición de las cortaduras, son iguales. El paso de «aproximaciones pequeñas» a «igualdad» usa un criterio ya demostrado, no una mera semejanza numérica.

### Compatibilidad del orden

La primera implicación exige convertir un recinto de $-A$ en intervalo admisible antes de utilizar la operación de suma; un extremo del recinto no pertenece necesariamente a la cortadura. Por esa razón se introduce un ensanchamiento racional que preserva positividad.

Escribimos $A<B$ cuando $A\subsetneq B$, y $B-A=B+(-A)$ con las operaciones de la construcción mediante recintos. Las identidades de cuerpo ya demostradas en el lema de transferencia pueden usarse aquí; aún no suponemos que el orden sea compatible con ellas.

**Primera dirección.** Supongamos $A<B$. Elegimos $r\in B\setminus A$ y, por ausencia de máximo de $B$, un $s\in B$ con $r<s$. Elegimos también $a\in A$ y $b\notin B$. Entonces $[a,r]$ es admisible para $A$ y $[s,b]$ para $B$.

La operación de opuesto de la construcción mediante recintos da el recinto $[-r,-a]$ de $-A$, es decir,

$$C_{-r}\subseteq -A\subseteq C_{-a}.$$

No se presupone que $-r\in-A$. Ponemos $\eta=(s-r)/2>0$ y usamos el intervalo

$$[-r-\eta,-a+\eta].$$

Es admisible para $-A$: el extremo inferior pertenece a $C_{-r}$ y el superior queda fuera de $C_{-a}$. La mitad elegida para el ensanchamiento cumple dos tareas simultáneas: garantiza pertenencia de los nuevos extremos y deja **una holgura positiva** después de sumar. Si consumiéramos toda la separación entre los dos testigos, la cota inferior podría convertirse en cero y esta dirección de la prueba no produciría el signo estricto buscado. Al sumarlo mediante la construcción por recintos con el intervalo admisible $[s,b]$ de $B$, obtenemos un recinto de $B-A$ con extremo inferior

$$s-r-\eta=\frac{s-r}{2}>0.$$

En consecuencia,

$$C_{(s-r)/2}\subseteq B-A.$$

Como $C_0\subsetneq C_{(s-r)/2}$ por la correspondencia entre el orden racional y la inclusión de cortaduras principales, resulta $B-A>C_0$. Esto demuestra $A<B\Rightarrow B-A>C_0$ sin utilizar previamente invariancia por traslación.

**Signo del opuesto.** Si $H>C_0$, escogemos un racional $h>0$ en $H$ y un $d\notin H$. El intervalo $[h,d]$ es admisible; la construcción mediante recintos da para $-H$ el recinto $[-d,-h]$. Así

$$-H\subseteq C_{-h}\subsetneq C_0,$$

por lo que $-H<C_0$. La prueba usa inclusión y el opuesto definido en la construcción mediante recintos, no una regla de signos de un cuerpo ordenado aún no establecido.

**Segunda dirección.** Supongamos $B-A>C_0$. Por tricotomía de las cortaduras, exactamente uno de los casos $A<B$, $A=B$ y $B<A$ ocurre.

Si $A=B$, las identidades del lema de transferencia dan $B-A=A+(-A)=C_0$, contradicción. Si $B<A$, la primera dirección ya demostrada da $A-B>C_0$. Aplicar el resultado del signo del opuesto y la identidad algebraica $-(A-B)=B-A$ del lema de transferencia produce $B-A<C_0$, también contradicción. Queda necesariamente $A<B$. Por tanto,

$$A<B\iff B-A>C_0.$$

**Compatibilidad con la suma.** Para cualquier $Z\in D$, el lema de transferencia da

$$ (B+Z)-(A+Z)=B-A.$$

La equivalencia recién demostrada implica

$$A<B\iff A+Z<B+Z.$$

No se utilizó esta compatibilidad para demostrar la equivalencia; se obtiene después de ella.

**Compatibilidad con el producto positivo.** Si $H,K>C_0$, escogemos racionales positivos $h\in H$, $k\in K$ y extremos superiores $d\notin H$, $e\notin K$. Son positivos porque $d>h>0$ y $e>k>0$. En los intervalos admisibles $[h,d]$ y $[k,e]$, el menor de los cuatro productos extremos es $hk>0$. La construcción mediante recintos da

$$C_{hk}\subseteq HK,$$

y la definición de las cortaduras da $C_0\subsetneq C_{hk}$, luego $HK>C_0$. Finalmente, si $A<B$ y $Z>C_0$, tenemos $B-A>C_0$ y $(B-A)Z>C_0$. Por distributividad e identidades algebraicas del lema de transferencia,

$$BZ-AZ=(B-A)Z>C_0.$$

Aplicar la equivalencia a $AZ,BZ$ da $AZ<BZ$. El orden total de la definición de las cortaduras es, pues, compatible con suma y multiplicación por positivos; $D$ es un cuerpo ordenado.

**Por qué el ensanchamiento de la compatibilidad del orden es necesario.** Del recinto $[-r,-a]$ para $-A$ no se puede inferir que $-r\in-A$. En realidad, un recinto sólo asegura que los elementos menores que $-r$ están en $-A$. La elección de $\eta>0$ convierte $[-r-\eta,-a+\eta]$ en un intervalo admisible; además, $\eta=(s-r)/2$ conserva un extremo inferior positivo después de sumar con $[s,b]$. Por eso la corrección no es tipográfica: sin ella, una aplicación de la construcción mediante recintos carecería de la hipótesis que define sus entradas.

### Completitud por unión de cortaduras

Sea \(\mathcal A\subseteq D\) una familia no vacía y acotada superiormente por una cortadura \(U\). Definimos

$$S=\bigcup_{A\in\mathcal A}A.$$

Es no vacía porque contiene una cortadura de la familia. Es propia porque \(S\subseteq U\ne\mathbb Q\). Es cerrada hacia abajo porque cada miembro de la familia lo es. No tiene máximo: si \(q\in S\), pertenece a alguna \(A\in\mathcal A\), que contiene un \(q'>q\). Así \(S\in D\).

Cada \(A\in\mathcal A\) está incluida en \(S\), luego \(S\) es cota superior. Si \(T\in D\) es otra cota superior, contiene a todas esas cortaduras y, por tanto, su unión \(S\). Luego \(S\le T\). Se ha demostrado \(S=\sup_D\mathcal A\).

Con la construcción alternativa completa existe un cuerpo ordenado completo. La demostración utiliza solamente racionales y conjuntos de racionales. No usa \(\pi\), densidad racional dentro de un cuerpo real previo ni la existencia de límites reales.

**Un ejemplo del mecanismo del supremo de cortaduras.** Consideremos la familia $\mathcal A=\{C_r:r\in\mathbb Q,\ r<1\}$. Su unión es $C_1$. En efecto, si $t<1$, el racional $r=(t+1)/2$ cumple $t<r<1$, de modo que $t\in C_r$. Recíprocamente, si $t\in C_r$ para algún $r<1$, entonces $t<r<1$ y $t\in C_1$. La unión de la familia es por tanto una cortadura y funciona como supremo.

El ejemplo no prueba por sí solo la completitud de $D$: la demostración de la completitud por unión necesita **cualquier** familia no vacía de cortaduras con cota superior, y ahí el argumento de la unión proporciona una solución uniforme.

## Unicidad por aproximaciones del cuerpo ordenado completo

Sean \(F,G\) cuerpos ordenados completos. Utilizamos las copias racionales ya construidas; escribimos \(q_F,q_G\) cuando sea necesario.

### Construcción de la correspondencia

Para \(x\in F\), sea

$$S_x=\{q\in\mathbb Q:q_F<x\},\qquad
\varphi(x)=\sup_G\{q_G:q\in S_x\}.$$

La propiedad arquimediana, demostrada antes, proporciona enteros inferiores y superiores a \(x\). Por ello, el conjunto cuyo supremo se toma es no vacío y está acotado superiormente en \(G\). \(\varphi\) está bien definida.

La propiedad clave es

$$q_G<\varphi(x)\iff q_F<x.\tag{*}$$

Si \(q_F<x\), la densidad racional produce \(r\in\mathbb Q\) con \(q_F<r_F<x\). Entonces \(q_G<r_G\le\varphi(x)\). Si \(q_F\ge x\), para cada \(r_F<x\) se tiene \(r<q\), de modo que \(q_G\) es cota superior y \(\varphi(x)\le q_G\). Esto prueba ambas direcciones.

Dos elementos de un mismo cuerpo ordenado completo con los mismos racionales estrictamente inferiores son iguales: si uno fuera menor que el otro, la densidad racional daría un racional entre ellos que distinguiría sus conjuntos inferiores.

Construimos \(\psi:G\to F\) del mismo modo. Por (*) para ambas funciones, \(\psi(\varphi(x))\) y \(x\) tienen los mismos racionales inferiores, y lo mismo ocurre con \(\varphi(\psi(y))\) y \(y\). Son iguales. Por tanto, \(\varphi\) es biyectiva. Además, (*) y el criterio anterior muestran que \(\varphi(q_F)=q_G\) para cada racional.

Si \(x<y\), tomamos \(q\in\mathbb Q\) con \(x<q_F<y\). Como \(q_F\ge x\), la prueba de (*) da \(\varphi(x)\le q_G\); como \(q_F<y\), da \(q_G<\varphi(y)\). Así \(\varphi(x)<\varphi(y)\). La inversa también preserva el orden por el mismo argumento.

**Qué significa construir $\varphi$ a partir de racionales.** El conjunto $S_x$ registra exactamente los racionales situados por debajo de $x$ en $F$. La fórmula (*) expresa que $\varphi(x)$ tiene el **mismo perfil racional inferior** en $G$. Dos elementos distintos de un cuerpo ordenado completo no pueden compartir ese perfil, porque entre ellos existe un racional (la densidad racional). Por eso los perfiles bastan para demostrar que $\varphi$ es inyectiva y que su construcción simétrica es una inversa.

La preservación de suma y producto requiere todavía otra demostración. No se debe inferir de la sola conservación del orden o de la fijación de los racionales sin exhibir el argumento que sigue.

### Conservación de las operaciones

En un cuerpo arquimediano, dos elementos que pertenecen a intervalos comunes de anchura racional arbitrariamente pequeña son iguales. Si \(u<v\), se elige \(n\) con \(n>(v-u)^{-1}\), de modo que \(1/n<v-u\); ningún intervalo de anchura menor que \(1/n\) puede contener a ambos.

Por densidad podemos acotar cada \(x\in F\) entre racionales \(a<x<b\) con \(b-a\) arbitrariamente pequeño. Para justificar explícitamente la anchura, dada \(h\in\mathbb Q_{>0}\), escogemos \(a\) entre \(x-h/2\) y \(x\), y \(b\) entre \(x\) y \(x+h/2\). Entonces \(b-a<h\).

Sean \(a<x<b\), \(c<y<d\), con ambas anchuras menores que \(h\). En \(F\), \(a+c<x+y<b+d\). Como \(\varphi\) conserva orden y racionales, \(\varphi(x+y)\) está entre \((a+c)_G\) y \((b+d)_G\). También \(\varphi(x)+\varphi(y)\) está entre esos extremos, por las desigualdades respectivas para cada sumando. La anchura es menor que \(2h\), arbitrariamente pequeña; luego

$$\varphi(x+y)=\varphi(x)+\varphi(y).$$

Para el producto, fijamos primero una cota racional \(M>0\) para los módulos de los extremos de los intervalos, posible por arquimedianidad. Refinamos sin salir de esos intervalos. Definimos

$$l=\min(ac,ad,bc,bd),\qquad u=\max(ac,ad,bc,bd).$$

El argumento de combinación con coeficientes no negativos de la construcción mediante recintos vale en cualquier cuerpo ordenado: usa únicamente división por cantidades positivas y distributividad. Por ello \(l_F\le xy\le u_F\). Conservar el orden da \(l_G\le\varphi(xy)\le u_G\). La misma estimación aplicada a \(\varphi(x),\varphi(y)\) da \(l_G\le\varphi(x)\varphi(y)\le u_G\). Por la cota de la construcción mediante recintos,

$$u-l\le M((b-a)+(d-c))<2Mh.$$

Al ser arbitrariamente pequeña esta anchura, concluimos

$$\varphi(xy)=\varphi(x)\varphi(y).$$

Ya se sabe que \(\varphi(0)=0\), \(\varphi(1)=1\). La conservación de suma y producto, junto con la unicidad de inversos, implica \(\varphi(-x)=-\varphi(x)\) y \(\varphi(x^{-1})=\varphi(x)^{-1}\) si \(x\ne0\). Así \(\varphi\) es un isomorfismo de cuerpos ordenados.

**Lectura de las estimaciones de la conservación de las operaciones.** Se eligen intervalos racionales estrechos alrededor de $x$ e $y$. La conservación del orden garantiza que tanto $\varphi(x+y)$ como $\varphi(x)+\varphi(y)$ quedan entre los **mismos extremos racionales**. Como la anchura puede ser tan pequeña como se quiera, ambos valores son iguales. En el caso del producto se necesita, además, una cota racional fija $M$ que controle los productos de extremos; la anchura resultante es a lo sumo $M((b-a)+(d-c))$. El argumento no presupone que $\varphi$ preserve operaciones: eso es precisamente lo que se establece por encerramiento racional.

### Unicidad del isomorfismo

Sea \(\theta:F\to G\) otro isomorfismo de cuerpos ordenados. Preserva \(1\), sumas, opuestos e inversos, de modo que fija las copias de naturales, enteros y racionales. Para todo racional \(q\),

$$q_G<\theta(x)\iff q_F<x\iff q_G<\varphi(x).$$

El criterio de igualdad por racionales inferiores implica \(\theta(x)=\varphi(x)\) para todo \(x\). El isomorfismo es único.

La afirmación demostrada es unicidad **como cuerpo ordenado**, hasta isomorfismo. No identifica literalmente los elementos de distintas realizaciones conjuntistas ni convierte una descripción axiomática en una elección única de conjunto subyacente.

# Otra identificación de un cuerpo completo con las cortaduras

La unicidad se puede justificar también mediante una correspondencia que a cada elemento le asocia el conjunto de racionales estrictamente inferiores. Presentamos íntegramente esta segunda prueba porque permite ver desde otro ángulo la relación entre orden, operaciones y supremos.

### Identificación de cuerpos completos mediante cortaduras

Este apartado no forma parte de la demostración desarrollada en la construcción por testigos. Completa la dependencia implícita en la conclusión escrita $D\cong\mathbb R$ sin presuponer unicidad. No reconstruye los documentos de la construcción por recintos: presenta aquí un argumento autónomo mediante la identificación de los cortes de un cuerpo completo cualquiera.

Sea $F$ un cuerpo ordenado completo. Sus naturales son las sumas finitas de $1_F$. Son positivos, y por ello $F$ tiene característica cero y una inclusión racional canónica $r\mapsto r_F$: la fracción $m/n$ se envía a $m_F(n_F)^{-1}$, con $n\ne0$. Dos fracciones equivalentes dan el mismo valor por multiplicación cruzada; el orden y las operaciones se conservan por los axiomas de cuerpo ordenado.

**Propiedad arquimediana.** Si los naturales de $F$ estuvieran acotados superiormente, tendrían un supremo $u$. El elemento $u-1_F$ no sería cota superior, así que algún natural $n_F$ cumpliría $u-1_F<n_F$. Entonces $u<(n+1)_F$, contradicción. En consecuencia los naturales superan cualquier elemento de $F$.

**Densidad racional en F.** Dados $x<y$, elegimos $n\in\mathbb N_{>0}$ con $1_F<n_F(y-x)$. Hay un entero mínimo $m$ con $n_Fx<m_F$: el conjunto de tales enteros es no vacío y está acotado inferiormente por la propiedad arquimediana; trasladarlo por un entero lo convierte en un subconjunto de naturales al que se aplica buen orden. La minimalidad da $(m-1)_F\le n_Fx<m_F$. Por tanto

$$x<(m/n)_F\le x+1_F/n_F<y.$$

Para $x\in F$, definimos

$$A_x=\{r\in\mathbb Q:r_F<x\}.$$

Las cotas racionales arquimedianas aseguran que es no vacío y propio. El orden racional asegura descenso, y la densidad en $F$ asegura ausencia de máximo. Por tanto $A_x\in D$. Si $x<y$, hay un racional entre ambos, que pertenece a $A_y\setminus A_x$; además $A_x\subseteq A_y$. Así $x\mapsto A_x$ preserva y refleja estrictamente el orden y es inyectiva.

Es sobreyectiva. Dada $A\in D$, el conjunto $\{r_F:r\in A\}$ es no vacío y tiene una cota superior $p_F$, con $p\in\mathbb Q\setminus A$. Sea $x$ su supremo en $F$. Si $r\in A$, hay $s\in A$ con $r<s$, de modo que $r_F<s_F\le x$ y $r\in A_x$. Si $r\in A_x$, entonces $r_F<x$ no es cota superior del conjunto; existe $s\in A$ con $r_F<s_F$, y el descenso de $A$ implica $r\in A$. Luego $A=A_x$.

También preserva la suma. Un testigo racional $q<a+b$ con $a_F<x$, $b_F<y$ implica $q_F<x+y$. Si $q_F<x+y$, ponemos $\delta=(x+y-q_F)/3>0$ en $F$. Elegimos racionales $a,b$ con $x-\delta<a_F<x$, $y-\delta<b_F<y$; entonces $q_F<a_F+b_F$ y obtenemos los testigos de $q\in A_x+A_y$. Así $A_{x+y}=A_x+A_y$. En particular preserva cero y, por unicidad del opuesto, signos aditivos.

Para $x,y>0$, la pertenencia por testigos positivos a $A_x\odot A_y$ implica $q_F<xy$. Para la inclusión contraria, si $0\le q_F<xy$, elegimos en $F$

$$0<e\le\min\left(x/2,y/2,1_F,\frac{xy-q_F}{2(x+y+1_F)}\right).$$

Por densidad hay racionales positivos $a,b$ con $x-e<a_F<x$, $y-e<b_F<y$. Se cumple

$$xy-a_Fb_F=x(y-b_F)+b_F(x-a_F)<e(x+y)<xy-q_F,$$

por lo que $q<ab$ y sirve como testigo del producto de cortaduras. Los racionales negativos pertenecen a ambas partes. Los casos cero se reducen a la identidad de cero; los negativos se reducen por el opuesto y la definición por signos. Luego $A_{xy}=A_xA_y$ en todos los casos. Se preserva $1_F$ porque $A_{1_F}=C_1$.

Así $F\to D$ es un isomorfismo de cuerpos ordenados, y su inversa muestra que todo cuerpo ordenado completo es isomorfo al construido. También es único: cualquier isomorfismo de cuerpos ordenados $f:D\to F$ fija las cortaduras racionales $C_r$ y sus imágenes $r_F$. Para toda cortadura $A$,

$$r\in A\iff C_r<A.$$

La dirección directa requiere sólo descenso: si $r\in A$, entonces $C_r\subseteq A$, y la inclusión es **estricta porque el propio $r$ pertenece a $A\setminus C_r$**. Para la inversa, $C_r\subsetneq A$ proporciona $s\in A\setminus C_r$, es decir, $s\ge r$; por igualdad o descenso resulta $r\in A$. **La ausencia de máximo no se necesita en esta equivalencia puntual**, aunque siga siendo imprescindible para que $A$ sea una cortadura y para otras etapas de esta construcción. Por tanto $r\in A\iff r_F<f(A)$, es decir, $A_{f(A)}=A$. La inyectividad del mapa $x\mapsto A_x$ determina $f(A)$ de manera única.

La completitud de $F$ se utilizó para propiedad arquimediana y para el supremo que representa una cortadura. La completitud de $D$ ya se probó en la completitud mediante unión. Ninguna de las dos se invocó para construir las operaciones de D, ni se utilizó previamente este isomorfismo para justificar la unión o las leyes de cuerpo.

# Comprobaciones transversales y comparación de construcciones

No se usarán los resultados de este apéndice para justificar retroactivamente las operaciones cuya construcción presuponen. Su papel es reunir las consecuencias ya demostradas, comprobar la coherencia entre métodos y exhibir con claridad las condiciones que no debemos omitir.

## La legitimidad de las operaciones por recintos

### Existencia de recintos racionales arbitrariamente estrechos

Para $A\in D$, un intervalo *admisible* es $[a,b]$ con $a\in A$ y $b\notin A$. La descendencia prueba $a<b$ y $C_a\subseteq A\subseteq C_b$. La bisección racional preserva ambas pertenencias y reduce la anchura a $(b-a)/2^n$. Dado $\varepsilon\in\mathbb Q_{>0}$, la desigualdad $2^n\ge n+1$ y la arquimedianidad **racional** permiten elegir $n$ con $(b-a)/2^n<\varepsilon$. No se ha supuesto ningún límite en $D$, y mucho menos un supremo en $\mathbb Q$.

Si sólo se tiene un *recinto* $C_l\subseteq A\subseteq C_u$, es incorrecto presuponer $l\in A$ o $u\notin A$. El intervalo $[l-\eta,u+\eta]$, con $\eta>0$ racional, **sí** es admisible: $l-\eta\in C_l\subseteq A$ y $u+\eta\notin C_u\supseteq A$. Esta conversión tiene un coste de anchura igual a $2\eta$, que no puede ignorarse cuando se propagan aproximaciones.

### Salidas de la construcción mediante recintos: existencia y control uniforme de los extremos

Las operaciones de la construcción por recintos asignan a intervalos admisibles recintos racionales de suma, opuesto, producto o recíproco; el resultado se define como la unión de los cortes principales de sus extremos inferiores. La unión es descendente y carece de máximo porque cada miembro es un $C_L$. No vacuidad se obtiene de cualquier elección admisible. Para demostrar que la unión es *propia* se necesita probar que **un mismo extremo superior racional** domina todos los extremos inferiores $L$ posibles.

La prueba no es una invocación de completitud: dos intervalos admisibles de una misma cortadura tienen interior común. En efecto, si $[a,b]$ y $[a',b']$ son admisibles, el mayor de $a,a'$ está dentro de la cortadura y el menor de $b,b'$ está fuera, luego $\max(a,a')<\min(b,b')$. Para cada variable se elige una entrada racional común en esa intersección. En la suma, opuesto y producto, la imagen racional de las entradas comunes pertenece a **ambos** recintos de salida. En el recíproco se usa la misma comparación, con intervalos sin cero y del mismo signo, que existen para una cortadura distinta de $C_0$. Por tanto todo extremo inferior de cualquier recinto de salida es menor o igual que el extremo superior de uno fijado previamente. Este último es cota racional del resultado y lo mantiene propio.

La misma comparación demuestra $C_L\subseteq\operatorname{Op}(A,B)\subseteq C_U$ para cada recinto de salida $[L,U]$. El producto se controla con la desigualdad racional

$$|tv-t'v'|\le M(|t-t'|+|v-v'|),$$

cuando todos los argumentos pertenecen a un intervalo de módulo menor o igual que $M$. El recíproco requiere adicionalmente $|t|,|t'|\ge g>0$ y entonces

$$\left|\frac1t-\frac1{t'}\right|=\frac{|t-t'|}{|tt'|}\le\frac{|t-t'|}{g^2}.$$

Estas estimaciones explican por qué **la separación racional de cero debe fijarse antes** de permitir el recíproco.

### Transferencia de identidades sin circularidad

Sean $E_1,E_2$ expresiones racionales con las mismas variables, y supongamos que cada subexpresión a la que se aplica un recíproco evalúa en una cortadura distinta de $C_0$. El lema de transferencia elige **una sola entrada racional por variable**, común a todas las apariciones y a ambos miembros. Primero, para los árboles finitos de subexpresiones se fijan cotas racionales uniformes $M$; para cada operando de recíproco se fija una separación $g>0$ de cero. Después se asignan tolerancias de raíces a hojas: suma, opuesto, producto y recíproco admiten las cotas de anchura $4\delta$, $2\delta$, $4M\delta$ y $2\delta/g^2$, respectivamente, después de convertir recintos hijos en intervalos admisibles de anchura menor que $2\delta$.

Para un nodo de tolerancia $\rho$, se pueden elegir, respectivamente, $\delta\le\rho/8$, $\delta\le\rho/4$, $\delta\le\rho/(8M)$ y $\delta\le\rho g^2/4$, además de las restricciones de signo. La inducción ascendente construye recintos de anchura menor que $\rho$ que contienen la evaluación racional sobre **esas entradas compartidas**. Si $E_1(t)=E_2(t)$ como identidad en los racionales donde ambos términos están definidos, los dos resultados cortadura quedan en un recinto común de anchura arbitrariamente pequeña. El criterio de igualdad de la definición de las cortaduras obliga a que sean la **misma cortadura**.

El lema de transferencia utiliza exclusivamente las definiciones de cortaduras y de las operaciones por recintos, identidades racionales y aproximaciones racionales finitas. No presupone axiomas de cuerpo para $D$ que precisamente pretende derivar. El hecho de que cada variable repetida conserve su entrada racional evita la falacia de sustituir, por ejemplo, $X-X$ por dos aproximaciones no coordinadas.

### El orden se obtiene después de las identidades algebraicas

Supongamos $A\subsetneq B$. Elegimos $r\in B\setminus A$ y $s\in B$ con $r<s$; elegimos $a\in A$ y $b\notin B$. Los intervalos $[a,r]$ de $A$ y $[s,b]$ de $B$ son admisibles. El intervalo $[-r,-a]$ es sólo un recinto de $-A$; **no** se puede usar sin más como argumento de una operación definida sobre admisibles.

Con $\eta=(s-r)/2>0$, el intervalo $[-r-\eta,-a+\eta]$ sí es admisible para $-A$. Al sumar con $[s,b]$ mediante la construcción mediante recintos, la cota inferior del recinto de $B-A$ es

$$s-r-\eta=\frac{s-r}{2}>0.$$

Por tanto $B-A>C_0$. Para la vuelta, la tricotomía descarta $A=B$ por cancelación, y descarta $B<A$ aplicando la dirección recién probada y el signo negativo del opuesto. Sólo **después** se establece

$$A<B\iff B-A>C_0\iff A+Z<B+Z.$$

La distributividad y la positividad de productos de dos cortaduras estrictamente positivas completan la compatibilidad multiplicativa. Esta secuencia impide que la regla de traslación, aún no legitimada en $D$, se use para demostrarse a sí misma.

## Las leyes del producto y el recíproco por testigos

### Una misma suma, dos fórmulas

Para $A,B\in D$,

$$A+_{\rm tes}B=\{q:\exists a\in A,\ b\in B,\ q<a+b\}=\{a+b:a\in A,b\in B\}.$$

La primera inclusión hacia sumas exactas reemplaza $a$ por $q-b<a$, que sigue en $A$ por descenso. La inclusión contraria reemplaza un testigo $a$ por uno estrictamente mayor dentro de $A$. De aquí se obtienen asociatividad y conmutatividad mediante operaciones **racionales**. El opuesto definido con racionales exteriores requiere un recinto admisible de anchura arbitrariamente pequeña para obtener $A+(-A)=C_0$; no puede resolverse sólo con una simetría gráfica.

### Distributividad en el cono positivo

Para $A,B,C\ge C_0$, la multiplicación por testigos positivos se define antes de extender los signos. Cuando los tres son estrictamente positivos, si $q\ge0$ pertenece a $(A\odot B)+(A\odot C)$, hay $u\in A\odot B$ y $v\in A\odot C$ con $q<u+v$. Incluso si $u<0$ o $v<0$, puede elegirse un testigo racional positivo cuyo producto sea mayor que ese elemento. Obtenemos entonces $a_1,a_2\in A$ y $b\in B,c\in C$, todos positivos, con

$$q<u+v<a_1b+a_2c\le a(b+c),\qquad a=\max(a_1,a_2)\in A.$$

Como $b+c\in B+C$ por la forma exacta de la suma, se tiene $q\in A\odot(B+C)$. La otra inclusión parte de $q<ad$ con $d\in B+C$ positivo; se escoge una representación $d=b+c$ y, aumentando los testigos dentro de $B,C$ si es necesario, pueden obtenerse $b,c>0$ y $q<a(b+c)=ab+ac$. Los productos racionales positivos $ab$ y $ac$ pertenecen a los cortes producto correspondientes (se aumenta ligeramente $a$ para transformar $ab$ en testigo estricto), de modo que $q$ pertenece a su suma. Los casos con un factor cero se resuelven por las identidades ya demostradas. Ningún paso presupone distributividad general de cortaduras negativas.

### Extensión del cono al cuerpo entero

Toda cortadura $X$ puede expresarse como $P-Q$ con $P,Q\ge C_0$. Para $T\ge C_0$ se define $h_T(P-Q)=P\odot T-Q\odot T$. Si $P-Q=P'-Q'$, el **grupo aditivo ya probado** da $P+Q'=P'+Q$, y la distributividad positiva da

$$P\odot T+Q'\odot T=P'\odot T+Q\odot T.$$

Por cancelación, $h_T$ no depende de la representación. Para $Y=R-S$, también con $R,S\ge C_0$, se define $XY=h_R(X)-h_S(X)$. La identidad $h_{T+U}=h_T+h_U$ hace independiente esa segunda representación. La fórmula expandida es

$$(P-Q)(R-S)=(P\odot R+Q\odot S)-(P\odot S+Q\odot R).$$

Así la multiplicación general queda **bien definida antes** de utilizar distributividad y asociatividad para elementos con signos arbitrarios. La expansión de tres diferencias tiene en ambos parentizados los mismos ocho monomios de productos del cono con sus respectivos signos; el resultado depende únicamente de las leyes ya probadas en el cono y del grupo aditivo.

### El recíproco según el signo de la cortadura

Para $A>C_0$, el conjunto

$$J_A=\{q\in\mathbb Q:\exists p\notin A,\ p>0,\ q<1/p\}$$

es una cortadura positiva. Para demostrar $A\odot J_A=C_1$, la inclusión no trivial toma un $q$ con $0\le q<1$, fija $a_0>0$ dentro de $A$ y refina un par admisible hasta obtener $a\in A$, $p\notin A$ con $a\ge a_0>0$ y

$$0<p-a<(1-q)a_0.$$

Entonces $a/p=1-(p-a)/p>q$, de modo que existe un racional $b$ con $q/a<b<1/p$ y $b>0$, lo que proporciona $q<ab$. Los negativos ya pertenecen al corte producto. Para $A<C_0$ se define $A^{-1}=-J_{-A}$; el cero carece de inverso. Aplicar la fórmula positiva a $C_{-1}$ daría todo $\mathbb Q$, por permitir $p>0$ exterior arbitrariamente pequeño. El dominio y el signo determinan la fórmula legítima del recíproco y forman parte de su buena definición.

## Los dos puentes del producto de supremos

Sean $F,G$ cuerpos ordenados completos supuestos, con copias racionales $q_F,q_G$. La aplicación $\varphi(x)=\sup_G\{q_G:q_F<x\}$ exige primero arquimedianidad y densidad de los racionales **en cada cuerpo**, obtenidas desde su propia completitud. No se invoca para esta construcción el cuerpo de cortaduras de la construcción por testigos.

Para $x,y>0_F$, definimos

$$A_x^+=\{a\in\mathbb Q:0<a_F<x\},\quad A_y^+=\{b\in\mathbb Q:0<b_F<y\},$$
$$U=\{q\in\mathbb Q:\exists a\in A_x^+,b\in A_y^+,\ q<ab\},\quad P=U\cap\mathbb Q_{>0},$$
$$V=\{a_Gb_G:a\in A_x^+,b\in A_y^+\}.$$

**Primer puente.** $U=A_{xy}$: cada testigo produce $q_F<xy$ al multiplicar por positivos. Si $0<q_F<xy$, se elige por densidad primero $b_F$ entre $q_F/x$ e $y$, y luego $a_F$ entre $q_F/b_F$ y $x$. Ambas divisiones tienen denominador positivo y $q<ab$. Para $q\le0$, cualquier producto positivo de dos testigos sirve. Como consecuencia, $P=A_{xy}^+$, pero **$P$ no es cortadura en todo $\mathbb Q$**: falta su lado negativo.

**Segundo puente.** Los conjuntos $V$ e $\iota_G[P]$ son incluso idénticos. Si $q\in P$ y $0<q<ab$, entonces $a'=q/b$ satisface $0<a'<a$ y, por descenso, $a'\in A_x^+$; por tanto $q=a'b$. Recíprocamente, si $ab$ es un producto exacto, la ausencia de máximo permite $a'>a$ todavía en $A_x^+$, y $0<ab<a'b$, por lo que $ab\in P$. Ambos pasos requieren $b>0$. De aquí $V=\iota_G[P]$.

**Producto de supremos.** Los conjuntos $S_x=\iota_G[A_x^+]$ y $S_y=\iota_G[A_y^+]$ son no vacíos, acotados y positivos; son cofinales respecto de las imágenes de los cortes completos. La regla $\sup(cS)=c\sup S$ para $c>0$ y el lema de aplanamiento de supremos dan

$$\varphi(x)\varphi(y)=\sup_G V=\sup_G\iota_G[P]=\varphi(xy).$$

En el último término se utiliza que $P=A_{xy}^+$ es cofinal en $A_{xy}$. Para signos no positivos sólo se usa después la aditividad ya demostrada: $\varphi(0)=0$ y $\varphi(-x)=-\varphi(x)$. La unidad procede de la idempotencia y de la positividad de $\varphi(1)$; la sobreyectividad se prueba por el corte inverso $B_y=\{q:q_G<y\}$ y un supremo en $F$. Ninguna de estas etapas emplea el isomorfismo buscado como premisa.

## De los cuadrados y las raíces a los espacios normados

Para $a,b$ en cualquier cuerpo ordenado, $|ab|=|a||b|$ y $ab\le|ab|$. Por expansión,

$$(a+b)^2=a^2+2ab+b^2\le(|a|+|b|)^2.$$

Ambos números $|a+b|$ y $|a|+|b|$ son no negativos. La función $t\mapsto t^2$ es estrictamente creciente sobre los no negativos, ya que si $0\le u<v$ entonces $v^2-u^2=(v-u)(v+u)>0$. Resulta $|a+b|\le|a|+|b|$. La notación $\sqrt{z^2}=|z|$ sólo recupera la raíz **de un cuadrado ya existente**; no presupone que cualquier positivo de un cuerpo ordenado tenga raíz. Así la demostración escalar no necesita completitud.

La existencia general de $\sqrt c$ para $c\ge0$ sí utiliza la propiedad del supremo: con $c>0$ se toma $S=\{t\ge0:t^2\le c\}$ y $s=\sup S$; si $s^2<c$ se aumenta racionalmente $s$ dentro de $S$ y si $s^2>c$ se produce una cota menor que $s$. Para ambos desplazamientos se escogen parámetros positivos que controlan denominadores y cuadrados. Con esto se obtiene una raíz no negativa única, sin invocar continuidad previa.

La desigualdad triangular euclídea para $\mathbb R^2$ requiere **otra** demostración: la identidad de Lagrange

$$(u_1^2+u_2^2)(v_1^2+v_2^2)-(u_1v_1+u_2v_2)^2=(u_1v_2-u_2v_1)^2\ge0$$

implica Cauchy–Schwarz; de éste y de la expansión de $\|u+v\|_2^2$ se deduce la desigualdad vectorial. No se obtiene reemplazando letras escalares por vectores en el resultado anterior. Para la norma euclídea, la igualdad exige un vector cero o dos vectores no nulos en el mismo sentido. Esta caracterización **no** se extiende a normas arbitrarias; en $\ell^1$, $(1,0)$ y $(0,1)$ son no paralelos y satisfacen igualdad triangular.

En el paso a sucesiones, la triangular controla el error de una suma, pero el cierre requiere escoger índices para tolerancias $\varepsilon/2$ y luego su máximo. La convergencia de dos sucesiones de Cauchy no se deduce de estar en cualquier espacio normado: para la recíproca hace falta completitud del **espacio**, diferente de la completitud del cuerpo escalar.

## Por qué coinciden las dos construcciones de cortaduras

**Teorema de comparación posterior.** Supongamos completadas **independientemente** dos construcciones de los reales: una que define las operaciones mediante recintos racionales, $(D,+_{\rm rec},\cdot_{\rm rec},\le)$, y otra que las define mediante testigos racionales, $(D,+_{\rm tes},\cdot_{\rm tes},\le)$. En ambas se han probado todas las leyes algebraicas, la compatibilidad con el orden y la completitud, sin utilizar este teorema de comparación. Ambas estructuras son cuerpos ordenados completos sobre el **mismo** conjunto de cortaduras, con el mismo orden por inclusión; la inclusión racional tiene en ambas la forma $r\mapsto C_r$.

El teorema de unicidad demuestra, para dos cuerpos ordenados completos arbitrarios, la existencia de un isomorfismo ordenado $\Phi:D_{\rm rec}\to D_{\rm tes}$. Por preservar unidad y operaciones, $\Phi(C_r)=C_r$ para todo $r\in\mathbb Q$. Además, en cualquier cortadura $A$ se cumple

$$r\in A\iff C_r<A.$$

En la implicación directa, $C_r\subseteq A$ por descenso y la inclusión es estricta porque **el propio $r$** pertenece a $A\setminus C_r$. En la inversa, un testigo $s\in A\setminus C_r$ satisface $s\ge r$; por descenso, o por igualdad, $r\in A$. La ausencia de máximo no es necesaria para esta equivalencia aislada, aunque sí lo sea en la definición de cortadura. Como $\Phi$ preserva y refleja inclusión estricta y fija cada $C_r$,

$$r\in A\iff C_r<A\iff C_r<\Phi(A)\iff r\in\Phi(A).$$

Se sigue $\Phi(A)=A$ por extensionalidad para **cada** cortadura. Al aplicar la condición de homomorfismo a dos cortaduras cualesquiera $A,B$,

$$A+_{\rm rec}B=A+_{\rm tes}B,\qquad A\cdot_{\rm rec}B=A\cdot_{\rm tes}B,$$

así como coincidencia de opuestos e inversos no nulos. **Alcance lógico:** este teorema compara dos construcciones después de completarlas y después de haber demostrado el teorema de unicidad. No se usa para justificar las pruebas de transferencia y orden de la construcción por recintos, la distributividad y los recíprocos de la construcción por testigos, ni la existencia previa del isomorfismo del teorema de unicidad. Reutilizarlo como premisa en esas pruebas sería circular. El resultado compara dos estructuras ya construidas: no puede emplearse como justificación previa de alguna de ellas.

# Símbolos y convenciones

$\mathbb N$, $\mathbb Z$ y $\mathbb Q$ designan, respectivamente, los naturales, los enteros y los racionales. Adoptamos la convención de que cero pertenece al conjunto de los naturales. Los denominadores se toman siempre no nulos; cuando se escriben como naturales, son estrictamente positivos.

Un **cuerpo ordenado** es un cuerpo con un orden total compatible con las dos operaciones. La palabra **completo** añade que todo subconjunto no vacío y acotado superiormente tiene supremo en el propio cuerpo.

$D$ es el conjunto de cortaduras inferiores de $\mathbb Q$. La cortadura principal asociada a $r\in\mathbb Q$ se escribe $C_r=\{q\in\mathbb Q:q<r\}$. Cuando el cuerpo sea abstracto, $q_H$ denotará la imagen de un racional $q$ en ese cuerpo. Los símbolos $q$, $q_F$ y $q_G$ pertenecen, en general, a conjuntos diferentes.

Para $x\in F$, el conjunto $A_x=\{q\in\mathbb Q:q_F<x\}$ es el **perfil racional inferior** de $x$; su parte positiva es $A_x^+=A_x\cap\mathbb Q_{>0}$. La parte positiva no constituye por sí sola una cortadura descendente de todos los racionales.

El símbolo $\sup_H S$ designa un supremo calculado **en $H$**, no en un conjunto ambiente implícito. Para los resultados de continuidad y límites, $\varepsilon>0$ será una tolerancia elegida antes de los índices $N$.

Finalmente, $|x|$ designa el valor absoluto de un escalar y $\|v\|$ una norma en un espacio vectorial. Un cuerpo ordenado completo y un espacio normado completo satisfacen propiedades de completitud distintas: la primera se refiere a supremos de conjuntos ordenados y la segunda a convergencia de sucesiones de Cauchy.

# Nota de procedencia y lecturas complementarias

El punto de partida audiovisual son cuatro clases seleccionadas del curso *Real Analysis* del canal de YouTube **Divergence is Divergence**:

- *Real Analysis: Lecture 1/37 — The Real Number System*: <https://www.youtube.com/watch?v=w26JekhZEUU>
- *Real Analysis: Lecture 1.5/37 — The Existence of Real Numbers*: <https://www.youtube.com/watch?v=RfAxW_UD_94>
- *Real Analysis: Lecture 1.5ii/37 — The Uniqueness of Real Numbers*: <https://www.youtube.com/watch?v=TUGvSs7Tr-g>
- *Real Analysis: Lecture 1.5iii/37 — The Triangle Inequality*: <https://www.youtube.com/watch?v=nv4jtXJVppE>

La selección y el orden de estudio corresponden al alcance de este libro y no equivalen al índice completo del curso. La exposición escrita, las demostraciones desarrolladas, las construcciones alternativas y los ejercicios son una **elaboración matemática editorial propia** a partir de esas ideas. No deben citarse como transcripción literal de las grabaciones. Las correcciones y ampliaciones son responsabilidad de esta edición; las pruebas de procedencia audiovisuales y las decisiones internas se conservan en un expediente documental separado de la versión de lectura.
