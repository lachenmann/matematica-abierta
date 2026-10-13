---
title: Capítulo 2. La derivada como operación
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
source-id: EDC-C02
source-sha256: 754fc9dd8bca846764d6101dbaaa0949dd42c6fe334fc67eb5dc33d6a995c193
content-id: MA-BCH-0333
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-02.html) · [Ejercicios](capitulo-02-ejercicios.html) · [Soluciones](capitulo-02-soluciones.html) · [Notas históricas](capitulo-02-notas.html)

[← Capítulo 1](capitulo-01.html) · [Capítulo 3 →](capitulo-03.html)

> **Pregunta generadora.** Si conocemos cómo varían dos funciones, ¿qué podemos deducir del cambio de su suma, su producto, su cociente o su composición? ¿Y cómo convertir ese conocimiento en un método para estudiar funciones cada vez más complejas?

La derivada de $x^2$ se obtiene con relativa facilidad a partir del cociente incremental: al desarrollar $(x+h)^2$, los términos que estorban se cancelan y queda una expresión cuyo límite reconocemos enseguida. Si queremos derivar $(x^2+1)(x-3)$, todavía podríamos multiplicar los paréntesis y repetir el cálculo sobre el polinomio resultante, aunque ese rodeo empieza a esconder una pregunta más interesante: puesto que sabemos cómo varía cada factor por separado, ¿no habrá una manera de aprovechar ese conocimiento para averiguar cómo varía el producto? La dificultad se hace más visible con una función como $\sqrt{1+x^4}$, donde desarrollar una expresión ya no ofrece ninguna salida comparable, a pesar de que conocemos las funciones sencillas de las que está compuesta.

En el trabajo corriente con funciones, las sumas, los productos, los cocientes y las composiciones aparecen constantemente, de manera que las derivadas calculadas una por una servirían de poco si cada combinación nos obligara a empezar de nuevo con el límite que las define. Nos interesa entender qué ocurre con el cambio de una función al efectuar esas operaciones y hasta qué punto la derivada de una expresión puede obtenerse de las derivadas de sus partes; la respuesta dependerá de la operación considerada, porque la variación de un producto, por ejemplo, tiene que recoger el movimiento de ambos factores y no queda descrita por $f'g'$. Esta posibilidad de pasar de unas funciones conocidas a otras que construimos con ellas exige, además, precisar qué significa tratar la derivación como una operación entre funciones.

Las reglas que obtengamos permitirán combinar muchas derivadas sin rehacer sus cálculos, pero todavía tendremos que justificar las correspondientes a las funciones elementales: una identidad algebraica del seno o de la exponencial puede sugerir una fórmula, aunque por sí sola no demuestra el límite del que esa fórmula depende. Seguiremos, por ello, el orden lógico de los resultados disponibles, sin acudir al teorema del valor medio que aparecerá en el capítulo 3, al teorema fundamental del cálculo del capítulo 6 ni a la teoría general de series del capítulo 8; en el caso de la exponencial construiremos una serie particular y demostraremos dentro de este capítulo las propiedades que necesitemos para trabajar con ella.

## 2.1. De un valor derivado a una función derivada

Hasta aquí hemos calculado derivadas fijando primero un punto $a$ y preguntando cómo se comporta una función en sus proximidades; el resultado de ese cálculo, $f'(a)$, era un número que dependía tanto de la función elegida como del punto en el que se estudiaba. Pero nada nos obliga a mantener fijo ese punto: si realizamos el mismo procedimiento en cada lugar de un intervalo, a cada $a$ le corresponderá el número $f'(a)$, y esos números formarán una nueva función. Para $f(x)=x^2$, por ejemplo, el cociente incremental nos dio $f'(a)=2a$ cualquiera que fuera $a\in\mathbb R$; al permitir que $a$ recorra la recta obtenemos $f'(x)=2x$, de modo que podemos pensar la derivación como una operación que toma una función y, cuando es posible efectuarla, produce otra.

Consideremos, para expresar esa operación con cuidado, un intervalo abierto no vacío $I\subseteq\mathbb R$ y una función $f:I\to\mathbb R$ derivable en todos sus puntos; como el valor de la derivada existe en cada $x\in I$, podemos asignarle el número

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h,
$$

calculado con $h\ne0$ y $x+h\in I$. Es el mismo límite que definimos al estudiar un punto fijo, pero ahora lo consideramos en todos los puntos del intervalo y obtenemos una nueva función, $f':I\to\mathbb R$, en lugar de un único número.

**Definición 2.1 (`EDC-C02-DEF-001`).** Designamos por $\mathcal D(I)$ el conjunto de funciones reales derivables en cada punto de $I$. El **operador derivación** es

$$
D:\mathcal D(I)\longrightarrow\mathbb R^I,
\qquad Df=f'.
$$

El codominio $\mathbb R^I$ es el conjunto de todas las funciones que llevan puntos de $I$ a números reales, sin exigirles continuidad ni derivabilidad, y esa amplitud es necesaria porque de la existencia de $f'(x)$ para cada $x$ no se sigue que la función $f'$ sea continua, mucho menos que pueda derivarse otra vez. Tampoco debe invertirse la implicación conocida entre derivabilidad y continuidad: la función $x\mapsto|x|$ es continua en toda la recta y, sin embargo, carece de derivada en $0$, por lo que no pertenece a $\mathcal D(\mathbb R)$.

Podemos escribir $Df=f'$ para destacar que estamos aplicando el operador $D$ a una función, y también, si $y=f(x)$, emplear la notación $dy/dx=f'(x)$, cuya ventaja se hará patente cuando una magnitud dependa de otra a través de varias funciones intermedias. Conviene conservar, sin embargo, la distinción entre la notación y aquello que hemos definido: la expresión $dy/dx$ representa aquí una derivada, y su apariencia de fracción no justifica tratar $dy$ y $dx$ como dos números reales cuya división esté ya establecida.

