---
title: Capítulo 10. De las leyes de cambio a las ecuaciones diferenciales
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
source-id: EDC-C10
source-sha256: 46bec6735e22422b5bdf25229961a68d07515fd3dcce067fe816abee29bcf6c0
content-id: MA-BCH-0341
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-10.html) · [Ejercicios](capitulo-10-ejercicios.html) · [Soluciones](capitulo-10-soluciones.html)

[← Capítulo 9](capitulo-09.html) · [Capítulo 11 →](capitulo-11.html)

> **Pregunta generadora.** Si no conocemos una función, pero sabemos cómo debe cambiar en cada instante, ¿podemos reconstruirla? ¿Cuánta información contiene una ley diferencial, qué añade una condición inicial y cuándo esa información determina una sola trayectoria?

Si conocemos la velocidad de un móvil en cada instante y su posición de partida, el Teorema Fundamental del Cálculo de C06 permite reconstruir su posición: acumulamos el desplazamiento producido desde aquel instante. La dificultad cambia cuando la velocidad depende de la posición que estamos buscando. Una población puede crecer más deprisa cuanto mayor sea; un cuerpo puede enfriarse más deprisa cuanto mayor sea su diferencia de temperatura con el ambiente. En esos problemas la tasa ya no es una función del tiempo que podamos integrar antes de conocer la trayectoria.

Una ecuación diferencial expresa esa relación entre una función desconocida y sus derivadas. Para $y'=ky$, por ejemplo, la exponencial ofrece una solución inmediata, aunque la ecuación admite distintas constantes multiplicativas. El dato inicial debe escoger una de ellas, y necesitamos justificar que la elección agota las posibilidades. En C09 hicimos algo semejante al identificar la suma del binomio mediante una relación de derivadas y su valor en cero.

Las herramientas de C00–C09 bastan para resolver varias familias de ecuaciones y comprobar dónde están definidas sus soluciones. Cada familia nos permitirá reconocer un mecanismo: acumulación cuando la tasa está dada, una derivada de producto para las ecuaciones lineales, una función inversa en la separación de variables y una cantidad conservada en la oscilación armónica. También encontraremos una ley que permite distintas trayectorias con el mismo dato inicial. La construcción general por aproximaciones sucesivas de Picard–Lindelöf queda fuera de este volumen.

## 10.1. La incógnita es una función, no un número

**Definición 10.1 (ecuación diferencial ordinaria; `EDC-C10-DEF-001`).** Una *ecuación diferencial ordinaria* (EDO) relaciona una función desconocida $y:I\to\mathbb R$, definida en un intervalo $I\subseteq\mathbb R$, con una o varias derivadas de $y$ respecto de **una** variable independiente. Una ecuación explícita de primer orden tiene la forma

$$
y'(t)=F(t,y(t)),
$$

donde $F:D\to\mathbb R$ está definida en un dominio $D\subseteq\mathbb R^2$. Una *solución clásica* es una función $y\in C^1(I)$ —si $I$ es abierto— cuya gráfica satisface $(t,y(t))\in D$ y la igualdad en cada $t\in I$. Cuando $I$ tiene extremos, se exige continuidad hasta ellos y la igualdad en su interior; una derivada lateral sólo se empleará si se anuncia explícitamente. Para una ecuación de segundo orden exigiremos $y\in C^2(I)$.

**Definición 10.2 (problema de valor inicial; `EDC-C10-DEF-002`).** Un problema de valor inicial (PVI) añade $y(t_0)=y_0$, con $t_0\in I$ y $(t_0,y_0)\in D$. *Existencia* pregunta si hay al menos una solución; *unicidad en una clase y dominio dados* pregunta si dos soluciones con ese dato deben coincidir donde ambas estén definidas. **Intervalo de existencia** designa el intervalo concreto sobre el que se ha verificado la trayectoria. No afirmaremos prolongación más allá de un punto donde la fórmula pierda sentido.

La ecuación $y'=2t$ prescribe una misma tasa a todas sus soluciones en cada instante: las curvas $t^2+C$ sólo difieren en altura. En $y'=-3y$, la pendiente depende del valor de la propia curva; una solución positiva desciende, mientras una negativa asciende. La ecuación $y'=t+y$ combina ambas dependencias. Las tres son de primer orden porque interviene la primera derivada, y en cada una buscamos una función que cumpla la relación a lo largo de todo un intervalo.

Para $y''+\omega^2y=0$ necesitamos considerar además la velocidad inicial: dos móviles que parten de la misma posición pueden hacerlo en direcciones distintas. Esta ecuación es de segundo orden y veremos cómo posición y velocidad determinan una trayectoria. La notación $dy/dt$ conserva la interpretación de tasa de cambio; cuando separemos variables, justificaremos las operaciones mediante la regla de la cadena.

## 10.2. Reconstrucción cuando la tasa es conocida

**Teorema 10.1 (reconstrucción mediante acumulación; `EDC-C10-THM-001`).** Sea $J\subseteq\mathbb R$ un intervalo abierto, $g:J\to\mathbb R$ continua, $t_0\in J$ y $y_0\in\mathbb R$. Existe una **única** solución $y\in C^1(J)$ del PVI

$$
y'=g(t),\qquad y(t_0)=y_0,
$$

y viene dada por

$$
\boxed{y(t)=y_0+\int_{t_0}^{t}g(s)\,ds\qquad(t\in J).}
$$

**Demostración.** La integral propuesta acumula la tasa desde el instante donde conocemos $y_0$. Para cada $t\in J$, el segmento entre $t_0$ y $t$ está contenido en $J$; como $g$ es continua, su integral propia existe por C05, cualquiera que sea la orientación. Al variar el extremo $t$, la primera parte del Teorema Fundamental de C06 da la derivada $g(t)$, que también es continua. En $t=t_0$ la integral vale cero y recuperamos el dato inicial.

