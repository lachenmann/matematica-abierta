---
content-id: MA-BCH-0246
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-011
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
title: Capítulo 11 — Series como laboratorio de convergencia
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C11.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-microcontroles.html)

Una sucesión de aportes puede tender a cero y seguir acumulando cantidades apreciables. Queremos decidir cuándo el proceso de sumación tiene un destino real, qué controla los bloques que aún faltan y cómo certificar una aproximación sin conocer la suma exacta. Las sumas parciales serán el puente entre acumulación y los límites de C06 y C10.

Trabajaremos con sucesiones reales e índices desde cero. Seleccionaremos mecanismos de convergencia por lo que permiten ver: fórmulas finitas, barreras positivas, control de magnitudes, cancelación alternada y conservación de los índices al agrupar. Cada mecanismo se prueba antes de emplearlo. El objetivo es reconocer qué hipótesis convierte una intuición de acumulación en un control uniforme de toda la cola.

## 11.1. De los términos a las sumas parciales

[]{#MA-SEC-ANM-01-011-001}

Los aportes $1,1/2,1/4,\ldots$ disminuyen; los totales $1,3/2,7/4,\ldots$ aumentan. Son dos sucesiones reales diferentes. Para estudiar lo que se acumula necesitamos construir la segunda a partir de la primera y decidir después si tiene un destino real.

Dada $a:\mathbb N\to\mathbb R$, con $\mathbb N=\{0,1,2,\ldots\}$, definimos su **sucesión de sumas parciales** $s=\operatorname{PS}(a)$ mediante

$$
s_0=a_0,\qquad s_{n+1}=s_n+a_{n+1}.
$$

Cada paso suma dos reales y determina un único real; la recursión define $s$ en todos los naturales y una inducción prueba su unicidad. Escribimos $s_n=\sum_{k=0}^n a_k$: contiene $n+1$ términos, no $n$. Una suma con ningún término se toma igual a cero cuando aparezca un bloque vacío.

La **serie de términos $a$** es este proceso de sumación. Decimos que converge si $s_n\to S$ para algún $S\in\mathbb R$, y entonces llamamos a $S$ su suma y escribimos

$$
\sum_{n=0}^{\infty}a_n=S.
$$

Antes de demostrar convergencia, el símbolo de serie designa el proceso que estamos estudiando; no afirma que ya exista ese real. El límite es único por C06. Una serie divergente puede tener sumas parciales no acotadas o puede oscilar dentro de una región acotada.

**Recuperar los aportes.** La construcción conserva toda la información de $a$, pues

$$
a_0=s_0,\qquad a_{n+1}=s_{n+1}-s_n.
$$

La primera igualdad es la condición inicial; la segunda se obtiene restando $s_n$ en la recursión. Por ello $\operatorname{PS}(a)=\operatorname{PS}(b)$ implica $a=b$. En cambio, tener la misma suma real no obliga a tener los mismos términos: $(1,0,0,\ldots)$ y $(1/2,1/2,0,\ldots)$ generan procesos diferentes que convergen ambos a uno.

Para $a_n=(-1)^n$, las sumas parciales son $s_{2k}=1$ y $s_{2k+1}=0$, como se verifica por parejas. La sucesión $s$ está acotada, pero no converge: después de cualquier corte hay sumas parciales de ambos valores. Para $a_n=0$ todos los totales valen cero. Incluso cuando término y total tienen el mismo valor en un índice, siguen cumpliendo papeles distintos.

En el ejemplo inicial $a_n=2^{-n}$, una inducción en la recursión da $s_n=2-2^{-n}$. Además $2^n\ge n+1$ por inducción, luego $2^{-n}\le1/(n+1)$. Para cualquier $\varepsilon>0$, elegir $N+1>1/\varepsilon$ hace tanto $|a_n|$ como $|s_n-2|$ menores que $\varepsilon$ para $n\ge N$. Así los dos destinos mostrados quedan probados directamente, antes de desarrollar la identidad geométrica general.

![Los aportes geométricos disminuyen hacia cero mientras los totales aumentan hacia dos. En el índice n se han acumulado n+1 términos: los paneles representan dos sucesiones distintas.](../../assets/books/anm/C11/C11-F01.svg){#fig-anm-c11-f01 fig-alt="Los aportes geométricos disminuyen hacia cero mientras los totales aumentan hacia dos. En el índice n se han acumulado n+1 términos: los paneles representan dos sucesiones distintas."}

La figura compara aportes y totales en el mismo índice. Leer un punto en el panel de términos no permite inferir el destino del panel de acumulación; éste es el objeto al que aplicaremos Cauchy.

### Antes de seguir

[]{#MA-MIC-ANM-01-011-001}

1. ¿Cuántos términos contiene $s_n=\sum_{k=0}^n a_k$?

[]{#MA-MIC-ANM-01-011-002}

2. ¿Cuál es el término inicial de $\operatorname{PS}(a)$?

[]{#MA-MIC-ANM-01-011-003}

3. ¿Qué condición permite llamar suma real a $\sum_{n=0}^{\infty}a_n$?

[]{#MA-MIC-ANM-01-011-004}

4. ¿Cómo se recupera $a_{n+1}$ a partir de dos totales?

[]{#MA-MIC-ANM-01-011-005}

5. ¿Tener la misma suma implica tener los mismos términos?

[]{#MA-MIC-ANM-01-011-006}

6. ¿Qué totales produce $a_n=(-1)^n$?

[]{#MA-MIC-ANM-01-011-007}

7. ¿La acotación de esos totales garantiza convergencia?

[]{#MA-MIC-ANM-01-011-008}

8. ¿Son $a$, $\operatorname{PS}(a)$ y su suma el mismo tipo de objeto?

## 11.2. Cauchy mide bloques completos

[]{#MA-SEC-ANM-01-011-002}

Dos totales tardíos difieren en lo que se sumó entre sus cortes. Si $p>q$, la recursión y una inducción sobre $p-q$ dan la identidad finita

$$
s_p-s_q=\sum_{k=q+1}^{p}a_k.
$$

El bloque empieza en $q+1$ porque $a_q$ ya forma parte de $s_q$. El caso $p=q+1$ es la recursión; al prolongar el extremo superior se añade $a_{p+1}$ a ambos miembros. Esta identidad traduce la pregunta sobre dos sumas parciales a una pregunta sobre cualquier acumulación tardía.

**Criterio de Cauchy para series reales.** La serie de $a$ converge si y sólo si

$$
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall p,q\in\mathbb N:
\quad p>q\ge N\ \Longrightarrow\
\left|\sum_{k=q+1}^{p}a_k\right|<\varepsilon.
$$

Por definición, la serie converge cuando converge $s$. C10 equivale esa convergencia real a que $|s_p-s_q|<\varepsilon$ para todos $p,q\ge N$, y la identidad demuestra una dirección. Recíprocamente, si los bloques ordenados cumplen el control, los pares con $p>q$ quedan controlados; si $q>p$, intercambiamos los índices y usamos simetría del valor absoluto; si $p=q$, la distancia es cero. Así $s$ es de Cauchy y C10 aporta un destino real. La completitud se usa en esta última existencia, no en la identidad finita.

El corte se escoge antes que los dos extremos; debe funcionar para bloques de cualquier longitud. Permitir un corte distinto para cada longitud fija debilitaría el enunciado.

**Condición necesaria.** Si una serie converge, entonces $a_n\to0$. En efecto, para $n\ge N+1$, el bloque con $q=n-1$ y $p=n$ tiene un término y da $|a_n|<\varepsilon$. Este argumento muestra también la limitación: controlar bloques de longitud uno no controla todos los bloques.

La serie de $a_n=1/(n+1)$ lo muestra. Sus términos tienden a cero. Para cualquier corte $N$, pongamos $m=N+1$, $q=m-1$ y $p=2m-1$. Ambos índices están después del corte y

$$
s_{2m-1}-s_{m-1}=\sum_{j=m+1}^{2m}\frac1j\ge m\frac1{2m}=\frac12.
$$

La tolerancia fija $1/2$ contradice el criterio. La longitud del bloque crece: muchos aportes pequeños pueden acumular una cantidad que no desaparece. Esta prueba de divergencia usa sumas finitas, no un valor supuesto de una suma infinita.

![Los bloques de m aportes armónicos entre los denominadores m+1 y 2m conservan suma al menos un medio. Los términos individuales se reducen, pero la longitud del bloque puede crecer.](../../assets/books/anm/C11/C11-F02.svg){#fig-anm-c11-f02 fig-alt="Los bloques de m aportes armónicos entre los denominadores m+1 y 2m conservan suma al menos un medio. Los términos individuales se reducen, pero la longitud del bloque puede crecer."}

| m | q = m−1 | p = 2m−1 | Cota inferior exacta del bloque |
|---|---|---|---|
| 4 | 3 | 7 | ≥ $1/2$ |
| 8 | 7 | 15 | ≥ $1/2$ |
| 16 | 15 | 31 | ≥ $1/2$ |

La muestra exhibe algunos bloques; la elección $m=N+1$ prueba que existen después de todo corte. La figura por sí sola no extiende un cálculo finito a todos los índices.

### Antes de seguir

[]{#MA-MIC-ANM-01-011-009}

1. ¿Por qué el bloque $s_p-s_q$ empieza en $q+1$?

[]{#MA-MIC-ANM-01-011-010}

2. ¿En qué orden se eligen tolerancia, corte y extremos de bloque?

[]{#MA-MIC-ANM-01-011-011}

3. ¿Puede el corte depender de la longitud del bloque?

[]{#MA-MIC-ANM-01-011-012}

4. ¿Cómo se cubre el caso $p=q$ al recuperar Cauchy?

[]{#MA-MIC-ANM-01-011-013}

5. ¿Dónde se usa completitud en el criterio de bloques?

[]{#MA-MIC-ANM-01-011-014}

6. ¿Por qué convergencia de la serie implica $a_n\to0$?

[]{#MA-MIC-ANM-01-011-015}

7. ¿Qué pares de cortes niegan Cauchy en la armónica?

[]{#MA-MIC-ANM-01-011-016}

8. ¿El término nulo es una condición suficiente?

## 11.3. Fórmulas finitas y restos exactos

[]{#MA-SEC-ANM-01-011-003}

Una fórmula para el total finito puede resolver simultáneamente existencia y error. La estrategia consiste en simplificar $s_n$ antes de tomar límites; manipular una supuesta suma infinita invertiría ese orden.

Si $a_n=c_n-c_{n+1}$, una inducción cancela términos consecutivos y entrega

$$
s_n=c_0-c_{n+1}.
$$

Por C06, si $c_n\to C$, entonces la serie converge y su suma es $c_0-C$. Recíprocamente, si $s_n\to S$, la misma identidad da $c_{n+1}\to c_0-S$, y la sucesión completa $c$ tiene ese límite: un único término inicial no altera el control eventual. Cuando convergen, el **resto** en el corte $n$ es el real

$$
R_n=S-s_n=c_{n+1}-C.
$$

Por ejemplo, $a_n=1/((n+1)(n+2))=1/(n+1)-1/(n+2)$ produce $s_n=1-1/(n+2)$, suma uno y resto $1/(n+2)$. No se requiere un criterio nuevo para cada fracción: se reconoce una diferencia finita y se reutiliza un límite conocido.

Para la serie geométrica $a_n=r^n$, las potencias naturales satisfacen $r^0=1$ y $r^{n+1}=r^nr$; en particular usamos $0^0=1$ como convención de exponente cero. Al restar la suma finita multiplicada por $r$, o por inducción, obtenemos

$$
(1-r)s_n=1-r^{n+1}.
$$

Si $|r|<1$, las potencias $r^{n+1}$ tienden a cero. Para $0<\rho=|r|<1$, escribimos $\rho^{-1}=1+t$ con $t>0$; la inducción da $(1+t)^n\ge1+nt$, por lo que $\rho^n\le1/(1+nt)\to0$ por arquimedianidad. Si $r=0$, el primer término vale uno y los siguientes cero. Como $1-r\ne0$, C06 aplicado a la identidad finita demuestra

$$
S=\frac1{1-r},\qquad R_n=\frac{r^{n+1}}{1-r},\qquad
|R_n|=\frac{|r|^{n+1}}{|1-r|}.
$$

La estimación precisa usa $|1-r|$; para razones negativas puede ser mejor que reemplazarlo por $1-|r|$. La serie geométrica converge exactamente para $|r|<1$. Si $|r|\ge1$, sus términos no tienden a cero: $|r^n|\ge1$ en cada índice, y la condición necesaria de §11.2 descarta convergencia. Esto incluye $r=1$ y $r=-1$ sin dividir por cero.

![La geométrica de razón menos un medio alterna sus totales alrededor de dos tercios. La identidad finita determina el resto con signo, no sólo una cota de su magnitud.](../../assets/books/anm/C11/C11-F03.svg){#fig-anm-c11-f03 fig-alt="La geométrica de razón menos un medio alterna sus totales alrededor de dos tercios. La identidad finita determina el resto con signo, no sólo una cota de su magnitud."}

Para $r=-1/2$, el total alterna alrededor de $2/3$ y su error exacto es $(2/3)2^{-(n+1)}$. El valor numérico del destino aparece después de la identidad y de la prueba del límite de las potencias.

### Antes de seguir

[]{#MA-MIC-ANM-01-011-017}

1. ¿Qué total produce $a_n=c_n-c_{n+1}$?

[]{#MA-MIC-ANM-01-011-018}

2. ¿Cuál es el resto telescópico si $c_n\to C$?

[]{#MA-MIC-ANM-01-011-019}

3. ¿Cuál es la suma de $1/((n+1)(n+2))$?

[]{#MA-MIC-ANM-01-011-020}

4. ¿Qué identidad geométrica es válida antes de cualquier límite?

[]{#MA-MIC-ANM-01-011-021}

5. ¿Para qué razones reales converge la geométrica?

[]{#MA-MIC-ANM-01-011-022}

6. ¿Qué ocurre con la geométrica de razón cero?

[]{#MA-MIC-ANM-01-011-023}

7. ¿Cuál es el resto exacto cuando $|r|<1$?

[]{#MA-MIC-ANM-01-011-024}

8. ¿Es correcto dividir por $1-r$ para estudiar $r=1$?

## 11.4. Acumulación positiva y barreras

[]{#MA-SEC-ANM-01-011-004}

Cuando $a_n\ge0$, cada nuevo aporte mueve el total hacia la derecha: $s_{n+1}-s_n=a_{n+1}\ge0$. El control de cancelaciones desaparece y la cuestión se reduce a encontrar una barrera superior para todos los totales.

**Barrera positiva.** Una serie de términos no negativos converge si y sólo si sus sumas parciales están acotadas superiormente. La necesidad se sigue de C06. Para probar suficiencia desde las bases de completitud, sea

$$
S=\sup\{s_n:n\in\mathbb N\}.
$$

El conjunto es no vacío y tiene cota superior por hipótesis, de modo que el supremo real existe por C03, la base de completitud heredada en C10. Dada $\varepsilon>0$, $S-\varepsilon$ no puede ser cota superior: existe $N$ con $S-\varepsilon<s_N\le S$. La no negatividad asegura que para todo $n\ge N$, $s_N\le s_n\le S$, luego $|S-s_n|<\varepsilon$. Hemos reconstruido el mecanismo de monotonía y barrera sin necesitar importar otro criterio de series.

Si los totales no tienen cota superior, exceden finalmente cualquier real $M$: existe $N$ con $s_N>M$, y todos los posteriores son mayores que $M$. Esta es una descripción de divergencia hacia arriba; no asigna a la serie una suma real llamada infinito.

**Comparación directa.** Si $0\le a_n\le b_n$ en todos los índices y la serie de $b$ converge, entonces la de $a$ también converge y sus sumas cumplen $0\le S_a\le S_b$. Las desigualdades se conservan al sumar finitamente, de modo que $0\le s_n\le t_n\le S_b$. La barrera positiva aporta $S_a$ y C06 conserva el orden al pasar al límite. También podemos comparar desde un índice fijo: se aplica el mismo argumento a las colas reindexadas, dejando el prefijo como una suma real finita. En ese caso, la desigualdad entre sumas completas requiere considerar sus prefijos y no se afirma automáticamente.

El ejemplo $a_n=1/(n+2)^2$ queda dominado por

$$
0\le\frac1{(n+2)^2}\le\frac1{(n+1)(n+2)}.
$$

La serie de la derecha tiene suma uno por §11.3, así que $\sum a_n$ converge con suma entre cero y uno. Incluso su resto se controla: para $p>n$ sumamos la comparación sólo en el bloque $n+1,\ldots,p$ y luego tomamos $p\to\infty$. El telescopaje entrega

$$
0\le S_a-s_n\le\frac1{n+2}.
$$

Encontrar una barrera puede probar existencia sin calcular el valor exacto del destino. El bloque posterior da además un certificado de error.

### Antes de seguir

[]{#MA-MIC-ANM-01-011-025}

1. ¿Qué hipótesis hace crecientes las sumas parciales?

[]{#MA-MIC-ANM-01-011-026}

2. ¿Qué cota basta para una serie no negativa?

[]{#MA-MIC-ANM-01-011-027}

3. ¿Qué conjunto se usa para construir el destino por supremo?

[]{#MA-MIC-ANM-01-011-028}

4. ¿Cómo se encuentra un total cercano por debajo del supremo?

[]{#MA-MIC-ANM-01-011-029}

5. ¿Por qué todos los totales posteriores siguen cerca?

[]{#MA-MIC-ANM-01-011-030}

6. ¿Qué conclusión da $0\le a_n\le b_n$ si la serie de $b$ converge?

[]{#MA-MIC-ANM-01-011-031}

7. ¿Una comparación eventual conserva automáticamente el orden de sumas completas?

[]{#MA-MIC-ANM-01-011-032}

8. ¿Qué resto garantiza la comparación para $a_n=1/(n+2)^2$?

## 11.5. Control absoluto de la acumulación

[]{#MA-SEC-ANM-01-011-005}

Con signos variables, una cota superior de $s_n$ no impide que los totales bajen u oscilen. Un control más fuerte suma las magnitudes y, mediante la desigualdad triangular, protege cualquier bloque independientemente de sus cancelaciones.

La serie de $a$ **converge absolutamente** cuando converge la serie de $|a_n|$. Si la original converge y la de magnitudes diverge, la convergencia es **condicional**. Este segundo término sólo se aplica cuando existe la suma de la original.

Escribamos $u_n=\sum_{k=0}^n|a_k|$. Una inducción basada en la desigualdad triangular prueba

$$
|s_n|\le u_n,\qquad
|s_p-s_q|\le u_p-u_q=\sum_{k=q+1}^p|a_k|\quad(p>q).
$$

En la inducción del bloque, añadir el siguiente término aumenta el lado derecho en su magnitud; el caso inicial de un término es igualdad. Estas estimaciones son finitas y no suponen convergencia.

**La convergencia absoluta implica convergencia.** Si $u_n\to A$, Cauchy aplicado a $u$ proporciona, para cada $\varepsilon>0$, un único corte que controla todos sus bloques. Como $u$ crece, $u_p-u_q=|u_p-u_q|<\varepsilon$ después de ese corte. La estimación anterior controla entonces $|s_p-s_q|$, y C10 garantiza $s_n\to S\in\mathbb R$. Completitud aparece en esa garantía de destino. Tomando límites en $|s_n|\le u_n$, mediante $||s_n|-|S||\le|s_n-S|$ y el orden de C06, resulta $|S|\le A$.

Hay una versión de error más útil que la desigualdad global. Fijado $n$, en todos los bloques posteriores $|s_p-s_n|\le u_p-u_n$; al tomar $p\to\infty$ obtenemos

$$
|R_n|=|S-s_n|\le A-u_n.
$$

Si $|a_n|\le C\rho^n$ con $C\ge0$ y $0<\rho<1$, la comparación de magnitudes con la geométrica prueba convergencia absoluta y

$$
|R_n|\le\frac{C\rho^{n+1}}{1-\rho}.
$$

Para $C=0$, todos los términos son cero. Para $C>0$, se escoge el corte usando el límite de $\rho^n$ ya probado; el número de términos sumados hasta $n$ sigue siendo $n+1$. Los signos pueden depender arbitrariamente del índice porque el control absoluto trabaja antes de toda cancelación.

La serie $a_n=(-1)^n$ muestra que acotación de $s$ no basta. La afirmación recíproca, que toda serie convergente sea absoluta, requiere otro examen: el próximo mecanismo conservará cancelaciones y permitirá un ejemplo condicional.

### Antes de seguir

[]{#MA-MIC-ANM-01-011-033}

1. ¿Qué significa convergencia absoluta?

[]{#MA-MIC-ANM-01-011-034}

2. ¿Qué condición adicional exige llamar condicional a una convergencia?

[]{#MA-MIC-ANM-01-011-035}

3. ¿Qué desigualdad domina un bloque con signos?

[]{#MA-MIC-ANM-01-011-036}

4. ¿Por qué un corte para las magnitudes sirve para la original?

[]{#MA-MIC-ANM-01-011-037}

5. ¿Se necesita sumar primero la original para aplicar control absoluto?

[]{#MA-MIC-ANM-01-011-038}

6. ¿Qué relación hay entre las sumas $S$ y $A$ de la original y las magnitudes?

[]{#MA-MIC-ANM-01-011-039}

7. ¿Qué cota de error proporciona $u_n\to A$?

[]{#MA-MIC-ANM-01-011-040}

8. ¿Qué error asegura $|a_n|\le C\rho^n$ con $0<\rho<1$?

## 11.6. Alternancia: encerrar sin sumar magnitudes

[]{#MA-SEC-ANM-01-011-006}

Supongamos $0\le b_{n+1}\le b_n$ y $b_n\to0$, y tomemos $a_n=(-1)^nb_n$. La alternancia fija los signos, el decrecimiento impide que la segunda magnitud de una pareja supere la primera y el límite cero hará pequeño cualquier bloque tardío. Debemos mostrar cómo cooperan esas tres condiciones.

**Lema de bloque alternado.** Si $c_0\ge c_1\ge\cdots\ge c_m\ge0$, entonces

$$
0\le c_0-c_1+c_2-\cdots+(-1)^mc_m\le c_0.
$$

La cota inferior se obtiene agrupando $(c_0-c_1)+(c_2-c_3)+\cdots$, con un último término no negativo si sobra. Para la superior, escribimos $c_0-(c_1-c_2)-(c_3-c_4)-\cdots$, y restamos también el último término si el índice final es impar. Cada diferencia entre magnitudes contiguas es no negativa. Las dos formas son reorganizaciones de una suma finita, no de una serie infinita.

**Criterio alternado.** La serie de $(-1)^nb_n$ converge. En un bloque desde $q+1$ hasta $p$, sacar el signo inicial y aplicar el lema da

$$
0\le(-1)^{q+1}(s_p-s_q)\le b_{q+1},\qquad
|s_p-s_q|\le b_{q+1}.
$$

Dada $\varepsilon>0$, elegimos $N$ tal que $b_j<\varepsilon$ para $j\ge N$. Si $p>q\ge N$, también $q+1\ge N$; la estimación vale para cualquier longitud del bloque y prueba Cauchy. C10 proporciona $S\in\mathbb R$. Hemos probado Leibniz directamente desde bloques, sin reunir dos límites de paridades mediante un resultado no explicado.

Fijado $n$, tomamos $p\to\infty$ en el control con signo para obtener

$$
0\le(-1)^{n+1}R_n\le b_{n+1},\qquad |R_n|\le b_{n+1}.
$$

Si $n$ es par, $s_{n+1}\le S\le s_n$; si $n$ es impar, $s_n\le S\le s_{n+1}$. En particular, los intervalos $[s_{2k+1},s_{2k}]$ contienen el destino. Sus extremos inferiores crecen porque $s_{2k+3}-s_{2k+1}=b_{2k+2}-b_{2k+3}\ge0$; los superiores decrecen porque $s_{2k+2}-s_{2k}=-b_{2k+1}+b_{2k+2}\le0$. La anchura es $b_{2k+1}$ y tiende a cero. Estos intervalos reinterpretan un destino cuya existencia ya se ha demostrado.

Para $b_n=1/(n+1)$, la serie alternada converge y $|R_n|\le1/(n+2)$. La serie de magnitudes es la armónica divergente de §11.2: la convergencia es condicional. No precisamos calcular $S$ ni identificarlo con un logaritmo para probar o estimar la convergencia.

![La cancelación mantiene los totales alternados en intervalos que se estrechan, aunque los totales de magnitudes crezcan sin barrera. Los extremos de paridad encierran la suma y la anchura es la siguiente magnitud.](../../assets/books/anm/C11/C11-F04.svg){#fig-anm-c11-f04 fig-alt="La cancelación mantiene los totales alternados en intervalos que se estrechan, aunque los totales de magnitudes crezcan sin barrera. Los extremos de paridad encierran la suma y la anchura es la siguiente magnitud."}

| k | Extremo inferior $s_{2k+1}$ | Extremo superior $s_{2k}$ | Anchura |
|---|---|---|---|
| 0 | 1/2 | 1 | 1/2 |
| 1 | 7/12 | 5/6 | 1/4 |
| 2 | 37/60 | 47/60 | 1/6 |
| 3 | 533/840 | 319/420 | 1/8 |
| 4 | 1627/2520 | 1879/2520 | 1/10 |
| 5 | 18107/27720 | 20417/27720 | 1/12 |

La figura conserva un eje de valores común para los intervalos y separa términos de sumas parciales. La anchura permite un error garantizado aunque el destino carezca todavía de una fórmula.

**Una hipótesis que no se puede borrar.** La alternancia y el término nulo sin decrecimiento no bastan. Sea $d_k=1/(k+1)$, $b_{2k}=2d_k$ y $b_{2k+1}=d_k$. Entonces $b_n\to0$ y los signos alternan, pero cada pareja aporta $d_k$. Las sumas parciales de índice $2m+1$ son $\sum_{k=0}^m d_k$, no acotadas por §11.4 y la divergencia armónica. La serie original tampoco converge, pues una extracción de una sucesión convergente tendría el mismo límite por el control ε–N. La monotonía impedía esa acumulación repetida del desequilibrio.

### Antes de seguir

[]{#MA-MIC-ANM-01-011-041}

1. ¿Qué tres condiciones se imponen a la alternancia?

[]{#MA-MIC-ANM-01-011-042}

2. ¿Qué cota tiene un bloque alternado que empieza en $q+1$?

[]{#MA-MIC-ANM-01-011-043}

3. ¿Qué hipótesis permite emparejar diferencias no negativas?

[]{#MA-MIC-ANM-01-011-044}

4. ¿Qué hipótesis hace pequeño el control del bloque?

[]{#MA-MIC-ANM-01-011-045}

5. ¿Qué error y signo tiene el resto?

[]{#MA-MIC-ANM-01-011-046}

6. ¿Qué intervalo contiene la suma entre los cortes $2k$ y $2k+1$?

[]{#MA-MIC-ANM-01-011-047}

7. ¿Por qué la armónica alternada es condicional?

[]{#MA-MIC-ANM-01-011-048}

8. ¿Qué falla si se alternan $2/(k+1)$ y $1/(k+1)$ por parejas?

## 11.7. Agrupar términos y conservar el recorrido

[]{#MA-SEC-ANM-01-011-007}

Agrupar términos consecutivos conserva los totales en los extremos de cada grupo, pero deja de mostrar los totales intermedios. Para precisar esta operación, sea $\phi:\mathbb N\to\mathbb N$ estrictamente creciente y definamos

$$
g_0=\sum_{j=0}^{\phi(0)}a_j,\qquad
g_k=\sum_{j=\phi(k-1)+1}^{\phi(k)}a_j\quad(k\ge1).
$$

Cada grupo es finito y no vacío. Una inducción y la partición de sumas finitas demuestran que sus sumas parciales son $t_k=s_{\phi(k)}$. Si la serie original converge a $S$, también converge la agrupada a $S$: la inducción da $\phi(k)\ge k$, de modo que el mismo corte ε–N controla $s_{\phi(k)}$. No se permutan términos.

La recíproca falla. Agrupar $(1,-1,1,-1,\ldots)$ por parejas produce $g_k=0$ y $t_k=0$, pero el proceso original alterna entre uno y cero. Hemos seleccionado una extracción convergente, no demostrado convergencia del recorrido completo.

**Qué información falta.** Para cada $n>\phi(0)$ existe un único $k\ge1$ con $\phi(k-1)<n\le\phi(k)$: basta tomar el menor índice cuyo extremo alcanza $n$, que existe porque $\phi(k)\ge k$. Si $t_k\to S$ y las distancias interiores a ese extremo tienden uniformemente a cero, los índices omitidos recuperan el mismo destino. En términos precisos, si para todo $\varepsilon>0$ existe $K$ tal que

$$
k\ge K,\quad \phi(k-1)<n\le\phi(k)
\quad\Longrightarrow\quad |s_n-s_{\phi(k)}|<\varepsilon,
$$

entonces $s_n\to S$. Para probarlo, hacemos menores que $\varepsilon/2$ tanto la distancia interior como $|t_k-S|$, con un corte común $K\ge1$. Todo $n\ge\phi(K-1)+1$ pertenece a un grupo con $k\ge K$; la desigualdad triangular da $|s_n-S|<\varepsilon$.

Una condición suficiente fácil de verificar es que los grupos tengan longitud acotada y $a_n\to0$. Si las longitudes son a lo sumo un natural $M\ge1$, entonces $s_{\phi(k)}-s_n$ suma a lo sumo $M$ términos del propio grupo. Dada $\varepsilon>0$, escogemos $J$ con $|a_j|<\varepsilon/M$ para $j\ge J$. Para $k\ge\max\{1,J\}$, $\phi(k-1)+1\ge k\ge J$; todos los términos interiores pertenecen a esa cola y su suma de magnitudes es menor que $\varepsilon$ cuando el bloque no es vacío. Si es vacío, la distancia es cero. La condición anterior queda probada. No negatividad no interviene: el control es absoluto y finito.

El límite cero del término por sí solo tampoco permite cualquier longitud de grupo. En el bloque número $m\ge1$, pongamos $m$ aportes $1/m$ seguidos de $m$ aportes $-1/m$. El bloque empieza en el índice $m(m-1)$ y termina en $m(m+1)-1$. Esos intervalos particionan $\mathbb N$. Los términos tienden a cero; los totales de fin de bloque son cero, mientras los totales tras la mitad positiva valen uno. Agrupar cada bloque produce suma cero, pero la serie original diverge. El grupo puede acumular una excursión fija aunque cada aporte sea pequeño.

![Cada grupo termina con total cero, pero su mitad alcanza uno. Los términos se hacen pequeños y los grupos más largos: conservar sólo sus extremos borra excursiones que impiden convergencia.](../../assets/books/anm/C11/C11-F05.svg){#fig-anm-c11-f05 fig-alt="Cada grupo termina con total cero, pero su mitad alcanza uno. Los términos se hacen pequeños y los grupos más largos: conservar sólo sus extremos borra excursiones que impiden convergencia."}

El dibujo muestra el recorrido que la agrupación ocultaría. El control de longitudes de grupo es una manera de impedir que esos índices intermedios se alejen del destino.

### Antes de seguir

[]{#MA-MIC-ANM-01-011-049}

1. ¿Qué son las sumas parciales de la serie agrupada?

[]{#MA-MIC-ANM-01-011-050}

2. ¿Por qué convergencia original implica convergencia agrupada?

[]{#MA-MIC-ANM-01-011-051}

3. ¿Puede fallar la recíproca?

[]{#MA-MIC-ANM-01-011-052}

4. ¿Qué índices deja de mostrar la agrupación?

[]{#MA-MIC-ANM-01-011-053}

5. ¿Qué condición interior recupera la convergencia completa?

[]{#MA-MIC-ANM-01-011-054}

6. ¿Qué dos hipótesis bastan para ese control interior?

[]{#MA-MIC-ANM-01-011-055}

7. ¿Cómo se usa la cota $M$?

[]{#MA-MIC-ANM-01-011-056}

8. ¿Qué muestra el bloque de $m$ aportes $1/m$ y $m$ aportes $-1/m$?

## 11.8. Elegir un control y certificar el error

[]{#MA-SEC-ANM-01-011-008}

La primera decisión ante una serie consiste en identificar qué sucesión de totales estamos estudiando y qué mecanismo controla sus bloques. Una fórmula telescópica puede dar el resto exacto; una comparación no negativa produce una barrera; el control absoluto garantiza estabilidad sin seguir los signos; el control alternado preserva cancelaciones y entrega un intervalo. Cada mecanismo responde a una dificultad concreta.

Un certificado útil separa existencia de precisión. Primero se prueba que $s_n\to S$; luego una cota $|S-s_n|\le E_n$ permite decidir si el total calculado cumple la tolerancia. Para asegurar error estrictamente menor que $\varepsilon$ se escoge $E_n<\varepsilon$, no sólo $E_n\le\varepsilon$. Si conocemos $L_n\le S\le U_n$, podemos usar el punto medio $M_n=(L_n+U_n)/2$ como aproximación, con

$$
|S-M_n|\le\frac{U_n-L_n}{2}.
$$

La prueba es finita: restar $M_n$ a las dos desigualdades deja fronteras simétricas. El punto medio es un real construido con dos totales; puede ser una mejor aproximación aunque no sea una suma parcial de la serie.

En la armónica alternada de §11.6, $L_k=s_{2k+1}$, $U_k=s_{2k}$ y $U_k-L_k=1/(2k+2)$. El punto medio tiene error a lo sumo $1/(4k+4)$. Con $k=2$, $s_4=47/60$, $s_5=37/60$, y por tanto

$$
\frac{37}{60}\le S\le\frac{47}{60},\qquad
M_2=\frac7{10},\qquad |S-M_2|\le\frac1{12}<\frac1{10}.
$$

El cálculo usa seis términos para construir ambos extremos; no convierte $7/10$ en el valor exacto de $S$. La precisión se certifica sin usar una fórmula del destino.

![El intervalo entre s_5 y s_4 contiene la suma de la armónica alternada. Su punto medio, siete décimos, tiene error a lo sumo un doceavo, menor que un décimo, sin afirmar que sea la suma exacta.](../../assets/books/anm/C11/C11-F06.svg){#fig-anm-c11-f06 fig-alt="El intervalo entre s_5 y s_4 contiene la suma de la armónica alternada. Su punto medio, siete décimos, tiene error a lo sumo un doceavo, menor que un décimo, sin afirmar que sea la suma exacta."}

La mitad de la anchura controla el error del punto medio; la anchura completa controla el de un extremo. Se conserva el origen de cada número para no confundir total, aproximación y suma.

Las operaciones entre series también requieren una traducción finita. Si las series de $a,b$ convergen a $A,B$ y $\alpha,\beta\in\mathbb R$, una inducción da

$$
\sum_{j=0}^n(\alpha a_j+\beta b_j)
=\alpha\sum_{j=0}^na_j+\beta\sum_{j=0}^nb_j.
$$

El álgebra de C06 prueba entonces convergencia y suma $\alpha A+\beta B$. No basta conocer $a_n\to0$ y $b_n\to0$. Si eliminamos un prefijo de longitud $m$, la cola reindexada $c_k=a_{m+k}$ tiene totales $s_{m+n}-P_m$, donde $P_m=\sum_{j=0}^{m-1}a_j$ y $P_0=0$. Su suma es $S-P_m$ cuando la original converge; recíprocamente, convergencia de la cola permite añadir el prefijo. Igual comportamiento de convergencia no significa igualdad numérica de las sumas.

El laboratorio deja varias maneras de controlar una acumulación, cada una con hipótesis identificables. Una lista finita de valores no decide por sí sola una convergencia infinita; la prueba debe alcanzar todos los bloques posteriores. A la vez, una estimación explícita puede convertir esa prueba en un corte utilizable cuando los términos y los datos de la cota pueden evaluarse. La definición de convergencia sola no proporciona ese procedimiento efectivo.

### Antes de seguir

[]{#MA-MIC-ANM-01-011-057}

1. ¿Basta $E_n\le\varepsilon$ para certificar error estrictamente menor que $\varepsilon$?

[]{#MA-MIC-ANM-01-011-058}

2. ¿Qué error tiene el punto medio de un intervalo certificado?

[]{#MA-MIC-ANM-01-011-059}

3. ¿Debe ese punto medio ser una suma parcial?

[]{#MA-MIC-ANM-01-011-060}

4. ¿Qué intervalo se obtiene con $s_4$ y $s_5$ en la armónica alternada?

[]{#MA-MIC-ANM-01-011-061}

5. ¿Ese cálculo demuestra que la suma vale $7/10$?

[]{#MA-MIC-ANM-01-011-062}

6. ¿Qué permite sumar linealmente dos series convergentes?

[]{#MA-MIC-ANM-01-011-063}

7. ¿Qué suma tiene la cola reindexada que elimina $m$ términos?

[]{#MA-MIC-ANM-01-011-064}

8. ¿Una muestra finita de totales demuestra convergencia?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-microcontroles.html)

[← Capítulo 10](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html) · [Capítulo 12 →](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html)