Con esta perspectiva podemos investigar las operaciones habituales entre funciones y demostrar, partiendo del cociente incremental, las reglas que nos permitirán calcular nuevas derivadas a partir de las que conocemos; sólo después de establecerlas podremos usarlas sin regresar a la definición en cada ejemplo.

## 2.2. Sumas, productos y cocientes

Si sumamos dos funciones, el cambio de su suma entre $a$ y $a+h$ se descompone de inmediato en los cambios de cada una de ellas, de modo que las propiedades de los límites permiten prever una regla especialmente sencilla. Con el producto ocurre algo distinto, como muestra el ejemplo más elemental: al tomar $f(x)=g(x)=x$ obtenemos $fg=x^2$ y, por consiguiente, $(fg)'(x)=2x$, mientras que $f'(x)g'(x)=1$. La fórmula correcta tendrá que explicar por qué intervienen los valores de los factores además de sus derivadas; una vez comprendido ese mecanismo, podremos tratar también el cociente, siempre que su denominador no se anule cerca del punto considerado.

**Teorema 2.1 (reglas algebraicas; `EDC-C02-THM-001`).** Sea $a$ un punto interior de un dominio común $D\subseteq\mathbb R$, y sean $f,g:D\to\mathbb R$ derivables en $a$. Para cualesquiera $\alpha,\beta\in\mathbb R$ se tiene

$$
(\alpha f+\beta g)'(a)=\alpha f'(a)+\beta g'(a),
$$

$$
(fg)'(a)=f'(a)g(a)+f(a)g'(a).
$$

Si además $g(a)\ne0$, el cociente $f/g$ está definido en un entorno de $a$ y

$$
\left(\frac fg\right)'(a)
=\frac{f'(a)g(a)-f(a)g'(a)}{g(a)^2}.
$$

**Demostración.** En una combinación lineal, los coeficientes $\alpha$ y $\beta$ permanecen fijos. Al restar los valores en $a+h$ y $a$ y dividir por $h\ne0$, el cociente se separa en el de $f$ multiplicado por $\alpha$ y el de $g$ multiplicado por $\beta$. El álgebra de límites de C00 permite pasar al límite en esa suma y obtener la primera fórmula.

En el producto cambian los dos factores, y necesitamos separar sus variaciones para aprovechar las derivadas conocidas. Podemos pasar de $f(a)g(a)$ a $f(a)g(a+h)$ cambiando sólo el segundo factor, y de ese valor a $f(a+h)g(a+h)$ cambiando el primero. Introducir el producto intermedio equivale a sumar y restar $f(a)g(a+h)$ y da

$$
\begin{aligned}
&\frac{f(a+h)g(a+h)-f(a)g(a)}h\\
&\qquad=\frac{f(a+h)-f(a)}h\,g(a+h)
+f(a)\frac{g(a+h)-g(a)}h.
\end{aligned}
$$

Cada diferencia aparece ahora dentro de su propio cociente incremental. El primero converge a $f'(a)$ y el segundo a $g'(a)$; el factor adicional $g(a+h)$ satisface $g(a+h)\to g(a)$ porque derivabilidad implica continuidad, según el Teorema 1.3 de C01 (`EDC-C01-THM-003`). Los dos sumandos producen así los dos términos de la fórmula.

Para el cociente hay una condición previa a la resta de fracciones. La continuidad de $g$ y $g(a)\ne0$ aseguran $g(a+h)\ne0$ para incrementos suficientemente pequeños: basta mantener $|g(a+h)-g(a)|<|g(a)|/2$. Con esas divisiones definidas, calculamos

$$
\frac{f(a+h)/g(a+h)-f(a)/g(a)}h
=\frac{g(a)[f(a+h)-f(a)]-f(a)[g(a+h)-g(a)]}{h\,g(a+h)g(a)}.
$$

Después de dividir el numerador por $h$, reconocemos los cocientes incrementales de $f$ y $g$, multiplicados por $g(a)$ y $f(a)$. El denominador restante converge a $g(a)^2\ne0$, de modo que el álgebra de límites permite obtener la fórmula del cociente. $\square$

Las igualdades $(cf)'=cf'$ y $(f+g)'=f'+g'$ expresan la **linealidad** de la derivación. En el producto intervienen también los valores de los factores, porque la variación de uno se combina con el valor del otro; por eso las expresiones $(fg)'=f'g'$ y $(f/g)'=f'/g'$ fallan en general.

**Proposición 2.1 (`EDC-C02-PRP-001`).** La derivada de una función constante es cero, la de $x\mapsto x$ es $1$ y, para cada entero $n\ge1$,

$$
\frac{d}{dx}x^n=nx^{n-1}\qquad(x\in\mathbb R).
$$

**Demostración.** Para una función constante de valor $c$, cada cociente incremental es $(c-c)/h=0$; para la función identidad, el cociente es $(x+h-x)/h=1$. Esta segunda afirmación proporciona también el caso $n=1$ de la fórmula de potencias.

Si la fórmula vale para un entero $n\ge1$, podemos escribir $x^{n+1}=x^n x$ y aplicar la regla del producto. La derivada es $nx^{n-1}x+x^n=(n+1)x^n$, que tiene la forma requerida para el exponente siguiente. La inducción prueba el resultado para todos los enteros positivos. $\square$

Para un exponente entero negativo, $x^{-n}=1/x^n$ se estudia en $x\ne0$; la regla del cociente produce $(x^{-n})'=-n x^{-n-1}$. En ningún caso una fórmula justifica evaluar una función fuera de su dominio.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Leibniz: aprender a calcular con piezas sencillas"}
*Lectura opcional.*

