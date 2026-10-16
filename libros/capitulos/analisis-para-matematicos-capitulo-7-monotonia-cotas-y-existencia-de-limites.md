---
content-id: MA-BCH-0230
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-007
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
title: Capítulo 7 — Monotonía, cotas y existencia de límites
date-modified: '2026-10-16'
provenance:
  type: original
  sources:
  - ANM-C07.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-7)

La definición de convergencia permite comprobar un número propuesto: fijamos el candidato y buscamos una cola dentro de cada ventana a su alrededor. En una recurrencia, sin embargo, podemos saber que los términos suben sin conocer una fórmula para ellos ni un número al que deban aproximarse. Si además nunca superan una barrera, el problema consiste en encontrar un destino a partir de esos dos datos.

La cota superior conocida puede dejar demasiado margen. Todos los términos de $1-1/(n+1)$ son menores que $2$, pero sus errores respecto de $2$ son mayores que $1$; esa barrera no puede ser su límite. Necesitamos una cota ajustada al conjunto entero de valores. C02 dio un nombre a la menor cota superior, y C03 garantizó su existencia real para conjuntos no vacíos y acotados superiormente. La monotonía permitirá convertir la proximidad a ese supremo en control de todos los términos posteriores.

Conservamos $\mathbb N=\{0,1,2,\ldots\}$ y las sucesiones $a:\mathbb N\to\mathbb R$. Las comparaciones de monotonía relacionan sus términos reales; el orden natural de los índices determina cuáles se comparan antes y después.

## 7.1. Comparar términos: qué significa ser monótona

