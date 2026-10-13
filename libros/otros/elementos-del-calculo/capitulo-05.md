---
title: Capítulo 5. De las sumas a la integral
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
source-id: EDC-C05
source-sha256: 1d302c080738bbcdbc840ef03fb7c28a863e91d2f25abfbb66826c41bb88e3f5
content-id: MA-BCH-0336
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-05.html) · [Ejercicios](capitulo-05-ejercicios.html) · [Soluciones](capitulo-05-soluciones.html) · [Notas históricas](capitulo-05-notas.html)

[← Capítulo 4](capitulo-04.html) · [Capítulo 6 →](capitulo-06.html)

> **Pregunta generadora.** ¿Qué garantiza que todas las aproximaciones razonables de una acumulación —con particiones desiguales y muestras distintas— determinan un único número real? ¿Qué sucede cuando no lo hacen?

En C04 conseguimos encerrar un valor entre aproximaciones cada vez más próximas, pero cada construcción tenía sus propias elecciones. Para los rectángulos bajo una gráfica podemos cambiar los puntos de corte y la altura elegida en cada tramo; si el resultado pretende representar una acumulación de la función, tendrá que resistir esos cambios. La función de Dirichlet mostró el obstáculo: incluso sobre una misma partición muy fina, las muestras racionales y las irracionales producen sumas distintas.

Las cotas inferiores y superiores permiten estudiar todas esas elecciones sin escoger una por adelantado. Primero tendremos que comparar cotas construidas con particiones diferentes. Reunir sus puntos de corte proporcionará esa comparación, y la completitud de los reales permitirá reunir después todas las cotas en dos números. Cuando esos números coincidan, tendremos una integral; quedará demostrar que cualquier partición suficientemente fina y cualquier selección de alturas aproximan ese mismo valor.

La construcción se apoyará en funciones acotadas, que pueden cambiar de signo y ser discontinuas. Las primitivas no intervienen en su definición: la relación con las derivadas será una pregunta posterior, cuando ya sepamos qué número hemos construido.

## 5.1. Qué estamos tratando de definir

Sean $a,b\in\mathbb R$ con $a<b$, y sea $f:[a,b]\to\mathbb R$ una **función acotada**: existe $B\ge0$ tal que $|f(x)|\le B$ para todo $x\in[a,b]$. El signo de $f$ puede cambiar. La exigencia de acotación permite construir cotas finitas en cada subintervalo; la continuidad **no** forma parte de la definición general.

Una partición $P$, ya presentada en `EDC-C04-DEF-002`, es una lista finita

$$
a=x_0<x_1<\cdots<x_n=b,\qquad \Delta_i=x_i-x_{i-1}>0,
\qquad \|P\|=\max_{1\le i\le n}\Delta_i.
$$

Una elección de etiquetas $\xi=(\xi_1,\ldots,\xi_n)$, con $\xi_i\in[x_{i-1},x_i]$, da la suma de Riemann **finita**

$$
S(f;P,\xi)=\sum_{i=1}^nf(\xi_i)\Delta_i.
$$

Al fijar $P$ y $\xi$ obtenemos un número, pero otra selección de alturas puede dar otro. Para estudiar cuánto pueden diferir las sumas de una misma partición, buscamos en cada tramo una cota inferior y una superior de la función. La acotación asegura que son finitas, aun cuando no haya un punto donde se alcance la altura extrema.

**Definición 5.1 (`EDC-C05-DEF-001`; cotas locales y sumas de Darboux).** Para cada intervalo cerrado $I_i=[x_{i-1},x_i]$ definimos

$$
m_i=\inf_{x\in I_i}f(x),\qquad M_i=\sup_{x\in I_i}f(x),
$$

que son reales por acotación y completitud. Las **sumas inferior y superior** son, respectivamente,

$$
L(f,P)=\sum_{i=1}^nm_i\Delta_i,
\qquad U(f,P)=\sum_{i=1}^nM_i\Delta_i.
$$

Se cumple siempre

$$
L(f,P)\le S(f;P,\xi)\le U(f,P),\qquad
U(f,P)-L(f,P)=\sum_i(M_i-m_i)\Delta_i\ge0.
$$

No exigimos que los valores $m_i$ o $M_i$ sean efectivamente alcanzados: en general son ínfimos y supremos, no mínimos ni máximos. Cuando $f$ es continua, el teorema de valores extremos de C00 garantiza además su realización. La cantidad $M_i-m_i$ mide la **oscilación** de $f$ en $I_i$. La suma de oscilaciones multiplicadas por anchuras será nuestro indicador del error de aproximación.

## 5.2. Por qué los refinamientos importan

**Definición 5.2 (`EDC-C05-DEF-002`; refinamiento común).** Una partición $R$ **refina** a $P$ si contiene todos los puntos de $P$ y acaso otros. Dos particiones $P,Q$ admiten el refinamiento común $P\cup Q$, formado por sus puntos reunidos y ordenados.

**Lema 5.1 (`EDC-C05-LEM-001`; monotonía del refinamiento).** Si $R$ refina a $P$, entonces

$$
L(f,P)\le L(f,R)\le U(f,R)\le U(f,P).
$$

**Demostración.** Una partición refinada se obtiene añadiendo un número finito de puntos. Podemos por ello estudiar primero un solo corte $z$ entre dos puntos consecutivos $u<v$ de $P$. Al restringir la función a $[u,z]$ o a $[z,v]$, sus cotas inferiores pueden mejorar: si $m$ es el ínfimo en $[u,v]$ y $m_1,m_2$ los de las dos partes, tenemos $m\le m_1,m_2$.

Las anchuras son positivas y suman $v-u$, así que