En octubre de 1684, los lectores de *Acta Eruditorum* encontraron un trabajo de siete páginas en el que Leibniz proponía un método para determinar máximos, mínimos y tangentes. El título de la *Nova methodus* anunciaba que el procedimiento no se detenía ante cantidades fraccionarias o irracionales. Junto a las figuras de curvas y tangentes aparecían las diferencias $dx$ y $dy$, con reglas para operar sobre sumas, productos y cocientes.

La regla del producto se comprende al seguir los dos lados de un rectángulo: cuando pasan de $x$ e $y$ a $x+\Delta x$ e $y+\Delta y$, el área aumenta en $y\,\Delta x+x\,\Delta y+\Delta x\,\Delta y$. Los primeros términos recogen el cambio de cada lado sobre el otro; el último es la pequeña esquina producida por ambos cambios a la vez. En nuestra formulación, si los lados son funciones derivables de una misma variable, el término mixto dividido por el incremento de esa variable tiende a cero y obtenemos $(xy)'=x'y+xy'$. La escritura diferencial conserva la relación compacta $d(xy)=x\,dy+y\,dx$.

Leibniz presentaba sus reglas dentro de una concepción del cálculo distinta de la definición moderna por límites. Su alcance se aprecia al volver al problema de las tangentes: descomponer la ecuación de una curva en operaciones conocidas permitía tratar expresiones complicadas mediante reglas comunes. Ése es también el valor que acabamos de encontrar en la prueba del producto.