[]{#MA-SEC-ANM-01-007-001}

Consideremos la sucesión $p$ definida por $p_{2k}=k$ y $p_{2k+1}=k$ para cada $k\in\mathbb N$. Todo índice natural es par o impar, así que estas dos cláusulas asignan un único valor a cada índice. Sus primeros términos son $0,0,1,1,2,2,3,3,\ldots$. Al pasar de un término al siguiente, el valor se conserva o aumenta; las repeticiones no cambian la dirección.

En los pasos de $p_{2k}$ a $p_{2k+1}$ hay igualdad; en los siguientes hay aumento. Ambas clases de paso mantienen una dirección, de modo que la comparación que buscamos debe admitir repeticiones. También una constante queda incluida al permitir la igualdad.

> **Monotonía de una sucesión real.** Una sucesión $a:\mathbb N\to\mathbb R$ es **no decreciente** si $a_n\le a_{n+1}$ para todo $n\in\mathbb N$, y es **no creciente** si $a_{n+1}\le a_n$ para todo $n\in\mathbb N$. Es **monótona** si satisface al menos una de estas dos propiedades.

La dirección debe mantenerse en todos los pasos, como expresa la disyunción

$$
\bigl(\forall n\in\mathbb N,\ a_n\le a_{n+1}\bigr)
\quad\text{o}\quad
\bigl(\forall n\in\mathbb N,\ a_{n+1}\le a_n\bigr).
$$

Cada una de las alternativas contiene su propio cuantificador universal. La disyunción es inclusiva y una constante $a_n=c$ satisface ambas, porque $c\le c$. Si pusiéramos la disyunción dentro del cuantificador y permitiéramos elegir dirección en cada índice, obtendríamos una condición verdadera para cualquier sucesión real: el orden total siempre compara $a_n$ con $a_{n+1}$.

Reservamos **estrictamente creciente** para $a_n<a_{n+1}$ en todo índice, y **estrictamente decreciente** para $a_{n+1}<a_n$ en todo índice. Estas propiedades excluyen las repeticiones adyacentes; cuando sólo se exige no decrecimiento o no crecimiento, la igualdad sigue permitida.

Para controlar una cola necesitaremos comparar un término con cualquiera de los posteriores, aunque no sean vecinos. Entre dos naturales fijados hay una cantidad finita de pasos, y la transitividad permite reunir sus comparaciones.

> **Comparación entre índices ordenados.** Para una sucesión real $a$, las siguientes condiciones son equivalentes:
>
> 1. $a_n\le a_{n+1}$ para todo $n\in\mathbb N$.
> 2. Para todos $n,m\in\mathbb N$ con $n\le m$, se cumple $a_n\le a_m$.
>
> También son equivalentes las condiciones $a_{n+1}\le a_n$ para todo $n$ y $a_m\le a_n$ para todos los índices $n\le m$.

**Demostración.** Supongamos primero que $a_k\le a_{k+1}$ para todo índice $k$. Fijemos $n,m\in\mathbb N$ con $n\le m$. Si $n=m$, la conclusión es $a_n\le a_n$. Si $n<m$, las comparaciones adyacentes dan la cadena finita

$$
a_n\le a_{n+1}\le\cdots\le a_m.
$$

Por transitividad, $a_n\le a_m$. Para hacer explícito el papel de la finitud, podemos escribir $m=n+r$ con $r\in\mathbb N$ e inducir sobre $r$: el caso $r=0$ es reflexividad, y el paso combina $a_n\le a_{n+r}$ con $a_{n+r}\le a_{n+r+1}$. Como los índices fijados eran arbitrarios, queda probada la condición para todo par ordenado.

Recíprocamente, supongamos que $a_n\le a_m$ siempre que $n\le m$. Para cualquier $n\in\mathbb N$, el natural $m=n+1$ satisface $n\le m$, así que $a_n\le a_{n+1}$. Se recupera la condición adyacente en todos los índices.

Para la dirección no creciente, supongamos que $a_{k+1}\le a_k$ para todo $k$. Si $n=m$, de nuevo basta reflexividad. Si $n<m$, la cadena es $a_m\le a_{m-1}\le\cdots\le a_n$; cada comparación usa una hipótesis adyacente y la transitividad da $a_m\le a_n$. En la dirección inversa, la comparación para $n\le m$ aplicada a $m=n+1$ da $a_{n+1}\le a_n$. Esto demuestra también la segunda equivalencia.

Cada cadena corresponde a dos índices naturales fijados, cuya diferencia es finita. La inducción justifica todas esas cadenas sin requerir un último término de la sucesión.

Las versiones estrictas siguen el mismo argumento: si cada comparación adyacente es estricta, entonces $a_n<a_m$ para $n<m$ en la dirección creciente, y $a_m<a_n$ para $n<m$ en la decreciente. Recíprocamente, esas comparaciones para índices distintos dan las adyacentes al elegir $m=n+1$. Aquí se exige $n<m$: incluir $n=m$ pediría $a_n<a_n$, imposible.

Si $a$ es no decreciente y $a_N>c$, la comparación entre índices da $c<a_N\le a_n$ para cada $n\ge N$. Así, una vez superada la barrera $c$, toda la cola permanece por encima. De $c\le a_N$ se obtiene igualmente $c\le a_n$, con desigualdad no estricta.

Para una sucesión no creciente ocurre lo mismo en la dirección inferior: de $a_N<c$ y $n\ge N$ se sigue $a_n\le a_N<c$. Esta propagación será útil cuando logremos encontrar un término próximo a una barrera elegida.

En la sucesión $p$, por ejemplo, $p_4=2$. Una vez verificado que $p$ no decrece, la proposición permite concluir $p_n\ge2$ para todo $n\ge4$. Para justificar la hipótesis en todo índice, distinguimos las dos paridades: de $2k$ a $2k+1$ los valores son iguales a $k$, y de $2k+1$ a $2k+2$ pasan de $k$ a $k+1$. Ambas comparaciones son no decrecientes. La muestra inicial sugería la dirección; estas dos cláusulas la demuestran para todos los pasos.

Cuando conocemos una fórmula, podemos examinar el signo de $a_{n+1}-a_n$ para un índice arbitrario. Sumando o restando el mismo real, $a_n\le a_{n+1}$ equivale a $a_{n+1}-a_n\ge0$, y la comparación opuesta equivale a diferencia no positiva.

Para $x_n=1-1/(n+1)$, los denominadores son positivos también en $n=0$, y

$$
x_{n+1}-x_n
=\frac1{n+1}-\frac1{n+2}
=\frac1{(n+1)(n+2)}>0.
$$

Esto demuestra que $x$ es estrictamente creciente. La sucesión $z_n=1/(n+1)$ tiene la diferencia opuesta, $z_{n+1}-z_n=-1/[(n+1)(n+2)]<0$, así que es estrictamente decreciente. La comparación entre índices vale globalmente en ambas, con su dirección correspondiente.

Para refutar una dirección universal basta un paso que la contradiga. En $r_n=(-1)^n$, tenemos $r_0=1>r_1=-1$, por lo que no es no decreciente. También $r_1=-1<r_2=1$, por lo que no es no creciente. Estas dos comparaciones refutan las dos alternativas de la definición: $r$ no es monótona. Una sola caída habría refutado únicamente el no decrecimiento; todavía habría que examinar la otra dirección.

| Sucesión | No decreciente | No creciente | Comparación decisiva |
|---|---|---|---|
| $a_n=1$ | Sí | Sí | Igualdad en cada paso |
| $p_{2k}=p_{2k+1}=k$ | Sí | No | Igualdad o subida; de índice 1 a 2 pasa de 0 a 1 |
| $x_n=1-1/(n+1)$ | Sí | No | Diferencia positiva para todo $n$ |
| $z_n=1/(n+1)$ | No | Sí | Diferencia negativa para todo $n$ |
| $r_n=(-1)^n$ | No | No | Baja de índice 0 a 1 y sube de 1 a 2 |

![Pasos iguales, aumentos y cambios de dirección en tres sucesiones. La monotonía compara términos en todos los índices; las repeticiones son compatibles con ella.](../../assets/books/anm/C07/C07-F01.svg){#fig-anm-c07-f01 fig-alt="Tres gráficas de puntos: una constante en 1, otra con pares de alturas iguales que aumentan, y otra que alterna entre 1 y menos 1."}

En la [figura de los pasos](#fig-anm-c07-f01), índices distintos pueden tener la misma altura. Los puntos representan pares $(n,a_n)$ y quedan separados: la función no asigna valores a posiciones intermedias entre naturales.

Las constantes cumplen ambas direcciones. También podemos demostrar la vuelta. Si $a$ es no decreciente y no creciente, para cualquier $n\in\mathbb N$ la comparación con el índice 0 da $a_0\le a_n$ y $a_n\le a_0$. Por antisimetría, $a_n=a_0$. Por tanto, **una sucesión es a la vez no decreciente y no creciente si y sólo si es constante**.

La constancia y los pares repetidos de $p$ son compatibles con la definición de función: cada índice recibe un único valor. Lo que cambia es cuántos índices comparten ese valor.

Una muestra creciente tampoco garantiza monotonía global. Definamos $b_n=n$ para $0\le n\le100$ y $b_n=-1$ para $n\ge101$. Es una función definida en todo $\mathbb N$, y sus primeros 101 términos son $0,1,\ldots,100$. Sin embargo, $b_{100}=100>b_{101}=-1$ refuta el no decrecimiento. El paso $b_0=0<b_1=1$ refuta el no crecimiento, de modo que la sucesión tampoco es monótona. Un listado finito puede ocultar el infractor que queda fuera de él.

### Ejercicios de la sección 7.1

[]{#ejercicios-7}

#### Ejercicio 1. Comparaciones y alcance de los cuantificadores

[]{#MA-EX-ANM-01-007-001}

Para una sucesión $a:\mathbb N\to\mathbb R$, considera estas afirmaciones:

- $P$: para todo $n\in\mathbb N$, $a_n\le a_{n+1}$.
- $Q$: para todos $n,m\in\mathbb N$, si $n\le m$, entonces $a_n\le a_m$.
- $R$: para todo $n\in\mathbb N$, $a_n<a_{n+1}$.
- $S$: para todos $n,m\in\mathbb N$, si $n<m$, entonces $a_n<a_m$.
- $M$: $(\forall n\in\mathbb N,\ a_n\le a_{n+1})\ \lor\ (\forall n\in\mathbb N,\ a_{n+1}\le a_n)$.
- $V$: para todo $n\in\mathbb N$, $a_n\le a_{n+1}\ \lor\ a_{n+1}\le a_n$.

Demuestra $P\Leftrightarrow Q$ y $R\Leftrightarrow S$, y explica el cambio de $n\le m$ a $n<m$. Determina cuáles caracterizan el no decrecimiento y cuáles el crecimiento estricto. Justifica $R\Rightarrow P$ y refuta la implicación inversa con una constante. ¿Qué propiedad expresa $M$? Decide si $M$ y $V$ son equivalentes, justificando tu respuesta con un ejemplo cuando haga falta. En las comparaciones, distingue índices y términos.

[]{#MA-SOL-ANM-01-007-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

La función $a$ es la sucesión; $n,m,n+1$ son índices naturales y $a_n,a_m,a_{n+1}$ son términos reales. Las desigualdades entre índices determinan qué posiciones se comparan; las desigualdades entre términos expresan la dirección de sus valores.

Si vale $P$ y fijamos $n\le m$, el caso $n=m$ da $a_n\le a_n$. Para $n<m$, la cadena finita $a_n\le a_{n+1}\le\cdots\le a_m$ da $a_n\le a_m$ por transitividad. Así se obtiene $Q$. Recíprocamente, $Q$ aplicada a $m=n+1$ da $P$ en cada índice. Por tanto, $P$ y $Q$ caracterizan el no decrecimiento.

El mismo razonamiento con desigualdades estrictas demuestra $R\Rightarrow S$: para $n<m$ hay al menos un paso y la cadena estricta llega de $a_n$ a $a_m$. Al tomar $m=n+1$, $S$ da $R$. Ambas caracterizan el crecimiento estricto. En $S$ no se incluye $n=m$, pues exigiría $a_n<a_n$, que es falso. En $Q$ sí puede incluirse, porque la desigualdad no estricta admite igualdad.

Toda desigualdad estricta implica la correspondiente no estricta, de modo que $R\Rightarrow P$. La sucesión constante $a_n=0$ satisface $P$ y $Q$, pero no $R$ ni $S$: sus términos de índices distintos también son iguales. La implicación inversa queda refutada.

$M$ es la definición de monotonía. Su disyunción permite una dirección universal o la otra, y admite ambas en una constante. $V$, en cambio, es verdadera para cualquier sucesión real, porque el orden total compara los dos términos en cada índice. En $r_n=(-1)^n$, $V$ sigue siendo verdadera, pero $r_0>r_1$ refuta la primera alternativa de $M$ y $r_1<r_2$ refuta la segunda. Por tanto, $M$ implica $V$ y $V$ no implica $M$. Permitir que la dirección cambie con el índice elimina la restricción que expresa la monotonía.

</details>

#### Ejercicio 2. Las mismas alturas en otro orden

[]{#MA-EX-ANM-01-007-002}

Sea $E=\{2j:j\in\mathbb N\}\subseteq\mathbb R$. Construye dos funciones $a,b:\mathbb N\to\mathbb R$ cuyo conjunto de valores sea $E$: una estrictamente creciente y otra que no sea monótona. Puedes partir de la enumeración natural de $E$ e intercambiar vecinos. Define ambas para todos los índices, prueba las dos igualdades de conjuntos y acredita cada afirmación sobre dirección. Explica por qué $a(\mathbb N)=b(\mathbb N)$ no implica $a=b$ ni igualdad de sus gráficas discretas.

[]{#MA-SOL-ANM-01-007-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Tomamos $a_n=2n$ y definimos $b_{2k}=4k+2$, $b_{2k+1}=4k$ para todo $k\in\mathbb N$. La paridad asigna a cada índice una única cláusula, de modo que $b$ está definida en todo $\mathbb N$. Ambas funciones tienen codominio $\mathbb R$ y valores en $E$.

Todo término de $a$ pertenece a $E$ y cada $2j\in E$ se obtiene en el índice $j$; así, $a(\mathbb N)=E$. Los términos de $b$ son $2(2k+1)$ y $2(2k)$, por lo que también pertenecen a $E$. Para la otra inclusión, si $j=2k$, el valor $2j=4k$ aparece en el índice $2k+1$; si $j=2k+1$, el valor $2j=4k+2$ aparece en el índice $2k$. Estas dos posibilidades cubren todo $j\in\mathbb N$, y prueban $E\subseteq b(\mathbb N)$. Por tanto, $b(\mathbb N)=E$.

Para todo $n$, $a_{n+1}-a_n=2>0$, así que $a$ es estrictamente creciente. En $b$, la caída $b_0=2>b_1=0$ refuta el no decrecimiento y la subida $b_1=0<b_2=6$ refuta el no crecimiento. Por eso $b$ no es monótona.

Las funciones son distintas porque $a_0=0$ y $b_0=2$. Sus gráficas, colecciones de pares $(n,a_n)$ y $(n,b_n)$, también son distintas: la primera contiene $(0,0)$ y la segunda no. Al formar el conjunto de valores se conserva la altura y se pierde la posición que la sucesión le asignaba. Las dos funciones tienen el mismo dominio, codominio y conjunto de valores, pero esa información no determina su evaluación en cada índice.

</details>

#### Ejercicio 3. Bloques de longitud variable

[]{#MA-EX-ANM-01-007-003}

Fija $m\in\mathbb N$ con $m\ge2$. Construye una sucesión $a^{(m)}:\mathbb N\to\mathbb R$ que tome el valor $k$ exactamente en los $m$ índices del bloque $mk,mk+1,\ldots,mk+m-1$, para cada $k\in\mathbb N$. Justifica que la regla asigna un único valor a cada índice. Demuestra el no decrecimiento distinguiendo el interior de un bloque de su frontera y prueba que los valores no tienen cota superior real. Decide si la sucesión es estrictamente creciente o no creciente, y explica por qué las repeticiones no impiden que sea función.

[]{#MA-SOL-ANM-01-007-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Usamos la división con resto de naturales: como $m>0$, cada $n\in\mathbb N$ se escribe de manera única como $n=mk+r$, con $k,r\in\mathbb N$ y $0\le r<m$. Definimos $a^{(m)}_n=k$, considerado como número real. La existencia de esa escritura cubre el dominio entero y su unicidad evita asignar dos valores al mismo índice. Para un $k$ fijo, el cociente es $k$ precisamente en los $m$ índices $mk,\ldots,mk+m-1$; los otros bloques tienen cocientes distintos.

Fijemos un índice $n=mk+r$. Si $r<m-1$, entonces $n+1=mk+(r+1)$ sigue en el mismo bloque, y $a^{(m)}_{n+1}=k=a^{(m)}_n$. Si $r=m-1$, entonces $n+1=m(k+1)$ comienza el bloque siguiente, y $a^{(m)}_{n+1}=k+1>k=a^{(m)}_n$. Los casos son exhaustivos y ambos dan $a^{(m)}_n\le a^{(m)}_{n+1}$. Queda probado el no decrecimiento en todo índice.

Para probar que no hay cota superior real, sea $U\in\mathbb R$ arbitrario. La propiedad arquimediana disponible desde C03 permite elegir $k\in\mathbb N$ con $k>U$. El índice $mk$ es natural y satisface $a^{(m)}_{mk}=k>U$. Como la construcción da un término que supera cada candidato $U$, ninguna cota superior real existe.

La sucesión no es estrictamente creciente: $m\ge2$ garantiza que $a^{(m)}_0=a^{(m)}_1=0$. Tampoco es no creciente, pues $a^{(m)}_{m-1}=0<1=a^{(m)}_m$. La repetición en cada bloque no afecta la definición de función: a cada índice se le asigna un solo valor, aunque varios índices compartan ese valor. Cuando $m=2$, la construcción recupera los pares repetidos de §7.1; el argumento de las fronteras sirve para todas las longitudes admitidas.

</details>

#### Ejercicio 4. Una suma que no cambia

[]{#MA-EX-ANM-01-007-004}

Sean $a,b:\mathbb N\to\mathbb R$ dos sucesiones no decrecientes y sea $c\in\mathbb R$. Supón que $a_n+b_n=c$ para todo $n\in\mathbb N$. Demuestra que cada sucesión es constante. Localiza dónde se usa la dirección común. Si se sustituye esa hipótesis por «cada sucesión es monótona, con direcciones posiblemente distintas», decide si la conclusión sigue siendo válida y justifica tu decisión. ¿Las hipótesis originales obligan además a que $a=b$ como funciones?

[]{#MA-SOL-ANM-01-007-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

La dirección común permite comparar incrementos del mismo signo. Para cada $n\in\mathbb N$, el no decrecimiento da $a_{n+1}-a_n\ge0$ y $b_{n+1}-b_n\ge0$. Al restar las igualdades de la suma en los índices $n+1$ y $n$, obtenemos

$$
(a_{n+1}-a_n)+(b_{n+1}-b_n)=c-c=0.
$$

Dos reales no negativos con suma cero deben ser ambos cero: si uno fuera positivo, al sumarle el otro la suma seguiría siendo positiva. Por tanto, $a_{n+1}=a_n$ y $b_{n+1}=b_n$ para todo $n$. La inducción desde el índice 0 da $a_n=a_0$ y $b_n=b_0$ en todos los índices. Cada sucesión es constante, y sus valores constantes satisfacen $a_0+b_0=c$.

Si las direcciones pueden ser distintas, los incrementos pueden cancelarse sin ser cero. Para cualquier $c\in\mathbb R$, las funciones $a_n=n$ y $b_n=c-n$ tienen suma $c$ en cada índice. La primera es estrictamente creciente y la segunda estrictamente decreciente; ninguna es constante. La hipótesis debilitada no implica la conclusión.

La conclusión original tampoco exige igualdad de las dos funciones. Por ejemplo, $a_n=c/2-1$ y $b_n=c/2+1$ son constantes, ambas no decrecientes y con suma $c$, pero difieren en cada índice. Bajo las hipótesis originales, $a=b$ se cumple si y sólo si $a_0=b_0$; junto con la suma, esto equivale a $a_0=b_0=c/2$. La constancia de cada función y la igualdad entre funciones son afirmaciones distintas.

</details>

## 7.2. El conjunto de valores y su mejor barrera

[]{#MA-SEC-ANM-01-007-002}

Para estudiar cotas podemos reunir los términos en $S_a=\{a_n:n\in\mathbb N\}\subseteq\mathbb R$. Este conjunto siempre es no vacío, pues contiene $a_0$, pero registra cada valor una sola vez, sin conservar los índices en que aparece.

En $p$, cada natural aparece dos veces como término y $S_p=\{0,1,2,\ldots\}$ como subconjunto de $\mathbb R$. La repetición desaparece al formar el conjunto, al igual que la información sobre el orden de aparición.

Esa pérdida incluye el orden de aparición. La sucesión $a_n=n$ y la función $b$ dada por $b_0=0$, $b_1=2$, $b_2=1$ y $b_n=n$ para $n\ge3$ tienen el mismo conjunto de valores. Sin embargo, $a$ es estrictamente creciente y $b$ no es monótona: sube de índice 0 a 1 y baja de 1 a 2. El conjunto sirve para estudiar cotas, pero no sustituye a la función cuando importa la monotonía.

Un real $U$ domina la sucesión si y sólo si domina $S_a$: cada término pertenece a ese conjunto y cada elemento suyo es algún término. Esta equivalencia permite aplicar los resultados de C02 sobre cotas a una función sin confundirla con su conjunto de valores.

Recordemos la distinción de C02. Un número $s$ es el **supremo** de $S_a$ si es cota superior y, además, $s\le U$ para toda cota superior $U$ de $S_a$. Un **máximo** es un elemento del conjunto que es mayor o igual que todos los demás. Por tanto, si un conjunto tiene máximo, ese máximo es también su supremo: al pertenecer al conjunto, cualquier cota superior debe estar por encima de él. La vuelta exige pertenencia. Si $s=\sup S_a$ y $s\in S_a$, entonces $s$ es máximo; si $s\notin S_a$, el conjunto no tiene máximo, pues cualquier máximo tendría que ser su supremo.

Con una cota superior real ya podemos invocar C03 §3.2: **todo subconjunto no vacío de $\mathbb R$ acotado superiormente tiene supremo real**. El conjunto $S_a$ cumple la no vaciedad gracias a $a_0$ y recibe la cota de la sucesión. La completitud proporciona así su supremo, aunque la sucesión no sea monótona; la dirección de sus términos tendrá otro papel en la prueba de convergencia.

Tampoco es necesario que una cota superior sea el supremo. Si $U$ es cota y $V\ge U$, entonces $a_n\le U\le V$ para todo $n$, por lo que $V$ también es cota. El supremo selecciona la menor entre ellas, aunque ese número no sea un término de la sucesión.

La menor cota superior deja valores inmediatamente por debajo de ella: para cada $\varepsilon>0$, la franja $(s-\varepsilon,s]$ debe contener algún $a_j$. Si estuviera vacía, podríamos bajar la cota hasta $s-\varepsilon$. Ésta es la caracterización de C02 §2.5 expresada mediante los índices de la sucesión.

> **Caracterización de la barrera superior.** Para una sucesión real $a$ y un número real $s$, son equivalentes:
>
> 1. $s=\sup S_a$.
> 2. $s$ es cota superior de $S_a$ y para cada $\varepsilon>0$ existe un $j\in\mathbb N$ con $s-\varepsilon<a_j$.

La condición de cota impide términos por encima de $s$ y la aproximación impide bajar esa cota. Las dos obligaciones permiten reconocer el supremo sin ninguna hipótesis de monotonía.

**Demostración.** Supongamos que $s=\sup S_a$ y fijemos $\varepsilon>0$. El número $s-\varepsilon$ es menor que $s$, por lo que no puede ser cota superior: si lo fuera, la minimalidad daría $s\le s-\varepsilon$, contradicción. Ser cota superior equivale a $a_n\le s-\varepsilon$ para todo $n$. La negación clásica de esa afirmación universal proporciona un índice $j$ con $a_j>s-\varepsilon$. Como $s$ sí es cota, también $a_j\le s$. Así se obtiene el valor en la franja.

Recíprocamente, supongamos que $s$ es cota superior y que cumple la aproximación indicada. Sea $U$ cualquier cota superior de $S_a$. Si $U<s$, la tolerancia $\varepsilon=s-U>0$ daría un índice $j$ con $a_j>s-\varepsilon=U$, contradiciendo que $U$ sea cota. Por tanto $s\le U$ para toda cota superior $U$. Junto con la condición de cota de $s$, esto demuestra $s=\sup S_a$.

Esta prueba reconoce un candidato; la existencia del supremo bajo no vaciedad y acotación sigue procediendo de C03. Para una tolerancia fijada basta justificar que existe un índice apropiado, aunque no dispongamos de una fórmula que lo encuentre. No hace falta elegir a la vez todos los testigos.

Volvamos a $x_n=1-1/(n+1)$. Como $n+1>0$, todos sus términos son menores que 1; por tanto 1 y 2 son cotas superiores, y ningún término vale 1. Para comprobar que 1 es el supremo, falta la obligación de aproximación.

En C06 §6.3 demostramos que $1/(n+1)$ converge a cero. Dada $\varepsilon>0$, esa prueba proporciona un índice $j$ con $1/(j+1)<\varepsilon$. De ahí $x_j=1-1/(j+1)>1-\varepsilon$. Por la caracterización anterior, $\sup S_x=1$. Como $1\notin S_x$, no hay máximo. Esta verificación usa una herramienta ya disponible y no presupone el teorema de convergencia monótona que demostraremos en §7.3.

En la constante $c_n=1$, el conjunto de valores es $S_c=\{1\}$. Tiene supremo y máximo iguales a 1, y para cualquier $\varepsilon>0$ el término $c_0=1$ satisface $1-\varepsilon<c_0\le1$. La propiedad de aproximación incluye este caso de error cero; no exige que los términos se acerquen desde puntos distintos del supremo.

Los dos supremos valen $1$, pero las funciones difieren ya en el índice cero: $x_0=0$ y $c_0=1$. También sus imágenes son distintas, pues sólo la constante contiene $1$. La cota $2$, disponible para ambas, deja un margen que impide que sea su supremo.

Con $\varepsilon=1/4$, la franja es $(3/4,1]$. Tenemos $x_3=3/4$, sobre la frontera inferior excluida, y $x_4=4/5$, dentro de la franja. El término constante 1 también está dentro. El contraste se lee sobre un eje de **valores**, sin necesidad de usar el eje de índices de una gráfica de sucesión. Marcar el punto 1 como barrera en el caso de $x$ no lo añade a su conjunto de valores.

![La cota 2 deja margen; el supremo 1 no. La misma barrera se alcanza en la constante y no se alcanza en $x$.](../../assets/books/anm/C07/C07-F02.svg){#fig-anm-c07-f02 fig-alt="Un eje real muestra valores discretos de x por debajo de 1, el valor único de la constante en 1 y la cota 2; la franja inferior excluye tres cuartos."}

Por abajo, una cota inferior $\ell$ cumple $\ell\le a_n$ para todo índice. C03 §3.3 garantiza un ínfimo real cuando $S_a$ está acotado inferiormente, pues ya sabemos que no es vacío. Ese ínfimo es la mayor cota inferior, y será mínimo exactamente si pertenece al conjunto.

La caracterización correspondiente afirma que $t=\inf S_a$ si y sólo si $t$ es cota inferior y para cada $\varepsilon>0$ hay un índice $j$ con $a_j<t+\varepsilon$. La cota añade $t\le a_j$, así que el valor está en $[t,t+\varepsilon)$, con frontera superior excluida.

Para justificarla, si $t$ es ínfimo, $t+\varepsilon$ no puede ser cota inferior: sería una cota mayor que la mayor de ellas. La negación de $t+\varepsilon\le a_n$ para todos los índices da un $j$ con $a_j<t+\varepsilon$. En la vuelta, supongamos cota y aproximación y sea $\ell$ cualquier cota inferior. Si $\ell>t$, tomamos $\varepsilon=\ell-t$ y obtenemos $a_j<t+\varepsilon=\ell$, contradicción. Así $\ell\le t$ para todas las cotas inferiores, que es la maximalidad requerida.

En $z_n=1/(n+1)$, el número 0 es cota inferior y, por la prueba de C06, hay valores menores que cualquier $\varepsilon>0$. Luego $\inf S_z=0$. Ningún término es cero, de modo que no hay mínimo. La ausencia de alcanzamiento es compatible con una barrera extremal también en esta dirección.

Encontrar un valor en cada franja sigue dejando abiertos los índices posteriores al testigo. La aproximación $\forall\varepsilon>0\ \exists j\in\mathbb N:\ s-\varepsilon<a_j\le s$ carece del control de toda una cola que exige C06.

En $r_n=(-1)^n$, el conjunto de valores es $\{-1,1\}$ y su supremo es 1. Para cualquier tolerancia positiva, el índice $j=0$ proporciona un término igual al supremo y satisface la aproximación. Sin embargo, $r$ no converge a 1: con $\varepsilon=1$, ante cualquier corte $N$ el índice impar $2N+1\ge N$ tiene término −1 y error $|-1-1|=2\ge1$. Esta refutación se refiere al candidato 1; no inferimos de ella por sí sola una afirmación sobre todos los candidatos.

### Ejercicios de la sección 7.2

#### Ejercicio 5. Cota, barrera mínima y posición de alcanzamiento

[]{#MA-EX-ANM-01-007-005}

Sean $a:\mathbb N\to\mathbb R$, $S_a=a(\mathbb N)$ y $U,s\in\mathbb R$. Justifica la equivalencia entre $a_n\le U$ para todo $n$, $S_a\subseteq(-\infty,U]$ y $S_a\cap(U,\infty)=\varnothing$. Escribe con cuantificadores qué obligación adicional convierte una cota $s$ en $\sup S_a$. Demuestra que $s$ es máximo de $S_a$ si y sólo si es su supremo y el conjunto de índices $I_s=\{j\in\mathbb N:a_j=s\}$ es no vacío.

Aplica estas distinciones a $d_0=-1$ y $d_n=4$ para $n\ge1$: determina $S_d$, clasifica la cota superior 6, calcula el supremo y el máximo, y describe $I_4$. Distingue el tipo del número 4, del conjunto de valores, del conjunto de índices y de la función $d$.

[]{#MA-SOL-ANM-01-007-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

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

</details>

#### Ejercicio 6. Una barrera prescrita, con y sin alcanzamiento

[]{#MA-EX-ANM-01-007-006}

Para cada $s\in\mathbb R$ y $h\ge0$, construye dos sucesiones reales $a^{s,h}$ y $b^{s,h}$ con todos sus términos en $[s-h,s]$ y con supremo del conjunto de valores igual a $s$. Si $h>0$, exige que la primera no alcance $s$ y que la segunda lo alcance en un único índice. Si $h=0$, determina qué funciones permite la condición sobre el intervalo y qué ocurre con el alcanzamiento. Verifica cota y aproximación para tus construcciones y declara sus dominios; no necesitas calcular límites.

[]{#MA-SOL-ANM-01-007-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Para cada par de parámetros admitido, definimos funciones de $\mathbb N$ a $\mathbb R$ mediante $a^{s,h}_n=s-h/(n+1)$ y

$$
b^{s,h}_0=s,\qquad b^{s,h}_n=s-\frac hn\quad(n\ge1).
$$

Los denominadores son positivos en sus respectivos dominios; la cláusula especial de $b$ evita dividir por cero. Como $0\le h/(n+1)\le h$ y $0\le h/n\le h$ para $n\ge1$, todos los términos de ambas funciones están en $[s-h,s]$. En particular, $s$ es cota superior.

Sea $\varepsilon>0$. Si $h>0$, la arquimedianidad de C03 permite elegir $j\in\mathbb N$ con $j+1>h/\varepsilon$. Entonces $h/(j+1)<\varepsilon$ y $s-\varepsilon<a^{s,h}_j\le s$. Si $h=0$, el índice $j=0$ da la misma aproximación con error cero. Por la caracterización de §7.2, el supremo de la imagen de $a^{s,h}$ es $s$. Para $b^{s,h}$, el índice 0 proporciona directamente el término $s$ para toda tolerancia; junto con la cota, demuestra que su supremo también es $s$.

Cuando $h>0$, cada $h/(n+1)$ es positivo, así que ningún término de $a^{s,h}$ vale $s$; su imagen no tiene máximo. En $b^{s,h}$, el término inicial vale $s$ y todos los de índice $n\ge1$ son menores que $s$. El máximo se alcanza sólo en el índice 0. Si $h=0$, el intervalo permitido es $[s,s]=\{s\}$. Toda función que satisfaga la condición debe ser la constante $s$; nuestras dos fórmulas coinciden en esa función y alcanzan $s$ en todos los índices. La exigencia de alcanzamiento único se aplica únicamente al caso $h>0$.

</details>

#### Ejercicio 7. Aproximar con una escala numerable

[]{#MA-EX-ANM-01-007-007}

Supón que $a:\mathbb N\to\mathbb R$ y que $s\in\mathbb R$ es cota superior de $S_a$. Demuestra que $s=\sup S_a$ equivale a la condición

$$
\forall k\in\mathbb N\ \exists j\in\mathbb N:\quad 0\le s-a_j<\frac1{k+1}.
$$

Señala cómo se pasa de una tolerancia real arbitraria a una de las tolerancias indicadas y de qué dato puede depender el índice $j$. Decide si la condición mostrada, por sí sola, seguiría caracterizando el supremo al omitir la hipótesis global de cota. No uses el teorema de convergencia monótona.

[]{#MA-SOL-ANM-01-007-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Si $s=\sup S_a$, dado $k\in\mathbb N$ la tolerancia $1/(k+1)$ es positiva. La caracterización por aproximación proporciona un índice $j$ con $s-1/(k+1)<a_j\le s$, que equivale a $0\le s-a_j<1/(k+1)$. Queda probada la condición en cada $k$, incluido $k=0$.

Para la vuelta, conservamos la hipótesis de que $s$ domina todos los términos. Recibida una tolerancia real $\varepsilon>0$, usamos la arquimedianidad para elegir $k\in\mathbb N$ con $k+1>1/\varepsilon$. Así, $1/(k+1)<\varepsilon$. La condición del enunciado para ese $k$ da un índice $j$ con $0\le s-a_j<\varepsilon$, y por tanto $s-\varepsilon<a_j\le s$. La cota y la aproximación para toda tolerancia demuestran $s=\sup S_a$ por §7.2. La elección sigue el orden $\varepsilon$, luego $k$ y después un testigo $j$ para ese $k$; no se exige que el mismo $j$ sirva para todas las escalas, ni se ha probado control sobre los índices posteriores a él.

La hipótesis global de cota es necesaria. En $a_n=n$ y $s=0$, para cada $k$ el índice $j=0$ satisface $0\le s-a_j=0<1/(k+1)$. Sin embargo, $s$ no es cota superior, pues $a_1=1>0$, y por eso no puede ser supremo. El control del error en los términos elegidos no controla los demás términos.

</details>

#### Ejercicio 8. Igual imagen acotada, distinto comportamiento

[]{#MA-EX-ANM-01-007-008}

Sea $E=\{0\}\cup\{1/(j+1):j\in\mathbb N\}$. Construye $a,b:\mathbb N\to\mathbb R$ con $a(\mathbb N)=b(\mathbb N)=E$, tales que $a$ converja a 0 y $b$ no converja a ningún real. Puedes cambiar cuántas veces aparece cada valor. Prueba la igualdad de ambas imágenes, da cotas comunes y justifica las afirmaciones de convergencia desde los cuantificadores de C06. Explica por qué tu construcción no representa una permutación biyectiva de los índices de la sucesión convergente.

[]{#MA-SOL-ANM-01-007-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Definimos $a_0=0$ y $a_n=1/n$ para $n\ge1$. Para la segunda función ponemos $b_{3k}=0$, $b_{3k+1}=1$ y $b_{3k+2}=1/(k+1)$ para todo $k\in\mathbb N$. Todo índice tiene una escritura única $3k+r$ con $r\in\{0,1,2\}$, así que las tres cláusulas definen $b$ en todo $\mathbb N$ sin ambigüedad. Todos los denominadores utilizados son positivos.

Cada término de $a$ está en $E$; 0 aparece en el índice 0 y el valor $1/(j+1)$ aparece en el índice $j+1$. Esto prueba $a(\mathbb N)=E$ por ambas inclusiones. En $b$, los valores 0 y 1 pertenecen a $E$, al igual que cada $1/(k+1)$, de modo que su imagen está contenida en $E$. Además, 0 aparece en el índice 0 y cada $1/(j+1)$ aparece en el índice $3j+2$. De ahí $E\subseteq b(\mathbb N)$ y la igualdad de imágenes. Ambas sucesiones satisfacen las cotas comunes $0\le a_n\le1$ y $0\le b_n\le1$ en todo índice.

Para $a_n\to0$, sea $\varepsilon>0$. Elegimos por arquimedianidad un natural $N>\max\{1,1/\varepsilon\}$. Si $n\ge N$, entonces $n\ge1$ y $|a_n|=1/n\le1/N<\varepsilon$. Este único corte controla todos los índices posteriores y prueba la convergencia a 0.

Para refutar todo límite real de $b$, fijemos un candidato $L\in\mathbb R$ y la tolerancia $\varepsilon_0=1/2$. Si $|L|\ge1/2$, ante cualquier corte $N\in\mathbb N$ el índice $n=3N\ge N$ da $|b_n-L|=|L|\ge\varepsilon_0$. Si $|L|<1/2$, la desigualdad triangular da $|1-L|\ge1-|L|>1/2$; el índice $n=3N+1\ge N$ tiene $b_n=1$ y también infringe la tolerancia. Los dos casos cubren todo candidato, y en cada uno existe un infractor después de cada corte. Por tanto, $b$ no converge a ningún número real, sin recurrir a resultados sobre subsucesiones.

Una permutación biyectiva de índices conserva cuántas posiciones toman cada valor. En $a$, el valor 1 aparece únicamente en el índice 1; en $b$ aparece en todos los índices $3k+1$, además del índice 2. Si $b_n=a_{\pi(n)}$ con $\pi:\mathbb N\to\mathbb N$ biyectiva, los índices distintos 1 y 4 de $b$ tendrían que satisfacer $\pi(1)=\pi(4)=1$, contradiciendo la inyectividad. La igualdad de conjuntos de valores permite cambiar multiplicidades; no convierte la construcción en una permutación de la sucesión convergente.

</details>

#### Ejercicio 9. Un testigo convertido indebidamente en corte

[]{#MA-EX-ANM-01-007-009}

La siguiente es una **prueba defectuosa**: «Como $s=\sup S_a$, para cada $\varepsilon>0$ hay un índice $j$ con $s-\varepsilon<a_j\le s$. Tomo $N=j$; entonces $|a_n-s|<\varepsilon$ para todo $n\ge N$, y por tanto $a_n\to s$».

Localiza la inferencia sin justificación y compara los cuantificadores de la premisa con los de la conclusión. Refútala mediante una sucesión cuyo supremo sea 3, no se alcance y para la que el candidato 3 falle como límite. Construye la sucesión usando, para cada $k\in\mathbb N$, tres posiciones consecutivas: un valor que se aproxime a 3, un valor 0 y un valor 1. Justifica el supremo y da una tolerancia fija con un infractor posterior a cada corte. Repara después el argumento general incorporando una hipótesis de comparación entre términos que permita usar §7.1; demuestra el paso reparado directamente, sin invocar el teorema de §7.3.

[]{#MA-SOL-ANM-01-007-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

La premisa ofrece $\forall\varepsilon>0\ \exists j\in\mathbb N$ con $s-\varepsilon<a_j\le s$. La conclusión requiere $\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\in\mathbb N$, con $n\ge N\Rightarrow |a_n-s|<\varepsilon$. La inferencia defectuosa añade el control universal sobre $n\ge j$ sin una hipótesis que compare esos términos con $a_j$. La cota $a_n\le s$ sí vale para todos los índices; la comparación inferior $s-\varepsilon<a_n$ sólo se ha acreditado en el índice testigo.

Como contraejemplo, definimos $r_{3k}=3-1/(k+1)$, $r_{3k+1}=0$ y $r_{3k+2}=1$ para $k\in\mathbb N$. La división con resto por 3 hace la regla exhaustiva y única. Todos los valores son menores que 3: los de la primera cláusula están en $[2,3)$ y los otros son 0 y 1. Por tanto, 3 es cota y no se alcanza. Dada $\varepsilon>0$, elegimos $k$ con $k+1>1/\varepsilon$; en el índice $j=3k$ tenemos $3-\varepsilon<r_j<3$. La caracterización de §7.2 demuestra que $3=\sup S_r$ y que la imagen no tiene máximo.

El candidato 3 falla como límite: fijamos $\varepsilon_0=1$. Para cada $N\in\mathbb N$, el índice $n=3N+1\ge N$ cumple $r_n=0$ y $|r_n-3|=3\ge1$. Ningún corte controla esa tolerancia, aunque existan términos tan próximos al supremo como se pida.

Una reparación suficiente consiste en añadir que $a$ es no decreciente. Dada $\varepsilon>0$, la aproximación al supremo proporciona $j$ con $s-\varepsilon<a_j\le s$. Tomamos $N=j$. Para cualquier $n\ge N$, la comparación entre índices de §7.1 da $a_j\le a_n$ y la condición de cota da $a_n\le s$. Se obtiene $s-\varepsilon<a_j\le a_n\le s$, de donde $|a_n-s|=s-a_n<\varepsilon$. El índice testigo se ha convertido en corte gracias a la dirección añadida; este argumento comprueba directamente la definición de C06 y no invoca el teorema posterior. La reparación establece una condición suficiente, sin afirmar que sea necesaria para converger al supremo.

La [figura del testigo y la captura](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f03) distingue obtener un término próximo de controlar todos los posteriores. Ilustra el mecanismo válido bajo monotonía; no representa la trayectoria del contraejemplo de este ejercicio.

</details>

## 7.3. La completitud convierte una barrera en límite

[]{#MA-SEC-ANM-01-007-003}

El alternante alcanza su supremo y regresa después al otro valor. Para una sucesión no decreciente ese regreso queda excluido: una vez encontrado $a_N>s-\varepsilon$, la comparación entre índices sostiene la misma desigualdad para todos los posteriores.

Si además existe una cota superior $U$, la completitud proporciona $s=\sup S_a$. El término próximo que obtenemos de su minimalidad inicia entonces una cola atrapada entre $s-\varepsilon$ y $s$, exactamente la estimación que necesita el candidato $s$.

> **Convergencia de una sucesión no decreciente y acotada superiormente.** Sea $a:\mathbb N\to\mathbb R$ una sucesión no decreciente. Si existe $U\in\mathbb R$ tal que $a_n\le U$ para todo $n\in\mathbb N$, entonces $a$ converge y su límite es $s=\sup\{a_n:n\in\mathbb N\}$.

La hipótesis admite constantes y repeticiones; el supremo puede alcanzarse o permanecer fuera del conjunto de valores. La prueba construye primero ese número real y después responde a cada tolerancia.

**Demostración.** Sea $S_a=\{a_n:n\in\mathbb N\}$. El conjunto es no vacío porque contiene $a_0$. La hipótesis $a_n\le U$ para todo índice implica que $U$ es cota superior de $S_a$. Por el principio del supremo de C03 §3.2 existe un real $s=\sup S_a$. En particular, $a_n\le s$ para todo $n$.

Fijemos una tolerancia real $\varepsilon>0$. Como $s-\varepsilon<s$, el número $s-\varepsilon$ no es cota superior de $S_a$: si lo fuera, la minimalidad de $s$ daría $s\le s-\varepsilon$. Negar la afirmación universal $a_n\le s-\varepsilon$ proporciona, por lógica clásica y el orden real, un índice $N\in\mathbb N$ con $a_N>s-\varepsilon$. Ésta es la propiedad de aproximación recuperada en §7.2; no requiere una segunda invocación de completitud.

Para cualquier índice natural $n\ge N$, el no decrecimiento y §7.1 dan $a_N\le a_n$, mientras que la cota $s$ da $a_n\le s$. Reunimos ambas comparaciones:

$$
s-\varepsilon<a_N\le a_n\le s,
\qquad 0\le s-a_n<\varepsilon.
$$

Como $a_n\le s$, el error es $|a_n-s|=s-a_n<\varepsilon$ para todo $n\ge N$. El corte obtenido para la tolerancia arbitraria cumple la definición de $a_n\to s$; por unicidad, $s$ es el límite.

El candidato depende de la sucesión y queda fijado antes de recibir $\varepsilon$. El índice testigo se elige después y controla todos los $n\ge N$, sin que necesitemos conocer el menor corte posible ni un procedimiento computable para hallarlo. Si resulta $N=0$, la misma prueba controla la sucesión entera.

La desigualdad final permite $a_n=s$, pues entonces el error es cero. La frontera inferior $s-\varepsilon$, en cambio, queda excluida: allí el error sería exactamente $\varepsilon$. Una comparación no estricta $s-\varepsilon\le a_N$ no daría con esta misma tolerancia la estimación estricta requerida.

La recurrencia $u_0=0$, $u_{n+1}=(u_n+1)/2$ permite usar el resultado sin conocer todavía el valor numérico del límite. Cada paso suma y divide por el real no nulo $2$, por lo que determina un único término real a partir del anterior y define $u$ en todo $\mathbb N$.

Primero verificamos por inducción que $0\le u_n\le1$ para todos los índices. En la base, $u_0=0$ cumple ambas desigualdades. Si $0\le u_n\le1$, sumar 1 y dividir por 2, positivo, da $1/2\le u_{n+1}\le1$, y en particular $0\le u_{n+1}\le1$. Queda probado el invariante y la cota superior 1.

Con esa cota ya podemos determinar el signo de cada incremento:

$$
u_{n+1}-u_n=\frac{1-u_n}{2}\ge0.
$$

La desigualdad usa el invariante ya demostrado. Por tanto $u$ es no decreciente. El teorema recién probado se aplica: existe un límite real $L=\sup S_u$. Además, $0=u_0\le L\le1$, porque el supremo domina cada valor y es menor o igual que la cota superior 1.

Ya existe, por tanto, un límite real. La ecuación que impone la recurrencia permitirá identificarlo en §7.6, cuando el desplazamiento y las reglas de C06 tengan esta existencia como hipótesis. Los primeros términos $0,1/2,3/4,7/8$ ilustran el invariante; su validez en todos los índices procede de la inducción.

El ejemplo $x_n=1-1/(n+1)$ permite separar visualmente los papeles de cada paso. En §7.1 probamos que no decrece y en §7.2 acreditamos $\sup S_x=1$. Para $\varepsilon=1/4$, el índice $N=4$ proporciona $x_4=4/5>3/4$. En cambio, $x_3=3/4$ está sobre la frontera inferior y no sirve para iniciar una captura con esa tolerancia: su error respecto de 1 es $1/4$.

Para cualquier $n\ge4$, la monotonía da $x_4\le x_n$ y la cota da $x_n\le1$. También podemos verificar directamente el error del ejemplo: $1-x_n=1/(n+1)\le1/5<1/4$. Los términos desde el corte 4 quedan en la franja $(3/4,1]$, contenida en la ventana abierta $(1-1/4,1+1/4)$ de C06.

La [figura del testigo y la captura](#fig-anm-c07-f03) sitúa el corte $4$ en el eje de índices y las fronteras $1$ y $3/4$ en el de valores. Sólo dibuja los índices $0$–$8$; la estimación anterior acredita también los que quedan fuera de la muestra. El corte $4$ corresponde a este ejemplo y a esta tolerancia.

![El testigo 4 entra estrictamente en la franja; la monotonía y la cota mantienen allí los términos posteriores. El supremo existe antes de elegir la tolerancia.](../../assets/books/anm/C07/C07-F03.svg){#fig-anm-c07-f03 fig-alt="Puntos de x hasta el índice 8, una frontera en tres cuartos y un corte en 4; el punto de índice 3 queda en el borde excluido y los posteriores al corte dentro."}

La cota inicial $U$ garantiza que el conjunto sea admisible para completitud; no tiene por qué ser el candidato al límite. Si $U>s$, tomando $\varepsilon=(U-s)/2$ se obtiene $U-\varepsilon=(U+s)/2>s$. Todos los términos quedan por debajo de esa frontera inferior, pues $a_n\le s$. En consecuencia, esta ventana alrededor de $U$ no captura ningún término y $U$ no puede ser límite. El supremo elimina ese margen que una cota arbitraria puede dejar.

Si el supremo se alcanza en un índice $K$, la misma estructura da una conclusión adicional. Para todo $n\ge K$, el no decrecimiento implica $s=a_K\le a_n$, y la cota implica $a_n\le s$. Así $a_n=s$ desde $K$. En una sucesión no decreciente, alcanzar el supremo obliga a que la cola sea constante. El teorema incluye este caso y el de la constante desde el índice 0; no exige una aproximación sin alcanzamiento.

### Ejercicios de la sección 7.3

#### Ejercicio 10. Reensamblar el argumento y localizar las hipótesis

[]{#MA-EX-ANM-01-007-010}

Sea $a:\mathbb N\to\mathbb R$ no decreciente y supón que $a_n\le U$ para todo $n$, con $U\in\mathbb R$. Los siguientes fragmentos de prueba están desordenados:

- A: para todo $n\ge N$, $s-\varepsilon<a_N\le a_n\le s$; por tanto $|a_n-s|<\varepsilon$.
- B: se forma $S_a=\{a_n:n\in\mathbb N\}$ y se verifica que es no vacío y acotado superiormente.
- C: dada $\varepsilon>0$, se obtiene un índice $N$ con $s-\varepsilon<a_N$.
- D: existe un real $s=\sup S_a$.

Ordénalos, completa sus justificaciones e identifica qué dato o hipótesis autoriza cada paso. Distingue el papel de $U$ del de $s$, y registra el orden en que se fijan $s$, $\varepsilon$, $N$ y $n$. Para $w_n=2-1/(n+1)$, acredita las hipótesis y el supremo, y comprueba que $N=0$ sirve con tolerancia 2. Decide si sigue sirviendo con tolerancia 1 y proporciona un corte válido en ese caso.

[]{#MA-SOL-ANM-01-007-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

El orden es B, D, C, A. En B, $S_a\subseteq\mathbb R$ es no vacío porque contiene $a_0$, y $U$ lo domina porque domina todos los términos. En D se usa completitud, mediante el principio del supremo de C03: esas dos condiciones garantizan un real $s=\sup S_a$. La cota $U$ garantiza que el conjunto es admisible; el supremo $s$ será el candidato al límite. No se exige $U=s$.

En C fijamos $\varepsilon>0$. El número $s-\varepsilon$ no puede ser cota superior, pues suponerlo contradice la minimalidad de $s$. Negar $a_n\le s-\varepsilon$ para todos los índices da un $N\in\mathbb N$ con $a_N>s-\varepsilon$. Este paso usa la propiedad del supremo ya obtenido, no una nueva aplicación de completitud. En A, para cualquier $n\ge N$, el no decrecimiento y §7.1 dan $a_N\le a_n$; la condición de cota de $s$ da $a_n\le s$. Luego $0\le s-a_n<\varepsilon$ y $|a_n-s|=s-a_n<\varepsilon$. La definición de C06 queda satisfecha. El orden de elección es: candidato $s$ fijado por $a$, tolerancia $\varepsilon$, índice testigo $N$ y, después, índice arbitrario $n\ge N$.

En $w_n=2-1/(n+1)$, el denominador es positivo y $w_{n+1}-w_n=1/[(n+1)(n+2)]>0$. La sucesión es no decreciente y 2 es cota superior. Para toda $\eta>0$, la arquimedianidad permite elegir $j$ con $j+1>1/\eta$, lo que da $2-\eta<w_j<2$. La caracterización de §7.2 demuestra que el supremo es 2.

Con tolerancia 2, $N=0$ sirve: para todo $n\ge0$, $|w_n-2|=1/(n+1)\le1<2$. Con tolerancia 1 no sirve, porque el índice 0 tiene error 1 y la definición exige error menor que 1. El corte $N=1$ sí controla todos los índices posteriores, ya que $1/(n+1)\le1/2<1$. Un corte 0 es tan admisible como cualquier otro natural; lo que decide su validez es la estimación para todos los términos desde él.

La [figura del testigo y la captura](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f03) permite volver a localizar las obligaciones: completitud fija el candidato y monotonía propaga la comparación.

</details>

#### Ejercicio 11. Una familia con denominador desplazado

[]{#MA-EX-ANM-01-007-011}

Sean $\alpha,\beta,q\in\mathbb R$, con $\beta\ge0$ y $q>0$. Estudia la sucesión $a_n=\alpha-\beta/(n+q)$ para $n\in\mathbb N$: verifica su buena definición, dirección, cotas y existencia de límite mediante §7.3. Identifica después su supremo y su límite. Separa $\beta=0$ de $\beta>0$, indica cuándo la dirección es estricta y justifica la elección de un índice para cada tolerancia. Explica por qué hay que controlar el denominador también en $n=0$.

[]{#MA-SOL-ANM-01-007-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Los parámetros $\alpha,\beta,q$ son reales; el índice $n$ es natural y $a_n$ es un término real. Como $q>0$ y $n\ge0$, el denominador $n+q$ es positivo en todo el dominio, incluido $n=0$. La fórmula define una función de $\mathbb N$ a $\mathbb R$. Si se admitiese $q=0$, la fórmula no definiría el término inicial cuando se presenta como ese cociente, incluso si $\beta=0$.

La diferencia adyacente es

$$
a_{n+1}-a_n
=\frac{\beta}{n+q}-\frac{\beta}{n+1+q}
=\frac{\beta}{(n+q)(n+1+q)}\ge0.
$$

Por tanto, $a$ no decrece. Los denominadores positivos y $n+q\ge q$ dan $0\le\beta/(n+q)\le\beta/q$, así que $a_0=\alpha-\beta/q\le a_n\le\alpha$. Ya están acreditadas las hipótesis de §7.3: existe un límite real y es el supremo de $S_a$.

Si $\beta=0$, todos los términos valen $\alpha$, la dirección no es estricta y el supremo y el límite son $\alpha$. Si $\beta>0$, la diferencia adyacente es positiva en todo índice, de modo que la sucesión es estrictamente creciente; además, ningún término alcanza $\alpha$. Para identificar el supremo, sea $\varepsilon>0$. Elegimos por arquimedianidad un natural $N>\max\{0,\beta/\varepsilon-q\}$. Entonces $N+q>\beta/\varepsilon$ y $\alpha-\varepsilon<a_N<\alpha$. La cota superior $\alpha$ y esta aproximación demuestran $\sup S_a=\alpha$. El límite cuya existencia ya se obtuvo es, por ello, $\alpha$. La misma elección controla toda la cola: si $n\ge N$, $|a_n-\alpha|=\beta/(n+q)\le\beta/(N+q)<\varepsilon$.

</details>

#### Ejercicio 12. Reconocer el supremo desde un límite ya conocido

[]{#MA-EX-ANM-01-007-012}

Sea $a:\mathbb N\to\mathbb R$ no decreciente y supón que $a_n\to L\in\mathbb R$. Sin aplicar el teorema de §7.3 para obtener una cota, demuestra que $a_k\le L$ para todo $k\in\mathbb N$. Usa esa cota y la convergencia para demostrar que $L=\sup S_a$. En el primer paso, explica cómo se coordina un índice $k$ previamente fijado con un corte de convergencia elegido después de una tolerancia. ¿Hace falta suponer de entrada una cota superior adicional?

[]{#MA-SOL-ANM-01-007-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Fijemos $k\in\mathbb N$. Si $a_k>L$, tomamos $\varepsilon=(a_k-L)/2>0$. La convergencia proporciona un corte $N$ para esa tolerancia. El índice $n=\max\{k,N\}$ está después de $k$ y después del corte: la monotonía da $a_k\le a_n$ y la convergencia da $a_n<L+\varepsilon=(a_k+L)/2<a_k$. Las dos desigualdades se contradicen. Por tanto, $a_k\le L$ para cada $k$, y $L$ es cota superior de $S_a$.

Recibida ahora cualquier tolerancia $\eta>0$, la convergencia permite elegir un corte $M$ con $|a_M-L|<\eta$. En particular, $L-\eta<a_M$, mientras que la cota recién probada da $a_M\le L$. Así se cumplen cota y aproximación para el candidato $L$; por §7.2, $L=\sup S_a$.

No hizo falta suponer una cota adicional ni usar el teorema de §7.3 para fabricarla. En el primer argumento se fija $k$, se construye una tolerancia a partir del supuesto $a_k>L$, se obtiene $N$ y se elige un índice que reúna ambas exigencias. La convergencia se usa para impedir que un término por encima de $L$ pueda propagarse a todos los posteriores.

</details>

#### Ejercicio 13. Recuperar la desigualdad estricta

[]{#MA-EX-ANM-01-007-013}

Supón que $a:\mathbb N\to\mathbb R$ es no decreciente, que $s\in\mathbb R$ domina todos sus términos y que para cada $\delta>0$ puedes obtener un índice $N_\delta$ con $s-\delta\le a_{N_\delta}$. Adapta la prueba ε–N para concluir $a_n\to s$, aunque el testigo sólo dé una desigualdad no estricta. Justifica también que $s=\sup S_a$. Explica por qué usar $\delta=\varepsilon$ y conservar cualquier testigo recibido no garantiza el error estricto; ilústralo con una sucesión no decreciente cuyo supremo sea 0, tolerancia 1 y testigo inicial situado en la frontera. Da una elección auxiliar que repare la prueba para toda tolerancia, no sólo para ese ejemplo.

[]{#MA-SOL-ANM-01-007-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

La tolerancia auxiliar debe ser menor que la tolerancia pedida. Sea $\varepsilon>0$ y tomemos $\delta=\varepsilon/2$. La hipótesis proporciona un índice $N=N_\delta$ con $s-\delta\le a_N$. Para todo $n\ge N$, §7.1 y la cota superior dan $s-\delta\le a_N\le a_n\le s$. Luego $|a_n-s|=s-a_n\le\delta=\varepsilon/2<\varepsilon$. Aunque el primer control admita igualdad, el margen reservado entre $\delta$ y $\varepsilon$ recupera el error estricto en toda la cola. Esto prueba $a_n\to s$ desde la definición.

También identifica el supremo sin circularidad. Para cada $\varepsilon>0$, ese mismo testigo satisface $a_N\ge s-\varepsilon/2>s-\varepsilon$. Junto con la cota global de $s$, la caracterización de §7.2 da $s=\sup S_a$.

Si se usase $\delta=\varepsilon$, sólo se obtendría error $\le\varepsilon$ desde el testigo, insuficiente para conservar ese corte. Por ejemplo, definamos $a_0=-1$ y $a_n=0$ para $n\ge1$. Es no decreciente y tiene supremo $s=0$, alcanzado desde el índice 1. La condición de aproximación no estricta se cumple para toda $\delta>0$, pues el índice 1 siempre sirve. Para $\delta=\varepsilon=1$, también es admisible el testigo $N_1=0$, ya que $s-1=-1=a_0$. Sin embargo, ese corte falla en la definición de convergencia con tolerancia 1: el término inicial tiene error 1. La elección $\delta=\varepsilon/2$ evita esta frontera para toda sucesión con las hipótesis indicadas.

La [figura de la frontera estricta](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f03) muestra por qué un punto en el borde no sirve con esa tolerancia. El margen auxiliar de esta prueba se obtiene por el argumento anterior, no de la muestra dibujada.

</details>

#### Ejercicio 14. Sumar valores con el mismo índice

[]{#MA-EX-ANM-01-007-014}

Sean $a,b:\mathbb N\to\mathbb R$ no decrecientes y acotadas superiormente. Escribe $s=\sup S_a$ y $t=\sup S_b$, y define $c_n=a_n+b_n$. Demuestra que $\sup S_c=s+t$, coordinando los testigos de aproximación de ambas sucesiones. Verifica las hipótesis de §7.3 para $c$ y deduce su límite.

Distingue $S_c=\{a_n+b_n:n\in\mathbb N\}$ del conjunto $T=\{x+y:x\in S_a,\ y\in S_b\}$. ¿Son necesariamente iguales? Justifica la inclusión que siempre vale y construye un ejemplo con las hipótesis indicadas en el que la inclusión sea estricta.

[]{#MA-SOL-ANM-01-007-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Las imágenes $S_a,S_b$ son conjuntos reales no vacíos y acotados superiormente; C03 garantiza los reales $s,t$. La fórmula $c_n=a_n+b_n$ define una sucesión real en todos los índices. Como $a_n\le s$ y $b_n\le t$, tenemos $c_n\le s+t$: la suma de los supremos es cota superior de $S_c$.

Sea $\varepsilon>0$. La aproximación a cada supremo, con tolerancia $\varepsilon/2$, proporciona índices $j$ y $k$ tales que $s-\varepsilon/2<a_j$ y $t-\varepsilon/2<b_k$. Tomamos $N=\max\{j,k\}$. Las dos direcciones no decrecientes permiten reunir los testigos: $a_j\le a_N$ y $b_k\le b_N$. Al sumar, $s+t-\varepsilon<a_N+b_N=c_N\le s+t$. Por la caracterización de §7.2, $\sup S_c=s+t$. Elegir un índice común es necesario porque $S_c$ contiene sumas de términos evaluados en la misma posición.

Además, $c_n=a_n+b_n\le a_{n+1}+b_{n+1}=c_{n+1}$ para todo $n$. La sucesión $c$ es no decreciente y tiene la cota superior real $s+t$. §7.3 garantiza que converge a su supremo, por tanto $c_n\to s+t$.

Siempre $S_c\subseteq T$: cada valor $a_n+b_n$ suma un elemento de $S_a$ y uno de $S_b$. La inclusión puede ser estricta. Tomemos $a_0=b_0=0$ y $a_n=b_n=1$ para $n\ge1$. Las dos funciones son no decrecientes y están acotadas superiormente por 1. Sus imágenes son $\{0,1\}$, de modo que $T=\{0,1,2\}$, mientras que $S_c=\{0,2\}$. El valor 1 combina alturas disponibles en posiciones distintas y nunca aparece como suma con el mismo índice. La igualdad de supremos demostrada no exige igualdad de esos conjuntos.

</details>

#### Ejercicio 15. Promedios finitos que conservan el destino

[]{#MA-EX-ANM-01-007-015}

Sea $a:\mathbb N\to\mathbb R$ no decreciente y acotada superiormente. Define $s=\sup S_a$ y la sucesión de promedios finitos $c_n=(a_0+\cdots+a_n)/(n+1)$. Prueba que está definida, que $a_0\le c_n\le a_n\le s$ y que no decrece. Obtén la existencia de su límite con §7.3 y demuestra que ese límite coincide con el de $a$.

Para identificarlo, compara los términos de un bloque final con un término $a_K$ previamente fijado y separa la contribución de los $K$ términos anteriores. Controla el error desde la definición ε–N, incluido el caso $K=0$. No invoques un teorema general sobre promedios de sucesiones convergentes ni teoría de series.

[]{#MA-SOL-ANM-01-007-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

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

Después de fijar $K$, el número $D=K(s-a_0)$ es un real no negativo fijo. Si $D=0$, tomamos $N=K$. Si $D>0$, la construcción del piso de C06 permite tomar $N=\max\{K,\lfloor2D/\varepsilon\rfloor+1\}$. En ambos casos $N\ge K$ y $N+1>2D/\varepsilon$. Para todo $n\ge N$ se cumple $D/(n+1)<\varepsilon/2$, y la elección de $K$ da $s-a_K<\varepsilon/2$. Luego $|c_n-s|=s-c_n<\varepsilon$. Esto demuestra directamente $c_n\to s$; la unicidad del límite de C06 identifica el límite ya obtenido como $t=s$.

Si $K=0$, el prefijo separado es vacío y su suma y contribución son cero. La estimación sigue válida: todos los términos están en el bloque final y $s-c_n\le s-a_0<\varepsilon/2$. La prueba controla un prefijo de longitud fija y el bloque restante; no emplea sumas infinitas ni un teorema general de promedios.

</details>

## 7.4. Cambiar la dirección y descartar un prefijo

[]{#MA-SEC-ANM-01-007-004}

Al cambiar el signo de cada término, una sucesión no creciente se vuelve no decreciente y una cota inferior se vuelve superior. Esa reflexión nos permite aprovechar el resultado anterior para la otra dirección.

Dada $a:\mathbb N\to\mathbb R$, definimos $b:\mathbb N\to\mathbb R$ por $b_n=-a_n$. Ambas funciones tienen el mismo dominio; el índice $n$ se conserva y el término cambia de signo. En general las funciones no son iguales. Sus conjuntos de valores se relacionan por $S_b=-S_a=\{-v:v\in S_a\}$: cada valor de una es el opuesto de un valor de la otra.

Si $a_{n+1}\le a_n$, multiplicar por −1 da $b_n=-a_n\le-a_{n+1}=b_{n+1}$. Si $\ell\le a_n$ para todo índice, entonces $b_n\le-\ell$. Quedan verificadas las dos hipótesis que necesita §7.3 para $b$. Todavía falta identificar qué significa para $a$ el supremo de esos valores reflejados.

> **Convergencia de una sucesión no creciente y acotada inferiormente.** Si $a:\mathbb N\to\mathbb R$ es no creciente y tiene una cota inferior real, entonces converge a $\inf S_a$.

**Demostración.** Sea $\ell_0\in\mathbb R$ una cota inferior de $a$ y definamos $b_n=-a_n$ en todo $\mathbb N$. Las comparaciones anteriores acreditan que $b$ es no decreciente y tiene cota superior $-\ell_0$. Por §7.3, existe $t=\sup S_b$ y $b_n\to t$.

Como $b_n\le t$, tenemos $-t\le a_n$ para todo índice, de modo que $-t$ es cota inferior de $S_a$. Para comprobar que es la mayor, sea $\ell$ cualquier cota inferior de $S_a$. De $\ell\le a_n$ se sigue $b_n\le-\ell$, así que $-\ell$ es cota superior de $S_b$. La minimalidad de $t$ da $t\le-\ell$, y cambiar el signo da $\ell\le-t$. Por tanto $-t$ es mayor o igual que toda cota inferior de $S_a$ y cumple $-t=\inf S_a$.

La regla del escalar de C06 §6.6, aplicada a $b_n\to t$ y al escalar −1, da $a_n=-b_n\to-t=\inf S_a$. También podemos verificar el transporte del error directamente: $|a_n-(-t)|=|-b_n+t|=|b_n-t|$, por lo que cualquier umbral de $b$ para una tolerancia sirve para $a$ con esa misma tolerancia. Quedan acreditados existencia, identificación extremal y convergencia en la dirección no creciente.

Hemos obtenido $\inf S_a=-\sup(-S_a)$. La reflexión cambia el signo de los valores y de las barreras, conserva los índices y no requiere que ninguno de esos extremos sea un término.

Consideremos $a_n=1+1/(n+1)$. La diferencia $a_{n+1}-a_n=-1/[(n+1)(n+2)]$ es negativa para todo $n$, y $a_n>1$. Así, $a$ es no creciente y tiene cota inferior 1. Además, C06 §6.3 proporciona para cualquier $\varepsilon>0$ un índice $j$ con $1/(j+1)<\varepsilon$, que da $a_j<1+\varepsilon$. La caracterización inferior de §7.2 acredita $\inf S_a=1$, sin mínimo porque ningún término vale 1. El resultado recién probado da $a_n\to1$.

La función reflejada tiene términos $b_n=-1-1/(n+1)$, es no decreciente y tiene supremo −1. Empieza en $b_0=-2$, mientras que $a_0=2$. Los pares $(n,a_n)$ y $(n,b_n)$ tienen la misma coordenada de índice y alturas opuestas; no hay desplazamiento horizontal. Las referencias inferior 1 y superior −1 se corresponden por signo. Una muestra de índices 0–5 permite leer esa relación, pero las comparaciones y la aproximación anteriores son las que la justifican para todos los índices.

![La reflexión cambia el signo de los valores y la dirección de monotonía; conserva cada índice y transporta el ínfimo al negativo del supremo.](../../assets/books/anm/C07/C07-F04.svg){#fig-anm-c07-f04 fig-alt="Dos conjuntos discretos de puntos a los mismos índices, uno descendente hacia 1 y otro ascendente hacia menos 1, reflejados respecto de la altura cero."}

Una sucesión puede mantener una dirección sólo después de algunos términos. Diremos que es **eventualmente no decreciente** si existe $T\in\mathbb N$ tal que $a_n\le a_{n+1}$ para todo $n\ge T$. Es **eventualmente no creciente** si desde algún índice vale la desigualdad opuesta. Es **eventualmente monótona** si cumple al menos una de esas propiedades. La dirección se fija para toda la cola; no se permite elegirla de nuevo en cada paso.

Para aplicar los resultados globales, debemos presentar esa cola como una sucesión con dominio natural. Fijado $T$, definimos $c:\mathbb N\to\mathbb R$ por $c_k=a_{T+k}$. La restricción de $a$ al conjunto $D_T=\{n\in\mathbb N:n\ge T\}$ tiene dominio $D_T$; la función $c$ tiene dominio $\mathbb N$. Si $T>0$, estos dominios son distintos. Ambas recorren el mismo conjunto de valores de cola,

$$
S_{a,T}=\{a_n:n\in\mathbb N,\ n\ge T\}=S_c.
$$

La igualdad de conjuntos se comprueba en los dos sentidos: $c_k=a_{T+k}$ es un valor de cola; si $n\ge T$, el natural $k=n-T$ satisface $c_k=a_n$. El conjunto es no vacío porque contiene $a_T=c_0$.

> **Convergencia de una cola monótona con cota pertinente.** Sean $a:\mathbb N\to\mathbb R$ y $T\in\mathbb N$. Si $a_n\le a_{n+1}$ para todo $n\ge T$ y existe $U\in\mathbb R$ con $a_n\le U$ para todo $n\ge T$, entonces $a_n\to\sup S_{a,T}$. Si $a_{n+1}\le a_n$ para todo $n\ge T$ y existe $\ell\in\mathbb R$ con $\ell\le a_n$ para todo $n\ge T$, entonces $a_n\to\inf S_{a,T}$.

**Demostración.** Definamos $c_k=a_{T+k}$ para todo $k\in\mathbb N$. En el primer caso, $T+k\ge T$ y por tanto $c_k=a_{T+k}\le a_{T+k+1}=c_{k+1}$. Si $U$ es la cota superior de la cola, también $c_k\le U$ para todo $k$. §7.3 da $c_k\to L=\sup S_c=\sup S_{a,T}$.

En el segundo caso, las hipótesis dan $c_{k+1}=a_{T+k+1}\le a_{T+k}=c_k$ para todo $k$, y la cota inferior de la cola también es cota inferior de $c$. El resultado no creciente demostrado en esta sección da $c_k\to L=\inf S_c=\inf S_{a,T}$.

En cualquiera de los dos casos, fijemos $\varepsilon>0$. La convergencia de $c$ proporciona un $K\in\mathbb N$ tal que $|c_k-L|<\varepsilon$ para todo $k\ge K$. Tomamos el umbral $N=T+K$ para $a$. Si $n\ge N$, entonces $k=n-T$ es natural y $k\ge K$, de modo que $|a_n-L|=|c_{n-T}-L|<\varepsilon$. Esto demuestra $a_n\to L$ desde la definición y coincide con la transferencia de cola de C06 §6.4.

El extremo corresponde al conjunto de valores de la cola $S_{a,T}$. El prefijo sigue perteneciendo a la sucesión original, pero queda fuera del corte $T+K$ que controla su error; por eso no tiene que compartir aquel extremo.

Si la monotonía empieza desde $T_m$ y la cota pertinente vale desde $T_c$, podemos reunir las hipótesis en $T=\max\{T_m,T_c\}$. Todo índice desde ese corte cumple ambas. Para un corte $T'$ mayor que uno ya admisible, el mismo resultado identifica el límite con el extremo de $S_{a,T'}$. Como C06 garantiza unicidad del límite de $a$, ambos extremos de cola son iguales. Esta afirmación se refiere a colas que cumplen las mismas hipótesis, no a cualquier conjunto obtenido eliminando valores sin atender a los índices.

Definamos $a_0=10$ y $a_n=1-1/n$ para $n\ge1$. Las cláusulas cubren todo $\mathbb N$ y evitan evaluar $1/n$ en cero. La sucesión no es no decreciente globalmente, porque baja de $a_0=10$ a $a_1=0$; tampoco es no creciente, porque $a_1=0<a_2=1/2$. Desde $T=1$, sin embargo, la cola no decrece.

Su reindexación es $c_k=a_{1+k}=1-1/(k+1)$, que coincide como función con $x$ de §§7.1–7.3. Esa función tiene supremo de valores 1 y converge a 1. Por el resultado eventual, $a_n\to1$. El supremo global es 10: es un término y domina los demás, que están entre 0 y 1. En cambio, $\sup S_{a,1}=1$, y 1 no pertenece a ese conjunto de cola. El límite de $a$ es el supremo de la cola monótona, no el supremo global 10.

| Objeto | Dominio | Valores iniciales | Supremo del conjunto de valores |
|---|---|---|---|
| $a$ | $\mathbb N$ | $10,0,1/2,2/3,\ldots$ | $10$ |
| Restricción de $a$ desde 1 | $D_1$ | En índices $1,2,3,\ldots$: $0,1/2,2/3,\ldots$ | $1$ |
| $c_k=a_{1+k}$ | $\mathbb N$ | En índices $0,1,2,\ldots$: $0,1/2,2/3,\ldots$ | $1$ |

Las dos últimas filas comparten conjunto de valores, pero sus funciones tienen dominios distintos. $a$ y $c$ comparten dominio natural, pero no son iguales: $a_0=10$ y $c_0=0$. Su igualdad de límites es una igualdad entre números reales.

En la [figura del prefijo y la cola](#fig-anm-c07-f05), la vista global conserva la altura $10$ y la ampliación declarada usa la escala $0$–$1$. Las filas de índices relacionan $n=1+k$ con las posiciones de la reindexación, sin unir los términos por una curva.

![El prefijo fija el máximo global 10; la cola monótona tiene supremo y límite 1. Restringir y reindexar conserva sus valores, pero cambia el dominio.](../../assets/books/anm/C07/C07-F05.svg){#fig-anm-c07-f05 fig-alt="Vista completa con el término inicial en 10 y ampliación explícita de los valores de cola entre cero y uno; dos filas de índices relacionan n con uno más k."}

Una cota global sigue siendo cota al restringirnos a una cola. La vuelta necesita incluir los valores del prefijo, aunque son sólo una cantidad finita. Si $U$ es cota superior desde $T$, el conjunto finito $\{U\}\cup\{a_n:n<T\}$ es no vacío y tiene máximo $M$. Para $n<T$, $a_n\le M$ porque el término pertenece a ese conjunto; para $n\ge T$, $a_n\le U\le M$. Así $M$ es cota superior global.

Para una cota inferior $\ell$ de cola, tomamos el mínimo $m$ del conjunto finito no vacío $\{\ell\}\cup\{a_n:n<T\}$. Si $n<T$, $m\le a_n$; si $n\ge T$, $m\le\ell\le a_n$. Por tanto $m$ es cota inferior global. Cuando $T=0$, el prefijo está vacío y los conjuntos siguen conteniendo $U$ o $\ell$, por lo que el argumento también cubre ese caso.

En este ejemplo, incorporar el término inicial obliga a elevar la cota superior de $1$ a $10$. Los máximos y mínimos finitos extienden cotas a toda la función, aunque el límite conserve el extremo de la cola admisible.

### Ejercicios de la sección 7.4

#### Ejercicio 16. Reflexión con una altura de referencia

[]{#MA-EX-ANM-01-007-016}

Sean $a:\mathbb N\to\mathbb R$ y $c\in\mathbb R$ fijo. Define $b_n=c-a_n$. Describe el dominio, codominio y conjunto de valores de $b$, y demuestra las equivalencias que transportan no decrecimiento a no crecimiento y viceversa. Transporta una cota inferior $\ell$ y una superior $U$ de $a$. Cuando los extremos correspondientes existan, prueba $\sup S_b=c-\inf S_a$ y $\inf S_b=c-\sup S_a$.

Si $a_n\to L$, identifica el límite de $b$ mediante una igualdad de errores. Describe qué cambia en los puntos de la gráfica y qué se conserva en sus coordenadas de índice. ¿Las funciones $a$ y $b$ son necesariamente iguales?

[]{#MA-SOL-ANM-01-007-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

$b$ es una función de $\mathbb N$ a $\mathbb R$, y su conjunto de valores es $S_b=\{c-x:x\in S_a\}$. Cada término $b_n$ tiene esa forma; recíprocamente, si $x=a_j$, entonces $c-x=b_j$. La transformación conserva el índice y cambia el término real.

Para cada $n$, $a_n\le a_{n+1}$ equivale a $c-a_{n+1}\le c-a_n$, es decir, a $b_{n+1}\le b_n$. Al exigirlo en todos los índices, el no decrecimiento de $a$ equivale al no crecimiento de $b$. Del mismo modo, $a_{n+1}\le a_n$ equivale a $b_n\le b_{n+1}$; el no crecimiento de $a$ equivale al no decrecimiento de $b$. Las implicaciones son reversibles porque $a_n=c-b_n$.

Una cota inferior $\ell\le a_n$ se transforma en la cota superior $b_n\le c-\ell$, y una cota superior $a_n\le U$ en la cota inferior $c-U\le b_n$. También estas correspondencias son equivalencias. Si $t=\inf S_a$, $c-t$ es cota superior de $S_b$. Sea $V$ cualquier otra cota superior de $S_b$. Entonces $c-V$ es cota inferior de $S_a$, por lo que $c-V\le t$ y $c-t\le V$. Así $\sup S_b=c-t$. Si $s=\sup S_a$, $c-s$ es cota inferior de $S_b$. Toda cota inferior $v$ de $S_b$ da una cota superior $c-v$ de $S_a$; de $s\le c-v$ resulta $v\le c-s$. Por ello $\inf S_b=c-s$. No se requiere que los extremos sean términos.

Si $a_n\to L$, la identidad $|b_n-(c-L)|=|-(a_n-L)|=|a_n-L|$ muestra que el mismo corte sirve para la misma tolerancia, y prueba $b_n\to c-L$. En las gráficas discretas, $(n,a_n)$ se convierte en $(n,c-a_n)$: la coordenada horizontal no cambia y la altura se refleja respecto de $c/2$. La igualdad $a=b$ no es necesaria; se cumple exactamente cuando $a_n=c/2$ para todo $n$, pues $a_n=c-a_n$ equivale a $2a_n=c$. Por ejemplo, las constantes $a_n=c/2+1$ y $b_n=c/2-1$ son distintas.

La [figura de la reflexión](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f04) representa el caso de altura de referencia cero. El transporte con la altura arbitraria de este ejercicio se justifica mediante las identidades anteriores.

</details>

#### Ejercicio 17. Un prefijo arbitrario y una barrera no alcanzada

[]{#MA-EX-ANM-01-007-017}

Fija $T\in\mathbb N$, $L\in\mathbb R$, $h>0$ y datos reales $x_0,\ldots,x_{T-1}$, entendiendo que no hay datos si $T=0$. Construye una sucesión $a:\mathbb N\to\mathbb R$ con ese prefijo y una cola cuyo término de posición reindexada $k$ esté a distancia $h/(k+1)$ por debajo de $L$.

Define la restricción a $D_T=\{n\in\mathbb N:n\ge T\}$ y la sucesión reindexada. Comprueba la dirección y el supremo de la cola, determina el límite de $a$ y calcula el supremo global. Si $T>0$, clasifica el alcanzamiento según el máximo del prefijo sea menor, igual o mayor que $L$. Trata también $T=0$, sin tomar el máximo de un conjunto vacío.

[]{#MA-SOL-ANM-01-007-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Definimos $a_n=x_n$ si $n<T$ y $a_n=L-h/(n-T+1)$ si $n\ge T$. Las cláusulas son disjuntas y cubren $\mathbb N$. En la segunda, $n-T$ es natural y el denominador es positivo. La restricción $a|_{D_T}$ tiene dominio $D_T$, mientras que la sucesión reindexada $v:\mathbb N\to\mathbb R$ tiene términos $v_k=a_{T+k}=L-h/(k+1)$. Sus conjuntos de valores son iguales: cada $v_k$ procede del índice $T+k$, y cada índice $n\ge T$ corresponde a $k=n-T$. Si $T=0$, los dominios también coinciden y $v=a$; si $T>0$, la restricción y $v$ tienen dominios distintos.

La diferencia $v_{k+1}-v_k=h/[(k+1)(k+2)]$ es positiva porque $h>0$. Además, $v_k<L$ para todo $k$. Para cada $\varepsilon>0$, la arquimedianidad permite elegir $k$ con $k+1>h/\varepsilon$, y entonces $L-\varepsilon<v_k<L$. Por §7.2, el supremo del conjunto de valores de la cola es $L$ y no se alcanza. El teorema eventual de §7.4 da $a_n\to L$. Explícitamente, un corte $K$ de $v$ se transfiere al corte $T+K$ de $a$.

Si $T>0$, el conjunto finito no vacío del prefijo tiene máximo $H=\max\{x_0,\ldots,x_{T-1}\}$. El número $G=\max\{H,L\}$ domina el prefijo y la cola, así que es cota superior global. Cualquier cota superior global $U$ domina el prefijo y por tanto $H\le U$; también domina la cola, por lo que su supremo cumple $L\le U$. Se sigue $G\le U$, y queda demostrado $\sup S_a=G$ por minimalidad.

Si $H<L$, el supremo global es $L$, pero ningún valor del prefijo ni de la cola lo alcanza; no hay máximo. Si $H=L$, el supremo es $L$ y se alcanza en los índices del prefijo cuyo valor es $H$; la cola no lo alcanza. Si $H>L$, el supremo es $H$ y también se alcanza en el prefijo, pues todos los términos de la cola son menores que $L<H$. En los dos últimos casos el supremo es máximo. Si $T=0$, no se define $H$: el conjunto global es el de la cola, tiene supremo $L$ y carece de máximo. El límite vale $L$ en todos los casos, aunque el prefijo pueda elevar el supremo global.

La [figura del prefijo y la cola](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f05) ilustra el caso T=1 con término inicial 10. La clasificación para el prefijo y el corte generales de este ejercicio procede de la prueba anterior.

</details>

#### Ejercicio 18. Incorporar el prefijo a los extremos

[]{#MA-EX-ANM-01-007-018}

Sea $a:\mathbb N\to\mathbb R$ y sea $T\in\mathbb N$. Supón que $Q=\{a_n:n\ge T\}$ está acotado por ambos lados y escribe $s=\sup Q$, $t=\inf Q$ y $P=\{a_n:n<T\}$. Prueba que

$$
\sup S_a=\max\bigl(\{s\}\cup P\bigr),
\qquad
\inf S_a=\min\bigl(\{t\}\cup P\bigr).
$$

Justifica que las expresiones están definidas y demuestra sus propiedades extremales, no sólo que proporcionan cotas. Explica el caso $T=0$ y por qué no hace falta que la cola sea monótona. Distingue los conjuntos $P,Q$ de sus extremos reales, que pueden no pertenecer a $Q$.

[]{#MA-SOL-ANM-01-007-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

El conjunto de valores de la cola $Q$ es no vacío porque contiene $a_T$. Al estar acotado por ambos lados, C03 garantiza sus extremos reales $s,t$. El conjunto $P$ es finito, posiblemente vacío. Por tanto, $\{s\}\cup P$ y $\{t\}\cup P$ son finitos y no vacíos, y tienen máximo y mínimo respectivamente. Denotemos esos números por $G$ y $g$.

Como $S_a=P\cup Q$, todo valor del prefijo es $\le G$ por la definición del máximo finito, y todo valor de la cola es $\le s\le G$. Así $G$ es cota superior de $S_a$. Si $U$ es cualquier cota superior global, domina $P$ y domina $Q$; de lo segundo se obtiene $s\le U$. Luego $U$ domina todos los elementos de $\{s\}\cup P$, así que $G\le U$. Queda probada la minimalidad de $G$ y, por tanto, $G=\sup S_a$.

En la dirección inferior, cada valor del prefijo es $\ge g$ y cada valor de la cola es $\ge t\ge g$. Por ello $g$ es cota inferior global. Si $\ell$ es otra cota inferior global, está por debajo de todos los valores de $P$ y es cota inferior de $Q$, de modo que $\ell\le t$. Entonces está por debajo de todos los elementos de $\{t\}\cup P$, incluido su mínimo $g$. Esto prueba $\ell\le g$ y la maximalidad de $g$ como cota inferior; así $g=\inf S_a$.

Si $T=0$, $P=\varnothing$ y los conjuntos finitos son los singletones $\{s\}$ y $\{t\}$: las fórmulas dan directamente $\sup S_a=s$ e $\inf S_a=t$. La monotonía no se ha usado; sólo se requieren extremos de la cola y finitud del prefijo. Los números $s,t$ se añaden a los conjuntos auxiliares para calcular sus extremos finitos, sin añadirlos al conjunto de valores $Q$. Pueden no pertenecer a la cola.

</details>

#### Ejercicio 19. Dos extensiones de la misma cola

[]{#MA-EX-ANM-01-007-019}

Sea $u:\mathbb N\to\mathbb R$ una sucesión monótona y acotada por ambos lados. Fija $T\in\mathbb N$ con $T\ge2$. Construye $a,b:\mathbb N\to\mathbb R$ tales que $a_{T+k}=b_{T+k}=u_k$ para todo $k\in\mathbb N$, con $a$ globalmente monótona y $b$ globalmente no monótona. La construcción debe servir también cuando $u$ sea constante.

Verifica todas las comparaciones de los prefijos y las fronteras necesarias, demuestra que ambas extensiones tienen el mismo límite e identifica ese límite según la dirección de $u$. Explica por qué un único término de prefijo no permitiría garantizar la construcción de $b$ para toda cola constante. Distingue igualdad de cola, igualdad de límite e igualdad de funciones.

[]{#MA-SOL-ANM-01-007-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Para $n<T$, ponemos $a_n=u_0$. Para la otra extensión, fijamos $b_0=u_0+1$ y $b_n=u_0-1$ en los índices $1\le n<T$. Desde $T$, definimos $a_n=b_n=u_{n-T}$. La condición $T\ge2$ permite las dos primeras posiciones del prefijo, y todas las cláusulas quedan dentro de sus dominios. Las funciones resultantes están definidas en todo $\mathbb N$.

En $a$, las comparaciones interiores al prefijo son igualdades; la frontera también lo es, pues $a_{T-1}=u_0=a_T$. Desde $T$, las comparaciones son las de $u$. Así $a$ conserva globalmente cualquier dirección de monotonía que satisfaga $u$. En $b$, la caída $b_0=u_0+1>b_1=u_0-1$ refuta el no decrecimiento. La subida en la frontera $b_{T-1}=u_0-1<b_T=u_0$ refuta el no crecimiento. Ambos infractores existen incluso si $u$ es constante; $b$ no es monótona.

Si $u$ es no decreciente, su cota superior permite aplicar §7.3 y obtener $u_k\to L=\sup S_u$. Si es no creciente, su cota inferior permite aplicar §7.4 y obtener $u_k\to L=\inf S_u$. Si cumple ambas direcciones, es constante y esos dos extremos coinciden con su valor. Dada una tolerancia, un corte $K$ para $u$ se transfiere a $N=T+K$ para ambas extensiones: para $n\ge N$, el índice $k=n-T$ satisface $k\ge K$ y $a_n=b_n=u_k$. Por ello $a_n\to L$ y $b_n\to L$.

Con un único término de prefijo y una cola constante $u_k=d$, cualquier extensión tiene la forma $x,d,d,\ldots$. Si $x\le d$, es no decreciente; si $x\ge d$, es no creciente. Nunca puede refutar ambas direcciones. Dos posiciones de prefijo permiten garantizar los dos infractores para toda cola admitida. En nuestra construcción, las extensiones tienen igual restricción al dominio $D_T$ e igual límite, pero son funciones distintas porque $a_0=u_0\ne u_0+1=b_0$.

</details>

#### Ejercicio 20. Mínimo y máximo de dos colas alineadas

[]{#MA-EX-ANM-01-007-020}

Sean $a,b:\mathbb N\to\mathbb R$ eventualmente no decrecientes y acotadas superiormente. Define $m_n=\min\{a_n,b_n\}$ y $M_n=\max\{a_n,b_n\}$. Demuestra que ambas sucesiones son eventualmente no decrecientes y tienen cota superior, y determina sus límites en términos de los límites de $a$ y $b$.

Reúne los cortes de monotonía, reindexa las dos colas desde un corte común y usa aproximaciones a sus supremos para identificar los supremos de los valores alineados de mínimo y máximo. Justifica la transferencia a las funciones originales. No uses continuidad de mínimo o máximo ni fórmulas de límites que se hayan supuesto antes de acreditar existencia.

[]{#MA-SOL-ANM-01-007-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Sean $T_a,T_b$ cortes de no decrecimiento y $U_a,U_b$ cotas superiores globales. Tomamos $T=\max\{T_a,T_b\}$ y definimos $x_k=a_{T+k}$, $y_k=b_{T+k}$ en $\mathbb N$. Ambas funciones no decrecen y tienen sus respectivas cotas superiores. Sus imágenes son los conjuntos de valores de las colas desde $T$. Por §7.3 existen $s=\sup S_x$, $t=\sup S_y$, con $x_k\to s$ e $y_k\to t$; la transferencia de §7.4 da $a_n\to s$ y $b_n\to t$.

Las funciones originales $m,M$ tienen dominio $\mathbb N$ y codominio $\mathbb R$, pues mínimo y máximo de dos reales están definidos. Sus reindexaciones son $p_k=m_{T+k}=\min\{x_k,y_k\}$ y $q_k=M_{T+k}=\max\{x_k,y_k\}$. Para cada $k$, $p_k\le x_k\le x_{k+1}$ y $p_k\le y_k\le y_{k+1}$, de modo que $p_k\le\min\{x_{k+1},y_{k+1}\}=p_{k+1}$. Asimismo, $q_{k+1}$ domina $x_{k+1}\ge x_k$ e $y_{k+1}\ge y_k$, y por tanto domina su máximo $q_k$. Así $p,q$ no decrecen, y $m,M$ son eventualmente no decrecientes desde $T$.

Como $x_k\le s$ y $y_k\le t$, se obtiene $p_k\le v=\min\{s,t\}$ y $q_k\le w=\max\{s,t\}$. Para identificar estos candidatos como supremos de las imágenes alineadas, sea $\varepsilon>0$. La aproximación a $s$ y $t$ proporciona índices $j,\ell$ con $x_j>s-\varepsilon$ e $y_\ell>t-\varepsilon$. Tomamos $K=\max\{j,\ell\}$; la monotonía implica $x_K>s-\varepsilon$ e $y_K>t-\varepsilon$. Ambos términos son mayores que $v-\varepsilon$, por lo que $p_K>v-\varepsilon$. Para el máximo, si $s\ge t$, $q_K\ge x_K>s-\varepsilon=w-\varepsilon$; si $t>s$, $q_K\ge y_K>t-\varepsilon=w-\varepsilon$. Las cotas y estas aproximaciones prueban $\sup S_p=v$ y $\sup S_q=w$ por §7.2.

Aplicando §7.3 a $p,q$ y transfiriendo sus cortes desde $T$, resulta $m_n\to\min\{s,t\}$ y $M_n\to\max\{s,t\}$. En términos de los límites originales, son respectivamente $\min\{\lim a_n,\lim b_n\}$ y $\max\{\lim a_n,\lim b_n\}$. Además, las funciones completas están acotadas superiormente: $m_n\le a_n\le U_a$ y $M_n\le\max\{U_a,U_b\}$ en todo índice. La prueba usa los extremos de colas comunes, no supone que coincidan con los extremos globales afectados por prefijos. No se ha utilizado continuidad de mínimo o máximo ni una fórmula de límites para acreditar su propia existencia.

</details>

## 7.5. Qué falla al retirar una hipótesis

[]{#MA-SEC-ANM-01-007-005}

Una sucesión no decreciente ya tiene cota inferior: $a_0\le a_n$ para todo índice. Eso deja abierta la posibilidad de subir más allá de cualquier barrera. Para garantizar un límite necesitamos la cota del otro lado.

En la dirección no creciente, $a_0$ proporciona automáticamente una cota superior y sigue haciendo falta una inferior. El lado de la cota que debemos buscar depende de la dirección.

La sucesión $a:\mathbb N\to\mathbb R$ dada por $a_n=n$ muestra la primera dificultad. Es estrictamente creciente y tiene cota inferior 0. Sin embargo, no tiene cota superior real: por la propiedad arquimediana, para cualquier $M\in\mathbb R$ existe un natural $N>M$, y entonces $a_N>M$. El término $a_N$ y el índice $N$ tienen aquí el mismo valor numérico; siguen desempeñando papeles diferentes en la función.

La falta de cota superior dice que cada barrera real es superada por algún término. Por sí sola, esa afirmación no exige que todos los términos posteriores la superen. La monotonía permite dar precisamente ese paso.

> **Escape por arriba.** Si $a:\mathbb N\to\mathbb R$ es no decreciente y no tiene cota superior, entonces para cada $M\in\mathbb R$ existe $N\in\mathbb N$ tal que $a_n>M$ para todo $n\ge N$.

**Demostración.** Fijemos una barrera $M\in\mathbb R$. Como no es cota superior, existe $N\in\mathbb N$ con $a_N>M$. Si $n\ge N$, la monotonía da $a_n\ge a_N>M$. Este mismo $N$ sirve para todos los índices posteriores. Hemos demostrado

$$
\forall M\in\mathbb R\ \exists N\in\mathbb N\ \forall n\in\mathbb N,
\qquad n\ge N\ \Longrightarrow\ a_n>M.
$$

El corte responde a la barrera $M$ y puede depender de ella. No podría funcionar uno solo para todas: tomando $M=a_N$, el propio índice $N$ incumpliría $a_N>M$. La monotonía es la que convierte superar una barrera una vez en superarla durante toda una cola.

Este escape excluye cualquier límite real. Para comprobarlo con todos los candidatos, fijemos $A\in\mathbb R$ y la tolerancia $\varepsilon_0=1$. Aplicando el escape a la barrera $M=A+1$, obtenemos un corte $T$ desde el cual $a_n>A+1$. Dado cualquier corte propuesto $K\in\mathbb N$, tomamos $n=\max\{K,T\}$. Entonces $n\ge K$ y $|a_n-A|>1$. Por tanto ningún corte hace que todos los errores posteriores sean menores que 1. Como el argumento vale para cada $A$, la sucesión no converge a ningún número real.

El escape describe términos reales frente a todas las barreras reales; no añade un número infinito al codominio. La prueba anterior excluye cada candidato mediante una tolerancia fija y un infractor después de cualquier corte.

> **Escape por abajo.** Si $a:\mathbb N\to\mathbb R$ es no creciente y no tiene cota inferior, entonces para cada $M\in\mathbb R$ existe $N\in\mathbb N$ tal que $a_n<M$ para todo $n\ge N$. Tampoco tiene límite real.

**Demostración.** Definamos $b_n=-a_n$ en todo $\mathbb N$. La dirección de $a$ hace que $b$ sea no decreciente. Si $b$ tuviera una cota superior $U$, tendríamos $a_n\ge-U$ para todo $n$, contradiciendo la ausencia de cota inferior. Así, $b$ no tiene cota superior. Aplicamos el escape por arriba a $b$ con la barrera $-M$: existe $N$ tal que $b_n>-M$ para todo $n\ge N$, lo que equivale a $a_n<M$.

Para excluir un candidato real $A$, usamos ahora la barrera $M=A-1$. Existe $T$ tal que $a_n<A-1$ para todo $n\ge T$. Con $\varepsilon_0=1$, cualquier corte $K$ admite el índice $n=\max\{K,T\}$, que cumple $n\ge K$ y $|a_n-A|>1$. Queda refutado cada candidato. La sucesión $a_n=-n$ realiza este caso: es no creciente, tiene cota superior 0 y carece de cota inferior real.

La otra hipótesis también hace trabajo. Para $d_n=(-1)^n$, todos los valores están en $[-1,1]$, pero $d_0>d_1$ y $d_1<d_2$ refutan las dos direcciones. Los mismos cambios reaparecen después de cualquier corte.

La acotación tampoco le proporciona un límite. Fijemos cualquier candidato $A\in\mathbb R$ y $\varepsilon_0=1$. Si $A\ge0$, para cualquier corte $K$ elegimos el índice impar $n=2K+1\ge K$. Entonces $d_n=-1$ y $|d_n-A|=1+A\ge1$. Si $A<0$, elegimos el índice par $n=2K\ge K$. Entonces $d_n=1$ y $|d_n-A|=1-A>1$. En ambos casos, ningún corte mantiene todos los errores estrictamente por debajo de 1. Esta prueba, coherente con la refutación de límites de C06, cubre todos los candidatos; las cotas sólo controlan el tamaño de los valores.

Para una sucesión monótona de valores reales podemos reunir los resultados en una equivalencia:

> Una sucesión monótona converge a un número real si y sólo si está acotada.

En la dirección de convergencia a acotación usamos el resultado ya demostrado en C06 §6.5, que vale para toda sucesión real convergente. En la dirección inversa, la acotación proporciona una cota superior si la sucesión es no decreciente, y §7.3 da la convergencia. Si es no creciente, proporciona una cota inferior y aplicamos §7.4. Una sucesión constante cumple ambas direcciones y converge a su valor constante. No se necesita monotonía estricta.

El alternante impide retirar la dirección de la implicación acotación–convergencia, mientras que $a_n=n$ impide retirar la cota de la afirmación para sucesiones monótonas. Bajo no decrecimiento basta la cota superior porque $a_0$ ya acota por abajo; bajo no crecimiento basta la inferior.

Retirar una hipótesis elimina la garantía del teorema; no obliga a que toda sucesión fuera de sus hipótesis diverja. Por ejemplo, $e_n=(-1)^n/(n+1)$ converge a 0, como se acreditó en C06 §6.3. No es siquiera eventualmente monótona: dado un corte $K$, el paso de $2K$ a $2K+1$ disminuye de un valor positivo a uno negativo, mientras que el paso de $2K+1$ a $2K+2$ aumenta de uno negativo a uno positivo. Ambas infracciones aparecen desde ese corte. Así, converger no implica monotonía, y las cotas no deciden por sí solas entre $d$ y $e$.

![La dirección sin cota y la acotación sin dirección no garantizan convergencia. El alternante amortiguado sí converge: faltar una hipótesis no obliga a divergir.](../../assets/books/anm/C07/C07-F06.svg){#fig-anm-c07-f06 fig-alt="Tres gráficas discretas: crecimiento que supera 4 desde 5, alternancia de amplitud uno fuera de una ventana pequeña y alternancia amortiguada dentro de esa ventana desde 2."}

La [figura de las hipótesis](#fig-anm-c07-f06) reúne tres gráficas discretas. Para $a_n=n$, la muestra supera $M=4$ desde $N=5$; la monotonía justifica que la desigualdad continúe fuera de ella. Para $d_n=(-1)^n$, la ventana de radio $1/2$ centrada en 0 excluye todos los valores, pero sólo examina ese candidato: la prueba anterior refuta los demás. Para $e_n=(-1)^n/(n+1)$, $|e_n|\le1/3<1/2$ desde $N=2$, mientras que $|e_1|=1/2$ queda en la frontera excluida. Las fórmulas justifican estas afirmaciones para todos los índices pertinentes. El contraste permite ver por qué faltar una hipótesis elimina la garantía sin obligar a divergir. Ninguno de los paneles asigna valores entre índices naturales.

### Ejercicios de la sección 7.5

#### Ejercicio 21. Superar una barrera y controlar una cola

[]{#MA-EX-ANM-01-007-021}

Para $a:\mathbb N\to\mathbb R$, escribe con todos sus dominios estas cuatro afirmaciones: no tiene cota superior, escapa eventualmente por arriba, no tiene cota inferior y escapa eventualmente por abajo. Obtén las negaciones de las dos afirmaciones de escape. Compara las obligaciones sobre índices en ausencia de cota y en escape, e indica qué propiedad de comparación permite pasar de una a otra en cada dirección.

Demuestra que escape implica ausencia de la cota correspondiente. ¿Puede el corte de escape depender de la barrera real? ¿Podría existir un único corte válido para todas las barreras? Explica por qué los cuantificadores deben incluir barreras de ambos signos.

[]{#MA-SOL-ANM-01-007-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

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

</details>

#### Ejercicio 22. Valores grandes con retornos arbitrariamente tardíos

[]{#MA-EX-ANM-01-007-022}

Fijado $r\in\mathbb R$, construye $a:\mathbb N\to\mathbb R$ sin cota superior que vuelva al valor $r$ después de cualquier corte. Da una definición completa por paridades y justifica ambas propiedades con sus cuantificadores. Refuta el escape eventual por arriba mediante una barrera real explícita y un índice infractor construido después de cada corte. ¿Qué paso de la prueba de escape monótono queda sin justificación en tu ejemplo? No uses resultados sobre subsucesiones.

[]{#MA-SOL-ANM-01-007-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Definimos $a_{2k}=r+k$ y $a_{2k+1}=r$ para todo $k\in\mathbb N$. Todo índice tiene una única paridad, así que la regla define una función de $\mathbb N$ a $\mathbb R$.

Sea $U\in\mathbb R$ cualquier candidato a cota superior. La arquimedianidad permite elegir $k\in\mathbb N$ con $k>U-r$. Entonces el índice $2k$ tiene término $a_{2k}=r+k>U$. Por tanto, $a$ carece de cota superior. Para cada corte $N\in\mathbb N$, el índice $n=2N+1\ge N$ cumple $a_n=r$, de modo que las visitas a $r$ ocurren después de cualquier corte.

Fijamos la barrera $M=r$. Ante cualquier $N$, ese mismo índice $n=2N+1$ satisface $a_n=r\le M$, y refuta el requisito $a_n>M$ de toda una cola. Ésta es la negación cuantificada del escape por arriba, aunque la sucesión no tenga cota superior.

La propagación monótona no está disponible: por ejemplo, $a_2=r+1>a_3=r$. En general, los pasos de $2k$ a $2k+1$ con $k\ge1$ vuelven de $r+k$ a $r$. Encontrar un término grande no obliga a los posteriores a permanecer por encima de la barrera. La refutación se construye directamente por índices, sin usar teoría de subsucesiones.

</details>

#### Ejercicio 23. Dos garantías de convergencia defectuosas

[]{#MA-EX-ANM-01-007-023}

Audita estas dos afirmaciones defectuosas:

1. «Si una sucesión real no decrece y tiene cota inferior, entonces converge a un real por el teorema monótono».
2. «Si todos los términos de una sucesión real están en un intervalo cerrado acotado, entonces converge a un real».

Refuta la primera con una familia de la forma $r+hn$, donde $r\in\mathbb R$ y $h>0$. Refuta la segunda mediante una sucesión periódica de tres valores distintos en $[r-h,r+h]$, excluyendo todos los candidatos reales a límite. Identifica la hipótesis ausente y formula una reparación suficiente para cada afirmación. Explica por qué la falta de una garantía no permite declarar divergente a toda sucesión que no sea eventualmente monótona; construye una familia convergente que lo demuestre y verifica su convergencia y sus infractores de dirección.

[]{#MA-SOL-ANM-01-007-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

La primera afirmación aporta una cota del lado equivocado. Para $u_n=r+hn$, con $h>0$, la diferencia adyacente es $h>0$ y todos los términos son $\ge r$. Sin embargo, ante cualquier barrera $M$, elegimos un natural $N>\max\{0,(M-r)/h\}$. Para todo $n\ge N$, $u_n\ge r+hN>M$. La familia escapa por arriba y, por §7.5, no tiene límite real. Una reparación suficiente consiste en exigir una cota superior además del no decrecimiento; §7.3 da entonces convergencia al supremo de los valores. La cota inferior ya está disponible en $u_0$ para toda sucesión no decreciente.

Para la segunda afirmación, definimos $v_{3k}=r-h$, $v_{3k+1}=r$ y $v_{3k+2}=r+h$. Las tres cláusulas cubren el dominio natural y todos los términos están en $[r-h,r+h]$. Los valores son distintos porque $h>0$. Fijemos un candidato $A\in\mathbb R$ y la tolerancia $h$. Si $A\ge r$, para cada corte $N$ el índice $n=3N$ tiene $|v_n-A|=A-r+h\ge h$. Si $A<r$, el índice $n=3N+2$ tiene $|v_n-A|=r+h-A>h$. Ambos índices están después del corte recibido, así que queda refutado todo candidato real. La acotación por sí sola no garantiza un límite. Una reparación suficiente es añadir monotonía global, o monotonía eventual usando §7.4 y las cotas del intervalo para la cola.

La falta de esa hipótesis de dirección no obliga a divergir. La familia $e_n=r+h(-1)^n/(n+2)$ está definida en todo $\mathbb N$ y converge a $r$: dada $\varepsilon>0$, elegimos un natural $N>h/\varepsilon$; para $n\ge N$, $|e_n-r|=h/(n+2)\le h/(N+2)<\varepsilon$. No es eventualmente monótona. Después de cualquier corte $T$, $e_{2T}>r>e_{2T+1}$ refuta el no decrecimiento, y $e_{2T+1}<r<e_{2T+2}$ refuta el no crecimiento. Los contraejemplos anteriores muestran que las premisas defectuosas no aseguran convergencia; no establecen que toda sucesión ajena a la garantía monótona carezca de límite.

La [figura de las hipótesis](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f06) contrapone dirección sin cota, acotación sin convergencia y convergencia sin monotonía eventual. La comparación recuerda qué garantía se pierde al retirar una hipótesis.

</details>

#### Ejercicio 24. Una tolerancia de refutación prescrita

[]{#MA-EX-ANM-01-007-024}

Fija de antemano $\varepsilon_0>0$. Supón que $a:\mathbb N\to\mathbb R$ escapa eventualmente por arriba. Para cada candidato $A\in\mathbb R$, usa la barrera $A+\varepsilon_0$ para construir, después de cualquier corte propuesto $K\in\mathbb N$, un índice $n\ge K$ con $|a_n-A|\ge\varepsilon_0$. Formula y demuestra la versión de escape por abajo con la barrera $A-\varepsilon_0$.

Registra el orden de los datos y elecciones, y concluye la ausencia de límite real en ambos casos. ¿La refutación exige error estrictamente mayor que la tolerancia o también admite igualdad? ¿Necesitas monotonía una vez que el escape ya está acreditado?

[]{#MA-SOL-ANM-01-007-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Fijada $\varepsilon_0>0$, recibamos un candidato $A\in\mathbb R$. El escape por arriba aplicado a $M=A+\varepsilon_0$ proporciona un corte $T$ tal que $a_n>A+\varepsilon_0$ para todo $n\ge T$. Ante cualquier corte propuesto $K\in\mathbb N$, tomamos $n=\max\{K,T\}$. Entonces $n\ge K$ y $|a_n-A|=a_n-A>\varepsilon_0$, lo que en particular cumple $|a_n-A|\ge\varepsilon_0$.

En escape por abajo usamos $M=A-\varepsilon_0$. Obtenemos $T$ con $a_n<A-\varepsilon_0$ para todo $n\ge T$ y, después de recibir $K$, elegimos de nuevo $n=\max\{K,T\}$. Se cumple $n\ge K$ y $|a_n-A|=A-a_n>\varepsilon_0$. En cualquiera de los dos casos hemos probado, para la tolerancia prescrita,

$$
\forall A\in\mathbb R\ \forall K\in\mathbb N\ \exists n\in\mathbb N:\quad n\ge K\ \text{y}\ |a_n-A|\ge\varepsilon_0.
$$

La tolerancia se fija al comienzo; el candidato determina la barrera y el corte de escape $T$ puede depender de ambos. El índice infractor se elige después del corte propuesto $K$, al reunirlo con $T$. La definición de convergencia exige error estrictamente menor que la tolerancia, de modo que un error igual a $\varepsilon_0$ también bastaría para refutarla. Aquí se obtiene una desigualdad mayor. El argumento excluye todos los candidatos reales y no requiere monotonía: usa sólo la propiedad de escape, cualquiera que haya sido el método para demostrarla.

</details>

#### Ejercicio 25. Escape y monotonía eventual no son conversas

[]{#MA-EX-ANM-01-007-025}

Para cada $c\in\mathbb R$, define $a^{(c)}_n=n+c(-1)^n$ en $\mathbb N$. Demuestra el escape eventual por arriba para todo parámetro y clasifica cuándo la sucesión es no decreciente o estrictamente creciente. Decide si puede ser no creciente, y si las clasificaciones cambian al exigir las propiedades sólo eventualmente.

Trata los valores frontera $c=1/2$ y $c=-1/2$, indicando dónde hay pasos de igualdad. Para los parámetros fuera del intervalo que admite no decrecimiento, construye después de cualquier corte infractores de ambas direcciones. Usa la familia para decidir si el escape eventual por arriba implica monotonía eventual, y distingue ese escape de la convergencia a un número real.

[]{#MA-SOL-ANM-01-007-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

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

</details>

## 7.6. Una recurrencia: existir antes de calcular

[]{#MA-SEC-ANM-01-007-006}

La sucesión $u_0=0$, $u_{n+1}=(u_n+1)/2$ ya tiene un límite real por §7.3. Llamémoslo $L_u$. La recurrencia puede ayudarnos a identificarlo porque sus dos miembros son sucesiones convergentes que coinciden término a término.

La recurrencia relaciona dos sucesiones: $n\mapsto u_n$ y $n\mapsto u_{n+1}$, ambas con dominio $\mathbb N$. Son funciones distintas, pues sus evaluaciones en 0 son 0 y $1/2$. Sin embargo, la regla de desplazamiento de C06 §6.4 da $u_{n+1}\to L_u$. El desplazamiento conserva el límite: si un corte $N$ controla el error de $u$, entonces $n\ge N$ implica $n+1\ge N$, por lo que ese corte también controla el error de la sucesión desplazada.

Por las reglas de suma y escalar de C06 §6.6, $(u_n+1)/2\to(L_u+1)/2$. Los dos lados de la recurrencia son iguales para cada índice y, por tanto, tienen el mismo límite. La unicidad demostrada en C06 permite escribir $L_u=(L_u+1)/2$. Multiplicar por 2 y restar $L_u$ da $L_u=1$.

La ecuación identifica el límite cuya existencia obtuvimos del teorema monótono. Por sí sola podría imponer una condición necesaria incluso a una sucesión que no convergiera.

Por ejemplo, la recurrencia $w_0=1$, $w_{n+1}=-w_n$ produce $w_n=(-1)^n$: la base coincide y cada paso cambia el signo. Si supusiéramos $w_n\to W$, el desplazamiento y la regla del escalar darían $W=-W$, luego $W=0$. La ecuación tiene una única solución real, pero §7.5 demostró que esta sucesión no converge. Sólo hemos obtenido una condición necesaria para un límite supuesto; no hemos demostrado que ese límite exista.

En una recurrencia con división aparece una dificultad anterior a cualquier cálculo de límites. Consideremos

$$
y_0=2,\qquad y_{n+1}=\frac{y_n+2/y_n}{2}\quad(n\in\mathbb N).
$$

Para evaluar el paso siguiente necesitamos $y_n\ne0$. La positividad resulta más útil: además de garantizar el inverso, se conserva porque tanto $y_n$ como $2/y_n$ son positivos. Una vez construidos todos los términos, una identidad cuadrática permitirá deducir el descenso y la cota que necesitamos.

La base $y_0=2$ es real y positiva. Si ya se ha construido $y_n>0$, su inverso existe en $\mathbb R$; además, $2/y_n>0$. La suma $y_n+2/y_n$ y su mitad son positivas, de modo que la fórmula define un único real $y_{n+1}>0$. La construcción recursiva elemental, con esta inducción, produce un término positivo para cada $n\in\mathbb N$. Ninguna división se ejecuta sobre un término cuya no anulación esté pendiente.

Con dato inicial $y_0=0$ no podríamos evaluar siquiera $y_1$. El dato $2$ proporciona una base positiva desde la que la inducción permite continuar indefinidamente.

El primer término nuevo es $y_1=3/2$, cuyo cuadrado todavía supera $2$. Para saber si esa desigualdad puede mantenerse, calculemos su error cuadrático usando la regla de iteración, ya legítima porque $y_n>0$:

$$
y_{n+1}^2-2
=\frac{y_n^2+4+4/y_n^2}{4}-2
=\frac{y_n^4-4y_n^2+4}{4y_n^2}
=\frac{(y_n^2-2)^2}{4y_n^2}.
$$

El denominador es positivo. Si $y_n^2>2$, también el numerador es positivo, porque se está elevando al cuadrado un número estrictamente positivo. En la base, $y_0^2=4>2$; la identidad demuestra por inducción que $y_n^2>2$ para todos los índices. Hemos conservado una desigualdad estricta, no sólo $y_n^2\ge2$.

De $y_n>0$ y $y_n^2>2$ se deduce $y_n>1$: si $0<y_n\le1$, tendríamos $y_n^2\le1<2$, contradicción. En particular, $1$ es una cota inferior conocida sin haber construido todavía una raíz ni demostrado la existencia del límite.

Para determinar la dirección, restamos $y_n$ de la fórmula de iteración:

$$
y_{n+1}-y_n
=\frac{2/y_n-y_n}{2}
=\frac{2-y_n^2}{2y_n}<0.
$$

El signo usa dos hechos ya probados: $2-y_n^2<0$ y $2y_n>0$. Así, $y$ es estrictamente decreciente y, en particular, no creciente. Comparando con el primer término obtenemos $y_n\le y_0=2$. Quedan reunidas las barreras $1\le y_n\le2$ y la dirección necesaria para aplicar §7.4.

Los primeros valores, calculados con fracciones exactas, son

| Índice $n$ | Término $y_n$ |
|---|---|
| 0 | $2$ |
| 1 | $3/2$ |
| 2 | $17/12$ |
| 3 | $577/408$ |

![Positividad e invariante cuadrático justifican cada paso, el descenso y la barrera 1. Esas hipótesis permiten probar existencia antes de calcular un límite.](../../assets/books/anm/C07/C07-F07.svg){#fig-anm-c07-f07 fig-alt="Cuatro puntos de una sucesión descendente entre las alturas 1 y 2, con valores exactos identificados aparte y una secuencia de obligaciones desde positividad hasta existencia."}

La [figura del invariante](#fig-anm-c07-f07) usa sólo las barreras conocidas $1$ y $2$. Los cuatro puntos sitúan los valores de la tabla; el descenso en todos los índices procede de la identidad y del invariante demostrado.

El teorema de §7.4 se aplica a la sucesión real $y$: es no creciente y tiene cota inferior 1. Por tanto existe $L\in\mathbb R$ tal que $y_n\to L$, y $L=\inf S_y$, donde $S_y=\{y_n:n\in\mathbb N\}$. La existencia de ese ínfimo recibe la completitud utilizada al demostrar el teorema. No se deduce de la apariencia de los primeros términos.

El orden de límites de C06 §6.7, aplicado a $1\le y_n\le2$, da $1\le L\le2$. En particular, $L>0$. Este margen es necesario antes de calcular con $2/L$: que ningún término sea cero no bastaría para asegurar un límite distinto de cero. Por ejemplo, todos los términos de $1/(n+1)$ son positivos y su límite es 0.

Tenemos ya los datos para el cociente de C06 §6.6: la sucesión constante de valor 2 converge a 2; el denominador $y_n$ converge a $L\ne0$ y no se anula en ningún índice. Así, $2/y_n\to2/L$. Las reglas de suma y escalar dan $(y_n+2/y_n)/2\to(L+2/L)/2$. A su vez, el desplazamiento de C06 §6.4 da $y_{n+1}\to L$. Como ambos lados de la recurrencia son iguales en cada índice, la unicidad del límite produce

$$
L=\frac{L+2/L}{2}.
$$

Multiplicando por 2 obtenemos $2L=L+2/L$, de donde $L=2/L$. Multiplicar por el real no nulo $L$ da $L^2=2$. La existencia del límite y el margen positivo estaban acreditados antes de estas operaciones.

Podemos identificar $L$ como la raíz positiva de 2. Para justificar que esa descripción determina un único número, sea $r>0$ otro real con $r^2=2$. Entonces $(L-r)(L+r)=L^2-r^2=0$. Como $L+r>0$, el segundo factor no se anula y resulta $L=r$. El símbolo $\sqrt2$ designa ese único real positivo; hemos demostrado $y_n\to\sqrt2$ mediante esta construcción.

También podemos precisar la posición de todos los términos respecto del límite. Puesto que $y_n^2>2=L^2$, tenemos $(y_n-L)(y_n+L)>0$. El factor $y_n+L$ es positivo, por lo que $y_n-L>0$. Así, $y_n>L$ para cada índice: la sucesión se aproxima por arriba y ningún término alcanza su límite.

La ecuación del límite se pudo usar porque el teorema monótono acreditó existencia y la cota $1$ aseguró que el denominador límite no fuera cero. Cada operación se justificó mediante reglas de sucesiones de C06, sin apelar a continuidad de la función de iteración.

### Ejercicios de la sección 7.6

#### Ejercicio 26. Una combinación que conserva el lado de una barrera

[]{#MA-EX-ANM-01-007-026}

Sean $c,r\in\mathbb R$ y $0<\lambda<1$. Define $v:\mathbb N\to\mathbb R$ por $v_0=r$ y $v_{n+1}=\lambda v_n+(1-\lambda)c$. Estudia por separado $r<c$, $r>c$ y $r=c$: buena definición, posición respecto de $c$, dirección, cotas y existencia de límite. Identifica después ese límite usando la recurrencia. No necesitas obtener una fórmula geométrica para $v_n$.

[]{#MA-SOL-ANM-01-007-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

La regla afín produce un único real en cada paso, sin denominadores variables. Las dos identidades útiles son

$$
v_{n+1}-c=\lambda(v_n-c),\qquad v_{n+1}-v_n=(1-\lambda)(c-v_n).
$$

Si $r<c$, la primera identidad conserva $v_n<c$ por inducción porque $\lambda>0$. La segunda da incremento positivo porque $1-\lambda>0$. Por tanto $r\le v_n<c$ y §7.3 garantiza un límite real. Si $r>c$, se conserva $v_n>c$, el incremento es negativo y $c<v_n\le r$; §7.4 garantiza un límite. Si $r=c$, la inducción da $v_n=c$ para todo $n$, con límite $c$.

En los dos casos no constantes ya existe $L\in\mathbb R$. Desplazamiento, suma y multiplicación por escalares de C06 dan $L=\lambda L+(1-\lambda)c$. Como $1-\lambda\ne0$, resulta $L=c$. Así, las tres sucesiones convergen a $c$; los casos estrictos no alcanzan ese valor en ningún índice. La completitud interviene mediante el teorema monótono, antes de resolver la ecuación.

</details>

#### Ejercicio 27. Una ecuación necesaria presentada como garantía

[]{#MA-EX-ANM-01-007-027}

Sean $c\in\mathbb R$ y $h>0$. Se prescribe $a_0=c+h$ y $a_{n+1}=2c-a_n$. Audita el razonamiento: «La ecuación del límite es $A=2c-A$; tiene la única solución $A=c$, de modo que $a_n\to c$». Localiza la obligación omitida, determina todos los términos y refuta la convergencia a cualquier real mediante una tolerancia explícita y un índice posterior a cualquier corte. ¿Qué cambiaría con dato inicial $a_0=c$?

[]{#MA-SOL-ANM-01-007-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

La regla define una sucesión real en todos los índices. La inducción da

$$
a_{2k}=c+h,\qquad a_{2k+1}=c-h\quad(k\in\mathbb N).
$$

En efecto, el paso transforma $c+h$ en $c-h$ y viceversa. El razonamiento sólo obtiene una condición necesaria bajo la hipótesis $a_n\to A$. Desplazamiento y operaciones de C06 permitirían entonces $A=2c-A$, luego $A=c$. Falta demostrar que tal límite existe; la unicidad de la solución de una ecuación no suple esa obligación.

Para cualquier candidato $A\in\mathbb R$, fija $\varepsilon_0=h$. Dado cualquier $N\in\mathbb N$, si $A\le c$ elige $n=2N$, para el que $|a_n-A|=c+h-A\ge h$. Si $A>c$, elige $n=2N+1$ y obtiene $|a_n-A|=A-c+h>h$. En ambos casos $n\ge N$ y falla el error estrictamente menor que $\varepsilon_0$. No hay límite real. Con $a_0=c$, la inducción produce la sucesión constante de valor $c$, y la existencia sí queda acreditada.

</details>

#### Ejercicio 28. Descenso desde un dato inicial variable

[]{#MA-EX-ANM-01-007-028}

Sea $r\in\mathbb R$ con $r>0$ y $r^2>2$. Para $y_0=r$ y $y_{n+1}=(y_n+2/y_n)/2$, demuestra que la prescripción define $y:\mathbb N\to\mathbb R$. Reconstruye la conservación estricta de $y_n^2>2$, una cota inferior positiva conocida y el descenso. Demuestra la existencia de límite antes de calcularlo, identifica su destino y decide si algún término puede alcanzarlo. No deduzcas propiedades universales de una tabla de valores.

[]{#MA-SOL-ANM-01-007-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Si $y_n>0$, el inverso existe y la regla produce un único $y_{n+1}>0$. La base $r>0$ permite esta inducción para todos los índices. Para cada término construido,

$$
y_{n+1}^2-2=\frac{(y_n^2-2)^2}{4y_n^2},\qquad
y_{n+1}-y_n=\frac{2-y_n^2}{2y_n}.
$$

La base $r^2>2$, la primera identidad y el denominador positivo conservan $y_n^2>2$ estrictamente: el numerador nunca es cero. Como $y_n>0$, se deduce $y_n>1$, pues $0<y_n\le1$ implicaría $y_n^2\le1$. La segunda identidad tiene numerador negativo y denominador positivo, luego $y$ es estrictamente decreciente y $1<y_n\le r$.

§7.4, que recibe aquí la completitud real, da $y_n\to L$. El orden de límites de C06 da $L\ge1$, de modo que $L\ne0$. Ahora están verificadas las hipótesis del cociente: los denominadores son no nulos y su límite también. Por desplazamiento y operaciones de límites,

$$
L=\frac{L+2/L}{2},\qquad L^2=2,\qquad L>0.
$$

El único real positivo con ese cuadrado es $R=\sqrt2$, construido en §7.6: si $q>0$ y $q^2=2$, $(L-q)(L+q)=0$ y $L+q>0$ fuerzan $L=q$. Finalmente $(y_n-L)(y_n+L)=y_n^2-2>0$, con segundo factor positivo, da $y_n>L$ para todo $n$. Ningún término alcanza el límite.

La [figura del invariante](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f07) ilustra el dato inicial 2. Para el dato variable de este ejercicio, positividad, invariante y dirección se acreditan con la prueba anterior.

</details>

#### Ejercicio 29. Cruzar la barrera en el primer paso

[]{#MA-EX-ANM-01-007-029}

Mantén la recurrencia del ejercicio 28 y toma ahora $r>0$. Resuelve los casos $r^2<2$ y $r^2=2$. En el primer caso, sitúa el primer término respecto de $r$ y de la raíz positiva de 2, determina la dirección desde el índice 1 y justifica la existencia y el destino del límite. Decide si la sucesión completa es monótona. En el segundo caso, prueba que la sucesión es constante. Reúne estos casos con el ejercicio 28 para clasificar todos los datos iniciales positivos.

[]{#MA-SOL-ANM-01-007-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Todos los términos se construyen positivos como en 28. Sea $R>0$ la raíz de 2 construida en §7.6. Si $r^2<2$, la positividad da $r<R$. Además,

$$
y_1-r=\frac{2-r^2}{2r}>0,\qquad
y_1^2-2=\frac{(r^2-2)^2}{4r^2}>0.
$$

Por tanto $y_1>R$ y $y_1>r$. Desde el índice 1, el argumento de 28 conserva cuadrado mayor que 2, descenso estricto y cota inferior 1. La sucesión $b_k=y_{k+1}$, con dominio $\mathbb N$, cumple exactamente las hipótesis de 28; converge a $R$. La transferencia de una cola de C06 da $y_n\to R$. La sucesión completa no es no creciente porque $y_1>y_0$, ni no decreciente porque $y_2<y_1$: sólo la cola desde 1 es decreciente.

Si $r^2=2$, entonces $2/r=r$ y la regla conserva $y_n=r=R$ por inducción. La sucesión es constante.

La clasificación positiva queda completa: $r>R$ produce descenso estricto global por encima de $R$; $0<r<R$ produce una subida inicial que cruza $R$ y después descenso estricto por encima de $R$; $r=R$ produce constancia. En todos los casos el límite es $R$.

</details>

#### Ejercicio 30. Construir la raíz de un parámetro positivo

[]{#MA-EX-ANM-01-007-030}

Sean $\rho>0$ y $r>0$ reales con $r^2>\rho$. Define $x_0=r$ y $x_{n+1}=(x_n+\rho/x_n)/2$. Construye la sucesión, conserva una desigualdad cuadrática estricta y deduce descenso. Justifica la cota inferior $m=\min\{1,\rho\}>0$ sin presuponer una raíz de $\rho$. Obtén existencia de límite, comprueba su no anulación antes de usar cocientes y demuestra que es el único real positivo cuyo cuadrado es $\rho$. Sitúa cada término respecto de ese límite.

[]{#MA-SOL-ANM-01-007-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

La base $x_0=r>0$ y la positividad de $\rho/x_n$ cuando $x_n>0$ construyen todos los términos positivos. Las identidades algebraicas son

$$
x_{n+1}^2-\rho=\frac{(x_n^2-\rho)^2}{4x_n^2},\qquad
x_{n+1}-x_n=\frac{\rho-x_n^2}{2x_n}.
$$

Por inducción desde $r^2>\rho$, la primera conserva la desigualdad estricta; la segunda implica descenso estricto. Para una barrera independiente de una raíz, fija $m=\min\{1,\rho\}$. Si $\rho\ge1$, $0<x_n\le1$ implicaría $x_n^2\le1\le\rho$, imposible. Si $0<\rho<1$, $0<x_n\le\rho$ implicaría $x_n^2\le\rho^2<\rho$, también imposible. Así $0<m<x_n\le r$.

§7.4 aplica monotonía, cota y completitud para dar un límite $L$. Por orden de límites, $L\ge m>0$. Sólo ahora pueden usarse el cociente, suma, escalar y desplazamiento de C06 para obtener

$$
L=\frac{L+\rho/L}{2},\qquad L^2=\rho.
$$

La construcción ha demostrado la existencia de un real positivo con ese cuadrado. Si $q>0$ también satisface $q^2=\rho$, entonces $(L-q)(L+q)=0$ y $L+q>0$ dan $q=L$: es único. Finalmente $(x_n-L)(x_n+L)=x_n^2-\rho>0$ da $x_n>L$. La barrera $m$ acreditó la no anulación del límite; la sola positividad de los términos no habría bastado.

</details>

#### Ejercicio 31. Datos negativos y una prescripción que no define sucesión

[]{#MA-EX-ANM-01-007-031}

Para la prescripción $y_0=r$, $y_{n+1}=(y_n+2/y_n)/2$, considera todos los datos reales $r<0$ y el dato $r=0$. En el caso negativo, construye una sucesión positiva auxiliar por reflexión y clasifica posición, dirección y límite según $r^2>2$, $r^2<2$ y $r^2=2$. Distingue dirección global de dirección desde el índice 1. En el caso cero, identifica el primer paso que falla y explica por qué no corresponde llamar divergente a una sucesión definida por esta prescripción.

[]{#MA-SOL-ANM-01-007-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Para $r<0$, pon $z_0=-r>0$ y construye la sucesión positiva $z$ por la regla de 28–29. Define $y_n=-z_n$. Es una sucesión $\mathbb N\to\mathbb R$ de términos negativos, ninguno cero, y

$$
\frac{y_n+2/y_n}{2}=-\frac{z_n+2/z_n}{2}=-z_{n+1}=y_{n+1}.
$$

Así cumple la prescripción original; en cada paso la regla determina un único real. La reflexión invierte las desigualdades y el límite es $-R$, donde $R=\sqrt2$.

Si $r^2>2$, 28 da $z_n>R$ y descenso estricto global. Por reflexión, $y_n<-R$ y $y$ crece estrictamente hacia $-R$ en todos los índices.

Si $r^2<2$, tenemos $r>-R$. Por 29, $z_1>z_0$ y $z_1>R$, luego $y_1<y_0$ y $y_1<-R$. Desde el índice 1, $y$ crece estrictamente, siempre por debajo de $-R$. No es monótona globalmente: tiene una bajada inicial y después subidas estrictas. La regla del escalar de C06 o la transferencia de la cola justifican su límite $-R$.

Si $r^2=2$, el dato negativo es $r=-R$ y la sucesión es constante por reflexión del caso positivo constante.

Con $r=0$, el cálculo de $y_1$ exige $2/0$, que no es un real definido. La prescripción no produce una función $\mathbb N\to\mathbb R$. La divergencia es una propiedad de una sucesión que sí está definida; aquí falta el objeto al que se atribuiría esa propiedad.

</details>

#### Ejercicio 32. Dos trayectorias ordenadas con un destino común

[]{#MA-EX-ANM-01-007-032}

Sea $R>0$ la raíz de 2 ya construida en §7.6, y sean $R<r<s$. Define dos sucesiones $y,z:\mathbb N\to\mathbb R$ con datos iniciales $y_0=r$, $z_0=s$ y la regla del ejercicio 28. Para la función de paso $F:(0,\infty)\to(0,\infty)$, $F(t)=(t+2/t)/2$, deriva

$$
F(x)-F(t)=\frac{x-t}{2}\left(1-\frac{2}{xt}\right).
$$

Determina el signo relevante cuando $x,t>R$ y demuestra que $y_n<z_n$ para todo índice. Justifica que ambas sucesiones tienen el mismo límite y, sin embargo, son funciones distintas. ¿Qué ocurre si $r=s$? No estimes velocidades de aproximación.

[]{#MA-SOL-ANM-01-007-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

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

</details>

## 7.7. La misma construcción sobre los racionales

[]{#MA-SEC-ANM-01-007-007}

Los términos $2$, $3/2$, $17/12$ y $577/408$ sugieren que esta construcción puede ejecutarse dentro de $\mathbb Q$: suma, producto e inverso no nulo conservan racionalidad. Sin embargo, que todos los términos sean racionales deja pendiente si el destino real también lo será.

Para examinarlo, llamaremos $y$ a la construcción racional y $\widetilde y$ a su composición con la inclusión:

$$
y:\mathbb N\to\mathbb Q,\qquad
\iota:\mathbb Q\to\mathbb R,\qquad
\widetilde y=\iota\circ y:\mathbb N\to\mathbb R.
$$

La aplicación $\iota$ es la inclusión canónica de los racionales en los reales. Conserva suma, producto, inversos de números no nulos y orden. Por eso podemos identificar un racional con su imagen al escribir números en la recta real; esa identificación de valores no identifica funciones con codominios distintos. En comparaciones de un término racional $y_n$ con un número real, su valor se interpreta mediante $\iota(y_n)=\widetilde y_n$. Mantendremos la tilde en los argumentos de límites para dejar visible esa interpretación.

Definimos en $\mathbb Q$ la misma recurrencia: $y_0=2$ y $y_{n+1}=(y_n+2/y_n)/2$. La base es un racional positivo. Si $y_n$ es racional positivo, su inverso es racional, $2/y_n$ es racional positivo y la suma y la mitad siguen siendo racionales positivas. El paso define, por tanto, un único $y_{n+1}\in\mathbb Q$ con $y_{n+1}>0$. Por inducción, la construcción produce una sucesión racional positiva en todo $\mathbb N$, sin denominadores nulos.

La inclusión transporta cada paso: $\widetilde y_0=2$ y, como conserva las operaciones,

$$
\widetilde y_{n+1}
=\iota\left(\frac{y_n+2/y_n}{2}\right)
=\frac{\widetilde y_n+2/\widetilde y_n}{2}.
$$

Así, $\widetilde y$ es exactamente la sucesión real de §7.6. La igualdad puede comprobarse por inducción: coinciden en el índice 0; si coinciden en $n$, la misma operación, ya definida, produce iguales términos en $n+1$. Esta coincidencia de las dos funciones reales permite reutilizar todos los resultados de aquella sección.

En particular, $\widetilde y_n^2>2$, $1\le\widetilde y_n\le2$ y $\widetilde y_{n+1}<\widetilde y_n$ para todo índice. Como la inclusión preserva y refleja el orden, la sucesión racional $y$ también es estrictamente decreciente y tiene las cotas racionales 1 y 2. Los índices no cambian: componer con la inclusión cambia el codominio de la sucesión y conserva las evaluaciones correspondientes, sin reindexarla.

Aplicado en $\mathbb R$, el teorema de §7.4 ya dio un límite $L=\inf S_{\widetilde y}$; §7.6 acreditó $L>0$, $L^2=2$ y $\widetilde y_n>L$ para todo $n$. Cada término de $\widetilde y$ pertenece a la imagen de $\mathbb Q$. Falta decidir si $L$ pertenece a ella.

Para decidir la pertenencia de $L$ a la imagen racional usamos que todo racional admite una fracción reducida $p/q$, con $p\in\mathbb Z$, $q\in\mathbb Z$, $q>0$ y sin divisor común mayor que $1$. Se obtiene cancelando el máximo común divisor. La propiedad de paridad necesaria para excluir esa representación se comprueba en el propio argumento.

**El límite $L$ no es racional.** Supongamos, para obtener una contradicción, que $L$ es la imagen de una fracción reducida $p/q$. De $L^2=2$, multiplicando por $q^2\ne0$, se sigue

$$
p^2=2q^2.
$$

Por tanto $p^2$ es par. Si un entero es impar, puede escribirse como $2k+1$, con $k\in\mathbb Z$, y su cuadrado es

$$
(2k+1)^2=4k^2+4k+1=2(2k^2+2k)+1,
$$

que es impar. En consecuencia, un cuadrado par sólo puede proceder de un entero par. Aplicando esta observación a $p$, escribimos $p=2h$ para algún $h\in\mathbb Z$. La igualdad anterior se convierte en $4h^2=2q^2$, luego $q^2=2h^2$. El cuadrado de $q$ también es par, y la misma observación obliga a que $q$ sea par.

Hemos obtenido que 2 divide tanto $p$ como $q$, contradiciendo que la fracción estuviera reducida. Así, $L$ no pertenece a la imagen de $\mathbb Q$ en $\mathbb R$. Bajo la identificación usual $\mathbb Q\subset\mathbb R$, esto se escribe $L\in\mathbb R\setminus\mathbb Q$. La irracionalidad procede de la ecuación y la paridad; no de inspeccionar términos ni de contar cifras decimales.

Para pedir que $y$ tenga límite en $\mathbb Q$, el candidato debe ser un racional $r$. La distancia es la misma que usamos al incluir los valores en la recta real. Con tolerancias reales positivas, la condición sería

$$
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\ge N,
\qquad |\iota(y_n)-\iota(r)|<\varepsilon.
$$

Como $\iota(y_n)=\widetilde y_n$, esta condición dice precisamente que la sucesión real $\widetilde y$ converge a $\iota(r)$. Pero ya converge a $L$. Por unicidad del límite real, tendríamos $\iota(r)=L$, en contradicción con la irracionalidad probada. Por tanto $y$ no tiene límite racional, aunque $\widetilde y$ sí tenga límite real.

También podemos ver dónde falla la captura de una cola alrededor de cualquier candidato racional. Fijado $r\in\mathbb Q$, la distancia $d=|L-\iota(r)|$ es positiva. La convergencia a $L$ proporciona un corte $T$ tal que $|\widetilde y_n-L|<d/2$ para todo $n\ge T$. Por la desigualdad triangular,

$$
d\le |L-\widetilde y_n|+|\widetilde y_n-\iota(r)|,
$$

de modo que $|\widetilde y_n-\iota(r)|>d/2$ desde ese corte. Con la tolerancia fija $\varepsilon_0=d/2$, cualquier corte propuesto $K$ admite el índice $n=\max\{K,T\}$, cuyo error supera $\varepsilon_0$. Cada candidato racional queda excluido. La tolerancia puede depender de $r$, mientras que el índice que refuta un corte se elige después de conocerlo.

Los índices y los valores correspondientes se conservan al componer con la inclusión, pero se amplía el conjunto de candidatos. La completitud real proporcionó el destino $L$; la contradicción de paridad muestra por qué no está disponible en $\mathbb Q$.

![La inclusión conserva índices y valores; el límite real positivo cuyo cuadrado es 2 queda fuera del codominio racional de la sucesión original.](../../assets/books/anm/C07/C07-F08.svg){#fig-anm-c07-f08 fig-alt="Un esquema de dominios y codominios acompaña puntos reales que descienden hacia un límite irracional sin alcanzarlo; una ampliación declarada permite distinguir los últimos valores."}

La [figura de la inclusión racional–real](#fig-anm-c07-f08) muestra la vista global y una ampliación declarada entre $L$ y $3/2$, donde pueden distinguirse $17/12$ y $577/408$. La referencia $L$, caracterizada por $L>0$ y $L^2=2$, se distingue de los puntos que representan términos. La ampliación conserva los valores; la desigualdad $\widetilde y_n>L$ y la irracionalidad proceden de las pruebas.

En $\mathbb Q$ se construyen todos los términos, se conservan la positividad y la desigualdad cuadrática, y se prueban descenso y cotas. El teorema monótono se aplica después en $\mathbb R$: la completitud garantiza allí el ínfimo del conjunto de valores y la monotonía permite convertirlo en límite.

Las reglas de C06 identifican ese límite existente y la paridad excluye que sea racional. Por tanto, una sucesión racional monótona y acotada puede carecer de límite racional, aunque su composición real converja.

El ejemplo localiza el uso de completitud en una construcción concreta; no demuestra una equivalencia general entre todas sus posibles formulaciones.

### Ejercicios de la sección 7.7

#### Ejercicio 33. Una iteración racional y su inclusión real

[]{#MA-EX-ANM-01-007-033}

Sean $\rho,r\in\mathbb Q$ con $\rho>0$, $r>0$ y $r^2>\rho$. Construye en $\mathbb Q$ la iteración $q_0=r$, $q_{n+1}=(q_n+\rho/q_n)/2$. Declara los tipos de $q$, de la inclusión $\iota:\mathbb Q\to\mathbb R$ y de $\widetilde q=\iota\circ q$. Justifica racionalidad, positividad, invariante cuadrático y dirección; explica qué conserva la inclusión. Demuestra que $\widetilde q$ coincide como función real con la iteración de parámetros $\iota(\rho),\iota(r)$ del ejercicio 30 y declara su límite real. ¿Se ha demostrado con ello que ese límite sea racional?

[]{#MA-SOL-ANM-01-007-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Los objetos son

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

La inclusión conserva operaciones de cuerpo, inversos no nulos y orden; también refleja el orden. En consecuencia,

$$
\widetilde q_0=\iota(r),\qquad
\widetilde q_{n+1}=\frac{\widetilde q_n+\iota(\rho)/\widetilde q_n}{2}.
$$

Los parámetros reales satisfacen las hipótesis de 30. La igualdad con aquella sucesión real se prueba por inducción: mismos términos iniciales y, a partir de términos iguales, la misma regla definida produce términos siguientes iguales. Por 30, existe $L>0$ con $\widetilde q_n\to L$, $L^2=\iota(\rho)$ y $\widetilde q_n>L$ para todo $n$; ese $L$ es la única raíz real positiva del parámetro.

Componer con la inclusión conserva los índices y transporta cada evaluación; no identifica $q$ y $\widetilde q$ como objetos con sus codominios declarados. La existencia se obtuvo en $\mathbb R$ mediante completitud. Todavía no se ha decidido si $L\in\iota(\mathbb Q)$: esa pertenencia exige un argumento adicional sobre el parámetro.

La [figura de la inclusión racional–real](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f08) separa sucesión racional, composición con la inclusión y candidato real. Sus datos corresponden al cuadrado 2; los parámetros de esta solución conservan su justificación propia.

</details>

#### Ejercicio 34. Una nueva ecuación y la misma obstrucción de paridad

[]{#MA-EX-ANM-01-007-034}

Construye $q:\mathbb N\to\mathbb Q$ mediante $q_0=3$ y $q_{n+1}=(q_n+8/q_n)/2$. Usa el ejercicio 33 para acreditar un límite real positivo $L$ de $\widetilde q=\iota\circ q$ con $L^2=8$. Demuestra que $L$ no pertenece a $\iota(\mathbb Q)$ reduciendo la ecuación a un cuadrado igual a 2 y reconstruyendo la contradicción de paridad. Deduce que $q$ no tiene límite racional. No importes una teoría nueva de divisibilidad.

[]{#MA-SOL-ANM-01-007-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Los parámetros racionales $\rho=8$ y $r=3$ cumplen $r>0$ y $r^2=9>8$. Por 33, la construcción es racional positiva, y su composición real converge a un único $L>0$ con $L^2=8$.

Supón que $L\in\iota(\mathbb Q)$. Entonces $L/2$ también es imagen de un racional y $(L/2)^2=2$. Representa ese racional por una fracción reducida $p/d$, con $p\in\mathbb Z$, $d\in\mathbb Z$, $d>0$ y sin divisor común mayor que 1. La inclusión conserva las operaciones y es inyectiva; multiplicar la ecuación por $d^2\ne0$ da la igualdad entera

$$
p^2=2d^2.
$$

Si un entero es impar, su forma $2k+1$ da cuadrado $2(2k^2+2k)+1$, también impar. Por tanto $p^2$ par obliga a $p$ par. Escribe $p=2h$; la ecuación produce $4h^2=2d^2$, luego $d^2=2h^2$. La misma observación obliga a $d$ par. Así 2 divide a numerador y denominador, contradiciendo la reducción. No existe tal racional; por tanto $L\notin\iota(\mathbb Q)$.

Si $q$ tuviera límite racional $r$, con la distancia de §7.7 y todas las tolerancias reales positivas, la definición diría que $\widetilde q_n\to\iota(r)$. La unicidad del límite real obligaría a $L=\iota(r)$, contradicción. Por ello $q$ no tiene límite racional, mientras que $\widetilde q$ sí tiene límite real. La contradicción no depende de una aproximación decimal.

</details>

#### Ejercicio 35. Dos destinos para sucesiones de términos racionales

[]{#MA-EX-ANM-01-007-035}

Se afirma: «Como todos los términos de una sucesión pertenecen a $\mathbb Q$, su límite real, si existe, pertenece a $\mathbb Q$». Se propone además la corrección: «Si todos los términos son racionales y ninguno alcanza el límite, entonces éste es irracional». Audita ambas afirmaciones comparando estas construcciones en $\mathbb Q$:

$$
u_0=0,\quad u_{n+1}=\frac{u_n+1}{2};\qquad
q_0=3,\quad q_{n+1}=\frac{q_n+8/q_n}{2}.
$$

Justifica su buena definición racional, sus límites después de la inclusión real y el no alcanzamiento de esos límites. Explica qué permite y qué no permite concluir el codominio racional de los términos. Distingue la existencia de límite real de la existencia de límite racional.

[]{#MA-SOL-ANM-01-007-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

El dato $u_0=0$ es racional y la suma con 1 y la división por 2 conservan racionalidad, por lo que $u:\mathbb N\to\mathbb Q$ está definida. Por inducción,

$$
0\le u_n<1,\qquad u_{n+1}-u_n=\frac{1-u_n}{2}>0.
$$

La base satisface la desigualdad y $u_n<1$ implica $(u_n+1)/2<1$, cerrando la inducción. Después de incluir los términos en $\mathbb R$, §7.3 garantiza existencia por dirección y cota superior 1. Si el límite es $U$, desplazamiento y operaciones de C06 dan $U=(U+1)/2$, luego $U=1$. Ningún término alcanza 1 porque $u_n<1$ para todo índice. El límite es racional; la misma condición de error acredita que $u$ tiene límite racional 1.

Por 33–34, $q:\mathbb N\to\mathbb Q$ está definida, sus términos son positivos, la composición real converge a $L>0$ con $L^2=8$ y $L\notin\iota(\mathbb Q)$. Además $\widetilde q_n>L$ para todo $n$, así que tampoco alcanza su límite. En este caso no hay límite racional, por unicidad del límite real.

La segunda construcción refuta la primera afirmación: pertenecer a $\mathbb Q$ en cada índice no fuerza que el límite real pertenezca a su imagen. La primera construcción refuta la corrección propuesta: no alcanzar un límite no implica que sea irracional. Ambas tienen términos racionales y un límite real no alcanzado; una tiene destino racional y la otra irracional.

El codominio declarado exige que cada término esté en $\mathbb Q$; no decide por sí solo qué candidatos reales satisfacen la condición de límite. Si el límite real de la composición pertenece a $\iota(\mathbb Q)$, su preimagen racional satisface esa misma condición de error. Si no pertenece, la unicidad excluye cualquier límite racional. En todo caso deben acreditarse primero la existencia real y después la pertenencia del destino.

</details>

#### Ejercicio 36. Excluir candidatos con tolerancias racionales

[]{#MA-EX-ANM-01-007-036}

Sea $a:\mathbb N\to\mathbb Q$, sea $\widetilde a=\iota\circ a$ y supón que $\widetilde a_n\to L\in\mathbb R\setminus\iota(\mathbb Q)$. Define «límite racional con tolerancias racionales» por

$$
\forall\eta\in\mathbb Q,\ \eta>0\quad\exists N\in\mathbb N\quad
\forall n\ge N,\quad |\iota(a_n)-\iota(r)|<\iota(\eta),
$$

para un candidato $r\in\mathbb Q$. Prueba que, para un candidato racional fijo, usar todas las tolerancias racionales positivas equivale a usar todas las tolerancias reales positivas. Construye las tolerancias necesarias mediante arquimedianidad. Refuta después cada candidato racional mediante una tolerancia racional explícitamente elegida por debajo de la distancia al límite real y un índice posterior a cualquier corte propuesto. Declara el orden de dependencia de las elecciones. No uses topología de $\mathbb Q$.

[]{#MA-SOL-ANM-01-007-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Fija $r\in\mathbb Q$. Si la condición vale para todas las tolerancias reales positivas, vale en particular para las imágenes de tolerancias racionales positivas.

Recíprocamente, supón la condición con tolerancias racionales. Dado $\varepsilon\in\mathbb R$, $\varepsilon>0$, tomamos $m=\lfloor1/\varepsilon\rfloor+1$, usando el piso construido en C06. Se cumple $m>1/\varepsilon$ y, por tanto, $m\ge1$ y $\eta=1/m\in\mathbb Q$ satisface $0<\iota(\eta)<\varepsilon$. El corte dado por la condición racional para esa $\eta$ asegura, para todo $n\ge N$,

$$
|\iota(a_n)-\iota(r)|<\iota(\eta)<\varepsilon.
$$

Así se obtiene la condición con tolerancias reales. El entero $m$ puede depender de $\varepsilon$ y el corte de la tolerancia racional escogida.

Fija ahora un racional $r$. Como $L$ no está en la imagen racional, $d=|L-\iota(r)|>0$. Toma $m=\lfloor2/d\rfloor+1\in\mathbb N$. La propiedad del piso da $m>2/d>0$, por lo que $m$ no es nulo y podemos fijar la tolerancia racional $\eta_0=1/m$. Entonces $0<\iota(\eta_0)<d/2$. La convergencia real a $L$ proporciona $T\in\mathbb N$ con $|\widetilde a_n-L|<d/2$ para todo $n\ge T$.

Por la desigualdad triangular, para esos índices,

$$
d\le |L-\widetilde a_n|+|\widetilde a_n-\iota(r)|,
\qquad |\widetilde a_n-\iota(r)|>d/2>\iota(\eta_0).
$$

Dado cualquier corte propuesto $K\in\mathbb N$, toma $n=\max\{K,T\}$. Es un índice posterior a $K$ cuyo error supera la tolerancia fija. Queda refutada la condición racional para ese candidato.

El orden de elecciones es: candidato $r$, distancia $d$, entero $m$ y tolerancia $\eta_0$, corte $T$, corte propuesto $K$ e índice infractor $n$. La tolerancia puede depender del candidato, pero queda fijada antes de los cortes propuestos. Como $r$ era arbitrario, no hay límite racional ni siquiera usando sólo tolerancias racionales; la composición conserva su límite real $L$.

</details>

## 7.8. Elegir el argumento y declarar su alcance

[]{#MA-SEC-ANM-01-007-008}

La fórmula $x_n=1-1/(n+1)$ permite comparar dos pruebas que responden a datos distintos. Si proponemos el candidato $1$, basta examinar el error. Si sólo usamos dirección y cota, el teorema monótono construye primero un destino como supremo y deja por identificar ese extremo.

Para la prueba directa, fijamos $\varepsilon>0$ y usamos el piso positivo de C06 para elegir $N=\lfloor1/\varepsilon\rfloor$. Si $n\ge N$, entonces $n+1\ge N+1>1/\varepsilon$, de donde $|x_n-1|=1/(n+1)<\varepsilon$. Así se acredita el candidato $1$ sin necesitar monotonía como hipótesis.

En la prueba por orden, $x_{n+1}-x_n=1/[(n+1)(n+2)]>0$ y $x_n<1$. El teorema de §7.3 da convergencia a $s=\sup S_x$. Para identificarlo sin usar la prueba directa, tomemos $B<1$ y elijamos $m=\lfloor1/(1-B)\rfloor+1$. Entonces $m>1/(1-B)$ y $1/(m+1)<1-B$, por lo que $x_m>B$. Ningún $B<1$ es cota superior y $1$ sí lo es; luego $s=1$.

La primera ruta controla un error alrededor de un candidato; la segunda construye un límite por completitud e identifica después su extremo. El piso usado en la primera procede de la propiedad arquimediana que C03 dedujo de completitud, de modo que la distinción entre rutas no afirma independencia lógica respecto de ella. Ninguna evaluación alcanza el destino, pues $1/(n+1)>0$ mantiene $x_n<1$.

Si después estudiamos $b_n=2x_n-3$, la convergencia de $x$ ya acreditada habilita suma y escalar de C06, y obtenemos $b_n\to2\cdot1-3=-1$. Esta aplicación de reglas comienza con un límite conocido. Para una recurrencia, §7.6 mostró el mismo orden lógico: las reglas identifican el destino después de que el teorema monótono haya garantizado su existencia.

El extremo debe corresponder al conjunto en el que verificamos la dirección. En el ejemplo de §7.4,

$$
a_0=10,\qquad a_n=1-\frac1n\quad(n\ge1).
$$

La fórmula recíproca no se evalúa en 0; ese término está definido por separado. La sucesión completa no es monótona: baja de $a_0=10$ a $a_1=0$ y después aumenta. La cola desde $T=1$ sí es no decreciente y tiene cota superior 1.

Definamos $c:\mathbb N\to\mathbb R$ por $c_k=a_{1+k}$. Entonces $c_k=1-1/(k+1)=x_k$, de modo que $c$ y $x$ son la misma función. La restricción de $a$ a $\{n\in\mathbb N:n\ge1\}$ tiene otro dominio; la reindexación $c$ tiene dominio $\mathbb N$. Su conjunto de valores coincide con el conjunto de cola $S_{a,1}$, cuyo supremo es 1. El teorema eventual de §7.4 da $a_n\to1$.

El traslado de cortes también queda declarado: si $K$ controla el error de $c$ para una tolerancia, $N=1+K$ controla el de $a$. Para $n\ge N$, el natural $k=n-1$ cumple $k\ge K$ y $|a_n-1|=|c_k-1|$. El prefijo se excluye mediante ese corte; no se elimina del conjunto global de valores cuando se calcula su extremo.

El supremo global sigue siendo $10$, porque es un término que domina los demás; el límite $1$ es el supremo de la cola admisible. Por eso una afirmación sobre monotonía eventual debe nombrar el conjunto de cola, sin sustituirlo por la imagen global.

La elección de una prueba depende también de qué hipótesis podemos acreditar. Las cotas $-1$ y $1$ de $d_n=(-1)^n$ no habilitan el teorema monótono, y la refutación de §7.5 excluye todos sus límites reales. Para $e_n=(-1)^n/(n+1)$ tampoco hay dirección eventual, pero el error sí acredita el límite cero. La falla de una hipótesis impide aquella aplicación sin decidir por sí sola la convergencia.

En $a_n=n$ sí hay monotonía y cota inferior $0$; falta la superior pertinente. El escape de §7.5 describe una cola por encima de cada barrera real y excluye un límite finito.

La recurrencia de §7.6 exigía distinguir tres cuestiones: $y_n>0$ permitía construir el siguiente término; descenso y cota inferior daban existencia de $L$; y $L\ge1$ permitía dividir por ese límite. Si se omitiera la última cota, el hecho de que todos los términos fueran no nulos no bastaría para autorizar $2/L$. Resolver la ecuación tampoco reemplazaría la prueba de existencia.

La construcción racional añade una exigencia sobre el candidato. Para $y:\mathbb N\to\mathbb Q$ y $\widetilde y=\iota\circ y:\mathbb N\to\mathbb R$, los valores correspondientes conservan orden y distancia, pero el límite real $L>0$ con $L^2=2$ queda fuera de la imagen racional. Afirmar que es racional porque lo son todos los términos atribuiría a $\mathbb Q$ una propiedad que este ejemplo refuta.

Estas conclusiones tienen obligaciones distintas sobre los índices. Para convergencia, cada tolerancia recibe un corte que controla todos los posteriores. Para escape, cada barrera real recibe su corte. Para refutar un candidato, se fija una tolerancia y se encuentra un infractor después de cualquier corte propuesto. El conjunto sobre el que tomamos el extremo y el universo al que exigimos pertenencia del límite forman parte de lo que cada prueba establece.

### Ejercicios de la sección 7.8

#### Ejercicio 37. Qué conclusión cierra cada argumento

[]{#MA-EX-ANM-01-007-037}

Audita este dossier de argumentos. En cada entrada decide si la conclusión está acreditada, identifica la hipótesis que falta cuando corresponda y repara el argumento o su conclusión con una prueba. No uses una muestra finita como garantía universal.

1. Para $a_n=2n+1$, se observa que es no decreciente y que $a_n\ge1$; se concluye que tiene límite real por el teorema monótono.
2. Para $b_0=7$ y $b_n=2-1/n$ cuando $n\ge1$, se observa que la cola desde 1 es creciente y acotada; se concluye que el límite es $\sup S_b=7$.
3. Para $c_0=0$ y $c_{n+1}=3-c_n$, se resuelve $C=3-C$ y se concluye $c_n\to3/2$.
4. Para $d_n=4-1/(n+2)$, se verifica no decrecimiento y cota superior 4, y se propone concluir $d_n\to4$ después de demostrar que ningún real menor que 4 es cota superior.

Declara dominio y codominio de las sucesiones, el conjunto sobre el que se toma cada extremo y el orden lógico entre existencia e identificación.

[]{#MA-SOL-ANM-01-007-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Las cuatro prescripciones definen funciones $\mathbb N\to\mathbb R$: las fórmulas recíprocas se evalúan sólo en índices con denominador no nulo, y la recurrencia afín siempre produce un real.

**Entrada 1.** El incremento $a_{n+1}-a_n=2$ es positivo, pero la cota inferior 1 no es la cota superior requerida para una sucesión no decreciente. Para cada barrera $M\in\mathbb R$, la arquimedianidad permite elegir $N\in\mathbb N$ con $N>(M-1)/2$. Todo $n\ge N$ cumple $a_n=2n+1>M$. Hay escape por arriba y, por §7.5, no hay límite real. La reparación consiste en esa conclusión; la falta de cota superior no puede suplirse aquí.

**Entrada 2.** La cola reindexada $u_k=b_{k+1}=2-1/(k+1)$ tiene dominio $\mathbb N$ y conjunto de valores $S_{b,1}$. Su incremento es positivo y $u_k<2$. Para cualquier $B<2$, elige $k\in\mathbb N$ con $k>1/(2-B)$; entonces $u_k>B$. Así $\sup S_{b,1}=2$, y §7.3 da $u_k\to2$. La transferencia de cola da $b_n\to2$. En cambio, $\sup S_b=7$ porque el primer término es 7 y los demás son menores que 2. La hipótesis monótona se verificó sobre la cola, no sobre el conjunto global.

**Entrada 3.** Por inducción, $c_{2k}=0$ y $c_{2k+1}=3$. La ecuación $C=3-C$ sólo sería necesaria si existiera el límite. Para cualquier candidato $A$, fija $\varepsilon_0=3/2$. Dado $N$, si $A\le3/2$, el índice $2N+1$ tiene error $|3-A|\ge3/2$; si $A>3/2$, el índice $2N$ tiene error $|A|>3/2$. Ambos índices son al menos $N$. Ningún candidato es límite. La reparación es excluir límites reales, no aceptar la solución formal de la ecuación.

**Entrada 4.** El argumento sí cierra su conclusión cuando completa la comprobación propuesta. El incremento es $1/[(n+2)(n+3)]>0$ y $d_n<4$. Si $B<4$, elige $m>1/(4-B)$ natural; entonces $d_m>B$. De ello resulta $\sup S_d=4$, y §7.3 da $d_n\to4$. La completitud proporciona existencia mediante el teorema; la prueba extremal identifica el límite. No basta mencionar una cota superior cualquiera para identificarla como supremo.

</details>

#### Ejercicio 38. Dos recorridos hacia una misma barrera

[]{#MA-EX-ANM-01-007-038}

Sean $c\in\mathbb R$ y $h>0$. Para la familia $x:\mathbb N\to\mathbb R$, $x_n=c-h/(n+1)^2$, demuestra $x_n\to c$ por dos recorridos completos: estimación del error con un corte $N(\varepsilon)$ explícitamente construido y teorema monótono con identificación del supremo. Justifica dirección, cotas y no alcanzamiento del destino. Señala dónde se usa directamente completitud y dónde se recibe su consecuencia arquimediana. No invoques el límite ya obtenido por una ruta para cerrar la otra.

[]{#MA-SOL-ANM-01-007-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Fija $\varepsilon>0$. La construcción del piso de C06 da el corte explícito $N=\lfloor\max\{1,h/\varepsilon\}\rfloor+1\in\mathbb N$, que satisface $N>\max\{1,h/\varepsilon\}$. Para todo $n\ge N$, se tiene $(n+1)^2>n+1>N>h/\varepsilon$, y por tanto

$$
|x_n-c|=\frac{h}{(n+1)^2}<\varepsilon.
$$

El corte depende de $\varepsilon$ y del parámetro fijo $h$; funciona para todos los índices posteriores. Esta prueba acredita directamente el candidato $c$.

Para todo $n\in\mathbb N$,

$$
x_{n+1}-x_n
=\frac{h(2n+3)}{(n+1)^2(n+2)^2}>0,\qquad
c-h=x_0\le x_n<c.
$$

El conjunto real no vacío $S_x$ tiene cota superior $c$. El teorema de §7.3 recibe completitud para dar un límite $s=\sup S_x$. Para identificar el extremo sin invocar la primera ruta, fija $B<c$ y elige $m\in\mathbb N$ con $m>\max\{1,h/(c-B)\}$. Entonces $(m+1)^2>h/(c-B)$ y $x_m>B$. Ningún $B<c$ es cota superior, luego $s=c$. Esta segunda prueba también da $x_n\to c$.

La positividad de $h/(n+1)^2$ demuestra que ningún término alcanza $c$. En la primera ruta se reutiliza arquimedianidad, cuya dependencia de completitud fue probada en C03; en la segunda se usa directamente completitud para obtener el supremo y además arquimedianidad para identificarlo. La separación de rutas no afirma independencia lógica respecto de completitud.

</details>

#### Ejercicio 39. Dos barreras que se encuentran

[]{#MA-EX-ANM-01-007-039}

Sean $a,b:\mathbb N\to\mathbb R$ con $a$ no decreciente, $b$ no creciente y $a_n\le b_n$ para todo $n$. No se supone que sus términos sean positivos. Supón además $b_n-a_n\to0$. Demuestra que ambas sucesiones tienen límite real y que sus límites coinciden. Si $c:\mathbb N\to\mathbb R$ satisface $a_n\le c_n\le b_n$ desde un índice $T$, demuestra que $c$ converge a ese mismo destino y construye un corte común para una tolerancia dada. Distingue lo que se obtiene sin la hipótesis sobre la distancia y da un ejemplo que muestre su necesidad para la igualdad de límites. No uses un teorema de intervalos encajados.

[]{#MA-SOL-ANM-01-007-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Las direcciones y el orden entre términos dan, para todo $n$,

$$
a_0\le a_n\le b_n\le b_0.
$$

Así $a$ tiene cota superior $b_0$ y $b$ cota inferior $a_0$, sin exigir signo positivo. §§7.3–7.4 dan $a_n\to A$ y $b_n\to B$, con $A,B\in\mathbb R$. El orden de límites de C06 da $A\le B$. La regla de resta da $b_n-a_n\to B-A$, mientras que la hipótesis da límite 0 para esa misma sucesión. Por unicidad, $B-A=0$. Denota el destino común por $L=A=B$.

Dado $\varepsilon>0$, toma cortes $N_a,N_b$ que aseguren $|a_n-L|<\varepsilon$ y $|b_n-L|<\varepsilon$ respectivamente. Define $N=\max\{T,N_a,N_b\}$. Para $n\ge N$,

$$
L-\varepsilon<a_n\le c_n\le b_n<L+\varepsilon,
$$

de donde $|c_n-L|<\varepsilon$. Ésta es la captura por sándwich de C06 con un corte común explícito; el prefijo de $c$ no influye.

Sin la hipótesis de distancia, se conservan la existencia de $A,B$ y $A\le B$, pero no necesariamente su igualdad ni la convergencia de $c$. Por ejemplo, $a_n=-1$ y $b_n=1$ son barreras constantes con límites distintos y distancia 2. La sucesión $c_n=(-1)^n$ permanece entre ambas y no tiene límite real, como se probó en §7.5. La condición sobre la distancia es la que obliga a encontrar un único destino común.

</details>

#### Ejercicio 40. Medias simultáneas y un producto conservado

[]{#MA-EX-ANM-01-007-040}

Sean $0<a_0\le b_0$ reales. Construye simultáneamente $a,b:\mathbb N\to\mathbb R$ mediante

$$
a_{n+1}=\frac{2a_nb_n}{a_n+b_n},\qquad
b_{n+1}=\frac{a_n+b_n}{2}.
$$

Demuestra buena definición, positividad y conservación de $a_n\le b_n$. Obtén las dos direcciones monótonas, cotas y conservación del producto. Acredita existencia de los dos límites antes de usar las recurrencias para identificarlos; demuestra que tienen un destino común y caracteriza éste por una ecuación y su signo. Trata el caso $a_0=b_0$ y decide si, partiendo de desigualdad estricta, alguna evaluación alcanza el destino.

Si $a_0,b_0$ son racionales, declara las dos construcciones con codominio $\mathbb Q$ y sus composiciones reales. Para $a_0=1$, $b_0=2$, determina si existe un límite racional y justifica tu conclusión. No uses continuidad, compactitud ni teoría general de iteraciones.

[]{#MA-SOL-ANM-01-007-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Supón $0<a_n\le b_n$. Entonces $a_n+b_n>0$, por lo que el paso armónico está definido, y ambos términos siguientes son positivos. Las identidades

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

Los teoremas monótonos aplicados a estas cotas dan $a_n\to A$ y $b_n\to B$. Aquí se recibe completitud real. El orden de límites da $a_0\le A\le B\le b_0$, en particular $A+B\ge2a_0>0$. Todos los denominadores $a_n+b_n$ son positivos y su límite es no nulo; así están verificadas las hipótesis del cociente de C06.

Por desplazamiento y operaciones de límites, las recurrencias dan

$$
A=\frac{2AB}{A+B},\qquad B=\frac{A+B}{2}.
$$

La segunda igualdad implica $A=B=L>0$. La primera es coherente con esa igualdad y se ha usado con sus hipótesis acreditadas. La regla de producto y la constancia del producto dan $AB=P$, luego $L^2=P$. Si $R>0$ es otro real con $R^2=P$, $(L-R)(L+R)=0$ y $L+R>0$ fuerzan $R=L$. El destino es el único real positivo de cuadrado $P$; su existencia ha quedado construida.

Si $a_0=b_0=t>0$, ambas reglas conservan $t$ por inducción: las sucesiones son constantes e iguales. Si $a_0<b_0$, la identidad de la diferencia conserva $a_n<b_n$ estrictamente en cada índice, y los dos incrementos anteriores son estrictos. Como $a_nb_n=L^2$, la positividad implica $a_n<L<b_n$: si $a_n\ge L$, el producto con $b_n>a_n$ sería mayor que $L^2$; si $b_n\le L$, el producto con $a_n<b_n$ sería menor. Ninguna evaluación alcanza el destino común.

Para datos racionales positivos, las operaciones conservan racionalidad y el denominador racional positivo tiene inverso racional. Así se construyen $a^{\mathbb Q},b^{\mathbb Q}:\mathbb N\to\mathbb Q$. Sus composiciones $\widetilde a=\iota\circ a^{\mathbb Q}$ y $\widetilde b=\iota\circ b^{\mathbb Q}$ tienen codominio $\mathbb R$ y cumplen las mismas reglas reales, porque la inclusión conserva operaciones y orden. Coinciden por inducción con las construcciones reales de los datos incluidos; no se identifica una función racional con otra de codominio real.

Con $a_0=1$, $b_0=2$, el producto es 2. Ambas composiciones convergen al real positivo $L$ con $L^2=2$. La prueba de paridad de §7.7 excluye $L\in\iota(\mathbb Q)$: una fracción reducida cuyo cuadrado fuera 2 tendría numerador y denominador pares. Si cualquiera de las sucesiones racionales tuviera límite racional $r$, su composición convergería también a $\iota(r)$; la unicidad real forzaría $\iota(r)=L$, contradicción. Hay destino real común y ningún límite racional para estas dos construcciones.

Las [obligaciones de existencia](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f07) y la [distinción de codominios](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html#fig-anm-c07-f08) sirven para comparar el método. Esas figuras representan la iteración de §7.6–§7.7, no las dos medias de este ejercicio; aquí el producto conservado y las desigualdades anteriores justifican el destino común.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-7)

[← Capítulo 6](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) · [Capítulo 8 →](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html)