Para demostrar unicidad, tomemos otra solución $z$ y comparemos sus valores con los de $y$. Ambas tienen la misma derivada, por lo que $(y-z)'=0$. Dados dos puntos de $J$, el segmento que los une queda dentro de ese intervalo y el teorema del valor medio de C03 muestra que la diferencia tiene el mismo valor en ambos. Es, pues, constante en $J$. Como en $t_0$ las dos soluciones valen $y_0$, esa constante es cero. $\square$

**Proposición 10.1 (forma integral del PVI; `EDC-C10-PRP-001`).** Sea $F:D\to\mathbb R$ continua y $y\in C^1(I)$ con gráfica en $D$, donde $I$ es intervalo. Entonces $y'=F(t,y)$ en el interior **si y sólo si**, para cualquier $t_0,t\in I$,

$$
y(t)=y(t_0)+\int_{t_0}^{t}F(s,y(s))\,ds.
$$

**Demostración.** La función $s\mapsto F(s,y(s))$ es continua porque $y$ lo es y su gráfica permanece en el dominio de $F$. Si $y$ satisface la ecuación diferencial, la regla de Newton–Leibniz de C06 da $y(t)-y(t_0)$ al integrar $y'$, y podemos sustituir ésta por $F(s,y(s))$. El argumento funciona también para $t<t_0$ gracias a la orientación de la integral.

Recíprocamente, fijemos $t_0$ en la identidad integral. El Teorema Fundamental permite derivar respecto del extremo $t$ y obtener $y'(t)=F(t,y(t))$ en el interior. Si el intervalo tiene extremos incluidos, la igualdad integral se extiende hasta ellos por continuidad; sólo hemos usado derivadas en puntos interiores. $\square$

La identidad integral expresa que cada valor de la trayectoria se obtiene del valor inicial y del cambio acumulado sobre ella. Será útil para comparar dos soluciones, porque convierte la diferencia de sus tasas en una integral. Para construir una solución sigue habiendo una dificultad: el integrando contiene la función $y$ que buscamos. La equivalencia anterior permite comprobar una función disponible, pero todavía no ofrece un procedimiento general que la produzca para cualquier $F$.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Reconstruir una curva a partir de sus tangentes"}
*Lectura opcional.*

En el prefacio de su *Analyse des infiniment petits* de 1696, L’Hôpital describe dos recorridos del cálculo. El diferencial desciende desde las magnitudes a sus pequeñas diferencias; el integral remonta desde esas diferencias hacia las magnitudes de las que proceden. Al presentar el segundo, reúne la búsqueda de curvas a partir de tangentes con el cálculo de longitudes, áreas, volúmenes y centros de gravedad.

Esa reunión tiene un interés matemático que todavía podemos reconocer. Cuando conocemos una curva, calculamos la dirección de su tangente mediante la derivada. Cuando se nos da una relación que prescribe esa dirección, la curva pasa a ser la incógnita: debemos reconstruir una trayectoria compatible con la ley. La acumulación resuelve el caso en que la pendiente ya está dada como función de la variable; si depende también de la curva buscada, aparecen las dificultades que estudia este capítulo.

Un punto inicial ayuda a escoger una trayectoria entre las posibles. En las ecuaciones lineales veremos cómo el cálculo permite justificar esa elección; más adelante encontraremos una ley continua que deja abiertas varias trayectorias desde el mismo punto.