$$
m(v-u)\le m_1(z-u)+m_2(v-z).
$$

El término inferior que correspondía a todo el tramo no supera la suma de los dos términos nuevos. Para los supremos sucede lo contrario: $M_1,M_2\le M$, y la suma superior de las partes no supera $M(v-u)$. Los demás tramos permanecen iguales. Repetimos la comparación al insertar cada punto nuevo y obtenemos las dos desigualdades exteriores del lema; la intermedia vale porque en cada subintervalo el ínfimo no supera al supremo. $\square$

**Teorema 5.1 (`EDC-C05-THM-001`; compatibilidad entre particiones).** Para cualesquiera particiones $P,Q$ de $[a,b]$ se tiene

$$
L(f,P)\le U(f,Q).
$$

**Demostración.** Las particiones $P$ y $Q$ pueden cortar el intervalo en lugares distintos, de modo que no intentamos emparejar directamente sus piezas. Reunimos sus puntos en $R=P\cup Q$, una partición que refina a ambas. El Lema 5.1 permite pasar de la suma inferior de $P$ a la inferior de $R$, y de la superior de $R$ a la superior de $Q$:

$$
L(f,P)\le L(f,R)\le U(f,R)\le U(f,Q).
$$

La comparación central se realiza sobre una misma partición, donde cada cota inferior queda por debajo de la superior correspondiente. Así obtenemos la desigualdad entre las particiones originales, cualquiera que sea la distribución de sus puntos. $\square$

Cada suma superior acota por arriba todas las sumas inferiores, incluso las obtenidas con otras particiones. Por eso podemos buscar el mayor límite inferior y el menor límite superior sin que se crucen. Esa compatibilidad responde a la dificultad que quedó abierta al final de C04.

<figure id="fig-edc-c05-01" class="quarto-float-fig">
<img src="/assets/books/elementos-del-calculo/EDC-C05-F01_SUMAS_DARBOUX.svg" alt="Dos paneles con la misma partición no uniforme para f(x)=x²: a la izquierda rectángulos inferiores, a la derecha superiores, encerrando la curva.">
<figcaption>Figura 5.1. Los valores inferiores y superiores dependen de los supremos e ínfimos de la misma partición; el argumento general exige además refinamientos comunes.</figcaption>
</figure>

## 5.3. Construcción por completitud

Una sola partición da un encaje, y al refinarlas podemos mejorar sus cotas. Para reunir todas las aproximaciones, consideremos el conjunto de sumas inferiores y el de sumas superiores. Ninguno está vacío, pues la partición $P=\{a,b\}$ produce un elemento de cada uno. Además, cada altura usada como cota local pertenece a $[-B,B]$ y las anchuras suman $b-a$, de modo que todas las sumas pertenecen a $[-B(b-a),B(b-a)]$. La completitud garantiza entonces un supremo de las inferiores y un ínfimo de las superiores, ambos finitos.

**Definición 5.3 (`EDC-C05-DEF-003`; integrales inferior y superior).** Para $f$ acotada en $[a,b]$, llamamos

$$
\underline{\mathcal I}_a^b(f)=\sup_P L(f,P),
\qquad
\overline{\mathcal I}_a^b(f)=\inf_P U(f,P).
$$

El Teorema 5.1 asegura

$$
\underline{\mathcal I}_a^b(f)\le
\overline{\mathcal I}_a^b(f).
$$

**Definición 5.4 (`EDC-C05-DEF-004`; integral de Riemann–Darboux).** Decimos que $f:[a,b]\to\mathbb R$, acotada y con $a<b$, es **integrable** si

$$
\underline{\mathcal I}_a^b(f)=\overline{\mathcal I}_a^b(f).
$$

El valor común se denota por

$$
\boxed{\int_a^b f(x)\,dx}.
$$

La letra $x$ es una variable muda: $\int_a^b f(t)\,dt$ designa el mismo número. La notación no exige que $f\ge0$; si la función toma valores negativos, la integral representa acumulación con signo y no el área geométrica no negativa entre la gráfica y el eje.

**Teorema 5.2 (`EDC-C05-THM-002`; criterio de Darboux).** Una función acotada $f:[a,b]\to\mathbb R$ es integrable si y sólo si

$$
\forall\varepsilon>0\ \exists P:\quad U(f,P)-L(f,P)<\varepsilon.
$$

**Demostración.** Supongamos que podemos hacer la diferencia de sumas menor que cualquier tolerancia. Para cada partición, la integral inferior es al menos $L(f,P)$ y la superior es a lo sumo $U(f,P)$, pues se definieron tomando el supremo de las primeras sumas y el ínfimo de las segundas. Por tanto,

$$
0\le\overline{\mathcal I}_a^b(f)-\underline{\mathcal I}_a^b(f)
\le U(f,P)-L(f,P)<\varepsilon,
$$

cuando elegimos una partición suficientemente buena. La diferencia entre las dos integrales es un número no negativo fijo; si fuera positivo, podríamos escoger una tolerancia menor y contradecir la desigualdad. Es cero, luego hay integrabilidad.

En sentido inverso, sea $I$ el valor común. Su definición como ínfimo de las sumas superiores permite elegir $P_1$ con $U(f,P_1)<I+\varepsilon/2$; su definición como supremo de las inferiores permite elegir $P_2$ con $L(f,P_2)>I-\varepsilon/2$. Cada elección resuelve una mitad del encaje, y no hay razón para que produzcan los mismos cortes. Para reunirlas tomamos $R=P_1\cup P_2$. El refinamiento mejora ambas cotas y da

$$
0\le U(f,R)-L(f,R)
\le U(f,P_1)-L(f,P_2)<\varepsilon.
$$

