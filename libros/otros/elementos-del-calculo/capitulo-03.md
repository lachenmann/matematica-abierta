---
title: Capítulo 3. Extremos, crecimiento y aproximación local
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-13'
license: GFDL-1.3-or-later
areas:
  - calculo
  - analisis
  - fundamentos
level: intermedio
topics:
  - calculo-de-una-variable
  - historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
    - role: idea
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C03
source-sha256: eb15cce0fdbfe5486083e385d90636d0812a6b370553955c03b25b42d0615cf8
content-id: MA-BCH-0334
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-03.html) · [Ejercicios](capitulo-03-ejercicios.html) · [Soluciones](capitulo-03-soluciones.html) · [Notas históricas](capitulo-03-notas.html)

[← Capítulo 2](capitulo-02.html) · [Capítulo 4 →](capitulo-04.html)

> **Pregunta generadora.** Si una derivada describe lo que ocurre muy cerca de un punto, ¿con qué derecho podemos utilizarla para decidir cómo se comporta una función en un intervalo entero, dónde alcanza sus extremos y cuánto nos equivocamos al sustituirla por una recta?

Una pendiente calculada en un punto parece decir muy poco sobre una curva entera. Si sabemos que $f'(a)>0$, podemos comparar $f(a)$ con los valores suficientemente próximos a él, pero todavía no hemos justificado que cualesquiera dos puntos de un intervalo estén ordenados del mismo modo. La dificultad aparece también al buscar extremos: en la función $x^3$, la derivada se anula en cero aunque la gráfica siga creciendo al atravesarlo, mientras que $|x|$ alcanza allí un mínimo y carece de derivada. Calcular pendientes y decidir el comportamiento de una función son tareas relacionadas que necesitan un argumento entre ellas.

El primer problema será comprender qué obliga a una pendiente a anularse en un extremo interior. La continuidad sobre un intervalo cerrado nos dará después un lugar donde aplicar esa observación, y podremos comparar el cambio entre los extremos del intervalo con una derivada tomada en algún punto intermedio. Esa comparación permitirá estudiar crecimiento, estimar errores y justificar la elección de un máximo o un mínimo; para construirla bastarán los resultados de C00–C02.

## 3.1. Un problema sencillo con una dificultad escondida

Sea $f(x)=x^3-3x$ en el intervalo $[-2,2]$. El cálculo algebraico de C02 da

$$
f'(x)=3x^2-3=3(x-1)(x+1).
$$

La derivada se anula en $-1$ y en $1$, dos puntos que interesan en la búsqueda de extremos, aunque todavía falta explicar qué relación hay entre una pendiente nula y un valor máximo o mínimo. El dominio también aporta dos puntos que ese cálculo no selecciona: $-2$ y $2$ son sus bordes y pertenecen a la función que estamos estudiando. Al comparar los cuatro valores obtenemos

$$
\begin{array}{c|rrrr}
x&-2&-1&1&2\\ \hline
f(x)&-2&2&-2&2.
\end{array}
$$

Los valores mayores y menores de esta tabla se repiten en un punto interior y en un borde. Tendremos que demostrar que no hay otros valores que los superen entre los puntos examinados, y para ello usaremos el signo de la derivada sobre intervalos completos. La búsqueda comienza por una observación más sencilla: cuando un punto interior realiza un extremo y la derivada existe, los cambios a su derecha y a su izquierda imponen exigencias opuestas al mismo límite.

## 3.2. Extremos locales y el principio de Fermat

**Definición 3.1 (`EDC-C03-DEF-001`).** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $c\in D$. Decimos que $f$ tiene un **máximo local** en $c$ si existe $\delta>0$ tal que

$$
f(x)\le f(c)\qquad(x\in D,\ |x-c|<\delta).
$$

Se define análogamente un **mínimo local** invirtiendo la desigualdad. Si la desigualdad es estricta para $x\ne c$, el extremo local es estricto. Un **máximo absoluto** exige $f(x)\le f(c)$ para **todo** $x\in D$; un mínimo absoluto se define de modo dual. Un extremo local se entiende siempre *relativo al dominio especificado*.

Los extremos absolutos existen para toda función continua en $[a,b]$, $a<b$, por el teorema de los valores extremos de C00 (`EDC-C00-THM-007`). Pero nada en dicho teorema asegura que los puntos que los realizan sean interiores.

**Teorema 3.1 (principio de Fermat; `EDC-C03-THM-001`).** Sea $f:D\to\mathbb R$ y sea $c$ un punto interior de $D$. Si $f$ tiene un extremo local en $c$ y es derivable allí, entonces

$$
f'(c)=0.
$$

**Demostración.** Supongamos primero que $c$ es un máximo local. Como es interior del dominio, podemos elegir incrementos pequeños de ambos signos que mantengan $c+h$ dentro de él; al reducir su magnitud, la condición de máximo local asegura $f(c+h)\le f(c)$. El numerador del cociente incremental es por tanto no positivo a ambos lados. Para $h>0$ suficientemente pequeño,

$$
\frac{f(c+h)-f(c)}{h}\le0,
$$

mientras que para $h<0$ suficientemente pequeño la división por un número negativo invierte el signo y la misma fracción es mayor o igual que cero. El límite por la derecha, si existe, no puede ser positivo; el de la izquierda no puede ser negativo. La derivabilidad bilateral afirma que ambos existen y coinciden con $f'(c)$, de modo que ese número debe ser a la vez no positivo y no negativo: $f'(c)=0$.

