## 22.1. La función integral acumulada {#sec-ta-22-1}

### Definición 22.1.1 — Función integral acumulada
Sea $f:[a,b]\to\mathbb R$ **integrable**. Por el corolario Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado, para cada $x\in[a,b]$ su restricción tipada

$$
f_x:=f\upharpoonright[a,x]:[a,x]\longrightarrow\mathbb R
$$

es integrable. Si $x=a$, la integral de $f_a$ existe por la convención de intervalo degenerado Definición §21.6.5 — Integración en un intervalo degenerado y vale cero. Si $a<x\le b$, su integral existe en el sentido de Definición §21.4.3 — Integral de Riemann–Darboux para funciones integrables. Definimos la **función integral acumulada de $f$ con origen $a$** como

$$
\boxed{F_{f,a}:[a,b]\longrightarrow\mathbb R,\qquad
F_{f,a}(x):=\int_a^x f_x.}
\tag{22.1.1}
$$

La fórmula define efectivamente una función: por lo anterior, para cada $x$ existe exactamente un real $z=\int_a^x f_x$. Por Separación en el conjunto ya existente $[a,b]\times\mathbb R$ se obtiene el grafo

$$
G_{F_{f,a}}:=\{\langle x,z\rangle\in[a,b]\times\mathbb R:
 z=\int_a^x (f\upharpoonright[a,x])\}.
\tag{22.1.2}
$$

El predicado de (22.1.2) comprende por casos la definición de §21.4 para $x>a$ y la de §21.6 para $x=a$; en ningún caso apela a una integral indefinida ni a una orientación no definida. La existencia y unicidad de $z$ hacen del grafo una función de dominio exacto $[a,b]$ y codominio $\mathbb R$; no se elige simultáneamente una familia de integrales.

### Proposición 22.1.2 — Valores extremos e identidad exacta de los incrementos
Sea $F_{f,a}$ la función anterior. Se cumplen

$$
\boxed{F_{f,a}(a)=0_{\mathbb R},\qquad
F_{f,a}(b)=\int_a^b f.}
\tag{22.1.3}
$$

Para cualesquiera $a\le x\le y\le b$, la restricción $f\upharpoonright[x,y]$ es integrable y

$$
\boxed{F_{f,a}(y)-F_{f,a}(x)
=\int_x^y\bigl(f\upharpoonright[x,y]\bigr).}
\tag{22.1.4}
$$

**Demostración.**
En $x=a$, la definición (22.1.1) y Definición §21.6.5 — Integración en un intervalo degenerado dan la primera igualdad de (22.1.3). Para $x=b$, la restricción $f\upharpoonright[a,b]$ coincide con $f$ por igualdad de dominio, codominio y grafo (Proposición §1.3.2 — Existencia y unicidad de la restricción), de donde se deduce la segunda.

Fijemos ahora $a\le x\le y\le b$. La restricción $f_y:=f\upharpoonright[a,y]$ es integrable, incluso cuando $y=a$. Aplicamos Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado a $f_y$ con el punto de corte $x$. El resultado garantiza la integrabilidad de sus dos restricciones y la identidad

$$
\int_a^y f_y
=\int_a^x(f_y\upharpoonright[a,x])
 +\int_x^y(f_y\upharpoonright[x,y]).
$$

Las restricciones sucesivas son, como **funciones tipadas**, respectivamente $f\upharpoonright[a,x]$ y $f\upharpoonright[x,y]$: tienen iguales dominios, codominio real y grafos. Las dos primeras integrales son entonces $F_{f,a}(y)$ y $F_{f,a}(x)$. Restarlas en el cuerpo real da (22.1.4). Si $x=y$, el último término es cero por §21.6; no se divide por $y-x$ ni se utiliza una partición estricta de un singleton. $\square$

**Lectura.** El cambio de la acumulación entre dos extremos ordenados es la integral sobre el tramo que los separa. La igualdad es anterior a cualquier afirmación acerca de la derivada y no necesita continuidad de $f$.

### Proposición 22.1.3 — Encierro del incremento y de su cociente medio
Sean $a\le x<y\le b$ y sean $m,M\in\mathbb R$ tales que

$$
m\le f(t)\le M\qquad(t\in[x,y]).
$$

Entonces

$$
\boxed{m(y-x)\le F_{f,a}(y)-F_{f,a}(x)\le M(y-x).}
\tag{22.1.5}
$$

En particular, los extremos locales existen y se obtiene

$$
\boxed{
\inf fx,y\ \le\
\frac{F_{f,a}(y)-F_{f,a}(x)}{y-x}
\ \le\ \sup fx,y.}
\tag{22.1.6}
$$

Aquí $fx,y$ denota la imagen directa del subintervalo $[x,y]$ por la función $f$, conforme a la convención $f[X]$; los corchetes dobles no representan intervalos anidados. El cociente sólo se escribe cuando $x<y$.

**Demostración.**
Por Proposición §22.1.2 — Valores extremos e identidad exacta de los incrementos, la función $g:=f\upharpoonright[x,y]$ es integrable y su integral coincide con $F_{f,a}(y)-F_{f,a}(x)$. Tiene las cotas globales $m,M$ **sobre su propio dominio**, de modo que Corolario §21.5.8 — Positividad y estimaciones por cotas constantes aplicado a $g$ proporciona