**Para seguir leyendo:** [Leibniz, *Nova methodus* (1684), traducción de Thiago Dourado (2022), pp. 47–49; reproducción del original latino de pp. 467–473 al final del artículo](https://www.rbhm.org.br/index.php/RBHM/article/download/377/340).
:::

## 2.3. La composición y la regla de la cadena

En una composición, la función interior cambia primero el argumento que recibe la exterior. Para derivar $(x^2+1)^3$, por ejemplo, necesitamos seguir el cambio de $x^2+1$ y después el efecto de ese cambio sobre el cubo. La aproximación lineal permite separar ambos pasos conservando sus errores y explicar por qué las dos derivadas aparecen multiplicadas.

**Teorema 2.2 (regla de la cadena; `EDC-C02-THM-002`).** Sean $I,J\subseteq\mathbb R$ intervalos abiertos, $g:I\to J$ y $f:J\to\mathbb R$. Si $g$ es derivable en $a\in I$ y $f$ es derivable en $b=g(a)$, entonces $f\circ g$ es derivable en $a$ y

$$
(f\circ g)'(a)=f'(g(a))\,g'(a).
$$

**Demostración.** Podríamos intentar formar un cociente de cambios de $f$ y multiplicarlo por otro de cambios de $g$, pero eso exigiría dividir por $g(a+h)-g(a)$. Ese incremento puede ser cero incluso con $h\ne0$, de modo que elegimos la aproximación lineal de C01, que expresa la variación de $f$ sin esa división. Para $u$ próximo a $0$,

$$
f(b+u)-f(b)=u\,[f'(b)+\eta(u)],
\qquad \eta(u)\longrightarrow0,
$$

con $\eta(0)=0$. La identidad vale también en $u=0$, porque ambos miembros se anulan. Tomemos $u=g(a+h)-g(a)$; la continuidad de $g$ en $a$ garantiza $u\to0$, y podemos sustituirlo en la aproximación de $f$. Al dividir únicamente por el incremento exterior $h\ne0$, obtenemos

$$
\frac{f(g(a+h))-f(g(a))}h
=\frac{g(a+h)-g(a)}h
\,[f'(b)+\eta(g(a+h)-g(a))].
$$

El primer factor converge a $g'(a)$. En el segundo, el error tiende a cero porque su argumento se aproxima a cero y $\eta(0)=0$; esa convención cubre también los incrementos para los que $g(a+h)=g(a)$. Su límite es por tanto $f'(b)$, y el producto da la derivada anunciada. $\square$

Por ejemplo, si $u(x)=x^2+1$ y $f(t)=t^3$, entonces

$$
\frac d{dx}(x^2+1)^3=3(x^2+1)^2(2x).
$$

La composición también puede ser derivable aunque una de las hipótesis del teorema falle. Si $f(t)=|t|$ y $g(x)=x^2$, la función exterior no es derivable en $0$, mientras que $f(g(x))$ coincide con $x^2$ y tiene derivada cero en ese punto. Las hipótesis de la regla de la cadena son suficientes, no condiciones necesarias para cada composición particular.

**Definición 2.2 (`EDC-C02-DEF-002`).** Una expresión de la forma $f\circ g$, con dominio efectivo $\{x\in\operatorname{dom}g:g(x)\in\operatorname{dom}f\}$, es una **composición admisible**. El dominio efectivo debe determinarse *antes* de derivar. Así, $\sqrt{1-x^2}$ está definida sobre $[-1,1]$, pero no tendrá derivada real bilateral en los extremos de ese intervalo.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Leibniz y una notación que cuenta una historia"}
*Lectura opcional.*

En la primera sección de su *Analyse des infiniment petits*, publicada en 1696, L’Hôpital advierte que usará la letra $d$ para marcar la diferencia de una cantidad variable y que esa marca tendrá un uso reservado. En una misma figura asigna letras a abscisas, ordenadas, arcos y áreas, y escribe sus diferencias como $dx$, $dy$ o $du$. La notación permite conservar qué cantidad está cambiando incluso cuando todas participan en un mismo cálculo.

Esa atención a las letras resulta útil al escribir hoy $dy/dx$. Si $y=f(u)$ y $u=g(x)$, la fórmula $dy/dx=(dy/du)(du/dx)$ mantiene visible la dependencia intermedia: primero cambia $u$ al cambiar $x$, y ese cambio modifica $y$. Las letras repetidas recuerdan el recorrido, mientras que la prueba de la cadena justifica multiplicar las tasas correspondientes.

El lenguaje de diferencias de aquel libro pertenece a su propia concepción de los infinitamente pequeños. Podemos apreciar la utilidad de su escritura y, al mismo tiempo, leer nuestra fórmula como una igualdad entre derivadas cuya existencia se comprueba en los puntos indicados.

**Para seguir leyendo:** [L’Hôpital, *Analyse des infiniment petits* (1696), sección I, p. 2, «Avertissement» sobre la característica $d$](https://www.hist-math.fr/textes/lHopital1696_InfinimentPetits.pdf).
:::

## 2.4. La derivada de la función inversa

En una inversa intercambiamos el argumento y el valor: una separación horizontal para $f$ pasa a ser vertical para su inversa. Esa imagen sugiere que las pendientes deberían ser recíprocas, pero necesita dos garantías. Debe existir una inversa que lleve los valores próximos al punto inicial, y la pendiente original debe ser distinta de cero para que su recíproco tenga sentido.

**Teorema 2.3 (derivada de la inversa; `EDC-C02-THM-003`).** Sea $I$ un intervalo abierto, $f:I\to\mathbb R$ continua y estrictamente monótona, y sea $a\in I$. Si $f$ es derivable en $a$ y $f'(a)\ne0$, entonces su inversa $F:f(I)\to I$ es derivable en $b=f(a)$ y

$$
F'(b)=\frac1{f'(a)}.
$$

**Demostración.** La monotonía estricta hace que cada valor de $f(I)$ tenga una única preimagen; la continuidad y el teorema del valor intermedio de C00 aseguran que esa imagen es un intervalo (`EDC-C00-THM-006`). Como $a$ es interior, podemos escoger dos puntos $a_\pm$ con $a_-<a<a_+$ en $I$. Los valores $f(a_-)$ y $f(a_+)$ quedan a lados opuestos de $b=f(a)$, tanto si la función crece como si decrece. Por valor intermedio, la imagen contiene un entorno de $b$, que es por tanto un punto interior de su dominio.

Para controlar la continuidad de $F$ en $b$, elegimos $a_-$ y $a_+$ tan próximos a $a$ como pida una tolerancia dada. Los valores suficientemente próximos a $f(a)$ quedan entre $f(a_-)$ y $f(a_+)$, y la monotonía sitúa sus preimágenes entre $a_-$ y $a_+$. Así obtenemos $F(y)\to a$ cuando $y\to b$.

Para $y\ne b$ en $f(I)$, escribamos $x=F(y)\ne a$. La inyectividad garantiza que también $f(x)-f(a)\ne0$, y podemos intercambiar los incrementos:

$$
\frac{F(y)-F(b)}{y-b}
=\frac{x-a}{f(x)-f(a)}
=\left[\frac{f(x)-f(a)}{x-a}\right]^{-1}.
$$

Cuando $y\to b$, la continuidad de la inversa permite concluir $x\to a$. La expresión entre corchetes se aproxima a $f'(a)\ne0$, por lo que su recíproco converge a $1/f'(a)$. Ése es el límite que define $F'(b)$. $\square$

La hipótesis $f'(a)\ne0$ no es una formalidad. Si $f(x)=x^3$, su inversa es $F(y)=\sqrt[3]{y}$: en $a=0$, $f'(0)=0$, y el cociente $F(h)/h=|h|^{-2/3}$ no tiene límite real finito. En cambio, para $f(x)=x^2$ restringida a $(0,\infty)$, obtenemos

$$
\frac d{dy}\sqrt y=\frac1{2\sqrt y},\qquad y>0.
$$

La derivada no se extiende como número real finito a $y=0$.

## 2.5. Derivar relaciones sin despejar primero

Algunas curvas se describen por una relación entre dos cantidades y no por una sola fórmula explícita. Pensemos en la circunferencia de radio $r>0$:

$$
x^2+y^2=r^2.
$$

Si en un intervalo $J\subset(-r,r)$ elegimos una rama diferenciable $y=y(x)$ que satisfaga la relación, las reglas ya demostradas dan

$$
2x+2y(x)y'(x)=0.
$$

Si $y(x)\ne0$ concluimos $y'(x)=-x/y(x)$. Esta forma evita despejar una raíz antes de empezar, pero **no prueba** por sí sola que exista una rama diferenciable. Para justificarla aquí basta escoger la rama superior explícita $y(x)=\sqrt{r^2-x^2}$ en $(-r,r)$, cuya diferenciabilidad se deduce de los teoremas de inversa y cadena; la inferior se trata de igual modo.

**Proposición 2.2 (derivación implícita condicionada; `EDC-C02-PRP-002`).** Si $P(x,y)$ es un polinomio y $y:J\to\mathbb R$ es una función derivable sobre un intervalo abierto $J$ tal que $P(x,y(x))=0$, la identidad se puede derivar término a término mediante producto y cadena. Si el coeficiente que multiplica a $y'(x)$ en la identidad obtenida es no nulo, esa ecuación determina $y'(x)$. Esta proposición no afirma existencia de $y$, ni unicidad de la rama ni un teorema general de la función implícita.

**Demostración.** Podemos descomponer el polinomio en una suma finita de monomios $c x^m y(x)^n$. En cada uno, la dependencia de $x$ aparece directamente en la potencia $x^m$ y a través de la función $y$ en la otra potencia. Las reglas de los §§2.2–2.3 permiten derivar ambos factores y su producto; cuando alguno de los exponentes es cero, el factor correspondiente es constante. La suma finita es por tanto derivable.

La relación $P(x,y(x))=0$ afirma que esa función compuesta permanece constante al recorrer $J$, de modo que su derivada vale cero. Al aplicar producto y cadena, los términos que contienen $y'$ aparecen multiplicados por funciones de $x$ y de $y(x)$; reunidos, dan una ecuación lineal en $y'$. Si su coeficiente no se anula, podemos dividir por él y determinar la derivada. Todo el argumento parte de una función $y$ ya existente y derivable: el cálculo de su pendiente no establece por sí mismo esas propiedades. $\square$

## 2.6. Un problema que las reglas no resuelven: la exponencial

Hasta aquí sabemos **combinar** derivadas, pero el problema de encontrar la derivada de una función nueva sigue abierto. La exponencial constituye un buen laboratorio: buscamos una función continua y positiva que convierta sumas de argumentos en productos y cuya tasa local vuelva a ser la propia función.

Los polinomios de sumas parciales que siguen permiten construir la función mediante límites. Tendremos que justificar su convergencia y las operaciones que identifican su suma; concentraremos las estimaciones en esta construcción, antes de disponer de la teoría general de series de C08.

**Lema 2.1 (serie exponencial particular; `EDC-C02-LEM-001`).** Para cada $x\in\mathbb R$ converge absolutamente la sucesión de sumas parciales

$$
E_N(x)=\sum_{n=0}^{N}\frac{x^n}{n!},\qquad 0!=1.
$$

Su límite, denotado por $E(x)$, satisface $E(0)=1$ y

$$
E(x+y)=E(x)E(y)\qquad (x,y\in\mathbb R).
$$

**Demostración.** Fijemos $R>0$ y controlemos los términos para $|x|\le R$. Al pasar del término de índice $n$ al siguiente, el módulo se multiplica por $|x|/(n+1)$, que acaba siendo pequeño. Si $N+2>R$, todos los cocientes posteriores al primer término de la cola quedan acotados por $R/(N+2)<1$. La comparación geométrica da

$$
\sum_{n=N+1}^{\infty}\frac{|x|^n}{n!}
\le\frac{R^{N+1}}{(N+1)!}
\frac1{1-R/(N+2)}.
$$

Esta cota se obtiene primero para cada suma finita de la cola, usando la fórmula de una progresión geométrica. Las sumas de términos absolutos son no decrecientes y están acotadas por un tramo inicial finito más esa cota, de modo que convergen por el Teorema 0.2 de C00; sólo entonces la desigualdad escrita con una cola infinita representa el límite de aquellas sumas finitas. Además, el factor $R^{N+1}/(N+1)!$ tiende a cero, porque a partir de cierto índice sus cocientes consecutivos son menores que $1/2$. El otro factor permanece acotado para $N$ grande, y la cota de las colas tiende a cero. Para los términos con signo, podemos separar sus partes positivas y negativas: ambas tienen sumas parciales crecientes acotadas por las sumas absolutas. Su diferencia converge y define $E(x)$. Para $x=0$ queda únicamente el término constante, luego $E(0)=1$.

Para $x,y$ fijados queremos multiplicar las sumas. Primero multiplicamos los polinomios finitos; sus productos son sumas rectangulares, con índices $0\le p,q\le N$, de términos $x^py^q/(p!q!)$, y por el álgebra de límites convergen a $E(x)E(y)$. El mismo cálculo con términos no negativos da

$$
\sum_{p,q\ge0}\frac{|x|^p|y|^q}{p!q!}=E(|x|)E(|y|)<\infty.
$$

La igualdad se entiende como límite de sumas **rectangulares finitas**. Para aplicar el binomio finito conviene reunir los términos cuyo grado total es $p+q=n$. Hay que justificar que esa forma de reunirlos conserva el límite. La contribución absoluta que queda fuera del cuadrado $0\le p,q\le K$ se acota por la cola de la primera serie multiplicada por $E(|y|)$ más la cola de la segunda multiplicada por $E(|x|)$; ambas tienden a cero cuando $K$ crece. El triángulo de índices $p+q\le N$ contiene el cuadrado de lado $\lfloor N/2\rfloor$ y está contenido en el cuadrado de lado $N$. Por tanto, el error entre las sumas triangulares y rectangulares queda controlado por esas mismas colas, y las dos formas de sumar tienen el mismo límite.

Dentro de cada grado la suma es finita, y la fórmula binomial produce

$$
\begin{aligned}
E(x)E(y)&=\sum_{n=0}^{\infty}\sum_{p=0}^{n}\frac{x^py^{n-p}}{p!(n-p)!}\\
&=\sum_{n=0}^{\infty}\frac{(x+y)^n}{n!}=E(x+y).
\end{aligned}
$$

La identidad procede así de productos y reagrupamientos finitos cuyo error controlamos al pasar al límite. No hemos derivado ni integrado término a término una serie de funciones. $\square$

**Proposición 2.3 (`EDC-C02-PRP-003`).** La función $E$ es positiva, continua y estrictamente creciente; $E(\mathbb R)=(0,\infty)$.

**Demostración.** La identidad multiplicativa permite controlar el signo antes de estudiar la variación. Al tomar los argumentos opuestos obtenemos $E(x)E(-x)=E(0)=1$, luego $E(x)\ne0$. Al dividir el argumento en dos mitades, la misma identidad da $E(x)=E(x/2)^2$, de donde $E(x)>0$.

Para $h>0$, la serie tiene términos positivos y $E(h)>1+h>1$. Si $y>x$, podemos escribir $E(y)=E(x)E(y-x)>E(x)$: el factor adicional corresponde a un argumento positivo y supera a uno. Esto demuestra el crecimiento estricto sin recurrir al signo de una derivada.

La identidad reduce también la continuidad en cualquier punto a lo que sucede en cero. Para $|h|\le1$, cada potencia absoluta de grado positivo queda acotada por $|h|$, y obtenemos $|E(h)-1|\le\sum_{n\ge1}|h|^n/n!\le|h|E(1)$. Por tanto, $E(h)\to1$; al usar $E(x+h)=E(x)E(h)$ concluimos la continuidad en $x$.

Para los argumentos positivos, $E(x)\ge1+x\to\infty$ cuando $x\to+\infty$. En el otro sentido, $E(-x)=1/E(x)\to0$ para $x\to+\infty$. Dado cualquier valor positivo, podemos encontrar dos argumentos cuyas imágenes queden a cada lado de él; la continuidad y el valor intermedio aseguran que se alcanza. Junto con la positividad ya demostrada, esto da $E(\mathbb R)=(0,\infty)$. $\square$

**Teorema 2.4 (derivada de la exponencial; `EDC-C02-THM-004`).** Para todo $x\in\mathbb R$,

$$
E'(x)=E(x).
$$

**Demostración.** Cerca de cero, los términos constante y lineal de la serie son $1$ y $h$. Para averiguar si la derivada es uno, restamos esos términos y controlamos el resto después de dividir por el incremento. Para $0<|h|\le1$,

$$
\left|\frac{E(h)-1}{h}-1\right|
\le\frac1{|h|}\sum_{n=2}^{\infty}\frac{|h|^n}{n!}
\le\frac{|h|}{2}E(1)\longrightarrow0,
$$

pues, al escribir $n=m+2$, tenemos $(m+2)!\ge2m!$ y $|h|^m\le1$. Esa estimación prueba $E'(0)=1$ sin intercambiar una derivada con la suma infinita.

Para trasladar el resultado a un punto $x$ fijo usamos la identidad multiplicativa: convierte el incremento de $E$ en ese punto en un múltiplo fijo del incremento en cero,

$$
\frac{E(x+h)-E(x)}h
=E(x)\frac{E(h)-1}h\longrightarrow E(x).
$$

Se obtiene $E'(x)=E(x)$ en toda la recta. $\square$

**Definición 2.3 (`EDC-C02-DEF-003`).** Escribimos $e=E(1)$ y $e^x=E(x)$, $x\in\mathbb R$. La definición es compatible con las potencias racionales ordinarias, pues $(E(m/n))^n=E(m)=e^m$ y $E(m/n)>0$. No se ha supuesto previamente que $e^x$ tenga derivada $e^x$: esa propiedad acaba de demostrarse.

La derivada quedó determinada por el control del resto en cero y por la identidad multiplicativa de $E$. La convergencia de la serie fue necesaria para construir la función, pero por sí sola no habría autorizado derivarla término a término. La justificación de ese intercambio para una clase general de series será un problema distinto en C08.

## 2.7. El logaritmo y las potencias reales

La función $E$ es continua, estrictamente creciente y transforma $\mathbb R$ sobre $(0,\infty)$. Posee, por tanto, una inversa en todo el semieje positivo.

**Definición 2.4 (`EDC-C02-DEF-004`).** Llamamos **logaritmo natural** a $\ln:(0,\infty)\to\mathbb R$, la inversa de $E$: $\ln(E(x))=x$ y $E(\ln y)=y$ para $y>0$. Para $a>0$ definimos la función exponencial de base $a$ por $a^x=E(x\ln a)$; si $a\ne1$, definimos $\log_a y=\ln y/\ln a$, $y>0$.

De $E(u+v)=E(u)E(v)$ y su inyectividad se obtiene

$$
\ln(xy)=\ln x+\ln y\qquad(x,y>0).
$$

**Teorema 2.5 (logaritmo y potencia real; `EDC-C02-THM-005`).** Para $x>0$, $a>0$ y $r\in\mathbb R$,

$$
(\ln x)'=\frac1x,\qquad
(a^x)'=a^x\ln a,\qquad
(x^r)'=r x^{r-1},
$$

siempre que $x^r$ se entienda, para base positiva, como $E(r\ln x)$.

**Demostración.** Para derivar $\ln x$, tomemos el punto $\ln x$ de la función original $E$. Su derivada es $E'(\ln x)=E(\ln x)=x>0$, de modo que el Teorema 2.3 permite tomar el recíproco y obtener $(\ln x)'=1/x$.

La base $a>0$ permanece fija en la exponencial $a^x$, y por eso $\ln a$ es una constante. La regla de la cadena y el Teorema 2.4 dan

$$
\frac d{dx}E(x\ln a)=E(x\ln a)\ln a.
$$

En la potencia $x^r$ fijamos en cambio el exponente $r$ y hacemos variar la base positiva. Su representación mediante el logaritmo permite aplicar la cadena:

$$
\frac d{dx}E(r\ln x)=E(r\ln x)\frac r x=rx^{r-1}.
$$

La última igualdad usa $x^r/x=x^{r-1}$, consecuencia de la identidad de productos de $E$ y de la definición para bases positivas. $\square$

Por ejemplo, $(\sqrt{x})'=1/(2\sqrt{x})$ si $x>0$, como ya dedujimos por la regla de la inversa. La función $x\mapsto\ln|x|$ está definida para $x\ne0$ y su derivada allí es $1/x$, mediante la cadena sobre cada semieje; **no** debe confundirse con $\ln x$, definida sólo para $x>0$.

**Nota de dominio.** La expresión $x^r$ para $x<0$ puede ser real para algunos exponentes racionales, pero no se deduce de la definición general $E(r\ln x)$. Cualquier ampliación a bases negativas exige un dominio y una justificación propios. En $x=0$, incluso para $r>0$, la existencia de la derivada debe analizarse por separado; la fórmula del teorema no lo incluye.

## 2.8. Por qué importan los radianes: seno y coseno

Las fórmulas de adición de la trigonometría se conocen sin cálculo diferencial:

$$
\sin(x+h)=\sin x\cos h+\cos x\sin h,
$$

$$
\cos(x+h)=\cos x\cos h-\sin x\sin h.
$$

Para derivarlas basta estudiar el comportamiento de $\sin h/h$ y $(\cos h-1)/h$ en el origen. Pero el primer límite depende de la **unidad angular**.

**Contrato geométrico previo (MAT-01).** La prueba siguiente emplea las identidades trigonométricas de adición y las reglas elementales de áreas poligonales: fórmula del triángulo, monotonía bajo inclusión y aditividad para piezas sin solapamiento interior. También emplea **un antecedente de geometría circular**: un sector del círculo unitario que subtiende un ángulo de $h$ radianes tiene área $h/2$. Esta relación puede obtenerse en geometría euclídea mediante agotamiento poligonal, pero **no se demuestra aquí la existencia general del área sectorial ni su normalización**. Es una premisa geométrica expresamente admitida, no una aplicación de la integral de Riemann aún indefinida ni una consecuencia del axioma del supremo de C00.

**Lema 2.2 (normalización circular; `EDC-C02-LEM-002`).** Si los argumentos trigonométricos se miden en radianes, entonces

$$
\lim_{h\to0}\frac{\sin h}{h}=1,
\qquad
\lim_{h\to0}\frac{\cos h-1}{h}=0.
$$

**Demostración geométrica.** Para $0<h<\pi/2$, el triángulo inscrito bajo el arco de la circunferencia unidad, el sector circular y el triángulo exterior determinado por la tangente tienen áreas ordenadas. La geometría elemental del círculo, con ángulos en radianes y área del sector unitario igual a $h/2$, da

$$
\frac{\sin h}{2}\le\frac h2\le\frac{\tan h}{2},
\qquad\text{luego}\qquad
\cos h\le\frac{\sin h}{h}\le1.
$$

El triángulo interior tiene área $\sin h/2$, el sector área $h/2$ por la premisa geométrica declarada, y el triángulo exterior área $\tan h/2$. El orden de inclusión de estas figuras justifica las desigualdades **condicionalmente a aquella premisa**. No usamos integrales ni derivadas en el argumento. Además, $0\le\sin h\le h$ y $\cos h=\sqrt{1-\sin^2h}\to1$, por lo que el encajonamiento da el primer límite por la derecha; la imparidad del seno lo extiende al lado izquierdo. Finalmente,

$$
\frac{\cos h-1}{h}=-\frac{\sin^2h}{h(1+\cos h)}\longrightarrow0,
$$

pues $|\sin h|\le|h|$ cerca de cero. $\square$

El alcance exacto es éste: los límites de seno y coseno quedan demostrados **a partir de** las identidades trigonométricas y de la medida geométrica previa de sectores. Una construcción independiente de esa medida mediante polígonos inscritos y circunscritos constituiría un desarrollo adicional de geometría. Esta dependencia explícita no debilita las conclusiones analíticas, pero impide describir el lema como demostrado únicamente desde la completitud de $\mathbb R$.

<figure id="fig-edc-c02-01" class="quarto-float-fig">
<img src="/assets/books/elementos-del-calculo/EDC-C02-F01_SECTOR_RADIANES.svg" alt="Sector del círculo unitario entre un radio horizontal y otro de ángulo h. Un triángulo interior, un sector y un triángulo exterior por tangente tienen áreas sen(h)/2, h/2 y tan(h)/2.">
<figcaption>Figura 2.1. Comparación sectorial utilizada en el Lema 2.2. La igualdad área del sector = h/2 es la premisa geométrica previa declarada, no una consecuencia de la futura integral.</figcaption>
</figure>

**Teorema 2.6 (derivadas trigonométricas; `EDC-C02-THM-006`).** Para todo $x\in\mathbb R$,

$$
(\sin x)'=\cos x,
\qquad (\cos x)'=-\sin x.
$$

En cada punto donde $\cos x\ne0$,

$$
(\tan x)'=\frac1{\cos^2x}=1+\tan^2x.
$$

**Demostración.** De las fórmulas de adición,

$$
\frac{\sin(x+h)-\sin x}h
=\sin x\frac{\cos h-1}h+\cos x\frac{\sin h}h.
$$

Por el Lema 2.2, su límite es $\cos x$. Análogamente,

$$
\frac{\cos(x+h)-\cos x}h
=\cos x\frac{\cos h-1}h-\sin x\frac{\sin h}h
\longrightarrow-\sin x.
$$

La fórmula de la tangente sale de la regla del cociente aplicada a $\sin x/\cos x$ en los intervalos donde $\cos x\ne0$. $\square$

Aplicando la regla de la cadena, para $g$ derivable donde corresponda,

$$
(\sin\circ g)'=(\cos\circ g)g',\qquad
(\cos\circ g)'=-(\sin\circ g)g'.
$$

Estas fórmulas **no** son válidas si se reemplazan radianes por grados sin el factor de conversión $\pi/180$.

## 2.9. Funciones trigonométricas inversas

En $(-\pi/2,\pi/2)$ el seno es estrictamente creciente: si $u<v$ allí, la identidad

$$
\sin v-\sin u=2\cos\!\left(\frac{u+v}2\right)
\sin\!\left(\frac{v-u}2\right)>0
$$

lo demuestra geométricamente, sin apelar al Teorema del Valor Medio. En ese intervalo el seno tiene inversa, denominada $\arcsin$, cuyo dominio es $(-1,1)$. Para la rama usual $\arccos:(-1,1)\to(0,\pi)$ se procede del mismo modo con el coseno estrictamente decreciente; la tangente es estrictamente creciente en $(-\pi/2,\pi/2)$ y su imagen es $\mathbb R$.

**Teorema 2.7 (`EDC-C02-THM-007`).** En los dominios abiertos indicados,

$$
\begin{aligned}
(\arcsin x)'&=\frac1{\sqrt{1-x^2}},&&-1<x<1,\\
(\arccos x)'&=-\frac1{\sqrt{1-x^2}},&&-1<x<1,\\
(\arctan x)'&=\frac1{1+x^2},&&x\in\mathbb R.
\end{aligned}
$$

**Demostración.** Al invertir una función trigonométrica, la rama elegida determina qué signo debemos tomar en las identidades del círculo. Si $y=\arcsin x$, entonces $-\pi/2<y<\pi/2$ y $\cos y>0$. La identidad $\cos^2y=1-\sin^2y$ da por tanto $\cos y=\sqrt{1-x^2}$, que no se anula para $-1<x<1$. La regla de la inversa produce $1/\cos(\arcsin x)=1/\sqrt{1-x^2}$.

Para $y=\arccos x$ tenemos $0<y<\pi$, por lo que $\sin y>0$ y $\sin y=\sqrt{1-x^2}$. La derivada de la función que invertimos es $-\sin y$; al tomar su recíproco obtenemos el signo negativo de la segunda fórmula. Finalmente, si $y=\arctan x$, la derivada $(\tan y)'=1+\tan^2y$ es positiva en toda la rama y su recíproco, evaluado en $y=\arctan x$, es $1/(1+x^2)$. En los tres casos quedan comprobadas las condiciones de la regla de la inversa. $\square$

La derivada de $\arcsin x$ se hace ilimitada cuando $x\to1^-$, pero esto no autoriza a afirmar una derivada finita en el extremo $x=1$: allí tampoco existe un entorno bilateral dentro del dominio de su rama cerrada.

## 2.10. Una función derivable cuya derivada no es continua

La continuidad obtenida en C01 se refiere a la **función original**. Al reunir sus derivadas en una nueva función $f'$, queda abierta otra pregunta: cuánto cambia esa pendiente cuando movemos el punto. La función oscilatoria ya conocida permite examinar la diferencia.

Definamos

$$
f(x)=\begin{cases}
x^2\sin(1/x),&x\ne0,\\
0,&x=0.
\end{cases}
$$

El cociente incremental en el origen es $f(h)/h=h\sin(1/h)\to0$, pues $|h\sin(1/h)|\le|h|$. Así $f'(0)=0$. Para $x\ne0$, producto y cadena dan

$$
f'(x)=2x\sin(1/x)-\cos(1/x).
$$

Si tomamos $x_n=1/(2\pi n)$ y $y_n=1/((2n+1)\pi)$, ambos tienden a cero; sin embargo, $f'(x_n)=-1$ y $f'(y_n)=1$. Por tanto, $f'$ no tiene límite en $0$ y no es continua allí. Esta discontinuidad no contradice el teorema de C01: **$f$ sí es continua en $0$**.

El factor $x^2$ basta para que el cociente incremental en el origen tienda a cero, pero al derivar fuera de él aparece una oscilación de amplitud constante. Así podemos tener una aproximación lineal en cada punto sin continuidad de las pendientes al pasar de un punto a otro.

## 2.11. Interpretar fórmulas: dominios, unidades y sensibilidad

En una magnitud física, $f'(x)$ conserva las unidades de $f$ divididas por las de $x$. La regla de la cadena respeta esa estructura. Si $s$ mide metros, $t$ segundos y $s=s(u(t))$, el producto $(ds/du)(du/dt)$ tiene unidades de metros por segundo, siempre que los dominios de las funciones estén correctamente identificados.

Una medida adimensional de sensibilidad es la **elasticidad**: para $x\ne0$ y $f(x)\ne0$ definimos

$$
\mathcal E_f(x)=\frac{x f'(x)}{f(x)}.
$$

Por ejemplo, si $f(x)=x^r$ con $x>0$, la elasticidad vale constantemente $r$. Si $f(x)=a^x$, con $a>0$ y $x\ne0$, vale $x\ln a$. En ambos casos estamos interpretando derivadas **ya demostradas**, no infiriendo una ley dinámica desconocida.

La regla de la cadena puede expresarse con notación de Leibniz, $dy/dx=(dy/du)(du/dx)$, cuando $y=f(u)$, $u=g(x)$ son derivables en los puntos pertinentes. Esa forma refleja la composición de razones de cambio; una cancelación puramente tipográfica de símbolos no sustituye la prueba de §2.3.

## 2.12. Síntesis y frontera del capítulo

Hemos construido una teoría operativa local:

$$
\boxed{\begin{gathered}
\text{derivadas de las funciones componentes}\\
\Downarrow\\
\text{sumas, productos, cocientes y composiciones}\\
\Downarrow\\
\text{derivadas de expresiones nuevas}.
\end{gathered}}
$$

Las reglas permiten construir derivadas a partir de otras conocidas y nos obligan a conservar los dominios de cada operación. La exponencial mostró además cómo podía construirse una función junto con su derivada mediante estimaciones propias; el logaritmo se obtuvo al invertirla, y la geometría circular aportó los límites que necesitaban seno y coseno.

Hemos calculado cómo cambia una función cerca de un punto. Para relacionar esas tasas con el cambio entre dos puntos de un intervalo hará falta otro argumento, el que desarrollaremos en C03 mediante Rolle y el valor medio. La función con derivada discontinua permanece como recordatorio de que las propiedades del nuevo objeto deben examinarse por separado.

### Mapa explícito de dependencias

- **De C00:** estructura de $\mathbb R$, completitud, álgebra de límites, convergencia monótona, continuidad, criterio secuencial y valor intermedio.
- **De C01:** definición de derivada en punto interior, derivabilidad implica continuidad y caracterización por aproximación afín.
- **Aportaciones de C02:** `EDC-C02-THM-001--007`, reglas y construcciones aquí demostradas; medida de ángulo en radianes como herramienta de geometría previa.
- **No utilizado:** Rolle, teorema del valor medio, integración de Riemann, Teorema Fundamental, Taylor ni resultados generales de análisis funcional.
- **Origen historiográfico de las notaciones y de las funciones:** [notas históricas y control de fuentes](capitulo-02-notas.html).

### Trabajo del lector

Los [ejercicios de este capítulo](capitulo-02-ejercicios.html) están organizados por objetivos, desde identificación de dominios y composición hasta demostraciones y contraejemplos. Las [soluciones desarrolladas](capitulo-02-soluciones.html) permanecen separadas de la exposición para preservar el valor del trabajo independiente.