Si $c$ es un mínimo local de $f$, es un máximo local de $-f$. La regla de derivación de un múltiplo constante da $(-f)'(c)=-f'(c)$, y el caso ya demostrado obliga también a que $f'(c)=0$. $\square$

La conclusión es **necesaria, no suficiente**. Para $f(x)=x^3$, se cumple $f'(0)=0$, pero $0$ no es máximo ni mínimo local: a ambos lados toma valores de signos opuestos. Para $f(x)=|x|$, $0$ sí es un mínimo local, pero $f'(0)$ no existe. Para $f(x)=x$ en $[0,1]$, el mínimo absoluto se alcanza en $0$, punto de borde; la derivada unilateral derecha vale $1$, no cero. Ninguno de estos hechos contradice el teorema, porque en cada ejemplo falta una hipótesis distinta.

**Definición 3.2 (`EDC-C03-DEF-002`).** Para una función definida sobre un intervalo, un punto **estacionario** interior es un punto donde existe $f'(c)=0$. Llamaremos **candidato crítico interior** a un punto interior donde $f'(c)=0$ o donde la función no es derivable. Usaremos esta expresión como instrumento para buscar extremos, sin afirmar que cada candidato sea uno.

Un candidato crítico señala un lugar que debe examinarse; su nombre no decide si allí hay un extremo. En un problema sobre un intervalo cerrado habrá que añadir los bordes a la búsqueda, porque en ellos no disponemos de los dos lados que utiliza la prueba de Fermat.

## 3.3. Rolle: dos valores iguales fuerzan una pendiente nula

Si una curva comienza y termina a la misma altura y alcanza alguna altura distinta entre ambos puntos, tiene que realizar un máximo o un mínimo lejos de los bordes. Esa observación ofrece un modo de encontrar una pendiente nula sin conocer de antemano el lugar donde ocurre: la continuidad asegurará que el extremo existe y la derivabilidad permitirá aplicar Fermat. La curva de $|x|$ muestra el obstáculo que hay que excluir, pues puede regresar a su altura inicial pasando por un vértice donde no existe pendiente.

**Teorema 3.2 (Rolle; `EDC-C03-THM-002`).** Sean $a<b$ y $f:[a,b]\to\mathbb R$. Supongamos que:

1. $f$ es continua en $[a,b]$;
2. $f$ es derivable en $(a,b)$;
3. $f(a)=f(b)$.

Entonces existe $c\in(a,b)$ tal que $f'(c)=0$.

**Demostración.** La continuidad en el intervalo cerrado permite aplicar el teorema de los valores extremos de C00: $f$ alcanza su máximo $M$ y su mínimo $m$ en $[a,b]$. Si $M=m$, todos los valores de la función coinciden, por lo que es constante y $f'(x)=0$ en cada punto interior.

Si $M>m$, el valor común $f(a)=f(b)$ no puede coincidir con los dos extremos a la vez. Elegimos uno de ellos que sea distinto de ese valor común. Existe un punto donde se alcanza, y ninguno de los bordes puede ser ese punto, porque ambos tienen el valor que acabamos de excluir. El extremo se realiza entonces en algún $c\in(a,b)$; allí la derivada existe por hipótesis, y el principio de Fermat da $f'(c)=0$. $\square$

El ejemplo $f(x)=|x|$ en $[-1,1]$ enseña por qué la derivabilidad interior importa: los valores extremos son iguales, $f(-1)=f(1)=1$, pero la derivada vale $-1$ para $x<0$, $1$ para $x>0$ y no existe en $0$. No hay ningún punto interior de derivada nula. El ejemplo $f(x)=x$ en $[0,1]$ muestra por qué hace falta la igualdad de extremos. Y la discontinuidad puede destruir la conclusión aunque exista derivada en todo punto interior donde la función está definida: por ejemplo, $f(0)=f(1)=0$ y $f(x)=x$ para $0<x<1$ no es continua en $1$ y tiene derivada interior $1$.

## 3.4. El teorema del valor medio

En un intervalo $[a,b]$, el cambio total $f(b)-f(a)$ determina la pendiente de la secante

$$
m=\frac{f(b)-f(a)}{b-a}.
$$

Para aplicar Rolle necesitamos valores iguales en los extremos, y aquí la diferencia entre ellos puede ser cualquiera. La recta secante contiene precisamente ese desnivel: si restamos su altura a la altura de la curva, la diferencia será cero tanto en $a$ como en $b$. Una pendiente nula de esa diferencia corresponderá a un punto donde la curva tenga la misma pendiente que la secante.

**Teorema 3.3 (valor medio de Lagrange; `EDC-C03-THM-003`).** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en $[a,b]$ y derivable en $(a,b)$. Existe un punto $c\in(a,b)$ tal que

$$
f'(c)=\frac{f(b)-f(a)}{b-a},
\qquad\text{equivalentemente}\qquad
f(b)-f(a)=f'(c)(b-a).
$$

**Demostración.** Restamos de la curva la recta que une sus extremos. Esa elección elimina el desnivel que impedía aplicar Rolle y conserva la diferencia de pendientes que queremos estudiar. Definimos

$$
g(x)=f(x)-\left[f(a)+\frac{f(b)-f(a)}{b-a}(x-a)\right].
$$

