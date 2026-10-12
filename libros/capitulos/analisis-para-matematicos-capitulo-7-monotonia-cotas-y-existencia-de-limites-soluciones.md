---
content-id: MA-BCH-0232
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-007-SOLUCIONES
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: Soluciones — Capítulo 7
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C07_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 7](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html) · [Ejercicios](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-microcontroles.html)

Las referencias numéricas remiten al banco principal de C07. En las construcciones se da una respuesta posible y se verifican todas las condiciones del enunciado.

## §7.1

### 1. Comparaciones y alcance de los cuantificadores

[]{#MA-EX-ANM-01-007-001}

[]{#MA-SOL-ANM-01-007-001}

[]{#MA-SEC-ANM-01-007-001}

La función $a$ es la sucesión; $n,m,n+1$ son índices naturales y $a_n,a_m,a_{n+1}$ son términos reales. Las desigualdades entre índices determinan qué posiciones se comparan; las desigualdades entre términos expresan la dirección de sus valores.

Si vale $P$ y fijamos $n\le m$, el caso $n=m$ da $a_n\le a_n$. Para $n<m$, la cadena finita $a_n\le a_{n+1}\le\cdots\le a_m$ da $a_n\le a_m$ por transitividad. Así se obtiene $Q$. Recíprocamente, $Q$ aplicada a $m=n+1$ da $P$ en cada índice. Por tanto, $P$ y $Q$ caracterizan el no decrecimiento.

El mismo razonamiento con desigualdades estrictas demuestra $R\Rightarrow S$: para $n<m$ hay al menos un paso y la cadena estricta llega de $a_n$ a $a_m$. Al tomar $m=n+1$, $S$ da $R$. Ambas caracterizan el crecimiento estricto. En $S$ no se incluye $n=m$, pues exigiría $a_n<a_n$, que es falso. En $Q$ sí puede incluirse, porque la desigualdad no estricta admite igualdad.

Toda desigualdad estricta implica la correspondiente no estricta, de modo que $R\Rightarrow P$. La sucesión constante $a_n=0$ satisface $P$ y $Q$, pero no $R$ ni $S$: sus términos de índices distintos también son iguales. La implicación inversa queda refutada.

$M$ es la definición de monotonía. Su disyunción permite una dirección universal o la otra, y admite ambas en una constante. $V$, en cambio, es verdadera para cualquier sucesión real, porque el orden total compara los dos términos en cada índice. En $r_n=(-1)^n$, $V$ sigue siendo verdadera, pero $r_0>r_1$ refuta la primera alternativa de $M$ y $r_1<r_2$ refuta la segunda. Por tanto, $M$ implica $V$ y $V$ no implica $M$. Permitir que la dirección cambie con el índice elimina la restricción que expresa la monotonía.

### 2. Las mismas alturas en otro orden

[]{#MA-EX-ANM-01-007-002}

[]{#MA-SOL-ANM-01-007-002}

Tomamos $a_n=2n$ y definimos $b_{2k}=4k+2$, $b_{2k+1}=4k$ para todo $k\in\mathbb N$. La paridad asigna a cada índice una única cláusula, de modo que $b$ está definida en todo $\mathbb N$. Ambas funciones tienen codominio $\mathbb R$ y valores en $E$.

Todo término de $a$ pertenece a $E$ y cada $2j\in E$ se obtiene en el índice $j$; así, $a(\mathbb N)=E$. Los términos de $b$ son $2(2k+1)$ y $2(2k)$, por lo que también pertenecen a $E$. Para la otra inclusión, si $j=2k$, el valor $2j=4k$ aparece en el índice $2k+1$; si $j=2k+1$, el valor $2j=4k+2$ aparece en el índice $2k$. Estas dos posibilidades cubren todo $j\in\mathbb N$, y prueban $E\subseteq b(\mathbb N)$. Por tanto, $b(\mathbb N)=E$.

Para todo $n$, $a_{n+1}-a_n=2>0$, así que $a$ es estrictamente creciente. En $b$, la caída $b_0=2>b_1=0$ refuta el no decrecimiento y la subida $b_1=0<b_2=6$ refuta el no crecimiento. Por eso $b$ no es monótona.

Las funciones son distintas porque $a_0=0$ y $b_0=2$. Sus gráficas, colecciones de pares $(n,a_n)$ y $(n,b_n)$, también son distintas: la primera contiene $(0,0)$ y la segunda no. Al formar el conjunto de valores se conserva la altura y se pierde la posición que la sucesión le asignaba. Las dos funciones tienen el mismo dominio, codominio y conjunto de valores, pero esa información no determina su evaluación en cada índice.

### 3. Bloques de longitud variable

[]{#MA-EX-ANM-01-007-003}

[]{#MA-SOL-ANM-01-007-003}

Usamos la división con resto de naturales: como $m>0$, cada $n\in\mathbb N$ se escribe de manera única como $n=mk+r$, con $k,r\in\mathbb N$ y $0\le r<m$. Definimos $a^{(m)}_n=k$, considerado como número real. La existencia de esa escritura cubre el dominio entero y su unicidad evita asignar dos valores al mismo índice. Para un $k$ fijo, el cociente es $k$ precisamente en los $m$ índices $mk,\ldots,mk+m-1$; los otros bloques tienen cocientes distintos.

Fijemos un índice $n=mk+r$. Si $r<m-1$, entonces $n+1=mk+(r+1)$ sigue en el mismo bloque, y $a^{(m)}_{n+1}=k=a^{(m)}_n$. Si $r=m-1$, entonces $n+1=m(k+1)$ comienza el bloque siguiente, y $a^{(m)}_{n+1}=k+1>k=a^{(m)}_n$. Los casos son exhaustivos y ambos dan $a^{(m)}_n\le a^{(m)}_{n+1}$. Queda probado el no decrecimiento en todo índice.

Para probar que no hay cota superior real, sea $U\in\mathbb R$ arbitrario. La propiedad arquimediana disponible desde C03 permite elegir $k\in\mathbb N$ con $k>U$. El índice $mk$ es natural y satisface $a^{(m)}_{mk}=k>U$. Como la construcción da un término que supera cada candidato $U$, ninguna cota superior real existe.

La sucesión no es estrictamente creciente: $m\ge2$ garantiza que $a^{(m)}_0=a^{(m)}_1=0$. Tampoco es no creciente, pues $a^{(m)}_{m-1}=0<1=a^{(m)}_m$. La repetición en cada bloque no afecta la definición de función: a cada índice se le asigna un solo valor, aunque varios índices compartan ese valor. Cuando $m=2$, la construcción recupera los pares repetidos de §7.1; el argumento de las fronteras sirve para todas las longitudes admitidas.

### 4. Una suma que no cambia

[]{#MA-EX-ANM-01-007-004}

[]{#MA-SOL-ANM-01-007-004}

La dirección común permite comparar incrementos del mismo signo. Para cada $n\in\mathbb N$, el no decrecimiento da $a_{n+1}-a_n\ge0$ y $b_{n+1}-b_n\ge0$. Al restar las igualdades de la suma en los índices $n+1$ y $n$, obtenemos

$$
(a_{n+1}-a_n)+(b_{n+1}-b_n)=c-c=0.
$$

Dos reales no negativos con suma cero deben ser ambos cero: si uno fuera positivo, al sumarle el otro la suma seguiría siendo positiva. Por tanto, $a_{n+1}=a_n$ y $b_{n+1}=b_n$ para todo $n$. La inducción desde el índice 0 da $a_n=a_0$ y $b_n=b_0$ en todos los índices. Cada sucesión es constante, y sus valores constantes satisfacen $a_0+b_0=c$.

Si las direcciones pueden ser distintas, los incrementos pueden cancelarse sin ser cero. Para cualquier $c\in\mathbb R$, las funciones $a_n=n$ y $b_n=c-n$ tienen suma $c$ en cada índice. La primera es estrictamente creciente y la segunda estrictamente decreciente; ninguna es constante. La hipótesis debilitada no implica la conclusión.

La conclusión original tampoco exige igualdad de las dos funciones. Por ejemplo, $a_n=c/2-1$ y $b_n=c/2+1$ son constantes, ambas no decrecientes y con suma $c$, pero difieren en cada índice. Bajo las hipótesis originales, $a=b$ se cumple si y sólo si $a_0=b_0$; junto con la suma, esto equivale a $a_0=b_0=c/2$. La constancia de cada función y la igualdad entre funciones son afirmaciones distintas.

## §7.2

### 5. Cota, barrera mínima y posición de alcanzamiento

[]{#MA-EX-ANM-01-007-005}

[]{#MA-SOL-ANM-01-007-005}

[]{#MA-SEC-ANM-01-007-002}

Si todos los términos son $\le U$, cada elemento $x\in S_a$ tiene la forma $x=a_n$ y pertenece a $(-\infty,U]$. Recíprocamente, la inclusión del conjunto implica $a_n\le U$ porque cada término pertenece a $S_a$. Para cualquier real $x$, $x\le U$ equivale a $x\notin(U,\infty)$; así, esa inclusión equivale a que la intersección indicada sea vacía. Se ha traducido una misma condición entre función, inclusión e intersección.

Para que la cota $s$ sea supremo se exige además que esté por debajo de toda cota superior. Con los dominios explícitos, las dos obligaciones son

$$
\bigl(\forall n\in\mathbb N,\ a_n\le s\bigr)
\quad\text{y}\quad
\forall U\in\mathbb R:\quad
\bigl(\forall n\in\mathbb N,\ a_n\le U\bigr)\Rightarrow s\le U.
$$

Si $s$ es máximo, domina todos los elementos y pertenece a $S_a$. La pertenencia proporciona un índice $j$ con $a_j=s$, así que $I_s$ es no vacío. Toda cota $U$ domina ese término y cumple $s\le U$; por ello $s$ es supremo. En la vuelta, si $s$ es supremo e $I_s$ es no vacío, $s$ domina el conjunto y pertenece a él por el índice testigo. Es, por definición, su máximo.

Para $d$, la imagen es $S_d=\{-1,4\}$. El número 6 es cota superior, pero no la menor, pues 4 también es cota y es menor que 6. Como 4 pertenece al conjunto y domina sus dos elementos, es máximo y supremo. Se alcanza precisamente en los índices $I_4=\{1,2,3,\ldots\}$. El máximo y el supremo son el mismo número real; $I_4$ es un conjunto de índices naturales y $S_d$ es un conjunto de valores reales. La sucesión $d$ es la función que asigna esos valores, no ninguno de esos conjuntos.

La [figura de la mejor barrera](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f02) permite comparar cota, supremo y alcanzamiento. Ilustra los valores 1 y 2 de otro ejemplo; los valores 4 y 6 de esta solución se justifican con sus propios datos.

### 6. Una barrera prescrita, con y sin alcanzamiento

[]{#MA-EX-ANM-01-007-006}

[]{#MA-SOL-ANM-01-007-006}

Para cada par de parámetros admitido, definimos funciones de $\mathbb N$ a $\mathbb R$ mediante $a^{s,h}_n=s-h/(n+1)$ y

$$
b^{s,h}_0=s,\qquad b^{s,h}_n=s-\frac hn\quad(n\ge1).
$$

Los denominadores son positivos en sus respectivos dominios; la cláusula especial de $b$ evita dividir por cero. Como $0\le h/(n+1)\le h$ y $0\le h/n\le h$ para $n\ge1$, todos los términos de ambas funciones están en $[s-h,s]$. En particular, $s$ es cota superior.

Sea $\varepsilon>0$. Si $h>0$, la arquimedianidad de C03 permite elegir $j\in\mathbb N$ con $j+1>h/\varepsilon$. Entonces $h/(j+1)<\varepsilon$ y $s-\varepsilon<a^{s,h}_j\le s$. Si $h=0$, el índice $j=0$ da la misma aproximación con error cero. Por la caracterización de §7.2, el supremo de la imagen de $a^{s,h}$ es $s$. Para $b^{s,h}$, el índice 0 proporciona directamente el término $s$ para toda tolerancia; junto con la cota, demuestra que su supremo también es $s$.

Cuando $h>0$, cada $h/(n+1)$ es positivo, así que ningún término de $a^{s,h}$ vale $s$; su imagen no tiene máximo. En $b^{s,h}$, el término inicial vale $s$ y todos los de índice $n\ge1$ son menores que $s$. El máximo se alcanza sólo en el índice 0. Si $h=0$, el intervalo permitido es $[s,s]=\{s\}$. Toda función que satisfaga la condición debe ser la constante $s$; nuestras dos fórmulas coinciden en esa función y alcanzan $s$ en todos los índices. La exigencia de alcanzamiento único se aplica únicamente al caso $h>0$.

### 7. Aproximar con una escala numerable

[]{#MA-EX-ANM-01-007-007}

[]{#MA-SOL-ANM-01-007-007}

Si $s=\sup S_a$, dado $k\in\mathbb N$ la tolerancia $1/(k+1)$ es positiva. La caracterización por aproximación proporciona un índice $j$ con $s-1/(k+1)<a_j\le s$, que equivale a $0\le s-a_j<1/(k+1)$. Queda probada la condición en cada $k$, incluido $k=0$.

Para la vuelta, conservamos la hipótesis de que $s$ domina todos los términos. Recibida una tolerancia real $\varepsilon>0$, usamos la arquimedianidad para elegir $k\in\mathbb N$ con $k+1>1/\varepsilon$. Así, $1/(k+1)<\varepsilon$. La condición del enunciado para ese $k$ da un índice $j$ con $0\le s-a_j<\varepsilon$, y por tanto $s-\varepsilon<a_j\le s$. La cota y la aproximación para toda tolerancia demuestran $s=\sup S_a$ por §7.2. La elección sigue el orden $\varepsilon$, luego $k$ y después un testigo $j$ para ese $k$; no se exige que el mismo $j$ sirva para todas las escalas, ni se ha probado control sobre los índices posteriores a él.

La hipótesis global de cota es necesaria. En $a_n=n$ y $s=0$, para cada $k$ el índice $j=0$ satisface $0\le s-a_j=0<1/(k+1)$. Sin embargo, $s$ no es cota superior, pues $a_1=1>0$, y por eso no puede ser supremo. El control del error en los términos elegidos no controla los demás términos.

### 8. Igual imagen acotada, distinto comportamiento

[]{#MA-EX-ANM-01-007-008}

[]{#MA-SOL-ANM-01-007-008}

Definimos $a_0=0$ y $a_n=1/n$ para $n\ge1$. Para la segunda función ponemos $b_{3k}=0$, $b_{3k+1}=1$ y $b_{3k+2}=1/(k+1)$ para todo $k\in\mathbb N$. Todo índice tiene una escritura única $3k+r$ con $r\in\{0,1,2\}$, así que las tres cláusulas definen $b$ en todo $\mathbb N$ sin ambigüedad. Todos los denominadores utilizados son positivos.

Cada término de $a$ está en $E$; 0 aparece en el índice 0 y el valor $1/(j+1)$ aparece en el índice $j+1$. Esto prueba $a(\mathbb N)=E$ por ambas inclusiones. En $b$, los valores 0 y 1 pertenecen a $E$, al igual que cada $1/(k+1)$, de modo que su imagen está contenida en $E$. Además, 0 aparece en el índice 0 y cada $1/(j+1)$ aparece en el índice $3j+2$. De ahí $E\subseteq b(\mathbb N)$ y la igualdad de imágenes. Ambas sucesiones satisfacen las cotas comunes $0\le a_n\le1$ y $0\le b_n\le1$ en todo índice.

Para $a_n\to0$, sea $\varepsilon>0$. Elegimos por arquimedianidad un natural $N>\max\{1,1/\varepsilon\}$. Si $n\ge N$, entonces $n\ge1$ y $|a_n|=1/n\le1/N<\varepsilon$. Este único corte controla todos los índices posteriores y prueba la convergencia a 0.

Para refutar todo límite real de $b$, fijemos un candidato $L\in\mathbb R$ y la tolerancia $\varepsilon_0=1/2$. Si $|L|\ge1/2$, ante cualquier corte $N\in\mathbb N$ el índice $n=3N\ge N$ da $|b_n-L|=|L|\ge\varepsilon_0$. Si $|L|<1/2$, la desigualdad triangular da $|1-L|\ge1-|L|>1/2$; el índice $n=3N+1\ge N$ tiene $b_n=1$ y también infringe la tolerancia. Los dos casos cubren todo candidato, y en cada uno existe un infractor después de cada corte. Por tanto, $b$ no converge a ningún número real, sin recurrir a resultados sobre subsucesiones.

Una permutación biyectiva de índices conserva cuántas posiciones toman cada valor. En $a$, el valor 1 aparece únicamente en el índice 1; en $b$ aparece en todos los índices $3k+1$, además del índice 2. Si $b_n=a_{\pi(n)}$ con $\pi:\mathbb N\to\mathbb N$ biyectiva, los índices distintos 1 y 4 de $b$ tendrían que satisfacer $\pi(1)=\pi(4)=1$, contradiciendo la inyectividad. La igualdad de conjuntos de valores permite cambiar multiplicidades; no convierte la construcción en una permutación de la sucesión convergente.

### 9. Un testigo convertido indebidamente en corte

[]{#MA-EX-ANM-01-007-009}

[]{#MA-SOL-ANM-01-007-009}

La premisa ofrece $\forall\varepsilon>0\ \exists j\in\mathbb N$ con $s-\varepsilon<a_j\le s$. La conclusión requiere $\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\in\mathbb N$, con $n\ge N\Rightarrow |a_n-s|<\varepsilon$. La inferencia defectuosa añade el control universal sobre $n\ge j$ sin una hipótesis que compare esos términos con $a_j$. La cota $a_n\le s$ sí vale para todos los índices; la comparación inferior $s-\varepsilon<a_n$ sólo se ha acreditado en el índice testigo.

Como contraejemplo, definimos $r_{3k}=3-1/(k+1)$, $r_{3k+1}=0$ y $r_{3k+2}=1$ para $k\in\mathbb N$. La división con resto por 3 hace la regla exhaustiva y única. Todos los valores son menores que 3: los de la primera cláusula están en $[2,3)$ y los otros son 0 y 1. Por tanto, 3 es cota y no se alcanza. Dada $\varepsilon>0$, elegimos $k$ con $k+1>1/\varepsilon$; en el índice $j=3k$ tenemos $3-\varepsilon<r_j<3$. La caracterización de §7.2 demuestra que $3=\sup S_r$ y que la imagen no tiene máximo.

El candidato 3 falla como límite: fijamos $\varepsilon_0=1$. Para cada $N\in\mathbb N$, el índice $n=3N+1\ge N$ cumple $r_n=0$ y $|r_n-3|=3\ge1$. Ningún corte controla esa tolerancia, aunque existan términos tan próximos al supremo como se pida.

Una reparación suficiente consiste en añadir que $a$ es no decreciente. Dada $\varepsilon>0$, la aproximación al supremo proporciona $j$ con $s-\varepsilon<a_j\le s$. Tomamos $N=j$. Para cualquier $n\ge N$, la comparación entre índices de §7.1 da $a_j\le a_n$ y la condición de cota da $a_n\le s$. Se obtiene $s-\varepsilon<a_j\le a_n\le s$, de donde $|a_n-s|=s-a_n<\varepsilon$. El índice testigo se ha convertido en corte gracias a la dirección añadida; este argumento comprueba directamente la definición de C06 y no invoca el teorema posterior. La reparación establece una condición suficiente, sin afirmar que sea necesaria para converger al supremo.

La [figura del testigo y la captura](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f03) distingue obtener un término próximo de controlar todos los posteriores. Ilustra el mecanismo válido bajo monotonía; no representa la trayectoria del contraejemplo de este ejercicio.

## §7.3

### 10. Reensamblar el argumento y localizar las hipótesis

[]{#MA-EX-ANM-01-007-010}

[]{#MA-SOL-ANM-01-007-010}

[]{#MA-SEC-ANM-01-007-003}

El orden es B, D, C, A. En B, $S_a\subseteq\mathbb R$ es no vacío porque contiene $a_0$, y $U$ lo domina porque domina todos los términos. En D se usa completitud, mediante el principio del supremo de C03: esas dos condiciones garantizan un real $s=\sup S_a$. La cota $U$ garantiza que el conjunto es admisible; el supremo $s$ será el candidato al límite. No se exige $U=s$.

En C fijamos $\varepsilon>0$. El número $s-\varepsilon$ no puede ser cota superior, pues suponerlo contradice la minimalidad de $s$. Negar $a_n\le s-\varepsilon$ para todos los índices da un $N\in\mathbb N$ con $a_N>s-\varepsilon$. Este paso usa la propiedad del supremo ya obtenido, no una nueva aplicación de completitud. En A, para cualquier $n\ge N$, el no decrecimiento y §7.1 dan $a_N\le a_n$; la condición de cota de $s$ da $a_n\le s$. Luego $0\le s-a_n<\varepsilon$ y $|a_n-s|=s-a_n<\varepsilon$. La definición de C06 queda satisfecha. El orden de elección es: candidato $s$ fijado por $a$, tolerancia $\varepsilon$, índice testigo $N$ y, después, índice arbitrario $n\ge N$.

En $w_n=2-1/(n+1)$, el denominador es positivo y $w_{n+1}-w_n=1/[(n+1)(n+2)]>0$. La sucesión es no decreciente y 2 es cota superior. Para toda $\eta>0$, la arquimedianidad permite elegir $j$ con $j+1>1/\eta$, lo que da $2-\eta<w_j<2$. La caracterización de §7.2 demuestra que el supremo es 2.

Con tolerancia 2, $N=0$ sirve: para todo $n\ge0$, $|w_n-2|=1/(n+1)\le1<2$. Con tolerancia 1 no sirve, porque el índice 0 tiene error 1 y la definición exige error menor que 1. El corte $N=1$ sí controla todos los índices posteriores, ya que $1/(n+1)\le1/2<1$. Un corte 0 es tan admisible como cualquier otro natural; lo que decide su validez es la estimación para todos los términos desde él.

La [figura del testigo y la captura](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f03) permite volver a localizar las obligaciones: completitud fija el candidato y monotonía propaga la comparación.

### 11. Una familia con denominador desplazado

[]{#MA-EX-ANM-01-007-011}

[]{#MA-SOL-ANM-01-007-011}

Los parámetros $\alpha,\beta,q$ son reales; el índice $n$ es natural y $a_n$ es un término real. Como $q>0$ y $n\ge0$, el denominador $n+q$ es positivo en todo el dominio, incluido $n=0$. La fórmula define una función de $\mathbb N$ a $\mathbb R$. Si se admitiese $q=0$, la fórmula no definiría el término inicial cuando se presenta como ese cociente, incluso si $\beta=0$.

La diferencia adyacente es

$$
a_{n+1}-a_n
=\frac{\beta}{n+q}-\frac{\beta}{n+1+q}
=\frac{\beta}{(n+q)(n+1+q)}\ge0.
$$

Por tanto, $a$ no decrece. Los denominadores positivos y $n+q\ge q$ dan $0\le\beta/(n+q)\le\beta/q$, así que $a_0=\alpha-\beta/q\le a_n\le\alpha$. Ya están acreditadas las hipótesis de §7.3: existe un límite real y es el supremo de $S_a$.

Si $\beta=0$, todos los términos valen $\alpha$, la dirección no es estricta y el supremo y el límite son $\alpha$. Si $\beta>0$, la diferencia adyacente es positiva en todo índice, de modo que la sucesión es estrictamente creciente; además, ningún término alcanza $\alpha$. Para identificar el supremo, sea $\varepsilon>0$. Elegimos por arquimedianidad un natural $N>\max\{0,\beta/\varepsilon-q\}$. Entonces $N+q>\beta/\varepsilon$ y $\alpha-\varepsilon<a_N<\alpha$. La cota superior $\alpha$ y esta aproximación demuestran $\sup S_a=\alpha$. El límite cuya existencia ya se obtuvo es, por ello, $\alpha$. La misma elección controla toda la cola: si $n\ge N$, $|a_n-\alpha|=\beta/(n+q)\le\beta/(N+q)<\varepsilon$.

### 12. Reconocer el supremo desde un límite ya conocido

[]{#MA-EX-ANM-01-007-012}

[]{#MA-SOL-ANM-01-007-012}

Fijemos $k\in\mathbb N$. Si $a_k>L$, tomamos $\varepsilon=(a_k-L)/2>0$. La convergencia proporciona un corte $N$ para esa tolerancia. El índice $n=\max\{k,N\}$ está después de $k$ y después del corte: la monotonía da $a_k\le a_n$ y la convergencia da $a_n<L+\varepsilon=(a_k+L)/2<a_k$. Las dos desigualdades se contradicen. Por tanto, $a_k\le L$ para cada $k$, y $L$ es cota superior de $S_a$.

Recibida ahora cualquier tolerancia $\eta>0$, la convergencia permite elegir un corte $M$ con $|a_M-L|<\eta$. En particular, $L-\eta<a_M$, mientras que la cota recién probada da $a_M\le L$. Así se cumplen cota y aproximación para el candidato $L$; por §7.2, $L=\sup S_a$.

No hizo falta suponer una cota adicional ni usar el teorema de §7.3 para fabricarla. En el primer argumento se fija $k$, se construye una tolerancia a partir del supuesto $a_k>L$, se obtiene $N$ y se elige un índice que reúna ambas exigencias. La convergencia se usa para impedir que un término por encima de $L$ pueda propagarse a todos los posteriores.

### 13. Recuperar la desigualdad estricta

[]{#MA-EX-ANM-01-007-013}

[]{#MA-SOL-ANM-01-007-013}

La tolerancia auxiliar debe ser menor que la tolerancia pedida. Sea $\varepsilon>0$ y tomemos $\delta=\varepsilon/2$. La hipótesis proporciona un índice $N=N_\delta$ con $s-\delta\le a_N$. Para todo $n\ge N$, §7.1 y la cota superior dan $s-\delta\le a_N\le a_n\le s$. Luego $|a_n-s|=s-a_n\le\delta=\varepsilon/2<\varepsilon$. Aunque el primer control admita igualdad, el margen reservado entre $\delta$ y $\varepsilon$ recupera el error estricto en toda la cola. Esto prueba $a_n\to s$ desde la definición.

También identifica el supremo sin circularidad. Para cada $\varepsilon>0$, ese mismo testigo satisface $a_N\ge s-\varepsilon/2>s-\varepsilon$. Junto con la cota global de $s$, la caracterización de §7.2 da $s=\sup S_a$.

Si se usase $\delta=\varepsilon$, sólo se obtendría error $\le\varepsilon$ desde el testigo, insuficiente para conservar ese corte. Por ejemplo, definamos $a_0=-1$ y $a_n=0$ para $n\ge1$. Es no decreciente y tiene supremo $s=0$, alcanzado desde el índice 1. La condición de aproximación no estricta se cumple para toda $\delta>0$, pues el índice 1 siempre sirve. Para $\delta=\varepsilon=1$, también es admisible el testigo $N_1=0$, ya que $s-1=-1=a_0$. Sin embargo, ese corte falla en la definición de convergencia con tolerancia 1: el término inicial tiene error 1. La elección $\delta=\varepsilon/2$ evita esta frontera para toda sucesión con las hipótesis indicadas.

La [figura de la frontera estricta](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f03) muestra por qué un punto en el borde no sirve con esa tolerancia. El margen auxiliar de esta prueba se obtiene por el argumento anterior, no de la muestra dibujada.

### 14. Sumar valores con el mismo índice

[]{#MA-EX-ANM-01-007-014}

[]{#MA-SOL-ANM-01-007-014}

Las imágenes $S_a,S_b$ son conjuntos reales no vacíos y acotados superiormente; C03 garantiza los reales $s,t$. La fórmula $c_n=a_n+b_n$ define una sucesión real en todos los índices. Como $a_n\le s$ y $b_n\le t$, tenemos $c_n\le s+t$: la suma de los supremos es cota superior de $S_c$.

Sea $\varepsilon>0$. La aproximación a cada supremo, con tolerancia $\varepsilon/2$, proporciona índices $j$ y $k$ tales que $s-\varepsilon/2<a_j$ y $t-\varepsilon/2<b_k$. Tomamos $N=\max\{j,k\}$. Las dos direcciones no decrecientes permiten reunir los testigos: $a_j\le a_N$ y $b_k\le b_N$. Al sumar, $s+t-\varepsilon<a_N+b_N=c_N\le s+t$. Por la caracterización de §7.2, $\sup S_c=s+t$. Elegir un índice común es necesario porque $S_c$ contiene sumas de términos evaluados en la misma posición.

Además, $c_n=a_n+b_n\le a_{n+1}+b_{n+1}=c_{n+1}$ para todo $n$. La sucesión $c$ es no decreciente y tiene la cota superior real $s+t$. §7.3 garantiza que converge a su supremo, por tanto $c_n\to s+t$.

Siempre $S_c\subseteq T$: cada valor $a_n+b_n$ suma un elemento de $S_a$ y uno de $S_b$. La inclusión puede ser estricta. Tomemos $a_0=b_0=0$ y $a_n=b_n=1$ para $n\ge1$. Las dos funciones son no decrecientes y están acotadas superiormente por 1. Sus imágenes son $\{0,1\}$, de modo que $T=\{0,1,2\}$, mientras que $S_c=\{0,2\}$. El valor 1 combina alturas disponibles en posiciones distintas y nunca aparece como suma con el mismo índice. La igualdad de supremos demostrada no exige igualdad de esos conjuntos.

### 15. Promedios finitos que conservan el destino

[]{#MA-EX-ANM-01-007-015}

[]{#MA-SOL-ANM-01-007-015}

Cada suma tiene $n+1$ términos reales y su denominador $n+1$ es positivo, incluido el índice 0. La fórmula define $c:\mathbb N\to\mathbb R$ y da $c_0=a_0$. Para $0\le j\le n$, §7.1 implica $a_0\le a_j\le a_n$. Al sumar las $n+1$ comparaciones y dividir por $n+1$, se obtiene $a_0\le c_n\le a_n\le s$.

El siguiente promedio se expresa como $c_{n+1}=((n+1)c_n+a_{n+1})/(n+2)$. Por tanto,

$$
c_{n+1}-c_n=\frac{a_{n+1}-c_n}{n+2}\ge0,
$$

porque $c_n\le a_n\le a_{n+1}$. Así, $c$ no decrece y tiene cota superior $s$. El teorema de §7.3 garantiza un límite real $t=\sup S_c$. El mismo teorema aplicado a $a$ da $a_n\to s$. Para identificar $t$, falta controlar cuánto pueden rebajar el promedio los términos iniciales.

Sea $\varepsilon>0$. La aproximación al supremo permite fijar $K\in\mathbb N$ con $s-\varepsilon/2<a_K\le s$. En un índice $n\ge K$, los primeros $K$ términos tienen errores $0\le s-a_j\le s-a_0$; los restantes, de índices $K,\ldots,n$, tienen errores $0\le s-a_j\le s-a_K$ por monotonía. Separando esas dos sumas finitas,

$$
0\le s-c_n
=\frac{\sum_{j=0}^{n}(s-a_j)}{n+1}
\le\frac{K(s-a_0)}{n+1}
+\frac{n-K+1}{n+1}(s-a_K)
\le\frac{K(s-a_0)}{n+1}+s-a_K.
$$

Después de fijar $K$, el número $D=K(s-a_0)$ es un real no negativo fijo. Elegimos por arquimedianidad un natural $N\ge K$ con $N+1>2D/\varepsilon$. Si $D=0$, puede tomarse $N=K$. Para todo $n\ge N$ se cumple $D/(n+1)<\varepsilon/2$, y la elección de $K$ da $s-a_K<\varepsilon/2$. Luego $|c_n-s|=s-c_n<\varepsilon$. Esto demuestra directamente $c_n\to s$; la unicidad del límite de C06 identifica el límite ya obtenido como $t=s$.

Si $K=0$, el prefijo separado es vacío y su suma y contribución son cero. La estimación sigue válida: todos los términos están en el bloque final y $s-c_n\le s-a_0<\varepsilon/2$. La prueba controla un prefijo de longitud fija y el bloque restante; no emplea sumas infinitas ni un teorema general de promedios.

## §7.4

### 16. Reflexión con una altura de referencia

[]{#MA-EX-ANM-01-007-016}

[]{#MA-SOL-ANM-01-007-016}

[]{#MA-SEC-ANM-01-007-004}

$b$ es una función de $\mathbb N$ a $\mathbb R$, y su conjunto de valores es $S_b=\{c-x:x\in S_a\}$. Cada término $b_n$ tiene esa forma; recíprocamente, si $x=a_j$, entonces $c-x=b_j$. La transformación conserva el índice y cambia el término real.

Para cada $n$, $a_n\le a_{n+1}$ equivale a $c-a_{n+1}\le c-a_n$, es decir, a $b_{n+1}\le b_n$. Al exigirlo en todos los índices, el no decrecimiento de $a$ equivale al no crecimiento de $b$. Del mismo modo, $a_{n+1}\le a_n$ equivale a $b_n\le b_{n+1}$; el no crecimiento de $a$ equivale al no decrecimiento de $b$. Las implicaciones son reversibles porque $a_n=c-b_n$.

Una cota inferior $\ell\le a_n$ se transforma en la cota superior $b_n\le c-\ell$, y una cota superior $a_n\le U$ en la cota inferior $c-U\le b_n$. También estas correspondencias son equivalencias. Si $t=\inf S_a$, $c-t$ es cota superior de $S_b$. Sea $V$ cualquier otra cota superior de $S_b$. Entonces $c-V$ es cota inferior de $S_a$, por lo que $c-V\le t$ y $c-t\le V$. Así $\sup S_b=c-t$. Si $s=\sup S_a$, $c-s$ es cota inferior de $S_b$. Toda cota inferior $v$ de $S_b$ da una cota superior $c-v$ de $S_a$; de $s\le c-v$ resulta $v\le c-s$. Por ello $\inf S_b=c-s$. No se requiere que los extremos sean términos.

Si $a_n\to L$, la identidad $|b_n-(c-L)|=|-(a_n-L)|=|a_n-L|$ muestra que el mismo corte sirve para la misma tolerancia, y prueba $b_n\to c-L$. En las gráficas discretas, $(n,a_n)$ se convierte en $(n,c-a_n)$: la coordenada horizontal no cambia y la altura se refleja respecto de $c/2$. La igualdad $a=b$ no es necesaria; se cumple exactamente cuando $a_n=c/2$ para todo $n$, pues $a_n=c-a_n$ equivale a $2a_n=c$. Por ejemplo, las constantes $a_n=c/2+1$ y $b_n=c/2-1$ son distintas.

La [figura de la reflexión](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f04) representa el caso de altura de referencia cero. El transporte con la altura arbitraria de este ejercicio se justifica mediante las identidades anteriores.

### 17. Un prefijo arbitrario y una barrera no alcanzada

[]{#MA-EX-ANM-01-007-017}

[]{#MA-SOL-ANM-01-007-017}

Definimos $a_n=x_n$ si $n<T$ y $a_n=L-h/(n-T+1)$ si $n\ge T$. Las cláusulas son disjuntas y cubren $\mathbb N$. En la segunda, $n-T$ es natural y el denominador es positivo. La restricción $a|_{D_T}$ tiene dominio $D_T$, mientras que la sucesión reindexada $v:\mathbb N\to\mathbb R$ tiene términos $v_k=a_{T+k}=L-h/(k+1)$. Sus conjuntos de valores son iguales: cada $v_k$ procede del índice $T+k$, y cada índice $n\ge T$ corresponde a $k=n-T$. Si $T=0$, los dominios también coinciden y $v=a$; si $T>0$, la restricción y $v$ tienen dominios distintos.

La diferencia $v_{k+1}-v_k=h/[(k+1)(k+2)]$ es positiva porque $h>0$. Además, $v_k<L$ para todo $k$. Para cada $\varepsilon>0$, la arquimedianidad permite elegir $k$ con $k+1>h/\varepsilon$, y entonces $L-\varepsilon<v_k<L$. Por §7.2, el supremo del conjunto de valores de la cola es $L$ y no se alcanza. El teorema eventual de §7.4 da $a_n\to L$. Explícitamente, un corte $K$ de $v$ se transfiere al corte $T+K$ de $a$.

Si $T>0$, el conjunto finito no vacío del prefijo tiene máximo $H=\max\{x_0,\ldots,x_{T-1}\}$. El número $G=\max\{H,L\}$ domina el prefijo y la cola, así que es cota superior global. Cualquier cota superior global $U$ domina el prefijo y por tanto $H\le U$; también domina la cola, por lo que su supremo cumple $L\le U$. Se sigue $G\le U$, y queda demostrado $\sup S_a=G$ por minimalidad.

Si $H<L$, el supremo global es $L$, pero ningún valor del prefijo ni de la cola lo alcanza; no hay máximo. Si $H=L$, el supremo es $L$ y se alcanza en los índices del prefijo cuyo valor es $H$; la cola no lo alcanza. Si $H>L$, el supremo es $H$ y también se alcanza en el prefijo, pues todos los términos de la cola son menores que $L<H$. En los dos últimos casos el supremo es máximo. Si $T=0$, no se define $H$: el conjunto global es el de la cola, tiene supremo $L$ y carece de máximo. El límite vale $L$ en todos los casos, aunque el prefijo pueda elevar el supremo global.

La [figura del prefijo y la cola](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f05) ilustra el caso T=1 con término inicial 10. La clasificación para el prefijo y el corte generales de este ejercicio procede de la prueba anterior.

### 18. Incorporar el prefijo a los extremos

[]{#MA-EX-ANM-01-007-018}

[]{#MA-SOL-ANM-01-007-018}

El conjunto de valores de la cola $Q$ es no vacío porque contiene $a_T$. Al estar acotado por ambos lados, C03 garantiza sus extremos reales $s,t$. El conjunto $P$ es finito, posiblemente vacío. Por tanto, $\{s\}\cup P$ y $\{t\}\cup P$ son finitos y no vacíos, y tienen máximo y mínimo respectivamente. Denotemos esos números por $G$ y $g$.

Como $S_a=P\cup Q$, todo valor del prefijo es $\le G$ por la definición del máximo finito, y todo valor de la cola es $\le s\le G$. Así $G$ es cota superior de $S_a$. Si $U$ es cualquier cota superior global, domina $P$ y domina $Q$; de lo segundo se obtiene $s\le U$. Luego $U$ domina todos los elementos de $\{s\}\cup P$, así que $G\le U$. Queda probada la minimalidad de $G$ y, por tanto, $G=\sup S_a$.

En la dirección inferior, cada valor del prefijo es $\ge g$ y cada valor de la cola es $\ge t\ge g$. Por ello $g$ es cota inferior global. Si $\ell$ es otra cota inferior global, está por debajo de todos los valores de $P$ y es cota inferior de $Q$, de modo que $\ell\le t$. Entonces está por debajo de todos los elementos de $\{t\}\cup P$, incluido su mínimo $g$. Esto prueba $\ell\le g$ y la maximalidad de $g$ como cota inferior; así $g=\inf S_a$.

Si $T=0$, $P=\varnothing$ y los conjuntos finitos son los singletones $\{s\}$ y $\{t\}$: las fórmulas dan directamente $\sup S_a=s$ e $\inf S_a=t$. La monotonía no se ha usado; sólo se requieren extremos de la cola y finitud del prefijo. Los números $s,t$ se añaden a los conjuntos auxiliares para calcular sus extremos finitos, sin añadirlos al conjunto de valores $Q$. Pueden no pertenecer a la cola.

### 19. Dos extensiones de la misma cola

[]{#MA-EX-ANM-01-007-019}

[]{#MA-SOL-ANM-01-007-019}

Para $n<T$, ponemos $a_n=u_0$. Para la otra extensión, fijamos $b_0=u_0+1$ y $b_n=u_0-1$ en los índices $1\le n<T$. Desde $T$, definimos $a_n=b_n=u_{n-T}$. La condición $T\ge2$ permite las dos primeras posiciones del prefijo, y todas las cláusulas quedan dentro de sus dominios. Las funciones resultantes están definidas en todo $\mathbb N$.

En $a$, las comparaciones interiores al prefijo son igualdades; la frontera también lo es, pues $a_{T-1}=u_0=a_T$. Desde $T$, las comparaciones son las de $u$. Así $a$ conserva globalmente cualquier dirección de monotonía que satisfaga $u$. En $b$, la caída $b_0=u_0+1>b_1=u_0-1$ refuta el no decrecimiento. La subida en la frontera $b_{T-1}=u_0-1<b_T=u_0$ refuta el no crecimiento. Ambos infractores existen incluso si $u$ es constante; $b$ no es monótona.

Si $u$ es no decreciente, su cota superior permite aplicar §7.3 y obtener $u_k\to L=\sup S_u$. Si es no creciente, su cota inferior permite aplicar §7.4 y obtener $u_k\to L=\inf S_u$. Si cumple ambas direcciones, es constante y esos dos extremos coinciden con su valor. Dada una tolerancia, un corte $K$ para $u$ se transfiere a $N=T+K$ para ambas extensiones: para $n\ge N$, el índice $k=n-T$ satisface $k\ge K$ y $a_n=b_n=u_k$. Por ello $a_n\to L$ y $b_n\to L$.

Con un único término de prefijo y una cola constante $u_k=d$, cualquier extensión tiene la forma $x,d,d,\ldots$. Si $x\le d$, es no decreciente; si $x\ge d$, es no creciente. Nunca puede refutar ambas direcciones. Dos posiciones de prefijo permiten garantizar los dos infractores para toda cola admitida. En nuestra construcción, las extensiones tienen igual restricción al dominio $D_T$ e igual límite, pero son funciones distintas porque $a_0=u_0\ne u_0+1=b_0$.

### 20. Mínimo y máximo de dos colas alineadas

[]{#MA-EX-ANM-01-007-020}

[]{#MA-SOL-ANM-01-007-020}

Sean $T_a,T_b$ cortes de no decrecimiento y $U_a,U_b$ cotas superiores globales. Tomamos $T=\max\{T_a,T_b\}$ y definimos $x_k=a_{T+k}$, $y_k=b_{T+k}$ en $\mathbb N$. Ambas funciones no decrecen y tienen sus respectivas cotas superiores. Sus imágenes son los conjuntos de valores de las colas desde $T$. Por §7.3 existen $s=\sup S_x$, $t=\sup S_y$, con $x_k\to s$ e $y_k\to t$; la transferencia de §7.4 da $a_n\to s$ y $b_n\to t$.

Las funciones originales $m,M$ tienen dominio $\mathbb N$ y codominio $\mathbb R$, pues mínimo y máximo de dos reales están definidos. Sus reindexaciones son $p_k=m_{T+k}=\min\{x_k,y_k\}$ y $q_k=M_{T+k}=\max\{x_k,y_k\}$. Para cada $k$, $p_k\le x_k\le x_{k+1}$ y $p_k\le y_k\le y_{k+1}$, de modo que $p_k\le\min\{x_{k+1},y_{k+1}\}=p_{k+1}$. Asimismo, $q_{k+1}$ domina $x_{k+1}\ge x_k$ e $y_{k+1}\ge y_k$, y por tanto domina su máximo $q_k$. Así $p,q$ no decrecen, y $m,M$ son eventualmente no decrecientes desde $T$.

Como $x_k\le s$ y $y_k\le t$, se obtiene $p_k\le v=\min\{s,t\}$ y $q_k\le w=\max\{s,t\}$. Para identificar estos candidatos como supremos de las imágenes alineadas, sea $\varepsilon>0$. La aproximación a $s$ y $t$ proporciona índices $j,\ell$ con $x_j>s-\varepsilon$ e $y_\ell>t-\varepsilon$. Tomamos $K=\max\{j,\ell\}$; la monotonía implica $x_K>s-\varepsilon$ e $y_K>t-\varepsilon$. Ambos términos son mayores que $v-\varepsilon$, por lo que $p_K>v-\varepsilon$. Para el máximo, si $s\ge t$, $q_K\ge x_K>s-\varepsilon=w-\varepsilon$; si $t>s$, $q_K\ge y_K>t-\varepsilon=w-\varepsilon$. Las cotas y estas aproximaciones prueban $\sup S_p=v$ y $\sup S_q=w$ por §7.2.

Aplicando §7.3 a $p,q$ y transfiriendo sus cortes desde $T$, resulta $m_n\to\min\{s,t\}$ y $M_n\to\max\{s,t\}$. En términos de los límites originales, son respectivamente $\min\{\lim a_n,\lim b_n\}$ y $\max\{\lim a_n,\lim b_n\}$. Además, las funciones completas están acotadas superiormente: $m_n\le a_n\le U_a$ y $M_n\le\max\{U_a,U_b\}$ en todo índice. La prueba usa los extremos de colas comunes, no supone que coincidan con los extremos globales afectados por prefijos. No se ha utilizado continuidad de mínimo o máximo ni una fórmula de límites para acreditar su propia existencia.

## §7.5

### 21. Superar una barrera y controlar una cola

[]{#MA-EX-ANM-01-007-021}

[]{#MA-SOL-ANM-01-007-021}

[]{#MA-SEC-ANM-01-007-005}

La ausencia de cota superior, obtenida al negar $\exists U\in\mathbb R\ \forall n\in\mathbb N:\ a_n\le U$, es $\forall M\in\mathbb R\ \exists j\in\mathbb N:\ a_j>M$. El escape por arriba exige

$$
\forall M\in\mathbb R\ \exists N\in\mathbb N\ \forall n\in\mathbb N:\quad n\ge N\Rightarrow a_n>M.
$$

La ausencia de cota inferior es $\forall M\in\mathbb R\ \exists j\in\mathbb N:\ a_j<M$. El escape por abajo exige

$$
\forall M\in\mathbb R\ \exists N\in\mathbb N\ \forall n\in\mathbb N:\quad n\ge N\Rightarrow a_n<M.
$$

Sus negaciones respectivas son $\exists M\in\mathbb R\ \forall N\in\mathbb N\ \exists n\in\mathbb N:\ n\ge N\ \text{y}\ a_n\le M$, y $\exists M\in\mathbb R\ \forall N\in\mathbb N\ \exists n\in\mathbb N:\ n\ge N\ \text{y}\ a_n\ge M$. En cada negación se fija una barrera antes de recibir cortes arbitrarios y se construye un infractor después de cada corte.

La ausencia de cota pide un término que supere la barrera en la dirección indicada. El escape pide un corte desde el que todos los términos la superen. Si $a$ no decrece, un testigo $a_j>M$ se propaga a cada $n\ge j$ por $a_j\le a_n$, y podemos tomar $N=j$. Si $a$ no crece, un testigo $a_j<M$ se propaga mediante $a_n\le a_j$ para $n\ge j$. Estas son las comparaciones que añaden el control universal de la cola. En sentido inverso, el escape por arriba o por abajo proporciona un testigo para ausencia de cota tomando $j=N$.

El corte puede depender de $M$, como indica el orden de cuantificadores. No puede haber un único corte $N$ para todas las barreras: por arriba, la barrera $M=a_N$ contradice el requisito $a_N>M$; por abajo, la misma barrera contradice $a_N<M$. Las barreras se cuantifican sobre todo $\mathbb R$, incluidos ambos signos, pues las definiciones no restringen las cotas ni las posiciones de los valores a una semirrecta. El índice $N$ es natural y el término $a_N$, usado como barrera en este argumento, es real.

### 22. Valores grandes con retornos arbitrariamente tardíos

[]{#MA-EX-ANM-01-007-022}

[]{#MA-SOL-ANM-01-007-022}

Definimos $a_{2k}=r+k$ y $a_{2k+1}=r$ para todo $k\in\mathbb N$. Todo índice tiene una única paridad, así que la regla define una función de $\mathbb N$ a $\mathbb R$.

Sea $U\in\mathbb R$ cualquier candidato a cota superior. La arquimedianidad permite elegir $k\in\mathbb N$ con $k>U-r$. Entonces el índice $2k$ tiene término $a_{2k}=r+k>U$. Por tanto, $a$ carece de cota superior. Para cada corte $N\in\mathbb N$, el índice $n=2N+1\ge N$ cumple $a_n=r$, de modo que las visitas a $r$ ocurren después de cualquier corte.

Fijamos la barrera $M=r$. Ante cualquier $N$, ese mismo índice $n=2N+1$ satisface $a_n=r\le M$, y refuta el requisito $a_n>M$ de toda una cola. Ésta es la negación cuantificada del escape por arriba, aunque la sucesión no tenga cota superior.

La propagación monótona no está disponible: por ejemplo, $a_2=r+1>a_3=r$. En general, los pasos de $2k$ a $2k+1$ con $k\ge1$ vuelven de $r+k$ a $r$. Encontrar un término grande no obliga a los posteriores a permanecer por encima de la barrera. La refutación se construye directamente por índices, sin usar teoría de subsucesiones.

### 23. Dos garantías de convergencia defectuosas

[]{#MA-EX-ANM-01-007-023}

[]{#MA-SOL-ANM-01-007-023}

La primera afirmación aporta una cota del lado equivocado. Para $u_n=r+hn$, con $h>0$, la diferencia adyacente es $h>0$ y todos los términos son $\ge r$. Sin embargo, ante cualquier barrera $M$, elegimos un natural $N>\max\{0,(M-r)/h\}$. Para todo $n\ge N$, $u_n\ge r+hN>M$. La familia escapa por arriba y, por §7.5, no tiene límite real. Una reparación suficiente consiste en exigir una cota superior además del no decrecimiento; §7.3 da entonces convergencia al supremo de los valores. La cota inferior ya está disponible en $u_0$ para toda sucesión no decreciente.

Para la segunda afirmación, definimos $v_{3k}=r-h$, $v_{3k+1}=r$ y $v_{3k+2}=r+h$. Las tres cláusulas cubren el dominio natural y todos los términos están en $[r-h,r+h]$. Los valores son distintos porque $h>0$. Fijemos un candidato $A\in\mathbb R$ y la tolerancia $h$. Si $A\ge r$, para cada corte $N$ el índice $n=3N$ tiene $|v_n-A|=A-r+h\ge h$. Si $A<r$, el índice $n=3N+2$ tiene $|v_n-A|=r+h-A>h$. Ambos índices están después del corte recibido, así que queda refutado todo candidato real. La acotación por sí sola no garantiza un límite. Una reparación suficiente es añadir monotonía global, o monotonía eventual usando §7.4 y las cotas del intervalo para la cola.

La falta de esa hipótesis de dirección no obliga a divergir. La familia $e_n=r+h(-1)^n/(n+2)$ está definida en todo $\mathbb N$ y converge a $r$: dada $\varepsilon>0$, elegimos un natural $N>h/\varepsilon$; para $n\ge N$, $|e_n-r|=h/(n+2)\le h/(N+2)<\varepsilon$. No es eventualmente monótona. Después de cualquier corte $T$, $e_{2T}>r>e_{2T+1}$ refuta el no decrecimiento, y $e_{2T+1}<r<e_{2T+2}$ refuta el no crecimiento. Los contraejemplos anteriores muestran que las premisas defectuosas no aseguran convergencia; no establecen que toda sucesión ajena a la garantía monótona carezca de límite.

La [figura de las hipótesis](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f06) contrapone dirección sin cota, acotación sin convergencia y convergencia sin monotonía eventual. La comparación recuerda qué garantía se pierde al retirar una hipótesis.

### 24. Una tolerancia de refutación prescrita

[]{#MA-EX-ANM-01-007-024}

[]{#MA-SOL-ANM-01-007-024}

Fijada $\varepsilon_0>0$, recibamos un candidato $A\in\mathbb R$. El escape por arriba aplicado a $M=A+\varepsilon_0$ proporciona un corte $T$ tal que $a_n>A+\varepsilon_0$ para todo $n\ge T$. Ante cualquier corte propuesto $K\in\mathbb N$, tomamos $n=\max\{K,T\}$. Entonces $n\ge K$ y $|a_n-A|=a_n-A>\varepsilon_0$, lo que en particular cumple $|a_n-A|\ge\varepsilon_0$.

En escape por abajo usamos $M=A-\varepsilon_0$. Obtenemos $T$ con $a_n<A-\varepsilon_0$ para todo $n\ge T$ y, después de recibir $K$, elegimos de nuevo $n=\max\{K,T\}$. Se cumple $n\ge K$ y $|a_n-A|=A-a_n>\varepsilon_0$. En cualquiera de los dos casos hemos probado, para la tolerancia prescrita,

$$
\forall A\in\mathbb R\ \forall K\in\mathbb N\ \exists n\in\mathbb N:\quad n\ge K\ \text{y}\ |a_n-A|\ge\varepsilon_0.
$$

La tolerancia se fija al comienzo; el candidato determina la barrera y el corte de escape $T$ puede depender de ambos. El índice infractor se elige después del corte propuesto $K$, al reunirlo con $T$. La definición de convergencia exige error estrictamente menor que la tolerancia, de modo que un error igual a $\varepsilon_0$ también bastaría para refutarla. Aquí se obtiene una desigualdad mayor. El argumento excluye todos los candidatos reales y no requiere monotonía: usa sólo la propiedad de escape, cualquiera que haya sido el método para demostrarla.

### 25. Escape y monotonía eventual no son conversas

[]{#MA-EX-ANM-01-007-025}

[]{#MA-SOL-ANM-01-007-025}

Para cada real fijo $c$, la fórmula asigna un único término real a cada índice natural. Como $c(-1)^n\ge-|c|$, se cumple $a^{(c)}_n\ge n-|c|$. Dada una barrera $M\in\mathbb R$, elegimos por arquimedianidad un natural $N>M+|c|$. Para todo $n\ge N$, $a^{(c)}_n\ge N-|c|>M$. Por tanto, todas las sucesiones de la familia escapan por arriba, con corte dependiente de $M$ y del parámetro fijo $c$.

La diferencia adyacente es

$$
a^{(c)}_{n+1}-a^{(c)}_n=1-2c(-1)^n
=\begin{cases}1-2c,&n\text{ par},\\1+2c,&n\text{ impar}.\end{cases}
$$

El no decrecimiento exige $1-2c\ge0$ y $1+2c\ge0$, equivalentes a $-1/2\le c\le1/2$. El crecimiento estricto exige ambas desigualdades estrictas y equivale a $-1/2<c<1/2$. Para $c=1/2$, los pasos de índice par son igualdades y los de índice impar tienen incremento 2. Para $c=-1/2$, los pasos de índice impar son igualdades y los de índice par tienen incremento 2. En ambos extremos la sucesión no decrece, pero no es estrictamente creciente.

El no crecimiento exigiría $1-2c\le0$ y $1+2c\le0$, es decir, simultáneamente $c\ge1/2$ y $c\le-1/2$, imposible. Estas clasificaciones no cambian al restringirse a una cola: después de todo corte $T$ hay un índice par $2T$ y uno impar $2T+1$, así que ambos incrementos vuelven a aparecer. En particular, los pasos de igualdad en los valores frontera impiden crecimiento estricto también eventualmente. Ningún parámetro permite no crecimiento eventual.

Para $c>1/2$, después de cualquier $T$ el paso de $2T$ a $2T+1$ tiene incremento negativo y refuta el no decrecimiento; el paso de $2T+1$ a $2T+2$ tiene incremento positivo y refuta el no crecimiento. Para $c<-1/2$, el paso par tiene incremento positivo y el impar negativo, por lo que refutan las direcciones opuestas. Los infractores aparecen después de cualquier corte; en esos parámetros no existe una cola monótona. Por ejemplo, $c=1$ da escape por arriba sin monotonía eventual, y refuta la conversa propuesta.

El escape frente a todas las barreras reales no es convergencia a un número real. La refutación de §7.5, o la versión con tolerancia prescrita del ejercicio 24, excluye todo candidato real para cada parámetro de la familia. Los términos y el codominio siguen siendo reales; el escape describe una condición sobre colas y barreras.

## §7.6

### 26. Una combinación que conserva el lado de una barrera

[]{#MA-EX-ANM-01-007-026}

[]{#MA-SOL-ANM-01-007-026}

[]{#MA-SEC-ANM-01-007-006}

**Control antes del cálculo.** La regla afín produce un único real en cada paso, sin denominadores variables. Las dos identidades útiles son

$$
v_{n+1}-c=\lambda(v_n-c),\qquad v_{n+1}-v_n=(1-\lambda)(c-v_n).
$$

Si $r<c$, la primera identidad conserva $v_n<c$ por inducción porque $\lambda>0$. La segunda da incremento positivo porque $1-\lambda>0$. Por tanto $r\le v_n<c$ y §7.3 garantiza un límite real. Si $r>c$, se conserva $v_n>c$, el incremento es negativo y $c<v_n\le r$; §7.4 garantiza un límite. Si $r=c$, la inducción da $v_n=c$ para todo $n$, con límite $c$.

**Identificación.** En los dos casos no constantes ya existe $L\in\mathbb R$. Desplazamiento, suma y multiplicación por escalares de C06 dan $L=\lambda L+(1-\lambda)c$. Como $1-\lambda\ne0$, resulta $L=c$. Así, las tres sucesiones convergen a $c$; los casos estrictos no alcanzan ese valor en ningún índice. La completitud interviene mediante el teorema monótono, antes de resolver la ecuación.

### 27. Una ecuación necesaria presentada como garantía

[]{#MA-EX-ANM-01-007-027}

[]{#MA-SOL-ANM-01-007-027}

La regla define una sucesión real en todos los índices. La inducción da

$$
a_{2k}=c+h,\qquad a_{2k+1}=c-h\quad(k\in\mathbb N).
$$

En efecto, el paso transforma $c+h$ en $c-h$ y viceversa. El razonamiento sólo obtiene una condición necesaria bajo la hipótesis $a_n\to A$. Desplazamiento y operaciones de C06 permitirían entonces $A=2c-A$, luego $A=c$. Falta demostrar que tal límite existe; la unicidad de la solución de una ecuación no suple esa obligación.

Para cualquier candidato $A\in\mathbb R$, fija $\varepsilon_0=h$. Dado cualquier $N\in\mathbb N$, si $A\le c$ elige $n=2N$, para el que $|a_n-A|=c+h-A\ge h$. Si $A>c$, elige $n=2N+1$ y obtiene $|a_n-A|=A-c+h>h$. En ambos casos $n\ge N$ y falla el error estrictamente menor que $\varepsilon_0$. No hay límite real. Con $a_0=c$, la inducción produce la sucesión constante de valor $c$, y la existencia sí queda acreditada.

### 28. Descenso desde un dato inicial variable

[]{#MA-EX-ANM-01-007-028}

[]{#MA-SOL-ANM-01-007-028}

**Construcción e invariante.** Si $y_n>0$, el inverso existe y la regla produce un único $y_{n+1}>0$. La base $r>0$ permite esta inducción para todos los índices. Para cada término construido,

$$
y_{n+1}^2-2=\frac{(y_n^2-2)^2}{4y_n^2},\qquad
y_{n+1}-y_n=\frac{2-y_n^2}{2y_n}.
$$

La base $r^2>2$, la primera identidad y el denominador positivo conservan $y_n^2>2$ estrictamente: el numerador nunca es cero. Como $y_n>0$, se deduce $y_n>1$, pues $0<y_n\le1$ implicaría $y_n^2\le1$. La segunda identidad tiene numerador negativo y denominador positivo, luego $y$ es estrictamente decreciente y $1<y_n\le r$.

**Existencia y destino.** §7.4, que recibe aquí la completitud real, da $y_n\to L$. El orden de límites de C06 da $L\ge1$, de modo que $L\ne0$. Ahora están verificadas las hipótesis del cociente: los denominadores son no nulos y su límite también. Por desplazamiento y operaciones de límites,

$$
L=\frac{L+2/L}{2},\qquad L^2=2,\qquad L>0.
$$

El único real positivo con ese cuadrado es $R=\sqrt2$, construido en §7.6: si $q>0$ y $q^2=2$, $(L-q)(L+q)=0$ y $L+q>0$ fuerzan $L=q$. Finalmente $(y_n-L)(y_n+L)=y_n^2-2>0$, con segundo factor positivo, da $y_n>L$ para todo $n$. Ningún término alcanza el límite.

La [figura del invariante](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f07) ilustra el dato inicial 2. Para el dato variable de este ejercicio, positividad, invariante y dirección se acreditan con la prueba anterior.

### 29. Cruzar la barrera en el primer paso

[]{#MA-EX-ANM-01-007-029}

[]{#MA-SOL-ANM-01-007-029}

Todos los términos se construyen positivos como en 28. Sea $R>0$ la raíz de 2 construida en §7.6. Si $r^2<2$, la positividad da $r<R$. Además,

$$
y_1-r=\frac{2-r^2}{2r}>0,\qquad
y_1^2-2=\frac{(r^2-2)^2}{4r^2}>0.
$$

Por tanto $y_1>R$ y $y_1>r$. Desde el índice 1, el argumento de 28 conserva cuadrado mayor que 2, descenso estricto y cota inferior 1. La sucesión $b_k=y_{k+1}$, con dominio $\mathbb N$, cumple exactamente las hipótesis de 28; converge a $R$. La transferencia de una cola de C06 da $y_n\to R$. La sucesión completa no es no creciente porque $y_1>y_0$, ni no decreciente porque $y_2<y_1$: sólo la cola desde 1 es decreciente.

Si $r^2=2$, entonces $2/r=r$ y la regla conserva $y_n=r=R$ por inducción. La sucesión es constante.

La clasificación positiva queda completa: $r>R$ produce descenso estricto global por encima de $R$; $0<r<R$ produce una subida inicial que cruza $R$ y después descenso estricto por encima de $R$; $r=R$ produce constancia. En todos los casos el límite es $R$.

### 30. Construir la raíz de un parámetro positivo

[]{#MA-EX-ANM-01-007-030}

[]{#MA-SOL-ANM-01-007-030}

**Construir sin conocer el destino.** La base $x_0=r>0$ y la positividad de $\rho/x_n$ cuando $x_n>0$ construyen todos los términos positivos. Las identidades algebraicas son

$$
x_{n+1}^2-\rho=\frac{(x_n^2-\rho)^2}{4x_n^2},\qquad
x_{n+1}-x_n=\frac{\rho-x_n^2}{2x_n}.
$$

Por inducción desde $r^2>\rho$, la primera conserva la desigualdad estricta; la segunda implica descenso estricto. Para una barrera independiente de una raíz, fija $m=\min\{1,\rho\}$. Si $\rho\ge1$, $0<x_n\le1$ implicaría $x_n^2\le1\le\rho$, imposible. Si $0<\rho<1$, $0<x_n\le\rho$ implicaría $x_n^2\le\rho^2<\rho$, también imposible. Así $0<m<x_n\le r$.

**Existencia antes de la ecuación.** §7.4 aplica monotonía, cota y completitud para dar un límite $L$. Por orden de límites, $L\ge m>0$. Sólo ahora pueden usarse el cociente, suma, escalar y desplazamiento de C06 para obtener

$$
L=\frac{L+\rho/L}{2},\qquad L^2=\rho.
$$

La construcción ha demostrado la existencia de un real positivo con ese cuadrado. Si $q>0$ también satisface $q^2=\rho$, entonces $(L-q)(L+q)=0$ y $L+q>0$ dan $q=L$: es único. Finalmente $(x_n-L)(x_n+L)=x_n^2-\rho>0$ da $x_n>L$. La barrera $m$ acreditó la no anulación del límite; la sola positividad de los términos no habría bastado.

### 31. Datos negativos y una prescripción que no define sucesión

[]{#MA-EX-ANM-01-007-031}

[]{#MA-SOL-ANM-01-007-031}

Para $r<0$, pon $z_0=-r>0$ y construye la sucesión positiva $z$ por la regla de 28–29. Define $y_n=-z_n$. Es una sucesión $\mathbb N\to\mathbb R$ de términos negativos, ninguno cero, y

$$
\frac{y_n+2/y_n}{2}=-\frac{z_n+2/z_n}{2}=-z_{n+1}=y_{n+1}.
$$

Así cumple la prescripción original; en cada paso la regla determina un único real. La reflexión invierte las desigualdades y el límite es $-R$, donde $R=\sqrt2$.

Si $r^2>2$, 28 da $z_n>R$ y descenso estricto global. Por reflexión, $y_n<-R$ y $y$ crece estrictamente hacia $-R$ en todos los índices.

Si $r^2<2$, tenemos $r>-R$. Por 29, $z_1>z_0$ y $z_1>R$, luego $y_1<y_0$ y $y_1<-R$. Desde el índice 1, $y$ crece estrictamente, siempre por debajo de $-R$. No es monótona globalmente: tiene una bajada inicial y después subidas estrictas. La regla del escalar de C06 o la transferencia de la cola justifican su límite $-R$.

Si $r^2=2$, el dato negativo es $r=-R$ y la sucesión es constante por reflexión del caso positivo constante.

Con $r=0$, el cálculo de $y_1$ exige $2/0$, que no es un real definido. La prescripción no produce una función $\mathbb N\to\mathbb R$. La divergencia es una propiedad de una sucesión que sí está definida; aquí falta el objeto al que se atribuiría esa propiedad.

### 32. Dos trayectorias ordenadas con un destino común

[]{#MA-EX-ANM-01-007-032}

[]{#MA-SOL-ANM-01-007-032}

La función $F$ tiene dominio $(0,\infty)$ y codominio $(0,\infty)$; sus argumentos $x,t$ son valores reales, no índices. Como ambos son no nulos,

$$
F(x)-F(t)=\frac{x-t+2(1/x-1/t)}2
=\frac{x-t}{2}\left(1-\frac2{xt}\right).
$$

Si $x,t>R>0$, entonces $xt>R^2=2$, de modo que el factor $1-2/(xt)$ es estrictamente positivo. Por tanto el signo de la diferencia de los pasos coincide con el signo de $x-t$ en esa región.

Por 28, las sucesiones $y,z$ están bien definidas, todos sus términos son mayores que $R$ y ambas convergen a $R$. La base $y_0=r<s=z_0$ y la identidad, aplicada con $x=z_n$ y $t=y_n$, dan

$$
z_{n+1}-y_{n+1}=\frac{z_n-y_n}{2}\left(1-\frac2{z_ny_n}\right)>0
$$

si $z_n-y_n>0$. La inducción demuestra $y_n<z_n$ para todo $n\in\mathbb N$. Son funciones distintas desde sus evaluaciones en 0, aunque el número que es su límite sea el mismo. La igualdad de límites no es igualdad de sucesiones. Si $r=s>R$, la igualdad inicial y la misma regla determinista dan $y_n=z_n$ por inducción: en ese caso sí son la misma función. No se ha utilizado una estimación de velocidad.

## §7.7

### 33. Una iteración racional y su inclusión real

[]{#MA-EX-ANM-01-007-033}

[]{#MA-SOL-ANM-01-007-033}

[]{#MA-SEC-ANM-01-007-007}

**Tipos y construcción.** Los objetos son

$$
q:\mathbb N\to\mathbb Q,\qquad \iota:\mathbb Q\to\mathbb R,\qquad
\widetilde q=\iota\circ q:\mathbb N\to\mathbb R.
$$

El índice $n$ es natural; $q_n$ es un valor racional. La base $r$ es racional positiva. Si $q_n\in\mathbb Q$ y $q_n>0$, su inverso existe en $\mathbb Q$; $\rho/q_n$ es racional positivo y la suma y la mitad también lo son. Esto construye un único término racional positivo en cada paso, sin denominadores nulos.

Dentro de $\mathbb Q$, el álgebra da

$$
q_{n+1}^2-\rho=\frac{(q_n^2-\rho)^2}{4q_n^2},\qquad
q_{n+1}-q_n=\frac{\rho-q_n^2}{2q_n}.
$$

La base $r^2>\rho$ y la primera identidad conservan $q_n^2>\rho$ estrictamente. La segunda tiene numerador negativo y denominador positivo: $q$ es estrictamente decreciente. El argumento de 30, válido también en el cuerpo ordenado racional, da $\min\{1,\rho\}<q_n\le r$.

**Transporte y existencia real.** La inclusión conserva operaciones de cuerpo, inversos no nulos y orden; también refleja el orden. En consecuencia,

$$
\widetilde q_0=\iota(r),\qquad
\widetilde q_{n+1}=\frac{\widetilde q_n+\iota(\rho)/\widetilde q_n}{2}.
$$

Los parámetros reales satisfacen las hipótesis de 30. La igualdad con aquella sucesión real se prueba por inducción: mismos términos iniciales y, a partir de términos iguales, la misma regla definida produce términos siguientes iguales. Por 30, existe $L>0$ con $\widetilde q_n\to L$, $L^2=\iota(\rho)$ y $\widetilde q_n>L$ para todo $n$; ese $L$ es la única raíz real positiva del parámetro.

Componer con la inclusión conserva los índices y transporta cada evaluación; no identifica $q$ y $\widetilde q$ como objetos con sus codominios declarados. La existencia se obtuvo en $\mathbb R$ mediante completitud. Todavía no se ha decidido si $L\in\iota(\mathbb Q)$: esa pertenencia exige un argumento adicional sobre el parámetro.

La [figura de la inclusión racional–real](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f08) separa sucesión racional, composición con la inclusión y candidato real. Sus datos corresponden al cuadrado 2; los parámetros de esta solución conservan su justificación propia.

### 34. Una nueva ecuación y la misma obstrucción de paridad

[]{#MA-EX-ANM-01-007-034}

[]{#MA-SOL-ANM-01-007-034}

Los parámetros racionales $\rho=8$ y $r=3$ cumplen $r>0$ y $r^2=9>8$. Por 33, la construcción es racional positiva, y su composición real converge a un único $L>0$ con $L^2=8$.

Supón que $L\in\iota(\mathbb Q)$. Entonces $L/2$ también es imagen de un racional y $(L/2)^2=2$. Representa ese racional por una fracción reducida $p/d$, con $p\in\mathbb Z$, $d\in\mathbb Z$, $d>0$ y sin divisor común mayor que 1. La inclusión conserva las operaciones y es inyectiva; multiplicar la ecuación por $d^2\ne0$ da la igualdad entera

$$
p^2=2d^2.
$$

Si un entero es impar, su forma $2k+1$ da cuadrado $2(2k^2+2k)+1$, también impar. Por tanto $p^2$ par obliga a $p$ par. Escribe $p=2h$; la ecuación produce $4h^2=2d^2$, luego $d^2=2h^2$. La misma observación obliga a $d$ par. Así 2 divide a numerador y denominador, contradiciendo la reducción. No existe tal racional; por tanto $L\notin\iota(\mathbb Q)$.

Si $q$ tuviera límite racional $r$, con la distancia de §7.7 y todas las tolerancias reales positivas, la definición diría que $\widetilde q_n\to\iota(r)$. La unicidad del límite real obligaría a $L=\iota(r)$, contradicción. Por ello $q$ no tiene límite racional, mientras que $\widetilde q$ sí tiene límite real. La contradicción no depende de una aproximación decimal.

### 35. Dos destinos para sucesiones de términos racionales

[]{#MA-EX-ANM-01-007-035}

[]{#MA-SOL-ANM-01-007-035}

**La primera construcción.** El dato $u_0=0$ es racional y la suma con 1 y la división por 2 conservan racionalidad, por lo que $u:\mathbb N\to\mathbb Q$ está definida. Por inducción,

$$
0\le u_n<1,\qquad u_{n+1}-u_n=\frac{1-u_n}{2}>0.
$$

La base satisface la desigualdad y $u_n<1$ implica $(u_n+1)/2<1$, cerrando la inducción. Después de incluir los términos en $\mathbb R$, §7.3 garantiza existencia por dirección y cota superior 1. Si el límite es $U$, desplazamiento y operaciones de C06 dan $U=(U+1)/2$, luego $U=1$. Ningún término alcanza 1 porque $u_n<1$ para todo índice. El límite es racional; la misma condición de error acredita que $u$ tiene límite racional 1.

**La segunda construcción.** Por 33–34, $q:\mathbb N\to\mathbb Q$ está definida, sus términos son positivos, la composición real converge a $L>0$ con $L^2=8$ y $L\notin\iota(\mathbb Q)$. Además $\widetilde q_n>L$ para todo $n$, así que tampoco alcanza su límite. En este caso no hay límite racional, por unicidad del límite real.

La segunda construcción refuta la primera afirmación: pertenecer a $\mathbb Q$ en cada índice no fuerza que el límite real pertenezca a su imagen. La primera construcción refuta la corrección propuesta: no alcanzar un límite no implica que sea irracional. Ambas tienen términos racionales y un límite real no alcanzado; una tiene destino racional y la otra irracional.

El codominio declarado exige que cada término esté en $\mathbb Q$; no decide por sí solo qué candidatos reales satisfacen la condición de límite. Si el límite real de la composición pertenece a $\iota(\mathbb Q)$, su preimagen racional satisface esa misma condición de error. Si no pertenece, la unicidad excluye cualquier límite racional. En todo caso deben acreditarse primero la existencia real y después la pertenencia del destino.

### 36. Excluir candidatos con tolerancias racionales

[]{#MA-EX-ANM-01-007-036}

[]{#MA-SOL-ANM-01-007-036}

**Comparar tolerancias.** Fija $r\in\mathbb Q$. Si la condición vale para todas las tolerancias reales positivas, vale en particular para las imágenes de tolerancias racionales positivas.

Recíprocamente, supón la condición con tolerancias racionales. Dado $\varepsilon\in\mathbb R$, $\varepsilon>0$, la arquimedianidad permite elegir $m\in\mathbb N$ con $m>1/\varepsilon$. Entonces $m\ge1$ y $\eta=1/m\in\mathbb Q$ satisface $0<\iota(\eta)<\varepsilon$. El corte dado por la condición racional para esa $\eta$ asegura, para todo $n\ge N$,

$$
|\iota(a_n)-\iota(r)|<\iota(\eta)<\varepsilon.
$$

Así se obtiene la condición con tolerancias reales. El entero $m$ puede depender de $\varepsilon$ y el corte de la tolerancia racional escogida.

**Refutar un candidato.** Fija ahora un racional $r$. Como $L$ no está en la imagen racional, $d=|L-\iota(r)|>0$. Elige por arquimedianidad un entero natural $m>2/d$, necesariamente no nulo, y fija la tolerancia racional $\eta_0=1/m$. Entonces $0<\iota(\eta_0)<d/2$. La convergencia real a $L$ proporciona $T\in\mathbb N$ con $|\widetilde a_n-L|<d/2$ para todo $n\ge T$.

Por la desigualdad triangular, para esos índices,

$$
d\le |L-\widetilde a_n|+|\widetilde a_n-\iota(r)|,
\qquad |\widetilde a_n-\iota(r)|>d/2>\iota(\eta_0).
$$

Dado cualquier corte propuesto $K\in\mathbb N$, toma $n=\max\{K,T\}$. Es un índice posterior a $K$ cuyo error supera la tolerancia fija. Queda refutada la condición racional para ese candidato.

El orden de elecciones es: candidato $r$, distancia $d$, entero $m$ y tolerancia $\eta_0$, corte $T$, corte propuesto $K$ e índice infractor $n$. La tolerancia puede depender del candidato, pero queda fijada antes de los cortes propuestos. Como $r$ era arbitrario, no hay límite racional ni siquiera usando sólo tolerancias racionales; la composición conserva su límite real $L$.

## §7.8

### 37. Qué conclusión cierra cada argumento

[]{#MA-EX-ANM-01-007-037}

[]{#MA-SOL-ANM-01-007-037}

[]{#MA-SEC-ANM-01-007-008}

Las cuatro prescripciones definen funciones $\mathbb N\to\mathbb R$: las fórmulas recíprocas se evalúan sólo en índices con denominador no nulo, y la recurrencia afín siempre produce un real.

**Entrada 1.** El incremento $a_{n+1}-a_n=2$ es positivo, pero la cota inferior 1 no es la cota superior requerida para una sucesión no decreciente. Para cada barrera $M\in\mathbb R$, la arquimedianidad permite elegir $N\in\mathbb N$ con $N>(M-1)/2$. Todo $n\ge N$ cumple $a_n=2n+1>M$. Hay escape por arriba y, por §7.5, no hay límite real. La reparación consiste en esa conclusión; la falta de cota superior no puede suplirse aquí.

**Entrada 2.** La cola reindexada $u_k=b_{k+1}=2-1/(k+1)$ tiene dominio $\mathbb N$ y conjunto de valores $S_{b,1}$. Su incremento es positivo y $u_k<2$. Para cualquier $B<2$, elige $k\in\mathbb N$ con $k>1/(2-B)$; entonces $u_k>B$. Así $\sup S_{b,1}=2$, y §7.3 da $u_k\to2$. La transferencia de cola da $b_n\to2$. En cambio, $\sup S_b=7$ porque el primer término es 7 y los demás son menores que 2. La hipótesis monótona se verificó sobre la cola, no sobre el conjunto global.

**Entrada 3.** Por inducción, $c_{2k}=0$ y $c_{2k+1}=3$. La ecuación $C=3-C$ sólo sería necesaria si existiera el límite. Para cualquier candidato $A$, fija $\varepsilon_0=3/2$. Dado $N$, si $A\le3/2$, el índice $2N+1$ tiene error $|3-A|\ge3/2$; si $A>3/2$, el índice $2N$ tiene error $|A|>3/2$. Ambos índices son al menos $N$. Ningún candidato es límite. La reparación es excluir límites reales, no aceptar la solución formal de la ecuación.

**Entrada 4.** El argumento sí cierra su conclusión cuando completa la comprobación propuesta. El incremento es $1/[(n+2)(n+3)]>0$ y $d_n<4$. Si $B<4$, elige $m>1/(4-B)$ natural; entonces $d_m>B$. De ello resulta $\sup S_d=4$, y §7.3 da $d_n\to4$. La completitud proporciona existencia mediante el teorema; la prueba extremal identifica el límite. No basta mencionar una cota superior cualquiera para identificarla como supremo.

### 38. Dos recorridos hacia una misma barrera

[]{#MA-EX-ANM-01-007-038}

[]{#MA-SOL-ANM-01-007-038}

**Ruta del error.** Fija $\varepsilon>0$. Por arquimedianidad, elige $N\in\mathbb N$ con $N>\max\{1,h/\varepsilon\}$. Para todo $n\ge N$, se tiene $(n+1)^2>n+1>N>h/\varepsilon$, y por tanto

$$
|x_n-c|=\frac{h}{(n+1)^2}<\varepsilon.
$$

El corte depende de $\varepsilon$ y del parámetro fijo $h$; funciona para todos los índices posteriores. Esta prueba acredita directamente el candidato $c$.

**Ruta de orden y extremo.** Para todo $n\in\mathbb N$,

$$
x_{n+1}-x_n
=\frac{h(2n+3)}{(n+1)^2(n+2)^2}>0,\qquad
c-h=x_0\le x_n<c.
$$

El conjunto real no vacío $S_x$ tiene cota superior $c$. El teorema de §7.3 recibe completitud para dar un límite $s=\sup S_x$. Para identificar el extremo sin invocar la primera ruta, fija $B<c$ y elige $m\in\mathbb N$ con $m>\max\{1,h/(c-B)\}$. Entonces $(m+1)^2>h/(c-B)$ y $x_m>B$. Ningún $B<c$ es cota superior, luego $s=c$. Esta segunda prueba también da $x_n\to c$.

La positividad de $h/(n+1)^2$ demuestra que ningún término alcanza $c$. En la primera ruta se reutiliza arquimedianidad, cuya dependencia de completitud fue probada en C03; en la segunda se usa directamente completitud para obtener el supremo y además arquimedianidad para identificarlo. La separación de rutas no afirma independencia lógica respecto de completitud.

### 39. Dos barreras que se encuentran

[]{#MA-EX-ANM-01-007-039}

[]{#MA-SOL-ANM-01-007-039}

**Existencia de las barreras.** Las direcciones y el orden entre términos dan, para todo $n$,

$$
a_0\le a_n\le b_n\le b_0.
$$

Así $a$ tiene cota superior $b_0$ y $b$ cota inferior $a_0$, sin exigir signo positivo. §§7.3–7.4 dan $a_n\to A$ y $b_n\to B$, con $A,B\in\mathbb R$. El orden de límites de C06 da $A\le B$. La regla de resta da $b_n-a_n\to B-A$, mientras que la hipótesis da límite 0 para esa misma sucesión. Por unicidad, $B-A=0$. Denota el destino común por $L=A=B$.

**Captura de la tercera sucesión.** Dado $\varepsilon>0$, toma cortes $N_a,N_b$ que aseguren $|a_n-L|<\varepsilon$ y $|b_n-L|<\varepsilon$ respectivamente. Define $N=\max\{T,N_a,N_b\}$. Para $n\ge N$,

$$
L-\varepsilon<a_n\le c_n\le b_n<L+\varepsilon,
$$

de donde $|c_n-L|<\varepsilon$. Ésta es la captura por sándwich de C06 con un corte común explícito; el prefijo de $c$ no influye.

Sin la hipótesis de distancia, se conservan la existencia de $A,B$ y $A\le B$, pero no necesariamente su igualdad ni la convergencia de $c$. Por ejemplo, $a_n=-1$ y $b_n=1$ son barreras constantes con límites distintos y distancia 2. La sucesión $c_n=(-1)^n$ permanece entre ambas y no tiene límite real, como se probó en §7.5. La condición sobre la distancia es la que obliga a encontrar un único destino común.

### 40. Medias simultáneas y un producto conservado

[]{#MA-EX-ANM-01-007-040}

[]{#MA-SOL-ANM-01-007-040}

**Mapa de obligaciones.** Primero se construyen términos positivos y se conserva el orden; después se obtienen direcciones, cotas y límites por completitud; sólo entonces se utilizan las recurrencias para identificar el destino. El producto conservado aportará su ecuación.

**Construcción y control.** Supón $0<a_n\le b_n$. Entonces $a_n+b_n>0$, por lo que el paso armónico está definido, y ambos términos siguientes son positivos. Las identidades

$$
a_{n+1}-a_n=\frac{a_n(b_n-a_n)}{a_n+b_n}\ge0,
\qquad b_n-b_{n+1}=\frac{b_n-a_n}{2}\ge0,
$$

$$
b_{n+1}-a_{n+1}=\frac{(b_n-a_n)^2}{2(a_n+b_n)}\ge0
$$

conservan el orden y dan las dos direcciones. La base $0<a_0\le b_0$ cierra la inducción y construye las sucesiones completas. Por ello $a_0\le a_n\le b_n\le b_0$ para todo índice. Además,

$$
a_{n+1}b_{n+1}
=\frac{2a_nb_n}{a_n+b_n}\frac{a_n+b_n}{2}
=a_nb_n.
$$

Por inducción, $a_nb_n=P=a_0b_0>0$ para todo $n$.

**Existencia antes del cálculo.** Los teoremas monótonos aplicados a estas cotas dan $a_n\to A$ y $b_n\to B$. Aquí se recibe completitud real. El orden de límites da $a_0\le A\le B\le b_0$, en particular $A+B\ge2a_0>0$. Todos los denominadores $a_n+b_n$ son positivos y su límite es no nulo; así están verificadas las hipótesis del cociente de C06.

Por desplazamiento y operaciones de límites, las recurrencias dan

$$
A=\frac{2AB}{A+B},\qquad B=\frac{A+B}{2}.
$$

La segunda igualdad implica $A=B=L>0$. La primera es coherente con esa igualdad y se ha usado con sus hipótesis acreditadas. La regla de producto y la constancia del producto dan $AB=P$, luego $L^2=P$. Si $R>0$ es otro real con $R^2=P$, $(L-R)(L+R)=0$ y $L+R>0$ fuerzan $R=L$. El destino es el único real positivo de cuadrado $P$; su existencia ha quedado construida.

**Igualdad y posición estricta.** Si $a_0=b_0=t>0$, ambas reglas conservan $t$ por inducción: las sucesiones son constantes e iguales. Si $a_0<b_0$, la identidad de la diferencia conserva $a_n<b_n$ estrictamente en cada índice, y los dos incrementos anteriores son estrictos. Como $a_nb_n=L^2$, la positividad implica $a_n<L<b_n$: si $a_n\ge L$, el producto con $b_n>a_n$ sería mayor que $L^2$; si $b_n\le L$, el producto con $a_n<b_n$ sería menor. Ninguna evaluación alcanza el destino común.

**Construcción racional y destino real.** Para datos racionales positivos, las operaciones conservan racionalidad y el denominador racional positivo tiene inverso racional. Así se construyen $a^{\mathbb Q},b^{\mathbb Q}:\mathbb N\to\mathbb Q$. Sus composiciones $\widetilde a=\iota\circ a^{\mathbb Q}$ y $\widetilde b=\iota\circ b^{\mathbb Q}$ tienen codominio $\mathbb R$ y cumplen las mismas reglas reales, porque la inclusión conserva operaciones y orden. Coinciden por inducción con las construcciones reales de los datos incluidos; no se identifica una función racional con otra de codominio real.

Con $a_0=1$, $b_0=2$, el producto es 2. Ambas composiciones convergen al real positivo $L$ con $L^2=2$. La prueba de paridad de §7.7 excluye $L\in\iota(\mathbb Q)$: una fracción reducida cuyo cuadrado fuera 2 tendría numerador y denominador pares. Si cualquiera de las sucesiones racionales tuviera límite racional $r$, su composición convergería también a $\iota(r)$; la unicidad real forzaría $\iota(r)=L$, contradicción. Hay destino real común y ningún límite racional para estas dos construcciones.

Las [obligaciones de existencia](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f07) y la [distinción de codominios](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f08) sirven para comparar el método. Esas figuras representan la iteración de §7.6–§7.7, no las dos medias de este ejercicio; aquí el producto conservado y las desigualdades anteriores justifican el destino común.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 7](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html) · [Ejercicios](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-microcontroles.html)