Hemos obtenido una sola partición cuyo error satisface la tolerancia, a partir de dos aproximaciones que podían ser distintas. $\square$

El criterio nos permite elegir una partición buena para cada tolerancia. Todas sus sumas etiquetadas quedan entonces próximas, porque comparten un encaje estrecho. Para que otro lector pueda elegir sus propios cortes, necesitamos demostrar algo más: que cualquier partición suficientemente fina proporciona también un encaje pequeño.

## 5.4. El desafío de las muestras arbitrarias

Una partición fina puede no contener ninguno de los cortes que hicieron buena a la partición anterior. Al reunirlas tendremos que añadir esos cortes, y algunos subintervalos de la nueva partición se dividirán. El efecto de esas divisiones se puede controlar porque hay un número fijo de cortes que añadir y cada uno afecta a un tramo corto. Esta observación permite pasar de una partición elegida a todas las particiones suficientemente finas.

**Lema 5.2 (`EDC-C05-LEM-002`; estabilidad para particiones finas).** Supongamos $|f(x)|\le B$ en $[a,b]$ y fijemos una partición $P_0$ con $r$ puntos interiores. Entonces toda partición $Q$ satisface

$$
\begin{aligned}
U(f,Q)&\le U(f,P_0)+2Br\,\|Q\|,\\
L(f,Q)&\ge L(f,P_0)-2Br\,\|Q\|.
\end{aligned}
$$

En consecuencia,

$$
U(f,Q)-L(f,Q)\le U(f,P_0)-L(f,P_0)+4Br\,\|Q\|.
$$

**Demostración.** Comparemos $Q$ con el refinamiento $R=P_0\cup Q$. Llamemos *intervalo conflictivo* de $Q$ al que contiene en su interior algún punto interior de $P_0$. Sólo esos intervalos se dividen al pasar a $R$; un punto de $P_0$ que ya sea extremo de un intervalo de $Q$ no añade un corte.

Hay a lo sumo $r$ intervalos conflictivos, porque cada uno contiene al menos un punto distinto de $P_0$ y sus interiores son disjuntos. Cada longitud es a lo sumo $\|Q\|$, luego la longitud total afectada no supera $r\|Q\|$.

En un intervalo conflictivo de longitud $d$, sea $M$ su supremo y sean $M_j$ los supremos de las partes que aparecen en $R$, con longitudes $d_j$. El descenso de la suma superior es $Md-\sum_jM_jd_j=\sum_j(M-M_j)d_j$, pues $\sum_jd_j=d$. Cada diferencia es no negativa y no supera $2B$, porque las cotas de la función pertenecen a $[-B,B]$. Así el descenso en ese intervalo no supera $2Bd$, y en todos ellos no supera $2Br\|Q\|$. En los intervalos restantes la contribución no cambia.

Obtenemos $U(f,Q)\le U(f,R)+2Br\|Q\|$. Como $R$ refina a $P_0$, también $U(f,R)\le U(f,P_0)$, y resulta la primera desigualdad. Para las sumas inferiores, el refinamiento aumenta las cotas: el aumento en cada intervalo conflictivo tampoco supera $2Bd$. De $L(f,R)\ge L(f,P_0)$ deducimos la segunda desigualdad. Al restarlas, los dos márgenes de error se suman y dan el factor $4Br\|Q\|$.

Si $r=0$, $P_0$ sólo contiene los extremos y $Q$ ya la refina, de modo que no hay intervalos conflictivos. Si $B=0$, la función es nula y todas las sumas son cero. $\square$

**Teorema 5.3 (`EDC-C05-THM-003`; equivalencia con sumas de Riemann).** Para una función acotada $f:[a,b]\to\mathbb R$ son equivalentes:

1. $f$ es integrable en el sentido de Darboux y $I=\int_a^b f$.
2. Existe $I\in\mathbb R$ tal que, para todo $\varepsilon>0$, hay $\delta>0$ con la propiedad de que **para toda** partición $P$ con $\|P\|<\delta$ y **para toda** elección de muestras $\xi_i\in[x_{i-1},x_i]$,

$$
\left|S(f;P,\xi)-I\right|<\varepsilon.
$$

El número $I$ de ambas formulaciones es el mismo.

**Demostración.** Supongamos primero que $f$ es integrable y fijemos $\varepsilon>0$. El criterio de Darboux proporciona una partición $P_0$ con $U(f,P_0)-L(f,P_0)<\varepsilon/2$. El Lema 5.2 compara cualquier otra partición $Q$ con ella: a esa diferencia añade un margen de a lo sumo $4Br\|Q\|$. Si $Br>0$, escogemos $\delta=\varepsilon/(8Br)$ para que $\|Q\|<\delta$ haga ese margen menor que $\varepsilon/2$; si $Br=0$, el margen es cero y podemos tomar cualquier $\delta>0$. En ambos casos $U(f,Q)-L(f,Q)<\varepsilon$.

Toda suma $S(f;Q,\xi)$ pertenece a $[L(f,Q),U(f,Q)]$. El valor integral $I$ pertenece también a ese intervalo, por su definición como supremo e ínfimo globales. La distancia entre ambos números no supera esa anchura, que es menor que la tolerancia, y obtenemos $|S-I|<\varepsilon$ para todas las etiquetas. La elección de $\delta$ precede a la de $Q$ y a la de sus muestras.

Supongamos ahora la condición 2. Dado $\varepsilon>0$, elegimos una partición de finura menor que el $\delta$ que corresponde a la tolerancia $\varepsilon/4$; por ejemplo, podemos dividir uniformemente el intervalo en un número suficientemente grande de piezas. Todas sus sumas etiquetadas están entre $I-\varepsilon/4$ e $I+\varepsilon/4$.

