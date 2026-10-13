---
title: Capítulo 8. Sumas infinitas y series de potencias
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
source-id: EDC-C08
source-sha256: b2276d69efa503d0ca16cd557eb3899ba1d4b290045a85b539f59be6a47d0c0c
content-id: MA-BCH-0339
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-08.html) · [Ejercicios](capitulo-08-ejercicios.html) · [Soluciones](capitulo-08-soluciones.html) · [Notas históricas](capitulo-08-notas.html)

[← Capítulo 7](capitulo-07.html) · [Capítulo 9 →](capitulo-09.html)

> **Pregunta generadora.** Una suma finita se obtiene realizando cierto número de adiciones. ¿Qué condiciones autorizan a escribir una suma con infinitos términos y, todavía más, a derivar o integrar una función presentada mediante esa suma?

En C04 una suma geométrica permitió controlar lo que faltaba después de cada aproximación; en C02 una serie concreta dio una construcción de la exponencial. En ambos casos realizábamos operaciones finitas y estudiábamos qué ocurría al prolongarlas. Una expresión con puntos suspensivos plantea esa misma pregunta: los primeros términos pueden calcularse, pero necesitamos saber si las sumas cada vez más largas se acercan a un número.

La dificultad crece cuando los términos dependen de una variable. La suma puede existir para unos valores y divergir para otros; incluso donde exista, derivar cada término todavía no demuestra que hayamos derivado la función resultante. Las series de potencias ofrecen un control que permitirá resolver ambas cuestiones en el interior de un intervalo. Allí podremos estimar las colas con una misma cota para todos los puntos y justificar después la integración y la derivación. En C09 utilizaremos esos resultados para investigar qué función representa una serie concreta.

## 8.1. El infinito como límite de operaciones finitas

**Definición 8.1 (serie numérica; `EDC-C08-DEF-001`).** Para una sucesión real $(a_n)_{n\ge0}$ definimos sus *sumas parciales* por $S_N=\sum_{n=0}^{N}a_n$. La serie $\sum_{n=0}^{\infty}a_n$ **converge** a $S\in\mathbb R$ si $S_N\to S$ cuando $N\to\infty$. En otro caso **diverge**. El símbolo $\sum_{n=0}^{\infty}a_n$ designa un número sólo cuando se ha demostrado ese límite, salvo que se indique explícitamente un procedimiento distinto de sumación, que no adoptaremos aquí.

La expresión $1-1+1-1+\cdots$ tiene sumas parciales iguales a uno o a cero según dónde nos detengamos. Esas dos respuestas siguen alternándose por lejos que avancemos, de modo que no aparece un límite común. Para que una identidad finita proporcione una suma infinita tendremos que examinar el término que permanece al final, antes de suprimirlo.

**Lema 8.1 (condición necesaria; `EDC-C08-LEM-001`).** Si $\sum_{n=0}^{\infty}a_n$ converge, entonces $a_n\to0$. **Demostración.** Para $n\ge1$, $a_n=S_n-S_{n-1}$; ambas sumas parciales tienen el mismo límite, de donde $a_n\to0$. $\square$

Si la suma tiene un límite, cada nuevo aporte debe tender a cero. Queda averiguar si esa condición controla también lo que aportan muchos términos juntos. La serie armónica mostrará que una cola puede conservar un tamaño apreciable aunque cada una de sus piezas sea pequeña.

## 8.2. La completitud y el criterio de Cauchy

**Teorema 8.1 (criterio de Cauchy para series; `EDC-C08-THM-001`).** Una serie real $\sum_{n=0}^{\infty}a_n$ converge si y sólo si, para todo $\varepsilon>0$, existe $N$ tal que

$$
\left|\sum_{n=p}^{q}a_n\right|<\varepsilon
\qquad\text{para cualesquiera enteros }q\ge p>N.
$$

**Demostración.** Una cola finita es la diferencia de dos sumas parciales: $\sum_{n=p}^{q}a_n=S_q-S_{p-1}$. Por tanto la condición del enunciado equivale a que dos sumas parciales suficientemente alejadas tengan una separación menor que cualquier tolerancia. Es la condición de Cauchy para la sucesión $(S_N)$; el desplazamiento del índice de $p$ a $p-1$ sólo modifica dónde comienza la cola.

Si $S_N\to S$, elegimos un índice a partir del cual cada suma diste de $S$ en menos que $\varepsilon/2$. La desigualdad triangular da entonces $|S_q-S_{p-1}|<\varepsilon$ para las colas correspondientes.

En sentido inverso, supongamos la condición de Cauchy. Primero obtenemos acotación: con tolerancia uno, todos los términos de una cola están a distancia menor que uno de un término fijo de ella. Los términos anteriores son una cantidad finita y también pueden acotarse. Bolzano–Weierstrass de C00 proporciona una subsucesión $S_{n_k}$ que converge a un número real $S$.

La condición de Cauchy permite extender ese límite a la sucesión entera. Dado $\varepsilon>0$, escogemos una cola donde dos términos cualesquiera disten en menos que $\varepsilon/2$. Elegimos después un término de la subsucesión que esté en esa cola y satisfaga $|S_{n_k}-S|<\varepsilon/2$. Para todo $S_n$ de la misma cola, $|S_n-S|\le|S_n-S_{n_k}|+|S_{n_k}-S|<\varepsilon$. Así todas las sumas parciales convergen a $S$. $\square$