$$
m(y-x)\le\int_x^y g\le M(y-x).
$$

Esto prueba (22.1.5). Como $[x,y]$ es no vacío y $f$ está acotada, Lema §21.2.2 — Existencia de las cotas extremas locales y comparación por inclusión permite tomar las cotas particulares $m=\inf fx,y$ y $M=\sup fx,y$. Dado que $y-x>0$, dividir (22.1.5) por esta anchura conserva ambas desigualdades y produce (22.1.6). No se selecciona un punto donde $f$ alcance alguno de los dos extremos; tales puntos pueden no existir. $\square$

La proposición expresa el control local necesario para el futuro teorema fundamental: el cociente incremental de la acumulación está entre el ínfimo y el supremo de los valores de $f$ en el pequeño tramo, antes de tomar límite alguno.

### Teorema 22.1.4 — Acotación global, condición de Lipschitz y continuidad uniforme
Si $f:[a,b]\to\mathbb R$ es integrable y $F_{f,a}$ es su función integral acumulada, existe un real $K\ge0$ tal que

$$
\boxed{|F_{f,a}(y)-F_{f,a}(x)|\le K|y-x|
\qquad(x,y\in[a,b]).}
\tag{22.1.7}
$$

Por tanto $F_{f,a}$ es **uniformemente continua** —y, en particular, continua en cada punto de su dominio— aun si $f$ no es continua.

**Demostración.**
La integrabilidad implica acotación (Definición §21.4.1 — Integrabilidad de Darboux por igualdad de integrales extremas, Definición §21.2.1 — Función acotada en el intervalo), por lo que existen dos reales $A,B$ con $A\le f(t)\le B$ en $[a,b]$. Fijemos **una sola vez** tales testigos. Por el orden total de $\mathbb R$ uno de $|A|$ y $|B|$ es el mayor; designémoslo $K$. Así $K\ge0$ y

$$
-K\le f(t)\le K\qquad(t\in[a,b]).
$$

Si $x<y$, aplicamos (22.1.5) a las cotas $m=-K$ y $M=K$:

$$
-K(y-x)\le F_{f,a}(y)-F_{f,a}(x)\le K(y-x).
$$

La definición de valor absoluto convierte esta doble desigualdad en (22.1.7), pues $|y-x|=y-x$. Para $y<x$ intercambiamos los nombres de los extremos y usamos la simetría del valor absoluto; si $x=y$, ambos miembros de (22.1.7) son cero.

Ahora sea $\varepsilon>0$ y construyamos el radio positivo

$$
\delta:=\frac{\varepsilon}{K+1_{\mathbb R}}>0.
$$

Para cualquier par $x,y\in[a,b]$ con $|x-y|<\delta$,

$$
|F_{f,a}(y)-F_{f,a}(x)|\le K|y-x|
<K\delta\le\varepsilon
$$

cuando $K>0$; si $K=0$, la primera desigualdad ya da $|F_{f,a}(y)-F_{f,a}(x)|=0<\varepsilon$. En ambos casos queda satisfecho el orden de cuantificadores de la continuidad uniforme Definición §17.6.1 — Continuidad uniforme relativa a un dominio: el **mismo** $\delta$ sirve para todos los pares de puntos. La continuidad relativa en cada punto se deduce de Proposición §17.6.2 — La uniformidad implica continuidad puntual y pasa a las restricciones. No se invocó la derivabilidad de $F_{f,a}$, ni un teorema del valor medio para integrales. $\square$

**Una distinción crucial.** La continuidad de la función acumulada no implica la continuidad de la integranda. La función escalón de §21.8, integrable a pesar de su salto, proporciona un ejemplo que se puede reutilizar aquí: su función acumulada es continua por (22.1.7). La pregunta más fuerte de si $F_{f,a}'(x)=f(x)$ requiere hipótesis locales adicionales y será el objeto de §22.2. La demostración no interpretará una derivada en un extremo como si fuera una derivada bilateral.

**Nota de consulta y contraste.** Jacob y Evans, *A Course in Analysis*, vol. I (2015), cap. 26, teorema 26.1, p. 369, formulan para integrandas continuas la derivabilidad de la función acumulada y recurren en su prueba a un teorema del valor medio para integrales. Hemos conservado la motivación del vínculo entre ambas operaciones, pero separado aquí un resultado previo más general: la continuidad de la acumulada sólo necesita que $f$ sea integrable y acotada. Nuestro encierro (22.1.6) se obtiene directamente de la estimación de integrales del Capítulo 21 y no presupone el valor medio integral.

**Transición.** Si $f$ es continua en un punto interior $x$, su oscilación en intervalos cortos que contienen $x$ puede hacerse arbitrariamente pequeña. La desigualdad (22.1.6) permitirá entonces probar que el cociente incremental de $F_{f,a}$ converge a $f(x)$; habrá que tratar separadamente los incrementos positivos y negativos sin invertir límites de integración.