Necesitamos pasar de esas sumas a las cotas de Darboux, aunque los ínfimos o supremos locales no sean alcanzados. La suma inferior es el ínfimo de todas las sumas etiquetadas de la partición: ya sabemos que es cota inferior, y podemos acercarnos a ella tanto como queramos eligiendo en cada subintervalo un valor de $f$ próximo a su ínfimo. Para una tolerancia auxiliar $\eta>0$, escogemos cada muestra con error menor que $\eta/[n\max\{1,b-a\}]$ en la altura. Al multiplicar por las anchuras y sumar, el error total es menor que esa cantidad por $b-a$, y por tanto menor que $\eta$. Las muestras de cada tramo se eligen independientemente y la suma es finita. El mismo argumento, aproximando los supremos locales desde abajo, muestra que la suma superior es el supremo de las sumas etiquetadas.

Como todas esas sumas están en el intervalo indicado, sus extremos satisfacen $L(f,P)\ge I-\varepsilon/4$ y $U(f,P)\le I+\varepsilon/4$. Tenemos $U-L\le\varepsilon/2<\varepsilon$, y el criterio de Darboux prueba integrabilidad.

Falta identificar el valor integral con $I$. La primera parte asegura que las sumas de una función integrable se aproximan a su valor Darboux para todas las particiones finas. Las mismas sumas se aproximan a $I$ por la hipótesis 2. Si esos dos números fueran distintos, elegir para ambas aproximaciones una tolerancia menor que un tercio de su distancia y una partición de finura menor que los dos umbrales daría, por desigualdad triangular, una distancia menor que dos tercios de sí misma. Deben coincidir. $\square$

**Advertencia de interpretación.** «La malla se hace fina» no significa meramente que el número de subintervalos crece. Una partición puede contener miles de segmentos diminutos y conservar uno de longitud $1/2$. El cuantificador de finura controla **el mayor** subintervalo y, a diferencia de una sola sucesión elegida a conveniencia, controla todas las etiquetas.

## 5.5. Cuándo existe la integral

**Teorema 5.4 (`EDC-C05-THM-004`; continuidad e integrabilidad).** Si $f:[a,b]\to\mathbb R$ es continua, con $a<b$, entonces es integrable.

**Demostración.** La continuidad en el intervalo cerrado garantiza acotación (`EDC-C00-THM-007`), así que las sumas de Darboux están definidas. También proporciona continuidad uniforme (`EDC-C00-THM-008`), que permite hacer pequeñas todas las oscilaciones con un único umbral de anchura.

Dado $\varepsilon>0$, elegimos $\eta=\varepsilon/[2(b-a)]$ y un $\delta>0$ tal que $|f(x)-f(y)|<\eta$ cuando $|x-y|<\delta$. Tomamos una partición con $\|P\|<\delta$. En cada subintervalo el máximo y el mínimo son alcanzados, y los puntos donde se alcanzan distan menos que $\delta$; por ello $M_i-m_i<\eta$. Sumando las oscilaciones por sus anchuras,

$$
0\le U(f,P)-L(f,P)
=\sum_i(M_i-m_i)\Delta_i
<\eta(b-a)=\varepsilon/2<\varepsilon.
$$

Esta es la estimación preparada en C04. El criterio de Darboux la convierte en integrabilidad, porque encontramos una partición con diferencia menor que cualquier tolerancia. $\square$

**Teorema 5.5 (`EDC-C05-THM-005`; monotonía e integrabilidad).** Si $f:[a,b]\to\mathbb R$ es monótona, es integrable, aunque pueda tener discontinuidades.

**Demostración.** Supongamos que $f$ es no decreciente. Todos sus valores quedan entre $f(a)$ y $f(b)$, por lo que es acotada. En cada subintervalo el ínfimo y el supremo son los valores de sus extremos: $m_i=f(x_{i-1})$ y $M_i=f(x_i)$. Las diferencias son no negativas, de modo que reemplazar cada anchura por la mayor da

$$
\begin{aligned}
U(f,P)-L(f,P)
&=\sum_i\bigl(f(x_i)-f(x_{i-1})\bigr)\Delta_i\\
&\le\|P\|\sum_i\bigl(f(x_i)-f(x_{i-1})\bigr)\\
&=\|P\|\bigl(f(b)-f(a)\bigr).
\end{aligned}
$$

La suma de variaciones telescopa a la diferencia entre los valores finales. Si éstos coinciden, la monotonía obliga a que la función sea constante y la diferencia de sumas es cero. Si $f(b)>f(a)$, elegimos una partición con $\|P\|<\varepsilon/[f(b)-f(a)]$ y el criterio de Darboux concluye.

Si $f$ es no creciente, $-f$ es no decreciente y admite particiones con diferencias arbitrariamente pequeñas. Cambiar el signo intercambia las cotas locales: $U(-f,P)=-L(f,P)$ y $L(-f,P)=-U(f,P)$. Las diferencias de sumas son iguales para $f$ y $-f$, de modo que el mismo criterio prueba integrabilidad de $f$. No hemos supuesto continuidad. $\square$

**Lema 5.3 (`EDC-C05-LEM-003`; funciones concentradas en pocos puntos).** Si $h:[a,b]\to\mathbb R$ es acotada y vale cero salvo en un conjunto **finito** $F$, entonces es integrable y $\int_a^b h=0$.