La cantidad entre corchetes es la altura de la recta secante en $x$. En $x=a$ vale $f(a)$ y en $x=b$ vale $f(b)$, de modo que $g(a)=g(b)=0$. La recta es continua y derivable; las hipótesis sobre $f$ y las reglas de C02 aseguran que su diferencia $g$ es continua en $[a,b]$ y derivable en $(a,b)$.

Rolle proporciona un punto $c\in(a,b)$ con $g'(c)=0$. La derivada de la recta es su pendiente constante, así que esa igualdad se escribe

$$
f'(c)-\frac{f(b)-f(a)}{b-a}=0.
$$

Obtenemos la pendiente requerida, y al multiplicar por $b-a>0$ resulta la forma equivalente del enunciado. $\square$

Para $f(x)=x^2$ entre $a=-1$ y $b=2$, la pendiente media es $(4-1)/(2-(-1))=1$. Como $f'(x)=2x$, el punto garantizado es $c=1/2$. En general, el teorema asegura la **existencia** de algún $c$; no identifica un único punto ni afirma que $c$ sea el punto medio de $[a,b]$.

El punto $c$ puede depender de los dos extremos elegidos y ser difícil de localizar. Para muchas aplicaciones bastará con saber que pertenece al intervalo: si conocemos una cota o un signo de la derivada en todos sus puntos, esa misma información valdrá en $c$ y podremos utilizarla para comparar $f(a)$ y $f(b)$.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — De una cumbre al teorema del valor medio"}
*Lectura opcional.*

Fermat propone un problema que podemos resolver con pocos trazos: dividir un segmento de longitud fija para que el rectángulo formado por sus dos partes tenga el área mayor posible. Si la longitud total es $B$ y una parte mide $A$, el área se escribe $A(B-A)$. En su *Methodus ad disquirendam maximam et minimam*, compara esa expresión con la obtenida al sustituir $A$ por $A+E$, cancela términos comunes, divide por $E$ y elimina después los términos que aún contienen el incremento. El cálculo lo conduce a $B=2A$: hay que partir el segmento por la mitad.

Al derivar hoy la misma expresión obtenemos $B-2A$, y reconocemos en su anulación la misma elección del punto. La comparación permite acercarse a la pregunta histórica por los extremos desde un problema concreto, aunque nuestro argumento por límites tenga sus propias hipótesis y justificación.

Rolle y el valor medio amplían la utilidad de esa búsqueda de pendientes nulas. Restar la secante transforma una curva con alturas finales distintas en otra con extremos a la misma altura; el extremo interior de la diferencia encuentra entonces una tangente paralela a la secante de la curva original.