**Para seguir leyendo:** [L’Hôpital, *Analyse des infiniment petits* (1696), prefacio, pasaje sobre el cálculo integral](https://www.hist-math.fr/textes/lHopital1696_InfinimentPetits.pdf).
:::

## 10.3. Crecimiento y decaimiento proporcionales

Para la ley $y'=ky$, con $k$ constante, la regla de derivación de la exponencial sugiere $y(t)=Ce^{kt}$. La constante se ajusta fácilmente al dato inicial. Falta averiguar si cualquier solución debe tener esa forma, y para ello conviene buscar una expresión cuyo cambio se anule. Multiplicar por $e^{-kt}$ compensa exactamente el crecimiento impuesto por la ecuación. Con un coeficiente variable, la acumulación de $a(t)$ ocupará el lugar de $kt$.

**Teorema 10.2 (ley proporcional, también variable; `EDC-C10-THM-002`).** Si $a:J\to\mathbb R$ es continua en un intervalo abierto $J$, entonces el PVI $y'=a(t)y$, $y(t_0)=y_0$ tiene una única solución $C^1$ sobre **todo** $J$:

$$
\boxed{y(t)=y_0\exp\left(\int_{t_0}^{t}a(s)\,ds\right).}
$$

**Demostración.** Sea $A(t)=\int_{t_0}^{t}a(s)\,ds$. El Teorema Fundamental proporciona $A'=a$; las reglas de cadena y producto de C02 dan entonces $(y_0e^A)'=ay_0e^A$. La fórmula define una función $C^1$ para cada $t\in J$, pues la integral sobre el segmento entre $t_0$ y $t$ existe. Además $A(t_0)=0$, de modo que la función vale $y_0$ en el instante inicial.

Para cualquier otra solución $z$, consideremos $e^{-A(t)}z(t)$. La derivada de la exponencial introduce el término $-a(t)e^{-A(t)}z(t)$, que cancela el término $e^{-A(t)}z'(t)$ gracias a la ecuación $z'=az$. Obtenemos así $e^{-A}(z'-az)=0$. Por el valor medio de C03, el producto es constante en $J$; evaluado en $t_0$, vale $y_0$. Al multiplicar por $e^{A(t)}$ recuperamos $z=y_0e^A$. El factor exponencial nunca se anula y no hemos dividido por $z$, por lo que el argumento incluye $y_0=0$. $\square$

La exponencial conserva el signo de $y_0$. Para $a=k>0$ hay crecimiento exponencial si $y_0>0$; para $k<0$ hay decaimiento hacia cero al avanzar el tiempo. Si $y_0=0$, la trayectoria sigue siendo idénticamente cero. Cuando $a(t)$ cambia de signo, la función $A(t)$ registra el crecimiento acumulado, no necesariamente monótono.

## 10.4. El factor integrante: un teorema completo de primer orden

En $y'+p(t)y=q(t)$ aparece un aporte externo $q(t)$ además del cambio proporcional a $y$. Si multiplicamos por una función $\mu$, la regla del producto produce $(\mu y)'=\mu y'+\mu' y$. Para que esos términos coincidan con $\mu(y'+py)$, debemos escoger $\mu'=p\mu$. Acabamos de resolver esa ecuación: la exponencial de una primitiva de $p$ da el factor que necesitamos. Su elección transforma la ecuación original en una acumulación con tasa conocida.

**Teorema 10.3 (EDO lineal inhomogénea; `EDC-C10-THM-003`).** Sean $p,q:J\to\mathbb R$ continuas, $J$ intervalo abierto y $(t_0,y_0)\in J\times\mathbb R$. Definamos

$$
P(t)=\int_{t_0}^{t}p(s)\,ds,\qquad \mu(t)=e^{P(t)}>0.
$$

Entonces existe una **única** solución $C^1$ sobre $J$ del PVI $y'+py=q$, $y(t_0)=y_0$, dada por

$$
\boxed{y(t)=e^{-P(t)}\left(y_0+\int_{t_0}^{t}e^{P(s)}q(s)\,ds\right).}
$$

**Demostración.** El Teorema Fundamental da $P'=p$, y la regla de la cadena, $\mu'=p\mu$. Para cualquier solución, $(\mu y)'=\mu(y'+py)=\mu q$. La función desconocida ha desaparecido del lado derecho: podemos integrar desde $t_0$, donde $\mu(t_0)=1$, y obtener $\mu(t)y(t)=y_0+\int_{t_0}^t\mu(s)q(s)\,ds$. Como $\mu$ es positiva, esta identidad obliga a $y$ a tener la forma anunciada. Con ello queda probada la unicidad si existe una solución.

La misma fórmula permite construirla. La continuidad de $p$ y $q$ asegura que $P$ y la nueva acumulación están definidas en todo $J$ y son $C^1$. Multiplicar la función propuesta por $\mu$ devuelve la identidad integral anterior; al derivarla obtenemos $\mu(y'+py)=\mu q$. Dividimos por $\mu>0$ y recuperamos la ecuación. En $t_0$, la integral se anula y la fórmula da $y_0$. Así quedan verificadas tanto la existencia sobre $J$ como la unicidad. $\square$

**Corolario 10.1 (variación de la constante; `EDC-C10-COR-001`).** Con $p,q$ continuas, toda solución sobre un intervalo $J$ de $y'+py=q$ se obtiene sumando una solución particular $y_p$ y una solución $Ce^{-P(t)}$ de la homogénea; $C\in\mathbb R$.

**Demostración.** La diferencia de dos soluciones satisface $z'+pz=0$ y el Teorema 10.2 da $z=Ce^{-P}$. Inversamente, por linealidad de la derivada $y_p+z$ satisface la ecuación. $\square$

**Ejemplo.** Si $y'+2y=3$, $y(0)=1$, entonces $P(t)=2t$ y

$$
y(t)=e^{-2t}\left(1+3\int_0^t e^{2s}ds\right)=\frac32-\frac12e^{-2t}.
$$

En este ejemplo la fuente constante lleva la solución hacia $3/2$, el valor donde $2y$ compensa el aporte $3$. La fórmula está definida en toda la recta y al derivarla se comprueba $y'+2y=3$. Dentro de la integral el factor $e^{P(s)}$ depende del instante que recorremos, mientras el factor exterior $e^{-P(t)}$ depende del extremo final; debemos completar la integración antes de combinar sus valores como en este cálculo.

## 10.5. La importancia del dato inicial y de la estabilidad

La condición inicial selecciona una curva de la familia de soluciones lineales. Si ese dato procede de una medición, conocer la fórmula también permite estudiar cómo se transmite su incertidumbre. Podemos comparar dos trayectorias con datos iniciales próximos e incluso con fuentes ligeramente distintas: su diferencia satisface otra ecuación lineal, y el factor integrante nos da una cota para esa diferencia a lo largo de un intervalo de tiempo.

**Teorema 10.4 (dependencia cuantitativa de datos y fuentes; `EDC-C10-THM-004`).** Sea $p$ continua en un intervalo $[t_0,T]$, $T>t_0$, y $|p(t)|\le P_*$ allí. Sean $y_1,y_2$ las soluciones de

$$
y_i'+py_i=q_i,\qquad y_i(t_0)=a_i\quad(i=1,2),
$$

con $q_1,q_2$ continuas y $|q_1(t)-q_2(t)|\le\eta$. Entonces, para $t_0\le t\le T$,

$$
\boxed{|y_1(t)-y_2(t)|\le e^{P_*(t-t_0)}\bigl(|a_1-a_2|+\eta(t-t_0)\bigr).}
$$

**Demostración.** La diferencia $w=y_1-y_2$ satisface $w'+pw=q_1-q_2$ y empieza con el valor $a_1-a_2$. La fórmula del factor integrante separa la contribución de ese dato de la contribución acumulada de la fuente: $w(t)=e^{-P(t)}(a_1-a_2)+\int_{t_0}^t e^{-P(t)}e^{P(s)}(q_1(s)-q_2(s))\,ds$. En el intervalo cerrado, esta identidad se obtiene directamente al integrar la derivada de $e^P w$, con la misma prueba del Teorema 10.3. Para cada instante $s$ entre $t_0$ y $t$, el factor que transporta la fuente hasta $t$ cumple

$$
|e^{-P(t)}e^{P(s)}|=\exp\left(-\int_s^t p(u)du\right)\le e^{P_*(t-s)}\le e^{P_*(t-t_0)}.
$$

El dato inicial se transporta mediante $e^{-P(t)}$, cuyo módulo también es a lo sumo $e^{P_*(t-t_0)}$. Al tomar módulos en la identidad de $w$, su primera contribución queda acotada por ese factor multiplicado por $|a_1-a_2|$. Para la integral, acotamos $|q_1-q_2|$ por $\eta$ y el factor de transporte por la misma constante, válida para todos los $s$ del segmento. La integral de esa cota es $e^{P_*(t-t_0)}\eta(t-t_0)$. Al reunir ambas contribuciones obtenemos el enunciado. $\square$

La cota muestra cuánto pueden separarse las soluciones de esta clase cuando cambian los datos y las fuentes. Aunque puede ser poco ajustada, basta para concluir que esas diferencias se hacen pequeñas al hacer pequeños $|a_1-a_2|$ y $\eta$ en un intervalo temporal fijo. Si ambas son cero, las trayectorias coinciden. La incertidumbre de un modelo físico requiere además examinar si la propia ley representa el fenómeno; aquí hemos medido la sensibilidad de las soluciones de la ecuación aceptada.

## 10.6. Separar variables sin dividir por cero

En $y'=a(t)b(y)$, la dependencia del tiempo y la del valor de la función aparecen en factores separados. Sobre una rama donde $b$ no se anula, podemos buscar una función $B$ tal que la derivada de $B(y(t))$ sea $a(t)$. La cadena muestra qué necesitamos: $B'(y)y'=B'(y)a(t)b(y)$, de modo que conviene tomar $B'=1/b$. Una vez integrada $a$, quedará la relación $B(y(t))=A(t)$, y para recuperar $y$ tendremos que invertir $B$. Esta construcción da sentido a la escritura abreviada $dy/b(y)=a(t)dt$ y permite ver dónde puede dejar de funcionar.

**Teorema 10.5 (construcción por separación; `EDC-C10-THM-005`).** Sean $a:J\to\mathbb R$ continua, $J$ intervalo abierto; $b:K\to\mathbb R$ continua sobre un intervalo abierto $K$ y sin ceros en $K$. Fijemos $t_0\in J$ y $y_0\in K$. Definamos

$$
A(t)=\int_{t_0}^{t}a(s)ds,\qquad B(u)=\int_{y_0}^{u}\frac{dv}{b(v)}\quad(u\in K).
$$

Entonces $B'(u)=1/b(u)$, por lo que $B$ es estrictamente monótona, con inversa $B^{-1}$ definida en el intervalo abierto $B(K)$. En el intervalo abierto

$$
J_*=\{t\in J:A(t)\in B(K)\}\quad\text{(componente que contiene a $t_0$)},
$$

la función $y(t)=B^{-1}(A(t))$ es una solución $C^1$ del PVI $y'=a(t)b(y)$, $y(t_0)=y_0$; **es la única solución cuya imagen permanece en $K$** sobre cualquier subintervalo común conectado que contenga $t_0$.

**Demostración.** La continuidad de $1/b$ permite aplicar el Teorema Fundamental y obtener $B'=1/b$. El signo de $b$ es constante en $K$: si tuviese valores de signos distintos, el valor intermedio de C00 obligaría a un cero entre ellos. Por tanto $B'$ tiene un signo fijo y nunca se anula; el valor medio de C03 hace a $B$ estrictamente monótona. Su imagen es un intervalo por continuidad, y es abierto porque cada punto de $K$ tiene puntos de $K$ a ambos lados cuyos valores de $B$ lo encierran estrictamente. Así $B$ posee una inversa en el intervalo abierto $B(K)$.

La regla de la inversa de C02 da $(B^{-1})'(v)=b(B^{-1}(v))$, una derivada continua. Como $A$ es continua, los tiempos con $A(t)\in B(K)$ forman un conjunto abierto; contiene a $t_0$ porque $A(t_0)=B(y_0)=0$. Su componente que contiene a $t_0$ es un intervalo abierto, y en él podemos componer $B^{-1}$ con $A$. La cadena da $y'=b(y)A'=a(t)b(y)$ y el valor en $t_0$ es $B^{-1}(0)=y_0$.

Para cualquier otra solución $z$ que permanezca en $K$, $b(z)$ nunca es cero. Podemos entonces calcular $(B\circ z)'=z'/b(z)=a(t)=A'(t)$. En el subintervalo común conectado, el valor medio hace constante a $B(z(t))-A(t)$, y el dato inicial fija esa constante en cero. La inyectividad de $B$ da $z(t)=B^{-1}(A(t))=y(t)$. La división por $b(z)$ se ha usado dentro de la rama donde está definida. $\square$

**Definición 10.3 (equilibrio; `EDC-C10-DEF-003`).** Para una EDO autónoma $y'=b(y)$, un *equilibrio* es una constante $c$ con $b(c)=0$; $y(t)\equiv c$ es entonces una solución. En la ecuación $y'=a(t)b(y)$ cualquier cero de $b$ también origina una solución constante, aunque $a$ dependa del tiempo.

**Proposición 10.2 (ramas y equilibrios; `EDC-C10-PRP-002`).** La división por $b(y)$ en el Teorema 10.5 **no descubre** las soluciones de equilibrio; éstas deben añadirse separadamente. Si la trayectoria queda en una rama $K$ sin ceros, no puede atravesar uno de esos ceros mientras permanezca en la clase de funciones obtenidas mediante $B^{-1}$.

**Demostración.** Para $b(c)=0$, la función constante satisface $y'=a(t)b(y)=0$. La fórmula $B$ no está definida a través de $c$ como integral de $1/b$, y la expresión $B^{-1}(A(t))$ siempre toma valores en $K$, donde $b$ no se anula. $\square$

Al dividir por $b(y)$ hemos excluido los ceros de $b$ y debemos volver a la ecuación original para encontrar sus soluciones constantes. Queda por decidir si una solución que parte de un equilibrio podría abandonarlo más tarde. La unicidad impediría esa salida, porque la trayectoria constante ya satisface el mismo dato; para campos meramente continuos, veremos que esa prohibición puede fallar.

## 10.7. Unicidad bajo regularidad y su fracaso sin ella

**Lema 10.1 (comparación exponencial elemental; `EDC-C10-LEM-001`).** Sea $u:[a,b]\to[0,\infty)$ de clase $C^1$, $u(a)=0$ y $u'(t)\le L u(t)$ para $L\ge0$. Entonces $u\equiv0$.

**Demostración.** La desigualdad $u'\le Lu$ limita el crecimiento de $u$ en proporción a su propio tamaño. Para compararlo con ese crecimiento exponencial, consideremos $v(t)=e^{-L(t-a)}u(t)$. La regla del producto da $v'=e^{-L(t-a)}(u'-Lu)\le0$, de modo que $v$ es no creciente por C03. Pero empieza en cero y es no negativa porque ambos factores lo son. Así $0\le v(t)\le v(a)=0$ para todo $t\in[a,b]$. La positividad de la exponencial obliga a $u(t)=0$. $\square$

**Teorema 10.6 (unicidad para soluciones existentes; `EDC-C10-THM-006`).** Sea $F$ continua en un rectángulo $D=[a,b]\times[c,d]$ y supongamos que existe $L\ge0$ tal que

$$
|F(t,u)-F(t,v)|\le L|u-v|
\qquad(t\in[a,b],\ u,v\in[c,d]).
$$

Si $y,z\in C^1([a,b])$ son **dos soluciones ya existentes** de $w'=F(t,w)$ cuyas imágenes están en $[c,d]$ y $y(t_0)=z(t_0)$ para algún $t_0\in[a,b]$, entonces $y=z$ en $[a,b]$.

**Demostración.** Queremos comprobar que una diferencia inicialmente nula no puede crecer bajo la cota del enunciado. La forma integral de la Proposición 10.1 expresa la diferencia de valores como la integral de $F(s,y(s))-F(s,z(s))$, porque los datos iniciales se cancelan. Para $t\ge t_0$, la desigualdad triangular y la hipótesis dan

$$
|y(t)-z(t)|\le L\int_{t_0}^{t}|y(s)-z(s)|ds.
$$

El valor absoluto de la diferencia es continuo, pero puede no ser derivable donde la diferencia se anula. Su acumulación $u(t)=\int_{t_0}^{t}|y(s)-z(s)|ds$ sí es $C^1$ por el Teorema Fundamental. Además $u(t_0)=0$, $u\ge0$ y la desigualdad anterior se convierte en $u'(t)\le Lu(t)$. El Lema 10.1 obliga a $u=0$, y como $u'=|y-z|$, las trayectorias coinciden a la derecha de $t_0$.

Para recorrer el intervalo hacia la izquierda, pongamos $Y(s)=y(t_0-s)$ y $Z(s)=z(t_0-s)$, con $0\le s\le t_0-a$. Sus derivadas son $Y'(s)=-F(t_0-s,Y(s))$ y $Z'(s)=-F(t_0-s,Z(s))$. El campo con tiempo invertido conserva la misma cota Lipschitz, pues el signo menos desaparece al tomar módulos. Las dos funciones empiezan con el mismo valor en $s=0$, de modo que el argumento de acumulación recién probado también las identifica. Esto da $y=z$ a la izquierda. Si uno de los tramos tiene longitud cero, sólo contiene el punto donde la igualdad ya está dada. $\square$

**Proposición 10.3 (campo continuo sin unicidad; `EDC-C10-PRP-003`).** El PVI $y'=\sqrt{|y|}$, $y(0)=0$ posee infinitas soluciones $C^1$ sobre $\mathbb R$.

**Demostración.** Para cada $c\ge0$ definamos

$$
y_c(t)=\begin{cases}0,&t\le c,\\(t-c)^2/4,&t>c.\end{cases}
$$

En $t=c$, ambas expresiones para la función valen cero. Su cociente incremental por la izquierda es cero y por la derecha vale $h/4$ para $h>0$, de modo que la derivada existe y vale cero. Fuera de ese punto, la derivada es cero a la izquierda y $(t-c)/2$ a la derecha; estos valores también se unen continuamente. Por tanto $y_c\in C^1(\mathbb R)$.

Para $t>c$, la raíz positiva de $(t-c)^2/4$ es $(t-c)/2$, que coincide con $y_c'(t)$; para $t\le c$ ambos miembros de la ecuación son cero. Como $c\ge0$, todas las funciones cumplen $y_c(0)=0$. Si $c_1<c_2$, un tiempo entre ambas partidas da un valor positivo para $y_{c_1}$ y cero para $y_{c_2}$, por lo que las trayectorias son distintas. También la función idénticamente nula satisface el PVI.

El campo continuo $F(y)=\sqrt{|y|}$ permite así que una trayectoria permanezca en el equilibrio durante un tiempo y luego lo abandone. La hipótesis del teorema de unicidad falla precisamente cerca de ese equilibrio: para $h>0$, el cociente $|F(h)-F(0)|/|h-0|$ es $1/\sqrt h$ y crece sin límite cuando $h\downarrow0$. Ninguna constante Lipschitz puede acotarlo en un entorno de cero. $\square$

Una ley y un dato inicial pueden admitir más de una evolución aun cuando el campo sea continuo. La desigualdad Lipschitz del Teorema 10.6 excluye esta separación de soluciones; su prueba compara trayectorias que ya existen y deja pendiente la pregunta general por su construcción.

## 10.8. Crecimiento logístico: el límite de una ley proporcional

Supongamos que la tasa de una población idealizada crece proporcionalmente a su tamaño, pero disminuye cuando éste se acerca a una capacidad $K>0$. El modelo elegido es

$$
y'=r y\left(1-\frac{y}{K}\right),\qquad r>0.
$$

Para valores positivos muy pequeños respecto de $K$, el factor $1-y/K$ está cerca de uno y la tasa se aproxima a $ry$. Cuando $y$ se acerca a $K$, ese factor reduce el crecimiento; si $y>K$, cambia de signo y la población del modelo disminuye. Los parámetros y el intervalo temporal deben justificarse con observaciones para una aplicación biológica. Aquí podemos estudiar qué trayectorias produce la ley una vez fijados $r$ y $K$.

**Teorema 10.7 (PVI logístico con dato positivo; `EDC-C10-THM-007`).** Para $r,K>0$, $t_0\in\mathbb R$ y $y_0>0$, el PVI anterior tiene sobre todo el semieje $t\ge t_0$ la solución

$$
\boxed{y(t)=\frac{K}{1+A e^{-r(t-t_0)}},\qquad A=\frac{K}{y_0}-1.}
$$

Es positiva, única entre las soluciones que permanecen acotadas en cada intervalo temporal compacto de existencia común, y satisface $\lim_{t\to\infty}y(t)=K$. Si $0<y_0<K$ es creciente; si $y_0>K$ es decreciente; si $y_0=K$, es constante.

**Demostración.** La forma de la candidata puede entenderse mediante la variable auxiliar $z=K/y-1$ en una rama positiva. Al derivar y sustituir la ley logística, obtenemos $z'=-Ky'/y^2=-r(K/y-1)=-rz$. La ecuación proporcional sugiere $z(t)=A e^{-r(t-t_0)}$, donde $A=K/y_0-1$, y al despejar $y$ aparece la fórmula anunciada. Este cálculo orienta la elección; verificaremos directamente la candidata y probaremos su unicidad sin suponer de antemano que toda solución permanezca positiva.

De $y_0>0$ resulta $A>-1$. Para $t\ge t_0$, el factor exponencial está en $(0,1]$. Si $A\ge0$, el denominador es al menos uno; si $-1<A<0$, es al menos $1+A>0$. La fórmula está, pues, definida y es positiva en todo el semieje. La derivación da

$$
y'(t)=\frac{KrA e^{-r(t-t_0)}}{(1+A e^{-r(t-t_0)})^2}
=r y(t)\left(1-\frac{y(t)}K\right),
$$

y en $t=t_0$ vale $K/(1+A)=y_0$. Para comparar esta solución con cualquier otra del mismo PVI, fijemos un intervalo temporal compacto del dominio común que contenga a $t_0$. La continuidad de ambas trayectorias permite encerrarlas en una banda acotada $[c,d]$. En ella, el campo polinómico cumple

$$
|F(u)-F(v)|=r|u-v|\left|1-\frac{u+v}{K}\right|\le L|u-v|
$$

con una constante finita $L$: si $|u|,|v|\le M$, podemos tomar $L=r(1+2M/K)$. El Teorema 10.6 identifica las dos soluciones en ese compacto. Como podemos llevar el extremo del compacto hasta cualquier tiempo del intervalo común, queda probada la unicidad allí.

Cuando $t\to\infty$, el factor exponencial tiende a cero y el denominador a uno, de modo que $y(t)\to K$. El signo de $y'$ en la fórmula es el de $A$. Éste es positivo para $y_0<K$, negativo para $y_0>K$ y cero para $y_0=K$, lo que da las tres posibilidades de monotonía. $\square$

**Corolario 10.2 (equilibrios y dominio; `EDC-C10-COR-002`).** $y\equiv0$ y $y\equiv K$ son equilibrios logísticos. Si $y_0<0$, la misma fórmula algebraica se anula en el denominador en un tiempo futuro finito; por consiguiente no describe una solución global sobre $[t_0,\infty)$.

**Demostración.** Los valores constantes anulan el campo. Para $y_0<0$, $A=K/y_0-1<-1$ y $1+A e^{-r(t-t_0)}=0$ cuando $t=t_0+(\ln(-A))/r>t_0$. En el intervalo desde $t_0$ hasta ese tiempo sin incluirlo la fórmula satisface la EDO; no puede prolongarse por ella a través del denominador nulo. $\square$

Los parámetros $r$ y $K$ no son conclusiones matemáticas extraídas de un censo: son hipótesis de un modelo que debe verificarse por otros medios. La curva logística está asociada a los estudios poblacionales decimonónicos de Verhulst.

<figure id="fig-edc-c10-01" class="quarto-float-fig">
<img src="/assets/books/elementos-del-calculo/EDC-C10-F01_TRAYECTORIAS_LOGISTICAS.svg" alt="Dos soluciones logísticas positivas con K=1,2: una crece desde y0=0,23 y otra decrece desde y0=1,85 hacia la recta de equilibrio y=K.">
<figcaption>Figura 10.1. Las dos ramas muestran el papel del dato inicial en el modelo idealizado; la unicidad se obtiene de las hipótesis demostradas, no del gráfico.</figcaption>
</figure>

## 10.9. Enfriamiento: una diferencia que disminuye

**Teorema 10.8 (enfriamiento lineal idealizado; `EDC-C10-THM-008`).** Sean $k>0$, $T_a\in\mathbb R$ constantes, $t_0\in\mathbb R$ y $T_0\in\mathbb R$. El PVI

$$
T'(t)=-k(T(t)-T_a),\qquad T(t_0)=T_0,
$$

tiene una única solución sobre $\mathbb R$:

$$
\boxed{T(t)=T_a+(T_0-T_a)e^{-k(t-t_0)}.}
$$

Para $t\ge t_0$, la diferencia respecto del ambiente conserva su signo y tiende a cero.

**Demostración.** La cantidad cuya tasa es proporcional a ella misma es la diferencia con el ambiente. Pongamos $u=T-T_a$. Como $T_a$ es constante, $u'=T'$ y la ecuación se convierte en $u'=-ku$, con $u(t_0)=T_0-T_a$. El Teorema 10.2 construye una única solución en toda la recta; al sumar $T_a$ recuperamos la temperatura anunciada. Para $t\ge t_0$, la exponencial es positiva y tiende a cero, de modo que la diferencia conserva el signo de su valor inicial y su módulo disminuye hacia cero. Si esa diferencia inicial es cero, la temperatura permanece en equilibrio con el ambiente. $\square$

**Proposición 10.4 (ambiente variable; `EDC-C10-PRP-004`).** Si $T_a(t)$ es continua, el PVI $T'=-k(T-T_a(t))$, $T(t_0)=T_0$ tiene la solución única

$$
T(t)=e^{-k(t-t_0)}\left(T_0+k\int_{t_0}^{t}e^{k(s-t_0)}T_a(s)ds\right).
$$

**Demostración.** Cuando el ambiente varía, restarlo ya no produce la ecuación homogénea anterior: su derivada introduciría un nuevo término, y sólo hemos supuesto continuidad de $T_a$. Podemos mantener como incógnita la temperatura $T$ y escribir $T'+kT=kT_a(t)$. El Teorema 10.3 se aplica con $p=k$, $q=kT_a$ y $P(t)=k(t-t_0)$, y proporciona exactamente la fórmula del enunciado. La fuente es continua en el intervalo donde lo sea $T_a$, que es el intervalo de existencia y unicidad obtenido. $\square$

Un coeficiente $k$ expresado en unidades de tiempo inverso permite que $k(t-t_0)$ sea adimensional. La ley no afirma que cualquier proceso real de transferencia de calor siga exactamente esta relación para diferencias arbitrariamente grandes ni que el ambiente permanezca constante: tales condiciones son parte del **modelo**, no de la demostración.

## 10.10. Fuerza resistiva y velocidad terminal

Consideremos el movimiento vertical hacia abajo de un cuerpo de masa $m>0$ sometido a gravedad idealizada $mg$ y resistencia lineal $-\gamma v$, con $g,\gamma>0$. El modelo escalar de Newton para la velocidad es

$$
mv'=mg-\gamma v.
$$

**Teorema 10.9 (aproximación a la velocidad terminal; `EDC-C10-THM-009`).** Para $m,g,\gamma>0$ y $v(t_0)=v_0$, la ecuación anterior tiene una única solución en toda la recta,

$$
\boxed{v(t)=v_\infty+(v_0-v_\infty)e^{-(\gamma/m)(t-t_0)},\qquad v_\infty=\frac{mg}{\gamma}.}
$$

Para $t\ge t_0$, $v(t)\to v_\infty$, conservando el signo de $v-v_\infty$.

**Demostración.** Dividiendo por la constante no nula $m$, la ecuación es $v'+(\gamma/m)v=g$. La función constante $v_\infty$ es una solución particular pues $(\gamma/m)v_\infty=g$. Su diferencia $w=v-v_\infty$ satisface $w'=-(\gamma/m)w$. El Teorema 10.2 proporciona la solución y su unicidad, mientras la exponencial decreciente prueba el límite. $\square$

En $v=v_\infty$, la resistencia $\gamma v$ iguala el peso $mg$ y la aceleración del modelo es cero. Si la velocidad inicial es menor, el peso domina y la velocidad aumenta; si es mayor, domina la resistencia y disminuye. La fórmula muestra que esa diferencia se reduce exponencialmente sin cambiar de signo. Con $m$ en kilogramos, $v$ en metros por segundo y $\gamma$ en kilogramos por segundo, $mg/\gamma$ tiene unidades de velocidad. Una resistencia cuadrática conduciría a otra ecuación y requeriría estudiar de nuevo sus soluciones.

## 10.11. Oscilación armónica y aproximación de una trayectoria

El cálculo de una variable permite también un ejemplo cerrado de **segundo orden** sin invocar un teorema general de existencia. Una fuerza restitutiva proporcional al desplazamiento da $x''+\omega^2x=0$, con $\omega>0$ constante.

**Teorema 10.10 (oscilador armónico; `EDC-C10-THM-010`).** Dados $\omega>0$, $t_0\in\mathbb R$, $x_0,v_0\in\mathbb R$, existe una única solución $C^2$ sobre $\mathbb R$ del PVI

$$
x''+\omega^2x=0,\qquad x(t_0)=x_0,\quad x'(t_0)=v_0,
$$

y es

$$
\boxed{x(t)=x_0\cos(\omega(t-t_0))+\frac{v_0}{\omega}\sin(\omega(t-t_0)).}
$$

**Demostración.** Derivando la fórmula con las reglas de C02, su derivada es $-\omega x_0\sin(\omega(t-t_0))+v_0\cos(\omega(t-t_0))$; una segunda derivación da $x''=-\omega^2x$. En $t=t_0$, el seno se anula y el coseno vale uno, de modo que se obtienen los dos datos $x_0$ y $v_0$.

Para demostrar unicidad, restemos dos soluciones: $w=x_1-x_2$ satisface la misma ecuación homogénea y tiene $w(t_0)=w'(t_0)=0$. Necesitamos controlar a la vez posición y velocidad; por ello consideramos la suma de sus cuadrados con el peso que introduce la ecuación,

$$
E(t)=(w'(t))^2+\omega^2(w(t))^2\ge0
$$

cuya derivada es $E'=2w'(w''+\omega^2w)=0$. El peso $\omega^2$ hace que los dos términos se cancelen al usar la ecuación de $w$. Por el valor medio, $E$ es constante en la recta, y los dos datos nulos hacen que esa constante sea cero. Sus sumandos son no negativos y $\omega>0$, de modo que $w(t)=w'(t)=0$ en todo instante. Las dos soluciones coinciden. $\square$

**Lema 10.2 (un paso de Euler y su error local; `EDC-C10-LEM-002`).** Si $y\in C^2([t,t+h])$, $h>0$, es una solución de $y'=F(s,y(s))$ y $|y''(s)|\le M$ en el intervalo, entonces

$$
\boxed{|y(t+h)-[y(t)+hF(t,y(t))]|\le\frac12Mh^2.}
$$

**Demostración.** Taylor–Lagrange de orden uno (C09) da $y(t+h)=y(t)+hy'(t)+\tfrac12h^2y''(\xi)$ para un $\xi\in(t,t+h)$. Sustituimos la ley diferencial y tomamos valores absolutos. $\square$

La expresión $y_{j+1}=y_j+hF(t_j,y_j)$ se denomina *paso explícito de Euler*: prolonga durante un tiempo $h$ la pendiente calculada en el punto de partida. Si ese punto pertenece exactamente a la solución, el lema mide cuánto se aparta el segmento de tangente del siguiente valor de la curva. Su cota es proporcional a $h^2$, porque el primer término que omitimos es de segundo orden.

Tras un paso, el punto calculado puede estar fuera de la trayectoria exacta. En el siguiente paso evaluaremos $F$ en ese nuevo punto, por lo que al error de aproximación local se añade la propagación de la diferencia ya adquirida. Una cota global para muchos pasos requiere controlar ambos efectos mediante hipótesis y estimaciones suplementarias.

## 10.12. Del problema inverso de tangentes a la teoría de las trayectorias

El problema inverso de tangentes reúne geométricamente lo que hemos estudiado: una ley prescribe la pendiente que debe tener una curva, y un punto inicial debe ayudarnos a reconstruirla. Los trabajos de Newton, Leibniz, los Bernoulli y Euler enlazaron estas preguntas con la mecánica y el cálculo.

La elección de una curva resulta tan importante como el cálculo que permite escribirla. Para las ecuaciones lineales, el factor integrante mostró que cualquier solución está obligada a satisfacer una misma fórmula una vez fijado el dato. En la separación de variables hubo que escoger una rama donde existiese la inversa. La raíz cuadrada permitió tiempos de espera distintos en un equilibrio, mientras la logística mostró que una fórmula puede divergir en tiempo finito para ciertos datos. Estos ejemplos dan contenido preciso a las preguntas por existencia, unicidad e intervalo de definición.

El oscilador añadió otra forma de comparar trayectorias: una cantidad conservada anuló la diferencia entre dos soluciones con los mismos datos. El paso de Euler volvió a la aproximación por tangentes, esta vez con una cota de Taylor para el error. En C11 retomaremos el alcance de estas herramientas dentro de la teoría del cálculo y las cuestiones que quedan abiertas al salir de las clases que hemos podido demostrar.

### Mapa de dependencias y frontera

- **C00:** continuidad, intervalos, valor intermedio, límites y teoremas de convergencia elementales.
- **C01–C03:** definición de derivada, producto, cadena, inversa, valor medio y monotonía.
- **C05–C07:** integral propia, Teorema Fundamental, primitiva e integración orientada.
- **C08–C09:** series sólo como funciones ya construidas, Taylor–Lagrange para la estimación del paso de Euler; no se importan resultados de EDO futura.
- **Resultados originales de C10:** `EDC-C10-THM-001--010`, `LEM-001--002`, `PRP-001--004`, `DEF-001--003`, `COR-001--002`.
- **Fuera del alcance:** teorema general de existencia de Peano, Picard–Lindelöf como teorema demostrado, problemas de frontera de orden alto, sistemas y EDP, teoría de control, estabilidad no lineal global y análisis funcional.

Los [treinta ejercicios](capitulo-10-ejercicios.html) desarrollan el diagnóstico de hipótesis, la construcción explícita de trayectorias, la unicidad, los equilibrios, los modelos y el error de aproximación. Las [soluciones](capitulo-10-soluciones.html) se presentan de forma separada, cada una con su identificador propio y comprobación por sustitución cuando corresponde.