El criterio permite buscar una suma sin conocerla de antemano: controla cuánto cambia cualquier suma parcial al añadir una cantidad finita de términos posteriores. La completitud de los reales, a través del resultado de C00, convierte ese control en existencia de un límite.

**Lema 8.2 (sumas de términos no negativos; `EDC-C08-LEM-002`).** Si $a_n\ge0$, la serie converge si y sólo si sus sumas parciales están acotadas superiormente. **Demostración.** Como $S_{N+1}-S_N=a_{N+1}\ge0$, las sumas parciales son no decrecientes. Si están acotadas, el teorema de convergencia monótona de C00 da su límite real. Una sucesión convergente está acotada. $\square$

## 8.3. El prototipo geométrico y el error de truncamiento

**Teorema 8.2 (serie geométrica; `EDC-C08-THM-002`).** Si $|q|<1$, entonces

$$
\sum_{n=0}^{\infty}q^n=\frac1{1-q},
\qquad
\left|\frac1{1-q}-\sum_{n=0}^{N}q^n\right|
=\frac{|q|^{N+1}}{|1-q|}.
$$

Si $|q|\ge1$, la serie no converge.

**Demostración.** Al multiplicar la suma finita por $1-q$, cada potencia intermedia se cancela con la siguiente. Para $q\ne1$ queda $(1-q)\sum_{n=0}^{N}q^n=1-q^{N+1}$. Si $|q|<1$, el resultado arquimediano usado en C04 asegura $q^{N+1}\to0$. Dividimos por $1-q$ y la identidad finita proporciona el límite $1/(1-q)$.

La misma identidad conserva el error: la diferencia entre el candidato y la suma parcial es $q^{N+1}/(1-q)$. Tomar módulos da el resto exacto del enunciado. Si $|q|\ge1$, los módulos de $q^n$ no tienden a cero, y el Lema 8.1 excluye convergencia, incluido $q=1$. $\square$

El resto decide hasta dónde puede usarse la fórmula infinita. Para una razón de módulo menor que uno, ese término desaparece; para las razones uno y menos uno, la sucesión de sumas parciales conserva el crecimiento o la alternancia que impiden un límite.

Como laboratorio numérico, con $q=1/2$ la suma parcial $1+1/2+\cdots+2^{-N}$ queda a distancia exacta $2^{-N}$ de $2$. En las aproximaciones de C04 el principio era el mismo, aunque allí había además que justificar que el área geométrica quedara encerrada entre figuras explícitas.

## 8.4. Comparación, potencias recíprocas y la serie armónica

**Teorema 8.3 (comparación de series positivas; `EDC-C08-THM-003`).** Sean $a_n,b_n\ge0$ para $n$ suficientemente grande. Si $a_n\le b_n$ eventualmente y $\sum b_n$ converge, entonces $\sum a_n$ converge. Si $a_n\le b_n$ eventualmente y $\sum a_n$ diverge, entonces $\sum b_n$ diverge.

**Demostración.** Elegimos un índice después del cual los términos sean no negativos y se cumpla la comparación. Las sumas parciales de esa cola de $a_n$ son no decrecientes y no superan las correspondientes de $b_n$. Si la serie de $b_n$ converge, estas últimas están acotadas, y el Lema 8.2 da un límite para la cola de $a_n$. Volver a añadir el prefijo finito sólo suma una constante y conserva convergencia.

La segunda afirmación se sigue por contraposición: si la serie mayor convergiera, la primera parte obligaría a converger a la menor. $\square$

**Proposición 8.1 (series $p$; `EDC-C08-PRP-001`).** Para $p>0$,

$$
\sum_{n=1}^{\infty}\frac1{n^p}
\begin{cases}\text{converge},&p>1,\\
\text{diverge},&0<p\le1.
\end{cases}
$$

**Demostración.** Agrupamos los índices por potencias de dos para comparar el número de términos de cada bloque con el tamaño de cada uno. Entre $2^k$ y $2^{k+1}-1$ hay $2^k$ índices. Si $p>1$, cada término es a lo sumo $(2^k)^{-p}$, y el bloque completo no supera $2^{-k(p-1)}$.

Esas cotas forman una serie geométrica de razón $2^{1-p}<1$. Cualquier suma parcial, aunque se detenga dentro de un bloque, no supera la suma de las cotas de los bloques completos que la contienen, porque todos los términos son positivos. Las sumas parciales quedan acotadas y el Lema 8.2 demuestra convergencia.

Para $p=1$, usamos una cota inferior en los mismos bloques. Cada uno de sus $2^k$ términos es mayor que $2^{-(k+1)}$, por lo que cada bloque aporta al menos $1/2$. Podemos reunir tantos bloques como queramos y hacer que las sumas parciales superen cualquier número fijado; la armónica diverge. Si $0<p<1$, tenemos $n^{-p}\ge n^{-1}$ para $n\ge1$, y la comparación con la armónica concluye. $\square$

La función $1/n$ **tiende a cero**, pero su serie diverge. Éste es el contraejemplo preciso que faltaba al Lema 8.1. La agrupación por potencias de dos también permite explicar históricamente algunos argumentos medievales sobre la armónica, sin identificar automáticamente la prueba moderna con un manuscrito particular; véanse las [notas H1](capitulo-08-notas.html).

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Los Bernoulli: una pregunta conduce a otra"}
*Lectura opcional.*