**Demostración.** Sea $|h|\le B$ y $|F|=N$. Si un subintervalo no contiene ningún punto de $F$, la función es cero en todo él y su contribución a la diferencia de sumas es nula. Un punto de $F$ puede estar en el interior de una pieza o ser un extremo compartido por dos piezas cerradas. Por eso el número de intervalos que pueden contribuir es a lo sumo $2N$, y su longitud total no supera $2N\|P\|$.

En cada uno, los valores están en $[-B,B]$ y la oscilación no supera $2B$. Resulta

$$
0\le U(h,P)-L(h,P)\le4BN\|P\|.
$$

Si $B=0$ o $N=0$, la función es nula. En los demás casos, una partición suficientemente fina hace la cota menor que cualquier tolerancia, y el criterio de Darboux da integrabilidad.

Para identificar el valor, las sumas etiquetadas sólo pueden recibir aportes no nulos de esos mismos intervalos. La altura de cada aporte tiene módulo a lo sumo $B$, de modo que $|S(h;P,\xi)|\le2BN\|P\|\to0$ cuando la finura tiende a cero, para cualquier etiqueta. El Teorema 5.3 identifica la integral con ese valor cero. $\square$

El control depende de que el número de puntos excepcionales sea fijo y finito. En un conjunto numerable arbitrario ya no tendríamos el mismo límite para el número de piezas afectadas; la función indicatriz de los racionales mostrará cuánto puede cambiar el problema.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Riemann y Darboux: medir desde abajo y desde arriba"}
*Lectura opcional.*

En su *Mémoire sur les fonctions discontinues* de 1875, Darboux comienza explicando que volverá sobre la definición de integral de Riemann con los desarrollos necesarios para estudiar funciones más generales. La pregunta ya no se limita a las curvas suaves: también interesa saber qué discontinuidades permiten integrar.

En la sección II forma dos sumas, una con las cotas superiores de la función en cada tramo y otra con las inferiores. Al subdividir, la primera disminuye o permanece igual y la segunda aumenta o permanece igual. La distancia entre ambas recoge las oscilaciones de la función multiplicadas por las longitudes de los intervalos.

La sección III examina después las alturas elegidas dentro de cada tramo. Esa elección puede cambiar la suma, y hay que averiguar cuándo deja de importar al hacer pequeños los intervalos. Es la dificultad que acabamos de resolver con el refinamiento y el control de todas las etiquetas.