**Para seguir leyendo:** [Fermat, *Œuvres*, tomo I (1891), pp. 133–134, *Methodus ad disquirendam maximam et minimam*](https://fr.wikisource.org/wiki/Œuvres_de_Fermat/I/Maxima_et_Minima); contexto de Rolle y del valor medio en las notas históricas del capítulo 3, H2–H3.
:::

## 3.5. Monotonía, constancia y unicidad

**Definición 3.3 (`EDC-C03-DEF-003`).** Una función $f:I\to\mathbb R$ es **no decreciente** cuando $x<y$ implica $f(x)\le f(y)$; es **estrictamente creciente** si la conclusión es $f(x)<f(y)$. Las definiciones de no creciente y estrictamente decreciente invierten esas comparaciones.

**Teorema 3.4 (criterios de monotonía; `EDC-C03-THM-004`).** Sea $I\subseteq\mathbb R$ un intervalo abierto y sea $f:I\to\mathbb R$ derivable. Entonces:

1. $f$ es no decreciente en $I$ **si y sólo si** $f'(x)\ge0$ para todo $x\in I$.
2. Si $f'(x)>0$ para todo $x\in I$, entonces $f$ es estrictamente creciente. Si $f'(x)<0$ en todo $I$, es estrictamente decreciente.
3. $f$ es constante en $I$ **si y sólo si** $f'(x)=0$ para todo $x\in I$.

Para intervalos de cualquier tipo que posean extremos de borde, las conclusiones entre puntos del intervalo se conservan si $f$ es continua en esos extremos y derivable en el interior.

**Demostración.** Para comparar valores cualesquiera de la función, tomemos $x<y$ en $I$. La condición de intervalo garantiza que $[x,y]\subset I$, y la derivabilidad en $I$ implica la continuidad que necesitamos también en los extremos de ese segmento. El valor medio proporciona un $c\in(x,y)$ tal que $f(y)-f(x)=f'(c)(y-x)$. Como $y-x>0$, el signo de la diferencia es el de la derivada en ese punto. Si $f'$ es no negativa en todo $I$, obtenemos $f(y)\ge f(x)$; si es positiva en todo $I$, la comparación es estricta. El caso de derivada negativa produce del mismo modo decrecimiento estricto.

Para la implicación recíproca de 1, supongamos que $f$ es no decreciente y fijemos $x\in I$. Con $h>0$ suficientemente pequeño, tanto $f(x+h)-f(x)$ como $h$ son no negativos, y el cociente incremental es no negativo. Con $h<0$, el valor $f(x+h)$ no supera a $f(x)$, de modo que numerador y denominador son no positivos y el cociente vuelve a ser no negativo. Al pasar al límite obtenemos $f'(x)\ge0$.

Si $f$ es constante, todos sus cocientes incrementales son cero y por tanto $f'=0$. En sentido inverso, si $f'=0$ en cada punto, la igualdad del valor medio da $f(y)=f(x)$ para cualquier par: $f$ es constante.

Si el intervalo incluye algún borde, una comparación que lo tenga como extremo sigue admitiendo el valor medio gracias a la continuidad allí. La derivada sólo se necesita entre los dos puntos comparados. $\square$

El recíproco estricto **no** exige $f'(x)>0$ en todos los puntos: la función $x\mapsto x^3$ es estrictamente creciente en $\mathbb R$ y tiene $f'(0)=0$. A su vez, $f'(x)\ge0$ sólo fuerza crecimiento no estricto: puede haber tramos donde la función sea constante.

**Corolario 3.1 (unicidad de primitivas potenciales; `EDC-C03-COR-001`).** Sea $I\subseteq\mathbb R$ un intervalo no vacío, abierto, cerrado, semiabierto o no acotado. Sean $f,g:I\to\mathbb R$ **continuas en todo $I$ según la definición de continuidad relativa de C00** (también en cualquier extremo incluido) y derivables en su interior $I^{\circ}$. Si $f'(x)=g'(x)$ para todo $x\in I^{\circ}$, entonces $f-g$ es constante en **todo $I$**. Para un intervalo de un solo punto, la conclusión es trivial. Por tanto, una función cuya derivada se conoce queda determinada **salvo una constante aditiva**, siempre que ya exista alguna función con esa derivada y se controlen sus valores de borde.

**Demostración.** Consideremos la diferencia $h=f-g$, cuya derivada es cero en el interior de $I$. Para demostrar que todos sus valores coinciden necesitamos comparar dos puntos cualesquiera, incluidos los bordes que pertenezcan al dominio. Si $u<v$ están en $I$, el segmento $[u,v]$ queda contenido en él por ser intervalo. La continuidad de $f$ y $g$ en todo $I$ asegura la de $h$ en ese segmento, también cuando $u$ o $v$ son bordes incluidos; en $(u,v)$ tenemos derivabilidad y $h'=0$.

El valor medio da un $c\in(u,v)$ con $h(v)-h(u)=h'(c)(v-u)=0$. Así $h(v)=h(u)$ para cualquier par. Si el intervalo consta de un único punto, ya hay un único valor y no hace falta comparación. $\square$

Esta observación será decisiva en la teoría integral. Por ahora no hemos probado que *toda* función dada sea derivada de otra, ni hemos definido una integral.

## 3.6. Estimar una variación sin calcularla exactamente

**Teorema 3.5 (cotas de incremento; `EDC-C03-THM-005`).** Sea $f:[a,b]\to\mathbb R$ continua en $[a,b]$ y derivable en $(a,b)$, donde $a<b$. Si $m,M\in\mathbb R$ satisfacen

$$
m\le f'(x)\le M\qquad(x\in(a,b)),
$$

entonces

$$
m(b-a)\le f(b)-f(a)\le M(b-a).
$$

En particular, si $|f'(x)|\le K$ para todo $x\in(a,b)$ y $K\ge0$, entonces

$$
|f(b)-f(a)|\le K|b-a|.
$$

**Demostración.** El valor medio expresa el incremento total mediante una pendiente que quizá no podamos calcular, pero que está sometida a las cotas de la hipótesis. Existe $c\in(a,b)$ con $f(b)-f(a)=f'(c)(b-a)$, y en ese punto vale $m\le f'(c)\le M$. Multiplicamos por $b-a>0$, conservando el sentido de las desigualdades, y obtenemos las cotas del incremento. Si $|f'|\le K$, podemos tomar $m=-K$ y $M=K$; la diferencia queda entre $-K(b-a)$ y $K(b-a)$, lo que da la cota absoluta. $\square$

**Aplicación: una desigualdad trigonométrica.** Como $|\cos x|\le1$ para todo real y $\sin'=\cos$ se demostró en C02, para cualesquiera $a,b\in\mathbb R$ tenemos

$$
|\sin b-\sin a|\le|b-a|.
$$

La misma cota sirve para todos los pares de argumentos reales: el cambio del seno nunca supera la magnitud del cambio de su argumento.

**Proposición 3.1 (inversas y control de sensibilidad; `EDC-C03-PRP-001`).** Sea $I$ un intervalo abierto y $f:I\to\mathbb R$ derivable, con $f'(x)\ge m>0$ en todo $I$. Entonces $f$ es estrictamente creciente, admite una inversa $F:f(I)\to I$ y

$$
|F(v)-F(u)|\le\frac{|v-u|}{m}\qquad(u,v\in f(I)).
$$

**Demostración.** La cota $f'\ge m>0$ implica monotonía estricta por el Teorema 3.4, luego cada valor de $f(I)$ tiene una única preimagen y existe la inversa $F$. Para controlar sus variaciones, volvemos primero a los argumentos de $f$: escribamos $u=f(x)$ y $v=f(y)$. Si $x<y$, el valor medio da $v-u=f'(c)(y-x)\ge m(y-x)$. La separación entre los valores de $f$ es por tanto al menos $m$ veces la separación entre sus argumentos, y al dividir por $m>0$ obtenemos la cota de esta última separación.

Como $x=F(u)$ e $y=F(v)$, esa separación es precisamente la variación de la inversa. Si se invierte el orden de los argumentos, basta intercambiarlos; si coinciden, ambas diferencias son cero. La expresión con valores absolutos reúne los tres casos. $\square$

La condición $f'\ge m>0$ impide que la gráfica se vuelva casi horizontal: un cambio apreciable del argumento siempre produce un cambio proporcional del valor. Por eso la inversión tiene un control uniforme de sensibilidad, además de existir como correspondencia.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — L’Hôpital y Bernoulli: de las lecciones al libro"}
*Lectura opcional.*

La tabla de contenidos de la *Analyse des infiniment petits*, publicada por L’Hôpital en 1696, permite ver cómo se enseñaba el nuevo cálculo: primero las reglas de diferencias, después las tangentes y luego los máximos y mínimos. Las técnicas se reunían alrededor de preguntas sobre curvas, con figuras que daban un lugar a cada cantidad del cálculo.

Al final del prefacio, L’Hôpital reconoce cuánto debe a los Bernoulli, especialmente al más joven, entonces profesor en Groningen, Johann. También declara haber utilizado descubrimientos de ellos y de Leibniz. Ese reconocimiento deja visible una parte del trabajo compartido detrás del tratado: un libro de enseñanza puede organizar ideas recibidas y convertirlas en un recorrido que otros lectores sean capaces de seguir.

La sección dedicada a máximos y mínimos ofrece una conexión inmediata con nuestro capítulo. Después de aprender a calcular cambios, el lector necesita saber cómo usarlos para elegir una altura mayor o menor. Hemos construido esa justificación mediante Fermat, Rolle y el valor medio; las páginas antiguas permiten observar otra manera de llevar las reglas hasta los problemas de las curvas.

**Para seguir leyendo:** [L’Hôpital, *Analyse des infiniment petits* (1696), final del prefacio, tabla y sección III](https://www.hist-math.fr/textes/lHopital1696_InfinimentPetits.pdf); [Bradley, Petrilli y Sandifer, edición anotada (2015)](https://link.springer.com/book/10.1007/978-3-319-17115-9).
:::

## 3.7. Aproximación lineal y control del error

En C01 probamos que la derivabilidad en $a$ equivale a

$$
f(a+h)=f(a)+f'(a)h+r_a(h),\qquad\frac{r_a(h)}{|h|}\longrightarrow0
\quad(h\to0,\ h\ne0).
$$

La condición sobre $r_a(h)$ dice que, al acercarnos a $a$, el error resulta pequeño frente a $|h|$, aunque no nos da por sí sola una cota numérica para un incremento fijado. El valor medio permite expresar ese error mediante el cambio de la pendiente entre $a$ y un punto intermedio; si conocemos cómo varía $f'$, podremos estimar cuánto se aparta la función de su recta tangente.

**Proposición 3.2 (error de linealización; `EDC-C03-PRP-002`).** Sea $I$ un intervalo abierto, $a\in I$, y supongamos que $f$ es derivable en $I$. Para $a+h\in I$, $h\ne0$, existe un punto $c$ estrictamente entre $a$ y $a+h$ tal que

$$
f(a+h)-f(a)-f'(a)h=[f'(c)-f'(a)]h.
$$

Si además $f'$ es continua en $a$, el error es $o(|h|)$, de acuerdo con C01. Si $f'$ es derivable en el intervalo entre $a$ y $a+h$ y $|f''|\le K$ allí, entonces

$$
|f(a+h)-f(a)-f'(a)h|\le K|h|^2.
$$

**Demostración.** Si $h>0$, aplicamos el valor medio sobre $[a,a+h]$; si $h<0$, lo aplicamos sobre $[a+h,a]$ y reordenamos la igualdad obtenida. En ambos casos existe un $c$ estrictamente entre los extremos con $f(a+h)-f(a)=f'(c)h$. Al restar $f'(a)h$ resulta la primera igualdad: el error de la recta tangente depende de cuánto difiere la pendiente intermedia de la pendiente en $a$.

El punto $c$ está entre $a$ y $a+h$, de modo que $|c-a|<|h|$. Por eso $c\to a$ cuando $h\to0$, y si $f'$ es continua en $a$ tenemos $f'(c)-f'(a)\to0$. Al dividir la magnitud del error por $|h|$ obtenemos esa misma diferencia en valor absoluto, que tiende a cero.

Para la cota cuadrática usamos una segunda aplicación del valor medio, esta vez a $f'$ entre $a$ y $c$, bajo las hipótesis indicadas para ese tramo. Da $|f'(c)-f'(a)|\le K|c-a|\le K|h|$. La primera igualdad contiene además el factor $h$, así que la magnitud del error queda acotada por $K|h|^2$. $\square$

La cota cuadrática mejora el control del error cuando conocemos una cota para la segunda derivada, aunque la constante obtenida puede ser mayor de lo necesario. En la parábola, por ejemplo, el error exacto permite ver cuánto margen deja esta estimación; el ejercicio 3.30 hará esa comparación. El capítulo 9 desarrollará fórmulas con restos más precisos.

## 3.8. Convexidad: de las pendientes a la forma de la gráfica

En la parábola $x^2$, las pendientes aumentan al recorrer la recta y la gráfica queda debajo de las secantes que unen dos de sus puntos. La segunda propiedad puede formularse sin suponer que exista derivada: para comparar una altura intermedia con la altura de la secante basta expresar la posición del punto como una combinación de los dos extremos. Esa comparación define la convexidad; después veremos por qué equivale al crecimiento de las pendientes cuando la función es derivable.

**Definición 3.4 (`EDC-C03-DEF-004`).** Una función $f:I\to\mathbb R$, sobre un intervalo $I$, es **convexa** si para cualesquiera $x,y\in I$ y $t\in[0,1]$ se cumple

$$
f((1-t)x+ty)\le(1-t)f(x)+tf(y).
$$

Si la desigualdad es estricta cuando $x\ne y$ y $0<t<1$, se dice que $f$ es **estrictamente convexa**. La **concavidad** se define por convexidad de $-f$.

**Teorema 3.6 (pendientes y convexidad; `EDC-C03-THM-006`).** Sea $I$ un intervalo abierto y $f:I\to\mathbb R$ derivable. Son equivalentes:

1. $f$ es convexa;
2. $f'$ es no decreciente;
3. para todo $x,y\in I$,

$$
f(y)\ge f(x)+f'(x)(y-x).
$$

Si $f'$ es estrictamente creciente, entonces $f$ es estrictamente convexa.

**Demostración.** Supongamos que $f$ es convexa y tomemos $x<y<z$. El punto $y$ se escribe $y=(1-t)x+tz$ con $t=(y-x)/(z-x)$, comprendido entre cero y uno. La definición compara $f(y)$ con la altura de la secante entre $x$ y $z$. Al restar $f(x)$ y dividir por $y-x>0$ obtenemos la primera comparación; al restar la misma desigualdad de $f(z)$ y dividir por $z-y>0$ obtenemos la segunda:

$$
\frac{f(y)-f(x)}{y-x}\le\frac{f(z)-f(x)}{z-x}\le\frac{f(z)-f(y)}{z-y}.
$$

La pendiente de la secante larga queda entre las de las secantes a ambos lados de $y$. Fijemos $x<z$ y acerquemos $y$ a $x$ por la derecha: el primer cociente tiende a $f'(x)$, mientras el central permanece fijo. Si acercamos $y$ a $z$ por la izquierda, el último cociente tiende a $f'(z)$. Resulta $f'(x)\le(f(z)-f(x))/(z-x)\le f'(z)$, y por tanto $f'$ es no decreciente. Hemos probado 1 $\Rightarrow$ 2.

Para 2 $\Rightarrow$ 3, supongamos que $f'$ es no decreciente. Si $y>x$, el valor medio da $f(y)-f(x)=f'(c)(y-x)$ con $x<c<y$. Como $f'(c)\ge f'(x)$ y el incremento es positivo, la diferencia queda por encima de $f'(x)(y-x)$. Si $y<x$, el punto intermedio satisface $y<c<x$ y $f'(c)\le f'(x)$; al multiplicar por el incremento negativo $y-x$, el sentido se invierte y obtenemos la misma desigualdad. En $y=x$ ambos miembros coinciden.

Para recuperar la definición de convexidad a partir de 3, necesitamos comparar la gráfica con una secante, aunque lo que conocemos son comparaciones con tangentes. Sea $z=(1-t)x+ty$. Elegimos como base común de las dos comparaciones el punto $z$: tenemos $f(x)\ge f(z)+f'(z)(x-z)$ y $f(y)\ge f(z)+f'(z)(y-z)$. Multiplicamos la primera por $1-t$ y la segunda por $t$, cantidades no negativas, y sumamos. La elección de $z$ asegura $(1-t)(x-z)+t(y-z)=0$, por lo que los términos de pendiente desaparecen y queda $f(z)\le(1-t)f(x)+tf(y)$. Esto prueba 3 $\Rightarrow$ 1.

Si $f'$ es estrictamente creciente, las comparaciones del valor medio son estrictas cuando los puntos difieren. Para $x\ne y$ y $0<t<1$, el punto $z$ difiere de ambos extremos y las dos ponderaciones son positivas; al sumarlas obtenemos la desigualdad estricta de convexidad. $\square$

En la desigualdad de soporte, $f(x)+f'(x)(y-x)$ es la altura de la recta tangente en $x$, evaluada en otro punto $y$ del intervalo. La gráfica de una función convexa derivable queda por encima de cada una de esas rectas en todo el intervalo, aunque la tangente se haya definido a partir de información local en su punto de contacto.

**Corolario 3.2 (criterio por la segunda derivada; `EDC-C03-COR-002`).** Si $f$ es dos veces derivable sobre un intervalo abierto $I$ y $f''(x)\ge0$ para todo $x\in I$, entonces $f$ es convexa. Si $f''(x)>0$ en todo $I$, es estrictamente convexa. Las afirmaciones duales valen cuando $f''\le0$ o $f''<0$.

**Demostración.** Apliquemos el criterio de monotonía del Teorema 3.4 a $f'$, que es derivable y tiene derivada $f''$. Después aplicamos el Teorema 3.6. $\square$

**Ejemplo.** Como $(\ln x)''=-1/x^2<0$ para $x>0$, el logaritmo es estrictamente cóncavo en $(0,\infty)$. La desigualdad de soporte para una función cóncava, con base $x=1$, produce

$$
\ln y\le\ln1+(\ln1)'(y-1)=y-1,\qquad y>0.
$$

Hay igualdad si $y=1$, y es estricta en los demás puntos. La propiedad no depende de haber definido todavía la integral del logaritmo.

## 3.9. Qué decide la segunda derivada en un punto

El principio de Fermat reduce la búsqueda de extremos interiores derivables a puntos donde $f'=0$. La segunda derivada puede ayudar a **clasificarlos**, pero sólo bajo sus hipótesis.

**Teorema 3.7 (criterio local de segunda derivada; `EDC-C03-THM-007`).** Sea $c$ interior de un intervalo abierto $I$, y supongamos que $f$ es derivable en una vecindad de $c$, que $f'(c)=0$ y que $f'$ es derivable en $c$. Si $f''(c)>0$, entonces $f$ tiene un mínimo local estricto en $c$. Si $f''(c)<0$, tiene un máximo local estricto allí.

**Demostración.** Supongamos que $f''(c)>0$. Este número es el límite del cociente incremental de $f'$, de modo que podemos mantener el cociente positivo para incrementos suficientemente pequeños. Existe $\delta>0$ tal que

$$
\frac{f'(c+h)-f'(c)}h>0\qquad(0<|h|<\delta).
$$

Reducimos $\delta$ si hace falta para permanecer en la vecindad donde $f$ es derivable. Como $f'(c)=0$, la desigualdad afirma que $f'(c+h)$ tiene el mismo signo que $h$: es negativa a la izquierda de $c$ y positiva a su derecha.

Para ver que el mínimo es estricto también frente al valor en $c$, tomemos un punto $x$ de esa vecindad. Si $x<c$, el valor medio en $[x,c]$ da $f(c)-f(x)=f'(\xi)(c-x)<0$, pues $x<\xi<c$. Si $x>c$, aplicado a $[c,x]$ da $f(x)-f(c)=f'(\xi)(x-c)>0$. En ambos casos $f(x)>f(c)$ cuando $x\ne c$. La continuidad en $c$ necesaria para esas aplicaciones se sigue de la derivabilidad de $f$ allí. Si $f''(c)<0$, aplicamos el caso positivo a $-f$ y obtenemos un máximo local estricto de $f$. $\square$

Cuando $f''(c)=0$, el criterio no resuelve nada. Las funciones $x^4$, $-x^4$ y $x^3$ tienen en $0$ primera y segunda derivadas nulas; la primera tiene mínimo, la segunda máximo y la tercera ningún extremo. No hay una regla correcta que convierta automáticamente la igualdad $f''(c)=0$ en una clasificación.

## 3.10. Las derivadas tienen una propiedad intermedia

La función oscilatoria de C02 tiene pendientes que no se aproximan a un único valor cerca del origen. Esa falta de continuidad deja abierta una pregunta más precisa: si una derivada toma dos valores distintos, ¿puede omitir alguno situado entre ellos? Para una función cualquiera la respuesta es afirmativa, como muestra una función escalonada. El hecho de ser una derivada impone una restricción adicional.

**Teorema 3.8 (propiedad de Darboux de la derivada; `EDC-C03-THM-008`).** Sea $f:I\to\mathbb R$ derivable en un intervalo abierto $I$, y sean $a<b$ dos puntos de $I$. Si un número $\lambda$ está estrictamente entre $f'(a)$ y $f'(b)$, existe $c\in(a,b)$ tal que $f'(c)=\lambda$.

**Demostración.** Queremos encontrar un punto donde $f'$ valga $\lambda$. Restar una recta de pendiente $\lambda$ convierte esa búsqueda en la de una derivada nula: definamos $g(x)=f(x)-\lambda x$. Entonces $g'(x)=f'(x)-\lambda$.

Supongamos primero que $f'(a)<\lambda<f'(b)$; tenemos $g'(a)<0<g'(b)$. La pendiente negativa en $a$ asegura que, con algún incremento positivo suficientemente pequeño, $g(a+h)<g(a)$: el cociente incremental es negativo y su denominador positivo. Podemos escoger ese incremento con $a+h<b$, por lo que $a$ no realiza el mínimo absoluto sobre $[a,b]$.

En $b$, la pendiente positiva produce un cociente incremental positivo también para incrementos negativos suficientemente pequeños. Al multiplicar por $h<0$ obtenemos $g(b+h)<g(b)$, y podemos mantener $b+h>a$. El otro borde tampoco realiza el mínimo.

La derivabilidad de $g$ en $I$ implica continuidad en $[a,b]$, así que el teorema de valores extremos asegura la existencia de un mínimo absoluto. Como acabamos de excluir los bordes, se alcanza en un punto interior $c$. Fermat da $g'(c)=0$, que equivale a $f'(c)=\lambda$. Si $f'(a)>\lambda>f'(b)$, aplicamos el caso anterior a $-f$ y al valor $-\lambda$, y recuperamos la misma conclusión. $\square$

La prueba utilizó la continuidad de $f$, que sí está asegurada, sin suponer continuidad de $f'$. Por eso la propiedad intermedia puede convivir con las oscilaciones de C02: una derivada puede oscilar sin aproximarse a un único valor al acercarnos a un punto, pero entre dos valores que alcanza debe alcanzar también cada valor intermedio.

## 3.11. Un método de optimización con hipótesis comprobables

Si $f$ es continua en $[a,b]$, sabemos que un máximo y un mínimo existen antes de comenzar el cálculo. La derivada permite reducir la búsqueda: cualquier extremo interior donde exista debe ser estacionario, mientras que los puntos de no derivabilidad y los bordes requieren un examen directo. Una lista finita de candidatos será útil porque contendrá todos los extremos; al comparar sus valores, podremos decidir cuáles los realizan.

En un intervalo abierto o ilimitado, la existencia ya no viene dada por aquel teorema. Habrá que estudiar las comparaciones o el comportamiento cerca de los bordes: una ecuación $f'(x)=0$ puede tener una solución sin que la función alcance un máximo absoluto, y puede no tener ninguna aunque el problema admita un extremo en otro tipo de punto.

**Proposición 3.3 (optimización en intervalos cerrados; `EDC-C03-PRP-003`).** Sea $f:[a,b]\to\mathbb R$ continua y derivable salvo quizás en un conjunto $S\subset(a,b)$. Todo punto donde $f$ alcanza un máximo o mínimo absoluto pertenece a $\{a,b\}\cup S\cup\{c\in(a,b)\setminus S:f'(c)=0\}$. Si este conjunto de candidatos es finito, comparar sus valores identifica los extremos absolutos.

**Demostración.** La existencia es el teorema de valores extremos. Si un extremo ocurre en $c\in(a,b)\setminus S$, existe derivada y Fermat impone $f'(c)=0$. Todo caso restante está entre los bordes o en $S$. Para un conjunto finito de candidatos, cada extremo absoluto tiene que estar en él y basta comparar los valores. $\square$

**Ejemplo 1: el rectángulo de perímetro fijo.** Si el perímetro es $P>0$, sus lados positivos $x,y$ satisfacen $x+y=P/2$ y el área es

$$
A(x)=x\left(\frac P2-x\right),\qquad0<x<\frac P2.
$$

El polinomio se extiende continuamente a $[0,P/2]$ con valores nulos en los extremos. Como $A'(x)=P/2-2x$, es positivo para $x<P/4$ y negativo para $x>P/4$. El valor máximo entre rectángulos no degenerados corresponde a $x=y=P/4$ y es $P^2/16$. La restricción geométrica importa: un lado negativo no pertenece al problema.

**Ejemplo 2: una familia con decaimiento.** Sean $\alpha,\lambda>0$ y

$$
F(x)=x^{\alpha}e^{-\lambda x},\qquad x>0.
$$

Por las reglas de C02,

$$
F'(x)=x^{\alpha-1}e^{-\lambda x}(\alpha-\lambda x).
$$

Los dos primeros factores son positivos, de modo que $F$ crece para $0<x<\alpha/\lambda$ y decrece después. El máximo global en el semieje positivo se realiza en $x=\alpha/\lambda$, con valor $(\alpha/\lambda)^{\alpha}e^{-\alpha}$. Cada punto del dominio queda a un lado del candidato o coincide con él. La monotonía en esos dos intervalos permite compararlo con el candidato y comprobar que su valor es menor; esa comparación cubre todo el semieje, aunque éste no sea compacto.

## 3.12. Historia, alcance y tránsito a las cuadraturas

El problema de partir un segmento que encontramos en Fermat relaciona esta búsqueda de extremos con una tradición algebraica anterior a la derivada moderna. El resultado asociado a Rolle procede también de un contexto de ecuaciones; las formulaciones posteriores del valor medio dieron a la relación entre pendientes e incrementos el alcance que utilizamos aquí. Los testimonios leídos y los límites del cotejo se distinguen en las [notas históricas](capitulo-03-notas.html).

La comparación que hizo posibles estas aplicaciones se expresa en la relación

$$
\text{derivada local}\xrightarrow[\text{continuidad y derivabilidad}]{\text{Rolle y valor medio}}
\text{crecimiento, cotas y extremos en intervalos}.
$$

Las cotas de incremento dan un control cuantitativo sobre lo que puede cambiar una función entre dos puntos. Al estudiar áreas, necesitaremos otra forma de aproximación: reunir piezas sencillas y controlar la diferencia entre lo que cubren y la región buscada. Las cuadraturas de C04 ofrecerán problemas concretos para desarrollar esa idea, que conducirá a la integral y a su relación con la derivación.

### Mapa de dependencias

- **De C00:** orden y completitud de $\mathbb R$, continuidad, valores extremos, criterio secuencial y teorema del valor intermedio.
- **De C01:** derivada bilateral en un punto interior, límites laterales, aproximación afín y derivabilidad implica continuidad.
- **De C02:** suma, producto, composición, inversas y derivadas de potencias, exponencial, logaritmo y trigonometría, todas en sus dominios.
- **Nuevos:** `EDC-C03-THM-001--008`, `EDC-C03-PRP-001--003`, `EDC-C03-COR-001--002`, y las definiciones locales; no se invoca un resultado de C04–C11.
- **Reservado:** integrales, teorema fundamental, Taylor con resto e hipótesis de convergencia de series generales.

### Trabajo del lector

El banco [Ejercicios del capítulo 3](capitulo-03-ejercicios.html) propone problemas de lectura de hipótesis, cálculo aplicado, demostración, contraejemplos, optimización y una síntesis final. Las [soluciones desarrolladas](capitulo-03-soluciones.html) se conservan en archivo independiente: resolver antes de consultarlas forma parte del método del libro.