En la sección XVI del *Tractatus de seriebus infinitis*, Jakob Bernoulli presentó un argumento sobre la divergencia de la armónica y atribuyó el hallazgo a su hermano Johann. William Dunham reconstruye ese razonamiento y reproduce el pasaje: el argumento aprovechaba otra serie, la formada por $1/[n(n+1)]$, cuya suma podía calcularse. Una suma conocida ayudaba a investigar una que crecía sin límite.

La pregunta siguiente resultó distinta. En la sección XVII, Jakob estudió $1+1/4+1/9+\cdots$. Pudo establecer que convergía, pero encontrar su suma seguía resistiéndose. Invitó a quien la hallara a comunicársela. El contraste es cercano al que acabamos de encontrar: una comparación puede demostrar que hay un número finito sin decirnos todavía cuál es.

Podemos ver la utilidad de la serie auxiliar con operaciones finitas: $1/[n(n+1)]=1/n-1/(n+1)$, de modo que sus sumas parciales se cancelan hasta dejar $1-1/(N+1)$. El límite vale uno. La estructura de las piezas ofrece información que su simple tamaño no revelaba.

**Para seguir leyendo:** [William Dunham, *The Bernoullis and the Harmonic Series* (1987), pp. 19–23, con reproducción del *Tractatus*, § XVI](https://www.ms.uky.edu/~dhje223/Bernoullis.pdf).
:::

## 8.5. Convergencia absoluta, alternancia y reordenación

**Definición 8.2 (convergencia absoluta y condicional; `EDC-C08-DEF-002`).** La serie $\sum a_n$ converge *absolutamente* si converge $\sum|a_n|$. Es *condicionalmente convergente* si $\sum a_n$ converge pero $\sum|a_n|$ no.

**Teorema 8.4 (convergencia absoluta; `EDC-C08-THM-004`).** Toda serie absolutamente convergente converge. Además, para cada índice $N$,

$$
\left|\sum_{n=N+1}^{\infty}a_n\right|
\le\sum_{n=N+1}^{\infty}|a_n|.
$$

**Demostración.** La convergencia de la serie de módulos permite hacer pequeñas todas sus colas finitas por el criterio de Cauchy. Para cada una, la desigualdad triangular da $|\sum_{n=p}^{q}a_n|\le\sum_{n=p}^{q}|a_n|$. La misma elección de índice controla entonces las colas de la serie original y el Teorema 8.1 demuestra su convergencia.

Para estimar el resto fijamos $p=N+1$ y dejamos crecer $q$ en esa desigualdad finita. La primera suma converge al resto de la serie original y la segunda al resto de la serie de módulos, ambos ya existentes. La continuidad del módulo y la conservación del orden al pasar al límite dan la cota anunciada. $\square$

**Teorema 8.5 (criterio alternante; `EDC-C08-THM-005`).** Sean $b_n\ge0$, $b_{n+1}\le b_n$ y $b_n\to0$. Entonces $\sum_{n=1}^{\infty}(-1)^{n-1}b_n$ converge. Su suma $S$ queda entre dos sumas parciales consecutivas y el error tras $N$ términos satisface $|S-S_N|\le b_{N+1}$.

**Demostración.** Separamos las sumas parciales según su paridad. Añadir una pareja de términos a una suma par produce $S_{2k+2}-S_{2k}=b_{2k+1}-b_{2k+2}\ge0$, porque los tamaños no aumentan. Las sumas pares crecen. Para las impares, $S_{2k+3}-S_{2k+1}=-b_{2k+2}+b_{2k+3}\le0$, de modo que decrecen.

Cada suma par queda por debajo de la impar siguiente, cuya diferencia es $b_{2k+1}$. Las pares están acotadas superiormente por la primera suma impar y las impares inferiormente por las pares. La convergencia monótona de C00 da un límite para cada subsucesión; como su separación $b_{2k+1}$ tiende a cero, esos límites coinciden. Tanto los términos pares como los impares de $(S_N)$ se acercan al mismo número, luego la sucesión completa converge a él.

Los dos recorridos encierran el límite. Para cualquier $N$, éste queda entre $S_N$ y $S_{N+1}$, cuya distancia es $b_{N+1}$. La distancia de $S_N$ al límite no supera esa anchura y obtenemos la estimación de error. $\square$

La serie armónica alternante $1-1/2+1/3-\cdots$ converge por este teorema, pero **no absolutamente**, porque su serie de valores absolutos es la armónica. El orden de sumación exige entonces más cuidado que en el caso absoluto.

**Proposición 8.2 (reordenaciones absolutas; `EDC-C08-PRP-002`).** Si $\sum a_n$ converge absolutamente y $\pi:\mathbb N_0\to\mathbb N_0$ es biyectiva, entonces $\sum_{j=0}^{\infty}a_{\pi(j)}$ converge a la misma suma.

**Demostración.** Escribamos $S$ para la suma original. Dado $\varepsilon>0$, escogemos $N$ con $\sum_{n>N}|a_n|<\varepsilon/2$. Los términos hasta $N$ forman un conjunto finito; como $\pi$ es biyectiva, todos aparecen después de una cantidad finita de pasos en el nuevo orden. Existe por ello $M$ tal que $\{0,\ldots,N\}\subseteq\{\pi(0),\ldots,\pi(M)\}$.

Para $m\ge M$, la suma reordenada contiene el prefijo original completo y algunos términos de índices mayores. La diferencia entre esa suma y el prefijo tiene módulo menor que $\varepsilon/2$, porque es una selección finita de la cola de módulos. La diferencia entre $S$ y el mismo prefijo también tiene módulo menor que $\varepsilon/2$, por el Teorema 8.4. La desigualdad triangular hace que la suma reordenada diste de $S$ en menos que $\varepsilon$. $\square$

**Advertencia sobre convergencia condicional.** En la armónica alternante, los términos positivos $1/(2k-1)$ forman una serie divergente, pues superan $1/(2k)$; las magnitudes de los negativos suman también una serie divergente, la mitad de la armónica. Podemos usar esa disponibilidad para dirigir las sumas hacia un número real $L$.

Tomamos los positivos no usados, en su orden, hasta quedar por encima de $L$; después añadimos los negativos no usados hasta quedar por debajo. Cada paso termina en un número finito de adiciones porque la subserie correspondiente diverge. Repetimos indefinidamente. Tras el primer cruce, cada etapa consume al menos un término nuevo de su signo, así que los índices avanzan sin límite y todos los términos se usan exactamente una vez.

Al cruzar $L$, la distancia final no supera el módulo del último término añadido, porque justo antes del cruce estábamos del otro lado. Esos módulos tienden a cero. Las sumas intermedias se mueven monótonamente entre el cruce anterior y el siguiente, por lo que sus distancias también quedan controladas por ambos márgenes. Toda la sucesión converge a $L$. La libertad que la convergencia absoluta concedía al orden deja de estar disponible en este ejemplo condicional.

## 8.6. Tests de razón y de raíz: qué concluyen y qué no

**Teorema 8.6 (criterios de razón y raíz; `EDC-C08-THM-006`).** Sea $(a_n)$ una sucesión real.

1. Si $a_n\ne0$ para $n$ suficientemente grande y existe $\lim_{n\to\infty}|a_{n+1}/a_n|=L<1$, entonces $\sum a_n$ converge absolutamente. Si $L>1$, diverge porque sus términos no tienden a cero.
2. Si existe $\lim_{n\to\infty}|a_n|^{1/n}=L<1$, entonces $\sum_{n\ge1}a_n$ converge absolutamente. Si $L>1$, diverge.
3. Para $L=1$ ninguno de estos criterios decide, sin hipótesis nuevas, si la serie converge.

**Demostración.** Si el límite de los cocientes es $L<1$, elegimos una razón $q$ estrictamente entre $L$ y uno. La convergencia del cociente asegura un índice $N$ después del cual $|a_{n+1}|\le q|a_n|$. Repetir esta desigualdad da $|a_{N+k}|\le|a_N|q^k$. La cola de módulos queda dominada por una geométrica convergente, y la comparación demuestra convergencia absoluta.

Si $L>1$, escogemos $q$ entre uno y $L$. En una cola se cumple $|a_{n+1}|\ge q|a_n|$; como sus términos son no nulos, la repetición hace crecer sus módulos al menos geométricamente. No pueden tender a cero, y la condición necesaria excluye convergencia.

Para la raíz usamos la misma idea sin repetir cocientes. Si $L<1$, elegir $L<q<1$ da eventualmente $|a_n|^{1/n}\le q$ y por tanto $|a_n|\le q^n$. Si $L>1$, con $1<q<L$ obtenemos $|a_n|\ge q^n$ en una cola. La comparación o la condición necesaria concluyen según el caso.

Para $L=1$, ninguna elección estricta de una razón a un lado de uno queda asegurada por ese límite. Las series $\sum1/n$ y $\sum1/n^2$ tienen límites de cociente y de raíz iguales a uno, pero la primera diverge y la segunda converge. Para comprobar las raíces, usamos $0\le\ln n=\int_1^n dt/t\le\int_1^n dt/\sqrt t=2(\sqrt n-1)$, por C05–C07. Así $\ln n/n\to0$; la definición de potencia y la continuidad de la exponencial de C02 dan $(n^{-p})^{1/n}=\exp(-p\ln n/n)\to1$ para $p=1,2$. Estos ejemplos prueban que el valor uno no decide. $\square$

En ambos criterios, elegir $q$ permite pasar de un límite a una desigualdad que vale para todos los términos de una cola. La serie geométrica convierte esa desigualdad en un control de la suma.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Cauchy: preguntar por la suma antes de calcularla"}
*Lectura opcional.*

En la introducción de su *Cours d’analyse* de 1821, Cauchy explica que, antes de sumar una serie, necesita examinar en qué casos puede ser sumada. Esa decisión guía el capítulo VI: empieza con las sumas de un número finito de términos y llama suma al límite al que se acercan. La geométrica aparece enseguida como un ejemplo donde el término restante permite decidir la convergencia.

Para estudiar otras series, en el § II compara raíces y cocientes de términos consecutivos con uno. En la prueba del criterio de la raíz elige un número intermedio entre el límite y la unidad, y así encuentra una progresión geométrica con la que comparar los términos.

Hemos usado la misma maniobra: el límite del cociente o de la raíz permite escoger una razón fija $q<1$, y esa razón convierte la información sobre términos individuales en una cota para las colas. El número intermedio tiene un trabajo preciso: deja el margen necesario para que la comparación siga valiendo después de cierto índice.

**Para seguir leyendo:** [Cauchy, *Cours d’analyse* (1821), introducción y capítulo VI, §§ I–II; transcripción francesa en Wikisource](https://fr.wikisource.org/wiki/Cours_d’analyse_de_l’école_royale_polytechnique/Texte_entier).
:::

## 8.7. Una serie cuyos términos dependen de $x$

Una sucesión de polinomios $P_N(x)$ puede converger para ciertos valores de $x$ y divergir para otros. Por ejemplo,

$$
P_N(x)=\sum_{n=0}^{N}x^n=\frac{1-x^{N+1}}{1-x}
\quad(x\ne1).
$$

Para $|x|<1$ converge a $(1-x)^{-1}$; para $|x|\ge1$, el término general no tiende a cero. Así una fórmula finita produce una función sobre un **intervalo preciso**, no sobre todo su dominio algebraico aparente.

**Definición 8.3 (serie de potencias y radio; `EDC-C08-DEF-003`).** Para un centro $c\in\mathbb R$ y coeficientes reales $(a_n)_{n\ge0}$ consideramos la serie de potencias $\sum_{n=0}^{\infty}a_n(x-c)^n$. Definamos

$$
\mathcal D=\left\{r\ge0:\sum_{n=0}^{\infty}|a_n|r^n\text{ converge}\right\}
\quad(0^0:=1),
$$

con la convención $R=\infty$ si $\mathcal D$ no está acotado y $R=\sup\mathcal D$ en otro caso. Llamamos $R\in[0,\infty]$ **radio de convergencia**. La condición $r=0$ siempre pertenece a $\mathcal D$, porque sólo queda el término constante $a_0$.

**Teorema 8.7 (intervalo de convergencia; `EDC-C08-THM-007`).** La serie de potencias converge absolutamente cuando $|x-c|<R$ y diverge cuando $|x-c|>R$. Para $R=0$ sólo se garantiza la convergencia en $x=c$; para $R=\infty$ converge absolutamente para todo real. Si $0<R<\infty$, las dos fronteras $x=c\pm R$ se investigan **por separado**.

**Demostración.** Si la serie de módulos converge a una distancia $s>0$, converge también a cualquier distancia $0\le r<s$: cada término $|a_n|r^n$ no supera a $|a_n|s^n$. Por tanto $\mathcal D$ contiene todas las distancias menores que cualquiera de sus elementos.

Supongamos $r<R$. Si $R$ es finito, la propiedad del supremo proporciona $s\in\mathcal D$ con $r<s$; si $R=\infty$, lo proporciona la falta de cota superior. La comparación anterior da $r\in\mathcal D$, es decir, convergencia absoluta en toda distancia interior. El centro ya converge por definición, también cuando $R=0$.

Para excluir un punto exterior, supongamos que la serie converge con $t=|x-c|>R$. Sus términos tienden a cero y están acotados, así que existe $B$ con $|a_n|t^n\le B$. Si elegimos cualquier $0\le s<t$, obtenemos $|a_n|s^n\le B(s/t)^n$. La comparación geométrica coloca entonces $s$ en $\mathcal D$. Como podemos escoger $R<s<t$, contradice que $R$ sea una cota superior de ese conjunto. La convergencia exterior es imposible.

Cuando la distancia es exactamente $R$, no queda una razón $s/t<1$ que dé esta contradicción. Los dos puntos fronterizos conservan una pregunta propia. $\square$

**Ejemplo de extremos distintos.** La serie $\sum_{n=1}^{\infty}x^n/n$ tiene radio $1$: para $|x|<1$ converge por comparación geométrica; en $x=1$ es la armónica divergente, pero en $x=-1$ converge condicionalmente por alternancia. En contraste, $\sum_{n=1}^{\infty}x^n/n^2$ converge absolutamente en ambos extremos, mientras la geométrica $\sum_{n\ge0}x^n$ diverge en ambos. La expresión «radio uno» no codifica la respuesta en la frontera.

## 8.8. El control local que necesitamos: una cota explícita

**Teorema 8.8 (control interior y continuidad; `EDC-C08-THM-008`).** Sea $R>0$ el radio de una serie de potencias centrada en $c$ y escribamos $F(x)=\sum_{n=0}^{\infty}a_n(x-c)^n$ para $|x-c|<R$. Dados $0\le r<s<R$, pongamos $B_s=\sum_{n=0}^{\infty}|a_n|s^n<\infty$ y $q=r/s<1$. Para todo $N\ge0$ y $|x-c|\le r$,

$$
\left|F(x)-\sum_{n=0}^{N}a_n(x-c)^n\right|
\le\frac{B_s q^{N+1}}{1-q}.
$$

En particular, los polinomios parciales aproximan $F$ **con el mismo error controlado** en $[c-r,c+r]$, y $F$ es continua en $|x-c|<R$.

**Demostración.** Elegir $s$ mayor que $r$ nos deja una razón $q=r/s<1$. Como $B_s$ suma términos no negativos, cada uno satisface $|a_n|s^n\le B_s$. Para $|x-c|\le r$, podemos separar esa cota del factor que depende de la distancia y obtener

$$
\sum_{n=N+1}^{\infty}|a_n||x-c|^n
\le B_s\sum_{n=N+1}^{\infty}q^n
=\frac{B_sq^{N+1}}{1-q}.
$$

La primera suma acota el módulo del resto por convergencia absoluta, y la última igualdad es el resto geométrico del Teorema 8.2. El miembro final tiende a cero y no depende de $x$. Si $r=0$, sólo consideramos el centro y el resto tras el término constante es cero.

Para demostrar continuidad en $x_0$ escogemos $|x_0-c|<r<s<R$. Dado $\varepsilon>0$, tomamos un polinomio parcial $P_N$ cuyo error sea menor que $\varepsilon/3$ en todo $[c-r,c+r]$. Por continuidad del polinomio, podemos exigir $|P_N(x)-P_N(x_0)|<\varepsilon/3$ al acercar $x$ a $x_0$, manteniéndolo dentro de ese intervalo. Comparar $F(x)$ con $P_N(x)$, los dos valores de $P_N$, y $P_N(x_0)$ con $F(x_0)$ da tres errores cuya suma es menor que $\varepsilon$. Así $F$ es continua. $\square$

Un mismo índice de truncamiento controla todos los puntos del intervalo menor. Éste es el sentido concreto de la convergencia uniforme que usaremos: deja escoger el polinomio antes de escoger el punto. La estimación necesita espacio entre $r$ y el radio y sólo se ha probado en intervalos interiores.

## 8.9. Por qué podemos integrar y derivar una serie de potencias

**Lema 8.3 (límite de integrales con error controlado; `EDC-C08-LEM-003`).** Si $f_N,f$ son continuas en $[u,v]$ y $|f_N(t)-f(t)|\le\varepsilon_N$ allí para todo $t$, con $\varepsilon_N\to0$, entonces $\int_u^v f_N\to\int_u^v f$.

**Demostración.** La continuidad da existencia de ambas integrales. Para $u\le v$, la diferencia $f_N-f$ queda entre las constantes $-\varepsilon_N$ y $\varepsilon_N$. La linealidad y el orden de C05 producen

$$
\left|\int_u^v(f_N-f)\right|\le(v-u)\varepsilon_N
$$

y la linealidad identifica el miembro izquierdo con la diferencia absoluta de las dos integrales. La longitud está fija y $\varepsilon_N\to0$, luego esa diferencia tiende a cero. Si $v<u$, invertimos los extremos y usamos orientación; si coinciden, ambas integrales son cero. $\square$

**Teorema 8.9 (integración y derivación término a término; `EDC-C08-THM-009`).** Sea $R>0$, $F(x)=\sum_{n=0}^{\infty}a_n(x-c)^n$ para $|x-c|<R$. Entonces, para cada $x$ interior,

$$
\boxed{F'(x)=\sum_{n=1}^{\infty}n a_n(x-c)^{n-1}.}
$$

Y para todo segmento orientado con extremos $u,v$ en $(c-R,c+R)$,

$$
\boxed{\int_u^v F(t)\,dt
=\sum_{n=0}^{\infty}\frac{a_n}{n+1}
\bigl[(v-c)^{n+1}-(u-c)^{n+1}\bigr].}
$$

Ambas series de la derecha convergen en los puntos interiores indicados.

**Demostración.** Trabajamos primero en un intervalo cerrado interior $[c-r,c+r]$, con $0<r<s<R$. La distancia mayor $s$ permite acotar los coeficientes por $|a_n|s^n\le B_s$. Al derivar un monomio aparece un factor $n$, pero conserva una potencia de la razón $q=r/s<1$:

$$
|n a_n(x-c)^{n-1}|\le\frac{B_s}{s}\,n q^{n-1}.
$$

La serie de cotas $\sum_{n\ge1}nq^{n-1}$ converge: para $q>0$, el cociente de términos consecutivos tiende a $q<1$ y el Teorema 8.6 concluye; para $q=0$ sólo queda el primero. Así cualquier cola finita de la serie de derivadas se controla por una cola de esa serie numérica, independientemente de $x$. El criterio de Cauchy proporciona un límite $G(x)$ para cada punto, y las mismas colas acotan la diferencia entre $G$ y cualquier suma parcial de derivadas.

Esto también demuestra continuidad de $G$. Una suma parcial de derivadas es un polinomio continuo. Escogemos una cuya distancia a $G$ sea menor que $\varepsilon/3$ en todo el intervalo y usamos su continuidad para el error central entre dos puntos, igual que en el Teorema 8.8.

Ya existe una función continua $G$, pero falta identificarla como derivada de $F$. Para ello usamos una identidad que sí conocemos para cada polinomio parcial $P_N(x)=\sum_{n=0}^{N}a_n(x-c)^n$. El Teorema Fundamental de C06 da

$$
P_N(x)-P_N(c)=\int_c^x P_N'(t)\,dt.
$$

En la izquierda, $P_N(x)$ tiende a $F(x)$ y $P_N(c)=a_0$. En la derecha, el error común entre $P_N'$ y $G$ tiende a cero sobre todo el segmento que une $c$ con $x$. El Lema 8.3 permite pasar al límite en esas integrales. Obtenemos $F(x)=a_0+\int_c^xG(t)\,dt$.

La primera parte del Teorema Fundamental identifica ahora $F'=G$ en el interior de ese intervalo. Para cualquier punto con $|x-c|<R$ podemos escoger $r$ mayor que su distancia al centro y después $s$ mayor que $r$, todavía menor que $R$. La fórmula de derivación vale por ello en todos los puntos anunciados.

Para integrar elegimos del mismo modo un intervalo interior que contenga el segmento entre $u$ y $v$. El Teorema 8.8 controla en él el error entre $P_N$ y $F$, y el Lema 8.3 hace que $\int_u^vP_N$ converja a $\int_u^vF$. Cada integral polinómica se calcula por una suma finita de integrales de potencias y da exactamente la suma parcial de la fórmula del enunciado. Su límite demuestra la identidad y la convergencia de la serie derecha, también con extremos invertidos. $\square$

La integración permite identificar la derivada sin suponer de antemano que derivar conmute con un límite. Primero construimos el límite continuo de las derivadas polinómicas; después lo integramos y reconocemos a $F$ como su acumulación. El control común de las colas es lo que une esos pasos.

**Proposición 8.3 (unicidad de coeficientes; `EDC-C08-PRP-003`).** Si dos series de potencias con radio positivo y el mismo centro representan una misma función en un intervalo abierto alrededor del centro, entonces sus coeficientes coinciden. **Demostración.** Para determinar el coeficiente de grado $k$ queremos derivar $k$ veces y evaluar en el centro. Debemos justificar esas derivaciones: aunque los factores que aparecen crecen con $n$, para cada orden fijo podemos compararlos con una potencia geométrica en un intervalo menor.

Si $m\ge1$ y $|x-c|\le r<s<R$, la derivada de orden $m$ del monomio de grado $n\ge m$ queda acotada por

$$
\frac{B_s}{s^m}\,n(n-1)\cdots(n-m+1)\left(\frac rs\right)^{n-m}.
$$

Para $r>0$, el cociente de cotas consecutivas tiende a $r/s<1$, de modo que la serie de cotas converge. Podemos repetir el razonamiento del Teorema 8.9 por inducción: el límite de las derivadas de orden $m$ es continuo por el control común de colas, y su integral identifica el límite de orden $m-1$ como una acumulación. Esto autoriza la derivación de cada orden fijo. Si sólo evaluamos en $r=0$, queda el término de grado $m$.

Al evaluar en $c$ después de $k$ derivaciones, los monomios de grado menor han desaparecido y los de grado mayor todavía contienen una potencia positiva de $x-c$. Sólo el de grado $k$ aporta $k!a_k$. Para $k=0$ la evaluación original da $F(c)=a_0$. Así cada coeficiente está determinado por $F^{(k)}(c)/k!$.

Si las dos series representan la misma función cerca del centro, elegimos un intervalo menor dentro de ambos radios y dentro de esa región de igualdad. Sus derivadas de todos los órdenes coinciden allí, en particular en el centro, y por tanto coinciden todos sus coeficientes. $\square$

Cuando una representación por serie de potencias existe, sus coeficientes están obligados por las derivadas en el centro. Para una función dada, formar esos coeficientes deja todavía por comprobar que la serie converja y que su suma recupere la función. Esas serán dos preguntas distintas en C09.

## 8.10. Multiplicar series sin reordenar a ciegas

**Teorema 8.10 (producto de Cauchy; `EDC-C08-THM-010`).** Si $\sum_{n=0}^{\infty}a_n=A$ y $\sum_{n=0}^{\infty}b_n=B$ convergen absolutamente, definimos $c_k=\sum_{j=0}^{k}a_jb_{k-j}$. Entonces $\sum_{k=0}^{\infty}c_k$ converge absolutamente y vale $AB$.

**Demostración.** Llamemos $A_*=\sum|a_n|$ y $B_*=\sum|b_n|$, ambos finitos. Cada coeficiente $c_k$ reúne una cantidad finita de productos con índices que suman $k$. La desigualdad triangular da

$$
\sum_{k=0}^{N}|c_k|
\le\sum_{k=0}^{N}\sum_{j=0}^{k}|a_j||b_{k-j}|
\le A_*B_*.
$$

Para la última cota, los pares usados tienen ambos índices entre cero y $N$; sus productos de módulos forman una parte del producto de dos sumas finitas, cada una acotada por $A_*$ o $B_*$. Las sumas parciales de módulos de $c_k$ son no decrecientes y acotadas, de modo que el Lema 8.2 da convergencia absoluta.

Para identificar el valor comparamos dos sumas finitas. La suma $T_N=\sum_{k=0}^{N}c_k$ reúne los pares $i+j\le N$, mientras $A_NB_N$ reúne todos los pares $0\le i,j\le N$. Los pares adicionales están fuera del triángulo de índices del primer conjunto. Si ambos índices fueran a lo sumo $\lfloor N/2\rfloor$, su suma no superaría $N$; por tanto al menos uno supera ese umbral en todo par adicional.

Separamos las contribuciones según cuál índice lo supera. Las regiones pueden solaparse, pero al estimar con módulos contar dos veces sólo amplía la cota:

$$
|A_NB_N-T_N|\le B_*\sum_{i>\lfloor N/2\rfloor}|a_i|
+A_*\sum_{j>\lfloor N/2\rfloor}|b_j|\longrightarrow0.
$$

Las colas tienden a cero porque las dos series de módulos convergen. Por las reglas de límites de C00, $A_NB_N\to AB$. La diferencia recién controlada obliga entonces a que $T_N$ tenga ese mismo límite. $\square$

**Corolario 8.1 (producto de series de potencias; `EDC-C08-COR-001`).** Si $F(x)=\sum a_n(x-c)^n$ y $G(x)=\sum b_n(x-c)^n$ tienen radios positivos $R_F,R_G$, para $|x-c|<\min(R_F,R_G)$,

$$
F(x)G(x)=\sum_{k=0}^{\infty}
\left(\sum_{j=0}^{k}a_jb_{k-j}\right)(x-c)^k.
$$

**Demostración.** Fijamos un punto con $|x-c|<\min(R_F,R_G)$. El Teorema 8.7 da convergencia absoluta de ambas series numéricas en ese punto, y el Teorema 8.10 permite multiplicarlas. En cada coeficiente del producto, todos los monomios tienen grado total $k$, porque $(x-c)^j(x-c)^{k-j}=(x-c)^k$. La suma finita de sus coeficientes da la expresión anunciada. $\square$

La elección del punto dentro de ambos radios asegura la convergencia absoluta que la prueba necesita. Fuera de ese intervalo común tendremos que estudiar primero qué representan los factores y qué operaciones siguen justificadas.

## 8.11. Un ejemplo integrador: logaritmo y arctangente

La serie geométrica da, para $|x|<1$,

$$
\frac1{1+x}=\sum_{n=0}^{\infty}(-1)^n x^n.
$$

Por el Teorema 8.9, la integración desde $0$ hasta $x$, dentro del radio, es legítima. Como $(\ln(1+x))'=1/(1+x)$ y $\ln1=0$ (C02), resulta

$$
\boxed{\ln(1+x)=\sum_{n=1}^{\infty}
\frac{(-1)^{n-1}}{n}x^n\qquad(|x|<1).}
$$

En $x=1$ la serie de la derecha converge por alternancia, pero el intervalo de integración tocaría el borde del radio. La prueba interior no identifica por sí sola esa suma con $\ln2$. Para hacerlo habría que controlar el resto hasta el borde o dar otro argumento que cubra ese punto.

Análogamente, $1/(1+x^2)=\sum_{n=0}^{\infty}(-1)^n x^{2n}$ si $|x|<1$. Integrar desde cero y usar $\arctan0=0$ produce

$$
\arctan x=\sum_{n=0}^{\infty}
\frac{(-1)^n}{2n+1}x^{2n+1}\qquad(|x|<1).
$$

Para llegar a $x=1$ podemos usar un resto finito explícito. Para cada $N$ y $0\le t\le1$, la identidad geométrica da

$$
\frac1{1+t^2}=\sum_{n=0}^{N}(-1)^nt^{2n}
+\frac{(-1)^{N+1}t^{2N+2}}{1+t^2}
$$

Todos los términos de esta igualdad son continuos en el intervalo cerrado. Integramos la suma finita y dejamos el resto como una integral. Su módulo no supera la integral de $t^{2N+2}$, porque $1+t^2\ge1$, y ésta vale $1/(2N+3)$ por C06. Esa cota tiende a cero.

La integral de la izquierda es $\arctan1-\arctan0=\pi/4$. La de cada monomio de la suma finita es $(-1)^n/(2n+1)$. Así sus sumas parciales se aproximan a $\pi/4$ con el error indicado y obtenemos

$$
\boxed{\frac\pi4=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}.}
$$

La estimación cubre directamente el segmento cerrado hasta uno. A diferencia del control interior general, aquí el resto particular de la función racional permite alcanzar el punto fronterizo. Los antecedentes de la fórmula y sus distintos niveles de lectura se registran en las [notas H3–H5](capitulo-08-notas.html).

## 8.12. Qué queda demostrado y qué permanece abierto

Las sumas parciales permiten estudiar una expresión infinita con operaciones finitas y límites de C00. En las series de potencias, el control en un intervalo menor que el radio hizo posible construir una función continua y justificar sus derivadas e integrales. La convergencia absoluta permitió además comparar órdenes de sumación y productos mediante colas de módulos.

La cuestión de representar una función dada sigue abierta. Una serie puede converger y definir una función sin que hayamos probado que sea la que buscábamos; disponer de sus derivadas en un punto tampoco demuestra esa identificación. En C09 estudiaremos cómo reconocer la suma del binomio de Newton y cómo el resto de Taylor permite comparar una función con sus aproximaciones polinómicas. Las fuentes históricas de las series y de sus condiciones de uso se conservan en las notas separadas.

### Mapa de dependencias

- **De C00:** completitud de $\mathbb R$, Bolzano–Weierstrass, sucesiones de Cauchy por argumento directo, convergencia monótona y límites.
- **De C02–C03:** reglas de derivación y teorema del valor medio para funciones elementales; identificación de derivadas de logaritmo y arctangente.
- **De C04–C05:** identidades geométricas finitas, integral de Riemann–Darboux, linealidad, orden, estimaciones y orientación.
- **De C06–C07:** las dos partes del Teorema Fundamental para polinomios y funciones continuas, usadas **después** de construir cada serie y justificar las operaciones.
- **Aportaciones de C08:** `THM-001--010`, `LEM-001--003`, `PRP-001--003`, `COR-001`, definiciones de series y radio, y justificación local explícita de productos, derivadas e integrales.
- **No utilizado:** fórmula de Taylor, serie binomial de Newton para exponente general ni criterios de analiticidad de C09; métodos de EDO C10; Fourier, Lebesgue, complejidad funcional general.

### Trabajo del lector

Los [treinta ejercicios](capitulo-08-ejercicios.html) distinguen pruebas de convergencia, estimación de errores, reordenación, fronteras, productos y operaciones interiores con series de potencias. Las [soluciones completas](capitulo-08-soluciones.html) se presentan por separado, con dominio, hipótesis y cálculos razonados; la [documentación histórica](capitulo-08-notas.html) conserva el estado de verificación de cada referencia.