**Para seguir leyendo:** [Darboux, *Mémoire* (1875), pp. 58, 65–66 y 72, secciones II–III](https://www.numdam.org/item/ASENS_1875_2_4__57_0.pdf); notas históricas del capítulo 5.
:::

## 5.6. Dos funciones que revelan los límites del concepto

La función indicatriz de los racionales en $[0,1]$ es

$$
d(x)=\begin{cases}1,&x\in\mathbb Q,\\0,&x\notin\mathbb Q.\end{cases}
$$

Cada subintervalo no degenerado contiene racionales e irracionales (`EDC-C00-LEM-003`). Por consiguiente, en **toda** partición se tiene $m_i=0$, $M_i=1$, y

$$
L(d,P)=0,\qquad U(d,P)=1.
$$

Así $\underline{\mathcal I}_0^1(d)=0$ y $\overline{\mathcal I}_0^1(d)=1$: **no existe integral de Riemann–Darboux** para $d$. La oscilación permanece igual a uno en cada pieza y la suma de anchuras es uno, de modo que ningún refinamiento reduce la distancia entre las dos cotas globales.

Comparemos ese comportamiento con un único salto. Definamos $s_c(x)=0$ para $x<c$ y $s_c(x)=1$ para $x\ge c$, con $a<c<b$. La función tiene un salto, pero es monótona, luego integrable por el Teorema 5.5. Su valor puede determinarse sin primitivas: para cualquier $\eta>0$ suficientemente pequeño, tomemos una partición que incluya $c-\eta$ y $c$. Fuera del intervalo $[c-\eta,c]$, las sumas inferiores y superiores coinciden con la longitud total de la parte situada a la derecha de $c$, a saber, $b-c$. El subintervalo de longitud $\eta$ tiene ínfimo $0$ y supremo $1$, por lo que

$$
L(s_c,P)=b-c,\qquad U(s_c,P)=b-c+\eta.
$$

Dejando $\eta$ arbitrariamente pequeño obtenemos

$$
\boxed{\int_a^b s_c(x)\,dx=b-c.}
$$

Por último, la función que vale $7$ en un solo punto $c$ y $0$ en los demás tiene integral cero por el Lema 5.3. La existencia de la integral no equivale a continuidad de la función, ni tampoco toda discontinuidad impide integrar.

## 5.7. Propiedades algebraicas y de orden

**Teorema 5.6 (`EDC-C05-THM-006`; linealidad).** Sean $f,g:[a,b]\to\mathbb R$ integrables y $\alpha,\beta\in\mathbb R$. Entonces $\alpha f+\beta g$ es integrable y

$$
\int_a^b(\alpha f(x)+\beta g(x))\,dx
=\alpha\int_a^b f(x)\,dx+\beta\int_a^b g(x)\,dx.
$$

**Demostración.** La combinación es acotada porque lo son $f$ y $g$. Para cualquier partición y etiquetas, la distributividad de una suma finita da

$$
S(\alpha f+\beta g;P,\xi)
=\alpha S(f;P,\xi)+\beta S(g;P,\xi)
$$

Queremos que su error respecto de la combinación de integrales sea menor que $\varepsilon$. Elegimos para las sumas de cada función una tolerancia $\tau=\varepsilon/[1+|\alpha|+|\beta|]$. El Teorema 5.3 proporciona umbrales $\delta_f$ y $\delta_g$ que aseguran esos errores para todas las etiquetas. Con $\delta=\min\{\delta_f,\delta_g\}$, ambos controles valen en una misma partición de finura menor que $\delta$.

La desigualdad triangular acota el error de la combinación por $|\alpha|$ veces el de $f$ más $|\beta|$ veces el de $g$, y resulta menor que $\varepsilon$. El denominador elegido funciona también si uno o ambos coeficientes son cero. La caracterización por sumas de Riemann prueba integrabilidad y da la fórmula. $\square$

**Teorema 5.7 (`EDC-C05-THM-007`; orden y estimaciones).** Si $f,g$ son integrables en $[a,b]$ y $f(x)\le g(x)$ para todo $x$, entonces

$$
\int_a^b f\le\int_a^b g.
$$

Si $m\le f(x)\le M$, se cumple

$$
m(b-a)\le\int_a^b f\le M(b-a).
$$

En particular, si $|f(x)|\le B$, entonces $\left|\int_a^b f\right|\le B(b-a)$.

**Demostración.** La desigualdad puntual y la positividad de las anchuras aseguran $S(f;P,\xi)\le S(g;P,\xi)$ para cualquier partición con las mismas etiquetas. Por el Teorema 5.3 esas sumas aproximan sus integrales. Si la integral de $f$ fuera mayor que la de $g$, podríamos exigir a ambas aproximaciones errores menores que un tercio de esa separación y elegir una partición de finura menor que los dos umbrales. Las sumas tendrían entonces el orden contrario al que acabamos de demostrar. Esto prueba el orden entre las integrales.

Para una constante $k$, todas las sumas valen exactamente $k(b-a)$ y por tanto ése es su valor integral. Comparamos $f$ con las constantes $m$ y $M$ para obtener las cotas del enunciado. Si $|f|\le B$, tomamos $m=-B$ y $M=B$; la integral queda entre $-B(b-a)$ y $B(b-a)$, que da la cota absoluta. $\square$

**Proposición 5.1 (`EDC-C05-PRP-001`; producto).** Si $f,g$ son integrables y acotadas en $[a,b]$, también lo es $fg$.

**Demostración.** Tomemos $|f|\le A$, $|g|\le B$, con $A,B\ge0$. El producto es acotado. Para controlar su oscilación, separamos el cambio de los dos factores añadiendo y restando $f(x)g(y)$. Para $x,y$ en un mismo subintervalo $I$, obtenemos

$$
|f(x)g(x)-f(y)g(y)|
\le A|g(x)-g(y)|+B|f(x)-f(y)|.
$$

La oscilación de una función acotada es el supremo de las diferencias absolutas entre parejas de sus valores: éstos están entre el ínfimo y el supremo, y podemos acercarnos a ambas cotas cuanto queramos. Al tomar ese supremo en la desigualdad anterior resulta

$$
\operatorname{osc}_I(fg)
\le A\operatorname{osc}_I(g)+B\operatorname{osc}_I(f).
$$

El criterio de Darboux permite elegir una partición buena para $f$ y otra para $g$. Para usarlas a la vez tomamos el refinamiento común, que no aumenta ninguna diferencia de sumas. Multiplicamos la cota de oscilación por la anchura de cada pieza y sumamos:

$$
U(fg,P)-L(fg,P)
\le A\bigl[U(g,P)-L(g,P)\bigr]+B\bigl[U(f,P)-L(f,P)\bigr],
$$

Elegir inicialmente cada diferencia menor que $\varepsilon/(1+A+B)$ hace el resultado menor que $\varepsilon$, también si alguna cota es cero. El producto satisface así el criterio de integrabilidad. $\square$

El resultado no autoriza a afirmar que $\int fg=(\int f)(\int g)$: esa identidad es generalmente falsa. Por ejemplo, para $f(x)=g(x)=x$ en $[0,1]$ la integral del producto es $1/3$, mientras el producto de integrales vale $1/4$.

**Proposición 5.2 (`EDC-C05-PRP-002`; valor absoluto y perturbaciones).** Si $f$ es integrable, entonces $|f|$ también es integrable y

$$
\left|\int_a^b f\right|\le\int_a^b |f|.
$$

Si además $g$ es integrable, entonces

$$
\left|\int_a^b f-\int_a^b g\right|
\le (b-a)\sup_{x\in[a,b]}|f(x)-g(x)|.
$$

**Demostración.** La desigualdad $||u|-|v||\le|u-v|$ dice que tomar módulos no aumenta la separación entre dos valores. Por tanto, la oscilación de $|f|$ en cualquier subintervalo no supera la de $f$. Sus diferencias de sumas tampoco la superan, y las particiones buenas para $f$ demuestran por Darboux la integrabilidad de $|f|$.

La comparación puntual $-|f|\le f\le|f|$, junto con el orden y la linealidad ya probados, coloca la integral de $f$ entre la integral de $|f|$ y su opuesta. Esto da la primera desigualdad.

Para la segunda, la diferencia $h=f-g$ es integrable por linealidad. Su módulo está acotado en todo el intervalo por el supremo indicado, que es finito porque ambas funciones son acotadas. Aplicamos la cota del Teorema 5.7 a $h$ y reemplazamos su integral por la diferencia de las integrales. $\square$

Ésta es una estimación del error particularmente útil en aproximación: si dos funciones integrables son cercanas en todos los puntos, sus acumulaciones también lo son, con un factor de escala igual a la longitud del intervalo.

## 5.8. Cortar y reunir intervalos

**Teorema 5.8 (`EDC-C05-THM-008`; aditividad por intervalos).** Sean $a<c<b$ y $f:[a,b]\to\mathbb R$ acotada. La función es integrable en $[a,b]$ si y sólo si sus restricciones son integrables en $[a,c]$ y $[c,b]$. Cuando se cumplen esas condiciones,

$$
\int_a^b f(x)\,dx
=\int_a^c f(x)\,dx+\int_c^b f(x)\,dx.
$$

**Demostración.** Supongamos primero integrabilidad en $[a,b]$. Para una tolerancia $\varepsilon>0$, elegimos una partición $P$ con $U(f,P)-L(f,P)<\varepsilon$ y añadimos el punto $c$. El refinamiento no aumenta esa diferencia. Sus sumas se separan en las contribuciones de $[a,c]$ y de $[c,b]$, de modo que la diferencia global es la suma de las dos diferencias parciales.

Cada diferencia parcial es no negativa y no puede superar el total, que es menor que $\varepsilon$. Las restricciones son acotadas y, para cada tolerancia, hemos obtenido una partición buena en cada una. El criterio de Darboux demuestra su integrabilidad.

En sentido inverso, supongamos integrabilidad en los dos lados. Elegimos una partición de $[a,c]$ con diferencia menor que $\varepsilon/2$ y una de $[c,b]$ con la misma propiedad. Al reunirlas obtenemos una partición de $[a,b]$; las contribuciones siguen separadas por $c$ y su diferencia total es menor que $\varepsilon$. Así hay integrabilidad global.

Para identificar el valor, las sumas etiquetadas de cualquier partición que contenga $c$ se descomponen exactamente en las de las dos restricciones. Podemos hacer pequeñas las finuras a ambos lados simultáneamente, y el Teorema 5.3 aproxima cada suma por su integral. La suma total aproxima a la vez la integral global y la suma de las dos integrales parciales; la unicidad del valor límite da la igualdad. El punto $c$ es extremo de dos subintervalos, pero los términos siempre están multiplicados por las anchuras de las piezas, y no se añade una contribución separada del punto compartido. $\square$

**Definición 5.5 (`EDC-C05-DEF-005`; intervalo degenerado y orientación).** Para una función definida en un intervalo que contiene $a$ y $b$, fijamos

$$
\int_a^a f=0,\qquad
\int_b^a f=-\int_a^b f\quad\text{si }a<b
$$

siempre que la integral del intervalo no orientado exista. Con esta convención, la aditividad se extiende a cualquier orden de tres extremos pertenecientes al mismo intervalo de integrabilidad: no es un nuevo teorema que todo signo pueda ignorarse.

## 5.9. El valor medio de una acumulación

**Teorema 5.9 (`EDC-C05-THM-009`; valor medio integral).** Si $f:[a,b]\to\mathbb R$ es continua y $a<b$, existe $c\in[a,b]$ tal que

$$
\boxed{\int_a^b f(x)\,dx=f(c)(b-a).}
$$

**Demostración.** La continuidad asegura que la integral existe, por el Teorema 5.4, y que $f$ alcanza un mínimo $m$ y un máximo $M$, por C00. El orden permite comparar su integral con las de esas dos constantes. Al dividir por la longitud positiva del intervalo obtenemos

$$
m\le\frac1{b-a}\int_a^b f(x)\,dx\le M.
$$

El número central es la altura constante que produciría la misma acumulación sobre todo el intervalo. Para que esa altura se alcance en la función necesitamos continuidad: entre un punto de mínimo y uno de máximo, el valor intermedio (`EDC-C00-THM-006`) proporciona cada altura comprendida entre $m$ y $M$. Existe por tanto un $c\in[a,b]$ con $f(c)$ igual al promedio. Si $m=M$, la función es constante y cualquier punto sirve. $\square$

Para $f$ meramente integrable no podemos asegurar que el promedio sea alcanzado como valor puntual. Consideremos en $[0,1]$ la función $f(x)=0$ si $x\le1/2$ y $f(x)=1$ si $x>1/2$. Es monótona e integrable, y su integral vale $1/2$; sin embargo, su imagen es $\{0,1\}$ y no contiene el valor promedio $1/2$. La continuidad es la hipótesis que garantiza que el promedio pertenezca a la imagen.

## 5.10. Calcular sin el Teorema Fundamental

Ya podemos volver a las cuadraturas de C04. Las sumas superiores e inferiores de $x^2$ en $[0,1]$, para la partición uniforme de $n$ subintervalos, eran

$$
L_n=\frac13-\frac1{2n}+\frac1{6n^2},\qquad
U_n=\frac13+\frac1{2n}+\frac1{6n^2}.
$$

La diferencia $U_n-L_n=1/n$ tiende a cero; por Darboux la función es integrable. El valor integral queda entre ambas sumas para cada $n$ y el encajonamiento de C00 identifica

$$
\boxed{\int_0^1x^2\,dx=\frac13.}
$$

Asimismo, para cada entero $p\ge1$, el Teorema 4.3 proporciona, sin recurrir a primitivas,

$$
\int_0^1x^p\,dx=\frac1{p+1}.
$$

La coincidencia con la cuadratura parabólica de C04 también puede verificarse sin ningún teorema de cambio de variable. Para $g(x)=k(x-a)(b-x)$ sobre $[a,b]$, con $d=b-a>0$ y $k>0$, usamos la partición uniforme $x_i=a+id/n$ y etiquetas derechas. Su suma es exactamente

$$
S_n(g)=kd^3\frac1n\sum_{i=1}^n\left(\frac in-\frac{i^2}{n^2}\right).
$$

Las identidades finitas de sumas de primeras y segundas potencias muestran que $S_n(g)\to kd^3(1/2-1/3)=kd^3/6$. Como $g$ es continua, su integral existe y todas las sumas suficientemente finas tienen ese límite. Por consiguiente,

$$
\int_a^b k(x-a)(b-x)\,dx=\frac{k(b-a)^3}{6}=\frac43T,
$$

El resultado coincide con la cuadratura de `EDC-C04-THM-002`. Aquí las coordenadas de la partición se sustituyeron directamente en una suma finita; la continuidad garantiza después que su límite es la integral. Así podemos comparar la construcción geométrica y la analítica sin usar un teorema de cambio de variable.

En un intervalo $[a,b]$ la integral de una constante $k$ es $k(b-a)$; esto se sigue porque todas sus sumas finitas son iguales a ese número. Combinando tales resultados con la linealidad podemos evaluar diversos polinomios de forma independiente del Teorema Fundamental.

**Proposición 5.3 (`EDC-C05-PRP-003`; polinomios en $[0,1]$).** Para $p(x)=\sum_{j=0}^N c_jx^j$, con coeficientes reales,

$$
\int_0^1p(x)\,dx=\sum_{j=0}^N\frac{c_j}{j+1}.
$$

**Demostración.** El término $j=0$ es constante y su integral en $[0,1]$ es $c_0$. Cada potencia de exponente positivo tiene la integral $1/(j+1)$ ya identificada mediante las sumas de C04. Multiplicamos por su coeficiente y aplicamos la linealidad a los $N+1$ términos, una cantidad finita. La contribución constante se escribe también como $c_0/(0+1)$, y obtenemos la fórmula en una sola suma. $\square$

El cálculo de estos polinomios reúne valores que ya conocíamos por sus sumas. Una regla general que permita hallar integrales mediante derivadas necesitará justificar por qué ese procedimiento recupera el número definido aquí.

## 5.11. Qué representa el número obtenido

Cuando $f\ge0$, la integral es compatible con la interpretación geométrica mediante rectángulos inscritos y circunscritos. Para una función con signo, en cambio, la integral añade acumulaciones positivas y negativas. La función constante $f=-2$ en $[0,3]$ tiene integral $-6$, mientras el área geométrica entre la gráfica y el eje es $6$ unidades cuadradas. Esa distinción evita confundir **desplazamiento** con **distancia recorrida**.

Si $v(t)$ representa una velocidad con unidades de longitud dividida por tiempo, una suma $\sum_i v(\xi_i)\Delta t_i$ tiene unidades de longitud. Su límite, cuando $v$ es integrable, define matemáticamente un **desplazamiento acumulado**. Interpretarlo como posición efectiva de un sistema físico demanda aceptar el modelo de aproximación y sus hipótesis; no hemos demostrado todavía que la derivada de esa acumulación devuelva $v(t)$ en todos los puntos. Eso será el contenido de C06 cuando la velocidad sea continua.

La integral de una densidad lineal $\rho(x)$ tiene unidades de masa; la integral de una tasa temporal de ingreso, unidades de dinero. La estructura matemática es común, pero las interpretaciones no son intercambiables sin atender a las magnitudes.

## 5.12. Una definición conquistada, un vínculo todavía pendiente

El refinamiento común permitió pasar de aproximaciones individuales a cotas compatibles sobre todas las particiones. La completitud hizo posible reunir esas cotas, y el control de las oscilaciones decidió cuándo coincidían. La relación entre las dos maneras de describir la integral queda expresada así:

$$
\begin{gathered}
\text{particiones y cotas locales}\\
\Downarrow\\
\text{sumas inferiores y superiores compatibles}\\
\Downarrow\\
\underline{\mathcal I}_a^b(f)\le\overline{\mathcal I}_a^b(f)\\
\Downarrow\quad\text{(igualdad cuando el error puede agotarse)}\\
\text{integral de Riemann--Darboux}\\
\Longleftrightarrow\\
\text{límite común de todas las sumas etiquetadas finas}.
\end{gathered}
$$

La integral puede existir aunque haya saltos o valores excepcionales en unos pocos puntos, pero las oscilaciones persistentes de la función de Dirichlet impiden cerrar el encaje. La prueba de equivalencia muestra por qué la precisión debe controlar todas las etiquetas y la anchura de cada pieza; aumentar simplemente el número de rectángulos no resuelve esa exigencia.

Tenemos ya una acumulación definida y reglas para combinarla, compararla y repartirla entre intervalos. Queda estudiar qué ocurre al mover uno de sus extremos: el cociente entre el cambio de la acumulación y el incremento del extremo ofrecerá en C06 una nueva relación con la derivada.

### Mapa de dependencias

- **C00:** axioma de completitud y supremo/ínfimo, límites, valor intermedio, extremos y continuidad uniforme.
- **C04:** particiones y finura, sumas finitas, estimación preparatoria para funciones continuas, sumas cuadráticas y potencias.
- **C01–C03:** ninguno de sus teoremas de derivación se usa para **definir** la integral; algunos cálculos especiales de C04 ya contenían el teorema del valor medio de C03.
- **C05:** `EDC-C05-THM-001--009`, tres lemas, tres proposiciones y cinco definiciones, con independencia de C06.
- **Excluidos:** integrales impropias, Lebesgue, teoremas de medida, convergencia uniforme sistemática y Teorema Fundamental del Cálculo.
- **Historia:** [notas históricas y procedencia de fuentes](capitulo-05-notas.html).

### Trabajo del lector

Los [ejercicios del capítulo](capitulo-05-ejercicios.html) distinguen el reconocimiento del valor integral, las pruebas de existencia y la auditoría de cuantificadores. Sus [soluciones desarrolladas](capitulo-05-soluciones.html) permanecen separadas de la exposición, sin adelantar procedimientos del capítulo siguiente.
