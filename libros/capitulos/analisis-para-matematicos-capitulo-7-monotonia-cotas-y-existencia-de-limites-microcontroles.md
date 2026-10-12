---
content-id: MA-BCH-0233
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-007-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 7
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C07_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 7](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html) · [Ejercicios](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-microcontroles.html)

Las soluciones corresponden, en su orden original, a los microcontroles de «Antes de seguir» del manuscrito canónico. Se conserva $\mathbb N=\{0,1,2,\ldots\}$. Las preguntas permanecen en el manuscrito; los metadatos internos fijan su sección, posición y huella literal.

## §7.1 — Comparar términos: qué significa ser monótona

### 1. Solución

[]{#MA-MIC-ANM-01-007-001}

[]{#MA-MSOL-ANM-01-007-001}

[]{#MA-SEC-ANM-01-007-001}

$a$ es una función $\mathbb N\to\mathbb R$, es decir, una sucesión real. $n$ y $n+1$ son índices naturales; $a_n=a(n)$ y $a_{n+1}=a(n+1)$ son términos reales. La relación $\le$ escrita compara esos dos valores reales. Aunque los índices siempre cumplen $n<n+1$, eso no determina el orden de los valores que la función les asigna.

### 2. Solución

[]{#MA-MIC-ANM-01-007-002}

[]{#MA-MSOL-ANM-01-007-002}

La condición es

$$
\bigl(\forall n\in\mathbb N,\ a_n\le a_{n+1}\bigr)
\lor
\bigl(\forall n\in\mathbb N,\ a_{n+1}\le a_n\bigr).
$$

Se exige una dirección válida en todos los índices; la disyunción inclusiva admite ambas. En cambio, $\forall n\in\mathbb N,\ (a_n\le a_{n+1}\lor a_{n+1}\le a_n)$ permite cambiar de dirección con $n$ y es verdadera para cualquier sucesión real por el orden total. Esta última condición no caracteriza monotonía.

### 3. Solución

[]{#MA-MIC-ANM-01-007-003}

[]{#MA-MSOL-ANM-01-007-003}

Todo paso empieza en un índice par o impar. Si empieza en $2k$, $p_{2k}=k=p_{2k+1}$. Si empieza en $2k+1$, $p_{2k+1}=k<k+1=p_{2k+2}$. Ambas comparaciones dan no decrecimiento. La subida $p_1=0<p_2=1$ refuta el no crecimiento. No es estrictamente creciente, pues $p_0=p_1=0$; las repeticiones no impiden que cada índice tenga un único valor.

### 4. Solución

[]{#MA-MIC-ANM-01-007-004}

[]{#MA-MSOL-ANM-01-007-004}

Supón $a_{k+1}\le a_k$ para todo $k\in\mathbb N$. Dados $n\le m$, si $n=m$ basta $a_n\le a_n$. Si $n<m$, la cadena finita $a_m\le a_{m-1}\le\cdots\le a_n$ da $a_m\le a_n$ por transitividad. Recíprocamente, si $a_m\le a_n$ para todo par $n\le m$, tomar $m=n+1$ da $a_{n+1}\le a_n$ en cada índice. Así las dos condiciones son equivalentes, incluido el caso de índices iguales.

### 5. Solución

[]{#MA-MIC-ANM-01-007-005}

[]{#MA-MSOL-ANM-01-007-005}

Para cada $n\in\mathbb N$, el no decrecimiento da $a_0\le a_n$ y el no crecimiento da $a_n\le a_0$. Por antisimetría, $a_n=a_0$ para todo índice: $a$ es constante. Recíprocamente, si $a_n=c$ siempre, ambas comparaciones adyacentes son $c\le c$. Una función exige un único valor por índice, no valores distintos en índices distintos; por ello una constante sigue siendo función.

### 6. Solución

[]{#MA-MIC-ANM-01-007-006}

[]{#MA-MSOL-ANM-01-007-006}

La caída $r_0=1>r_1=-1$ refuta el no decrecimiento. La subida $r_1=-1<r_2=1$ refuta el no crecimiento. Como fallan ambas alternativas, $r$ no es monótona. Una sola caída refuta sólo la primera alternativa: una sucesión estrictamente decreciente tiene caídas y sigue siendo monótona. Hace falta excluir también la dirección no creciente.

### 7. Solución

[]{#MA-MIC-ANM-01-007-007}

[]{#MA-MSOL-ANM-01-007-007}

Si $n\ge N$, la comparación entre índices para una sucesión no decreciente da $a_N\le a_n$. Junto con $c<a_N$, resulta $c<a_N\le a_n$, luego $a_n>c$ para todos los índices indicados.

La versión opuesta dice: si $a$ es no creciente y $a_N<c$, entonces $a_n<c$ para todo $n\ge N$. En efecto, $a_n\le a_N<c$ por la comparación no creciente. $N,n$ son índices naturales y $c,a_N,a_n$ son valores reales; la dirección propaga la comparación inicial.

### 8. Solución

[]{#MA-MIC-ANM-01-007-008}

[]{#MA-MSOL-ANM-01-007-008}

En los índices 0–100, la muestra coincide con la sucesión identidad y aumenta estrictamente. Pero la monotonía exige una dirección para todos los pasos, incluidos los que la muestra no contiene. La caída $b_{100}=100>b_{101}=-1$ refuta el no decrecimiento; la subida $b_0=0<b_1=1$ refuta el no crecimiento. Así $b$ no es monótona. La función $u:\mathbb N\to\mathbb R$, $u_n=n$, es estrictamente creciente en todo índice y difiere de $b$, por ejemplo en 101: $u_{101}=101\ne-1=b_{101}$. Coincidir en una muestra no es ser la misma función.

## §7.2 — El conjunto de valores y su mejor barrera

### 9. Solución

[]{#MA-MIC-ANM-01-007-009}

[]{#MA-MSOL-ANM-01-007-009}

[]{#MA-SEC-ANM-01-007-002}

$S_p=\{0,1,2,\ldots\}$, considerado como subconjunto de $\mathbb R$: cada $k$ aparece en $p$ y ningún término toma otro valor. El conjunto registra cada valor una sola vez, aunque $p_{2k}=p_{2k+1}=k$. Se pierden la multiplicidad de aparición y los índices a los que corresponde cada valor, incluido su orden. $p:\mathbb N\to\mathbb R$ es una función; $S_p$ es su conjunto de valores, no la misma clase de objeto.

### 10. Solución

[]{#MA-MIC-ANM-01-007-010}

[]{#MA-MSOL-ANM-01-007-010}

Si $a_n\le U$ para todo $n$, cada $x\in S_a$ tiene la forma $x=a_j$ y cumple $x\le U$; así $U$ es cota superior del conjunto. Recíprocamente, si $U$ domina $S_a$, domina cada $a_n$ porque todos los términos pertenecen a ese conjunto. $S_a$ es no vacío ya que contiene $a_0$, un valor real de la función definida en el índice natural 0.

### 11. Solución

[]{#MA-MIC-ANM-01-007-011}

[]{#MA-MSOL-ANM-01-007-011}

Las hipótesis son que $S_a\subseteq\mathbb R$ sea no vacío y esté acotado superiormente. La primera se acredita con $a_0$; la segunda exige una cota real $U$ para todos los términos. El principio del supremo garantiza entonces la existencia de algún $s\in\mathbb R$ que es su supremo. La caracterización por cota y aproximación permite verificar si un candidato real dado es ese supremo; no asegura por sí sola que exista un candidato que cumpla las dos condiciones. No se requiere monotonía para obtener el supremo.

### 12. Solución

[]{#MA-MIC-ANM-01-007-012}

[]{#MA-MSOL-ANM-01-007-012}

Si $s=\sup S_a$, ya es cota superior. Dada $\varepsilon>0$, $s-\varepsilon$ no puede ser cota superior, pues sería una cota menor que la menor cota. Se niega la afirmación universal $\forall n\in\mathbb N,\ a_n\le s-\varepsilon$ y se obtiene $j\in\mathbb N$ con $a_j>s-\varepsilon$. La cota $s$ añade $a_j\le s$.

Recíprocamente, supón que $s$ domina todos los términos y que para cada $\varepsilon>0$ existe $j$ con $a_j>s-\varepsilon$. Sea $U$ otra cota superior. Si $U<s$, toma $\varepsilon=s-U>0$. El testigo satisface $a_j>s-\varepsilon=U$, contradiciendo que $U$ sea cota. Así $s\le U$ para toda cota superior, y junto con la condición de cota resulta $s=\sup S_a$.

### 13. Solución

[]{#MA-MIC-ANM-01-007-013}

[]{#MA-MSOL-ANM-01-007-013}

$x_3=3/4$ queda fuera de $(3/4,1]$ porque coincide con su frontera inferior excluida. $x_4=4/5$ está dentro, pues $3/4<4/5<1$. El término 1 de la sucesión constante también está dentro, en la frontera superior incluida. La aproximación al supremo exige $s-\varepsilon<a_j$, una desigualdad estricta por abajo, pero la condición de cota permite $a_j\le s$, incluida la igualdad con el supremo.

### 14. Solución

[]{#MA-MIC-ANM-01-007-014}

[]{#MA-MSOL-ANM-01-007-014}

En ambas sucesiones, 2 es cota superior y el supremo es 1. Para $x$, todos los términos son menores que 1 y, dada $\varepsilon>0$, C06 §6.3 proporciona $j$ con $1/(j+1)<\varepsilon$; entonces $x_j>1-\varepsilon$. Esto acredita el supremo 1, sin alcanzamiento y sin máximo. Para $c$, el conjunto de valores es $\{1\}$: su supremo y máximo valen 1 y se alcanzan en todo índice.

La igualdad de los supremos es igualdad entre números reales; también ambas admiten la misma cota 2, que no es su supremo. Las funciones siguen siendo distintas porque $x_0=0\ne1=c_0$, y sus conjuntos de valores también son distintos: sólo $S_c$ contiene 1.

### 15. Solución

[]{#MA-MIC-ANM-01-007-015}

[]{#MA-MSOL-ANM-01-007-015}

La caracterización dice que $t=\inf S_a$ si y sólo si

$$
\forall n\in\mathbb N,\quad t\le a_n,
\qquad
\forall\varepsilon>0\ \exists j\in\mathbb N,\quad a_j<t+\varepsilon.
$$

Para $z_n=1/(n+1)$, todos los términos son positivos, de modo que 0 es cota inferior. La convergencia $1/(n+1)\to0$, demostrada en C06 §6.3, garantiza para cada $\varepsilon>0$ un término $z_j<\varepsilon=0+\varepsilon$. Cota y aproximación acreditan el ínfimo 0. Como ningún término vale 0, el ínfimo no pertenece al conjunto, que por ello no tiene mínimo.

### 16. Solución

[]{#MA-MIC-ANM-01-007-016}

[]{#MA-MSOL-ANM-01-007-016}

$S_r=\{-1,1\}$ tiene supremo 1, alcanzado por $r_0=1$. Para cualquier $\varepsilon>0$, el mismo testigo $j=0$ cumple $1-\varepsilon<r_j\le1$.

Para refutar el candidato 1 como límite, fija $\varepsilon_0=1$. Dado cualquier corte $N\in\mathbb N$, el índice $n=2N+1\ge N$ es impar y tiene $r_n=-1$, luego $|r_n-1|=2\ge\varepsilon_0$. No existe un corte que controle esa tolerancia. La caracterización del supremo sólo exige un término próximo para cada tolerancia; falta el control de todos los términos desde un corte. Esta refutación excluye el candidato 1, sin pretender por sí sola excluir todos los candidatos reales.

## §7.3 — La completitud convierte una barrera en límite

### 17. Solución

[]{#MA-MIC-ANM-01-007-017}

[]{#MA-MSOL-ANM-01-007-017}

[]{#MA-SEC-ANM-01-007-003}

Si $a:\mathbb N\to\mathbb R$ es no decreciente y existe $U\in\mathbb R$ con $a_n\le U$ para todo $n$, entonces converge al real $s=\sup\{a_n:n\in\mathbb N\}$. No exige crecimiento estricto: admite repeticiones y constantes. Tampoco exige que $s$ sea un término; el supremo puede no alcanzarse.

### 18. Solución

[]{#MA-MIC-ANM-01-007-018}

[]{#MA-MSOL-ANM-01-007-018}

Las cuatro obligaciones son: verificar que $S_a$ es no vacío y acotado superiormente, usando $a_0$ y la cota $U$; obtener $s=\sup S_a\in\mathbb R$ por completitud; encontrar, dada $\varepsilon>0$, un término $a_N>s-\varepsilon$ por minimalidad del supremo; y propagar esa comparación a todo $n\ge N$ por no decrecimiento, conservando $a_n\le s$. Completitud se usa en la existencia de $s$. El término próximo se obtiene de una propiedad de ese supremo ya existente, sin invocar de nuevo el principio de existencia.

### 19. Solución

[]{#MA-MIC-ANM-01-007-019}

[]{#MA-MSOL-ANM-01-007-019}

Si $s-\varepsilon$ fuera cota superior, la minimalidad de $s$ implicaría $s\le s-\varepsilon$, imposible porque $\varepsilon>0$. La negación de $\forall n\in\mathbb N,\ a_n\le s-\varepsilon$ proporciona $N\in\mathbb N$ con $a_N>s-\varepsilon$. Primero se fija $s$ a partir de la sucesión; después se recibe $\varepsilon>0$, se obtiene $N$ para esa tolerancia y se considera un índice arbitrario $n\ge N$. El corte puede depender de la tolerancia, pero debe controlar todos esos índices.

### 20. Solución

[]{#MA-MIC-ANM-01-007-020}

[]{#MA-MSOL-ANM-01-007-020}

De $a_n\le s$ se obtiene $|a_n-s|=s-a_n$. La comparación $a_n\ge a_N>s-\varepsilon$ da $s-a_n<\varepsilon$, luego $|a_n-s|<\varepsilon$. Si $a_N=s-\varepsilon$, el error en el propio índice $N$ es exactamente $\varepsilon$, de modo que ese corte no cumple la desigualdad estricta requerida. Si $a_n=s$, el error es cero y satisface la condición porque $\varepsilon>0$.

### 21. Solución

[]{#MA-MIC-ANM-01-007-021}

[]{#MA-MSOL-ANM-01-007-021}

La regla define un real en cada paso, pues sólo divide por el número no nulo 2. La base $u_0=0$ cumple $0\le u_0\le1$. Si $0\le u_n\le1$, entonces $1/2\le(u_n+1)/2\le1$, lo que implica $0\le u_{n+1}\le1$. La inducción conserva ambas barreras en todo índice. Además,

$$
u_{n+1}-u_n=\frac{1-u_n}{2}\ge0.
$$

Así $u$ es no decreciente y tiene cota superior 1. El teorema de §7.3 garantiza un límite real $L=\sup S_u$, con $0\le L\le1$. Esta conclusión acredita existencia y descripción extremal; no calcula su valor numérico mediante la recurrencia.

### 22. Solución

[]{#MA-MIC-ANM-01-007-022}

[]{#MA-MSOL-ANM-01-007-022}

Para todo $n\ge4$,

$$
|x_n-1|=\frac1{n+1}\le\frac15<\frac14.
$$

Por tanto $N=4$ controla todos los índices posteriores. En cambio, $N=3$ falla ya en el índice 3 porque $|x_3-1|=1/4$, igual a la tolerancia y no menor. Una gráfica finita sólo exhibe los puntos de los índices representados; la estimación universal, o la propagación monótona con la cota 1, es lo que acredita el control de toda la cola. El corte 4 es un índice natural, mientras que 1 y 3/4 son alturas reales.

### 23. Solución

[]{#MA-MIC-ANM-01-007-023}

[]{#MA-MSOL-ANM-01-007-023}

Fija $\varepsilon_0=(U-s)/2>0$. Para todo $n\in\mathbb N$, la cota del supremo da $a_n\le s<U$, luego

$$
|a_n-U|=U-a_n\ge U-s=2\varepsilon_0>\varepsilon_0.
$$

Ante cualquier corte propuesto $N$, el propio índice $n=N$ infringe esa tolerancia. La sucesión no converge a $U$. Una cota mayor que $s$ deja un margen real respecto de todos los valores y no proporciona términos arbitrariamente próximos a ella; la propiedad de menor cota superior sí permite obtenerlos.

### 24. Solución

[]{#MA-MIC-ANM-01-007-024}

[]{#MA-MSOL-ANM-01-007-024}

Si $a_K=s$ y $n\ge K$, el no decrecimiento da $s=a_K\le a_n$. Como $s$ es cota superior, también $a_n\le s$. Por antisimetría, $a_n=s$ para todo $n\ge K$. El teorema admite esa cola constante: no exige dirección estricta ni ausencia de alcanzamiento. Para cualquier tolerancia positiva, el corte $K$ controla error cero en toda la cola; si $K=0$, la sucesión completa es constante.

## §7.4 — Cambiar la dirección y descartar un prefijo

### 25. Solución

[]{#MA-MIC-ANM-01-007-025}

[]{#MA-MSOL-ANM-01-007-025}

[]{#MA-SEC-ANM-01-007-004}

Define $b:\mathbb N\to\mathbb R$ por $b_n=-a_n$. Si $a_{n+1}\le a_n$, cambiar el signo da $b_n\le b_{n+1}$, así que $b$ es no decreciente. De $\ell_0\le a_n$ se obtiene $b_n\le-\ell_0$ para todo índice: $-\ell_0$ es cota superior. En las gráficas, $(n,a_n)$ se transforma en $(n,-a_n)$; se conserva la coordenada de índice y se refleja la altura respecto de cero. El dominio no cambia, pero los valores cambian de signo y las funciones no son necesariamente iguales.

### 26. Solución

[]{#MA-MIC-ANM-01-007-026}

[]{#MA-MSOL-ANM-01-007-026}

Como $b_n\le t$ para todo $n$, cambiar el signo da $-t\le a_n$: $-t$ es cota inferior de $S_a$. Si $\ell$ es cualquier otra cota inferior, $\ell\le a_n$ implica $b_n\le-\ell$, de modo que $-\ell$ es cota superior de $S_b$. La minimalidad de $t$ da $t\le-\ell$ y por tanto $\ell\le-t$. Así $-t$ es la mayor cota inferior y $\inf S_a=-t=-\sup S_b$. El argumento no exige que $t$ o $-t$ sean términos.

### 27. Solución

[]{#MA-MIC-ANM-01-007-027}

[]{#MA-MSOL-ANM-01-007-027}

Por la regla del escalar de C06, multiplicar $b_n\to t$ por −1 da $a_n=-b_n\to-t$. Directamente,

$$
|a_n-(-t)|=|-b_n+t|=|b_n-t|.
$$

Si un corte $N$ garantiza $|b_n-t|<\varepsilon$ para todos los $n\ge N$, esa igualdad garantiza $|a_n+t|<\varepsilon$ en los mismos índices. No hace falta cambiar el corte ni la tolerancia.

### 28. Solución

[]{#MA-MIC-ANM-01-007-028}

[]{#MA-MSOL-ANM-01-007-028}

La restricción $a|_{D_T}:D_T\to\mathbb R$ conserva las evaluaciones de $a$ en $D_T=\{n\in\mathbb N:n\ge T\}$. La reindexación $c:\mathbb N\to\mathbb R$ asigna $c_k=a_{T+k}$. Cada valor de $c$ es un valor de la restricción porque $T+k\ge T$. Recíprocamente, si $n\ge T$, entonces $k=n-T\in\mathbb N$ y $a_n=c_k$. Ambas imágenes son $S_{a,T}$.

Si $T>0$, los dominios $D_T$ y $\mathbb N$ son distintos, aunque las imágenes coincidan. Si $T=0$, $D_T=\mathbb N$ y $c_k=a_k$; tanto la restricción como la reindexación son la misma función $a$.

### 29. Solución

[]{#MA-MIC-ANM-01-007-029}

[]{#MA-MSOL-ANM-01-007-029}

Para $n\ge T$, no decrecimiento y una cota superior real habilitan $a_n\to\sup S_{a,T}$; no crecimiento y una cota inferior real habilitan $a_n\to\inf S_{a,T}$. En cada caso, $c_k=a_{T+k}$ tiene la dirección y cota correspondientes en todo $\mathbb N$, por lo que se aplica el teorema global pertinente.

Si $|c_k-L|<\varepsilon$ para todo $k\ge K$, toma $N=T+K$. Para $n\ge N$, $k=n-T$ es natural y cumple $k\ge K$, luego $|a_n-L|=|c_k-L|<\varepsilon$. Si la dirección empieza desde $T_m$ y la cota desde $T_c$, se reúnen en $T=\max\{T_m,T_c\}$, desde donde valen ambas hipótesis.

### 30. Solución

[]{#MA-MIC-ANM-01-007-030}

[]{#MA-MSOL-ANM-01-007-030}

La cláusula $a_0=10$ define el índice cero por separado; $1/n$ sólo se evalúa para $n\ge1$, donde el denominador es no nulo. La caída $a_0=10>a_1=0$ refuta el no decrecimiento global, y la subida $a_1=0<a_2=1/2$ refuta el no crecimiento global. Por ello $a$ no es monótona globalmente.

Desde 1, la reindexación es $c_k=a_{1+k}=1-1/(k+1)$, la función estudiada en §§7.1–7.3. Es no decreciente, tiene supremo 1 y converge a 1. La transferencia de cola da $a_n\to1$ y $\sup S_{a,1}=1$. El supremo global es 10: aparece en $a_0$ y domina todos los demás términos, que están en $[0,1)$. El prefijo altera el extremo global, pero no el límite.

### 31. Solución

[]{#MA-MIC-ANM-01-007-031}

[]{#MA-MSOL-ANM-01-007-031}

Si $a_n\le U$ para $n\ge T$, define

$$
M=\max\bigl(\{U\}\cup\{a_n:n<T\}\bigr).
$$

El conjunto es finito y no vacío. Para $n<T$, el término pertenece al conjunto y es $\le M$; para $n\ge T$, $a_n\le U\le M$. Así $M$ es cota superior global.

Si $\ell\le a_n$ desde $T$, define $m=\min(\{\ell\}\cup\{a_n:n<T\})$. Para $n<T$, $m\le a_n$ por el mínimo; para $n\ge T$, $m\le\ell\le a_n$. Es cota inferior global. Si $T=0$, el prefijo está vacío y los conjuntos auxiliares son $\{U\}$ y $\{\ell\}$: resultan $M=U$ y $m=\ell$, sin tomar extremos de un conjunto vacío.

### 32. Solución

[]{#MA-MIC-ANM-01-007-032}

[]{#MA-MSOL-ANM-01-007-032}

Desde $T'\ge T$ siguen valiendo no decrecimiento y la misma cota superior. El resultado eventual aplicado desde $T$ da $a_n\to s=\sup S_{a,T}$; aplicado desde $T'$ da $a_n\to s'=\sup S_{a,T'}$. La unicidad del límite real de C06 obliga a $s=s'$.

Esto no obliga a coincidir con el supremo global: en $a_0=10$ y $a_n=1-1/n$ para $n\ge1$, el supremo de cualquier cola desde $T'\ge1$ es 1, mientras que $\sup S_a=10$. La igualdad obtenida se refiere a las colas que cumplen las hipótesis.

## §7.5 — Qué falla al retirar una hipótesis

### 33. Solución

[]{#MA-MIC-ANM-01-007-033}

[]{#MA-MSOL-ANM-01-007-033}

[]{#MA-SEC-ANM-01-007-005}

§7.3 exige una cota superior real; la cota inferior $a_0$ sólo impide que los términos bajen por debajo del inicial, sin impedir que crezcan más allá de toda barrera. Por ejemplo, $a_n=n$ es no decreciente y tiene cota inferior 0, pero carece de cota superior: para cualquier $U\in\mathbb R$, la arquimedianidad proporciona $N\in\mathbb N$ con $N>U$, luego $a_N>U$. Por §7.5 escapa por arriba y no tiene límite real.

### 34. Solución

[]{#MA-MIC-ANM-01-007-034}

[]{#MA-MSOL-ANM-01-007-034}

La comparación monótona entre índices da $a_N\le a_n$ para todo $n\ge N$. Con $a_N>M$, resulta $a_n\ge a_N>M$ en todos esos índices. Así el testigo se convierte en corte gracias al no decrecimiento. $N$ se elige después de fijar la barrera real $M$ y puede depender de ella, para la sucesión dada; no se exige un mismo corte para todas las barreras.

### 35. Solución

[]{#MA-MIC-ANM-01-007-035}

[]{#MA-MSOL-ANM-01-007-035}

Fija $A\in\mathbb R$ y $\varepsilon_0=1$. El escape aplicado a $M=A+1$ da $T\in\mathbb N$ con $a_n>A+1$ para todos los $n\ge T$. Ante cualquier corte propuesto $K$, elige $n=\max\{K,T\}$. Entonces $n\ge K$ y $|a_n-A|=a_n-A>1$. Por tanto ningún $K$ controla error menor que 1 en toda su cola, y $A$ no es límite. La barrera depende del candidato; $T$ se obtiene antes de recibir el corte propuesto y el índice infractor después de éste.

### 36. Solución

[]{#MA-MIC-ANM-01-007-036}

[]{#MA-MSOL-ANM-01-007-036}

Si $b$ tuviera cota superior $U$, de $b_n=-a_n\le U$ se seguiría $a_n\ge-U$ para todo $n$, contradiciendo la ausencia de cota inferior de $a$. Así $b$ carece de cota superior. Además, $a$ no creciente hace $b$ no decreciente. La exigencia $a_n<M$ equivale a $b_n>-M$: se aplica el escape por arriba de $b$ a la barrera $-M$. Cambiar el signo conserva el índice y revierte la desigualdad entre valores.

### 37. Solución

[]{#MA-MIC-ANM-01-007-037}

[]{#MA-MSOL-ANM-01-007-037}

Fija la tolerancia $\varepsilon_0=1$. Si $A\ge0$, para cualquier corte $K$ elige el índice impar $n=2K+1\ge K$. Su término es $d_n=-1$ y $|d_n-A|=1+A\ge1$. Si $A<0$, elige el índice par $n=2K\ge K$; entonces $d_n=1$ y $|d_n-A|=1-A>1$. Los dos casos cubren todos los candidatos reales. Un error igual a 1 basta porque la definición exige que todos los errores posteriores sean estrictamente menores que la tolerancia 1.

### 38. Solución

[]{#MA-MIC-ANM-01-007-038}

[]{#MA-MSOL-ANM-01-007-038}

La implicación convergencia real $\Rightarrow$ acotación no requiere monotonía: es el resultado general de C06 §6.5. Para acotación $\Rightarrow$ convergencia sí se necesita la hipótesis monótona en esta equivalencia. Si la dirección es no decreciente, basta una cota superior, porque $a_0$ ya es cota inferior; se aplica §7.3. Si es no creciente, basta una cota inferior, porque $a_0$ ya es cota superior; se aplica §7.4. La constante cumple ambas direcciones y también está incluida.

### 39. Solución

[]{#MA-MIC-ANM-01-007-039}

[]{#MA-MSOL-ANM-01-007-039}

La ventana $|d_n|<1/2$ examina únicamente el candidato 0. Una muestra finita no acredita por sí sola el comportamiento de toda la sucesión; la fórmula $d_n=(-1)^n$ permite comprobar $|d_n|=1$ en todo índice y refutar ese candidato.

Para excluir todos los candidatos se fija un real arbitrario $A$ y se usa la refutación de 037: con tolerancia 1, después de cada corte $K$ se toma $2K+1$ si $A\ge0$ o $2K$ si $A<0$. En ambos casos el error es al menos 1. La conclusión universal procede de ese argumento por casos, no de la única ventana centrada en 0.

### 40. Solución

[]{#MA-MIC-ANM-01-007-040}

[]{#MA-MSOL-ANM-01-007-040}

$e_n=(-1)^n/(n+1)$ converge a 0 por C06 §6.3, sin monotonía eventual: después de cualquier corte $K$, el paso de $2K$ a $2K+1$ baja de positivo a negativo y el de $2K+1$ a $2K+2$ sube de negativo a positivo. Esos dos pasos refutan ambas direcciones en toda cola.

$x_n=1-1/(n+1)$ y $c_n=1$ convergen ambos a 1. La primera nunca lo alcanza porque $1/(n+1)>0$; la constante lo alcanza en cada índice. La igualdad de sus límites es igualdad de números reales, no de funciones: $x_0=0\ne1=c_0$. Las tres tienen dominio $\mathbb N$ y codominio $\mathbb R$, pero son sucesiones distintas.

## §7.6 — Una recurrencia: existir antes de calcular

### 41. Solución

[]{#MA-MIC-ANM-01-007-041}

[]{#MA-MSOL-ANM-01-007-041}

[]{#MA-SEC-ANM-01-007-006}

El teorema monótono de §7.3 acredita primero la existencia de $L_u$: $u$ es no decreciente y tiene cota superior 1. El desplazamiento de C06 §6.4 da $u_{n+1}\to L_u$, mientras que las reglas de suma y escalar de C06 §6.6 dan $(u_n+1)/2\to(L_u+1)/2$. La recurrencia iguala estas dos sucesiones término a término; la unicidad del límite obliga a que $L_u=(L_u+1)/2$, de donde $L_u=1$. La ecuación identifica un límite cuya existencia ya estaba demostrada.

### 42. Solución

[]{#MA-MIC-ANM-01-007-042}

[]{#MA-MSOL-ANM-01-007-042}

Ambas son funciones de $\mathbb N$ en $\mathbb R$, pero en el índice 0 la primera vale $u_0=0$ y la desplazada vale $u_1=1/2$. Esa diferencia basta para que sean sucesiones distintas. El dominio de la desplazada sigue siendo $\mathbb N$: su regla evalúa $u$ en $n+1$. Compartir el límite real 1 no las iguala como funciones.

### 43. Solución

[]{#MA-MIC-ANM-01-007-043}

[]{#MA-MSOL-ANM-01-007-043}

Queda pendiente demostrar que existe un límite real. Bajo la suposición $w_n\to W$, el desplazamiento y la regla del escalar permiten obtener $W=-W$, luego $W=0$; esto sólo restringe el valor de un límite supuesto. La inducción da $w_n=(-1)^n$, y §7.5 refuta su convergencia. En particular, con tolerancia 1 y cualquier corte $K$, el índice $n=K$ tiene $|w_n-0|=1$, por lo que 0 tampoco es límite.

### 44. Solución

[]{#MA-MIC-ANM-01-007-044}

[]{#MA-MSOL-ANM-01-007-044}

Antes de evaluar $2/y_n$ debe conocerse $y_n\ne0$; aquí se demuestra la propiedad más fuerte $y_n>0$. La base $y_0=2$ la cumple. Si $y_n>0$, su inverso existe y $2/y_n>0$, de modo que $y_{n+1}=(y_n+2/y_n)/2>0$ es un único real definido. La inducción permite continuar para todo $n\in\mathbb N$. Con $y_0=0$, el cociente $2/y_0$ no está definido y la prescripción no produce $y_1$.

### 45. Solución

[]{#MA-MIC-ANM-01-007-045}

[]{#MA-MSOL-ANM-01-007-045}

La positividad de los términos está acreditada antes de usar la identidad. La base es $y_0^2=4>2$. Si $y_n^2>2$, entonces $(y_n^2-2)^2>0$ y $4y_n^2>0$; por tanto

$$
y_{n+1}^2-2=\frac{(y_n^2-2)^2}{4y_n^2}>0.
$$

La positividad estricta del numerador conserva la desigualdad estricta; un numerador meramente no negativo sólo daría $y_{n+1}^2\ge2$. La inducción prueba $y_n^2>2$ en todos los índices. Si algún término satisficiera $0<y_n<1$, tendríamos $y_n^2<y_n<1$, contradicción. Así $y_n\ge1$ para todo $n$, sin presuponer una raíz ni el límite.

### 46. Solución

[]{#MA-MIC-ANM-01-007-046}

[]{#MA-MSOL-ANM-01-007-046}

En $y_{n+1}-y_n=(2-y_n^2)/(2y_n)$, el invariante $y_n^2>2$ hace negativo el numerador y la positividad $y_n>0$ hace positivo el denominador. La diferencia es estrictamente negativa, luego $y$ es decreciente y, en particular, no creciente. Junto con la cota inferior 1 demostrada, esto habilita el teorema de §7.4 y garantiza un límite real. La cota superior 2 se obtiene de la dirección: por comparación de índices, $y_n\le y_0=2$.

### 47. Solución

[]{#MA-MIC-ANM-01-007-047}

[]{#MA-MSOL-ANM-01-007-047}

Una sucesión positiva puede converger a 0: $1/(n+1)$ es un ejemplo de C06. Por eso la positividad de cada $y_n$ no asegura por sí sola $L\ne0$. Aquí primero se acredita la existencia de $L$ y se aplica el orden de límites a $1\le y_n\le2$, obteniendo $1\le L\le2$, luego $L>0$. Para el cociente de C06 §6.6 se usan la convergencia de la constante 2 a 2, $y_n\to L\ne0$ y $y_n\ne0$ en todos los índices. Sólo con esos datos se concluye $2/y_n\to2/L$.

### 48. Solución

[]{#MA-MIC-ANM-01-007-048}

[]{#MA-MSOL-ANM-01-007-048}

Si otro real $r>0$ satisface $r^2=2$, entonces $(L-r)(L+r)=L^2-r^2=0$. Como $L+r>0$, ese factor es no nulo y resulta $L=r$: la raíz positiva es única. Para cada $n\in\mathbb N$, el invariante da

$$
(y_n-L)(y_n+L)=y_n^2-L^2=y_n^2-2>0.
$$

Como $y_n+L>0$, se sigue $y_n-L>0$, es decir, $y_n>L$ en todo índice. Los cuatro puntos de la tabla sólo verifican cuatro términos; no acreditan el invariante para todo $n$, la existencia del límite ni la desigualdad universal respecto de él. La inducción y el teorema monótono cierran esas obligaciones. La unicidad de la raíz se prueba por factorización, no por inspección de la muestra.

## §7.7 — La misma construcción sobre los racionales

### 49. Solución

[]{#MA-MIC-ANM-01-007-049}

[]{#MA-MSOL-ANM-01-007-049}

[]{#MA-SEC-ANM-01-007-007}

Los tipos son $y:\mathbb N\to\mathbb Q$, $\iota:\mathbb Q\to\mathbb R$ y $\widetilde y=\iota\circ y:\mathbb N\to\mathbb R$. Componer cambia el codominio de la sucesión y lleva cada valor racional a su imagen real: $\widetilde y_n=\iota(y_n)$. Conserva el dominio $\mathbb N=\{0,1,2,\ldots\}$ y el índice de cada evaluación; no desplaza ni reordena los términos. La identificación usual de los valores no iguala las dos funciones con codominios distintos.

### 50. Solución

[]{#MA-MIC-ANM-01-007-050}

[]{#MA-MSOL-ANM-01-007-050}

La base $y_0=2$ es racional positiva. Si $y_n\in\mathbb Q$ y $y_n>0$, entonces $y_n\ne0$: esa no anulación autoriza el inverso en el cuerpo $\mathbb Q$. Además, $1/y_n>0$, luego $2/y_n$ es racional positivo. La suma $y_n+2/y_n$ y su mitad son racionales positivas, por lo que la fórmula define un único $y_{n+1}\in\mathbb Q$ positivo. La inducción acredita ambas propiedades en todo índice, antes de ejecutar cada división.

### 51. Solución

[]{#MA-MIC-ANM-01-007-051}

[]{#MA-MSOL-ANM-01-007-051}

La inclusión conserva las operaciones y los inversos de valores no nulos, así que $\widetilde y_0=2$ y $\widetilde y_{n+1}=(\widetilde y_n+2/\widetilde y_n)/2$. Esta sucesión y la real de §7.6 tienen el mismo dominio y codominio. Coinciden en 0; si coinciden en $n$, la fórmula ya definida produce términos iguales en $n+1$. Por inducción coinciden en toda evaluación y son la misma función real. En cambio, $y$ tiene codominio $\mathbb Q$ y $\widetilde y$ tiene codominio $\mathbb R$; su relación es la composición explícita con $\iota$.

### 52. Solución

[]{#MA-MIC-ANM-01-007-052}

[]{#MA-MSOL-ANM-01-007-052}

Si $p$ fuera impar, sería $p=2k+1$ para algún $k\in\mathbb Z$, y $p^2=2(2k^2+2k)+1$ sería impar. Por contraposición, $p^2$ par obliga a $p$ par. La ecuación $p^2=2q^2$ permite escribir $p=2h$ y obtener $4h^2=2q^2$, luego $q^2=2h^2$. Así $q^2$ también es par y el mismo argumento hace par a $q$. El divisor común 2 contradice que $p/q$ estuviera reducida; esa hipótesis se usa precisamente al cerrar la contradicción.

### 53. Solución

[]{#MA-MIC-ANM-01-007-053}

[]{#MA-MSOL-ANM-01-007-053}

La condición de límite racional $r$ sería, para cada tolerancia real $\varepsilon>0$, encontrar $N\in\mathbb N$ tal que $n\ge N$ implique $|\iota(y_n)-\iota(r)|<\varepsilon$. Como $\iota(y_n)=\widetilde y_n$, esto afirma $\widetilde y_n\to\iota(r)$ en $\mathbb R$. Pero §7.6 ya dio $\widetilde y_n\to L$. La unicidad del límite real de C06 obligaría a $\iota(r)=L$, contradiciendo que $L$ no pertenece a la imagen de $\mathbb Q$. Por tanto no existe tal límite racional.

### 54. Solución

[]{#MA-MIC-ANM-01-007-054}

[]{#MA-MSOL-ANM-01-007-054}

Fija $r\in\mathbb Q$. La irracionalidad de $L$ implica $L\ne\iota(r)$, luego $d=|L-\iota(r)|>0$. Elige la tolerancia fija $\varepsilon_0=d/2$. Como $\widetilde y_n\to L$, existe $T\in\mathbb N$ con $|\widetilde y_n-L|<d/2$ para todo $n\ge T$. La desigualdad triangular da

$$
|\widetilde y_n-\iota(r)|\ge d-|L-\widetilde y_n|>d/2.
$$

Ante cualquier corte propuesto $K$, toma $n=\max\{K,T\}$. Este índice es al menos $K$ y su error supera $\varepsilon_0$, refutando la condición de límite para ese corte. La tolerancia y $T$ pueden depender de $r$; el índice infractor se elige después de conocer $K$.

### 55. Solución

[]{#MA-MIC-ANM-01-007-055}

[]{#MA-MSOL-ANM-01-007-055}

Los cuatro puntos representan sólo cuatro evaluaciones exactas y permiten comparar esos valores. La inducción acredita racionalidad, positividad e invariantes en todos los índices; con ellos se obtienen descenso y cotas. El teorema monótono garantiza un límite real, las reglas de C06 lo identifican y la paridad prueba su irracionalidad. La ampliación cambia la escala de representación, no los valores ni la función: no puede convertir $L$ en un término. En cada índice, $\widetilde y_n>L$ por §7.6; además, los términos están en la imagen de $\mathbb Q$ y $L$ no pertenece a ella.

### 56. Solución

[]{#MA-MIC-ANM-01-007-056}

[]{#MA-MSOL-ANM-01-007-056}

La completitud real se usa al aplicar §7.4: garantiza que el conjunto real no vacío de valores, acotado inferiormente, tenga un ínfimo $L\in\mathbb R$; la monotonía permite demostrar después la convergencia a ese extremo. Dentro de $\mathbb Q$ se ejecutan la construcción recursiva, los inversos de términos no nulos, la inducción de racionalidad y positividad, la identidad cuadrática, las comparaciones, el descenso y las cotas racionales 1 y 2. La paridad excluye cualquier racional cuyo cuadrado sea 2. Así, $y:\mathbb N\to\mathbb Q$ es monótona y acotada pero carece de límite racional, mientras que $\widetilde y:\mathbb N\to\mathbb R$ converge al real positivo $L=\sqrt2$. El conjunto de candidatos permitidos cambia, aunque los índices y valores correspondientes se conservan.

## §7.8 — Elegir el argumento y declarar su alcance

### 57. Solución

[]{#MA-MIC-ANM-01-007-057}

[]{#MA-MSOL-ANM-01-007-057}

[]{#MA-SEC-ANM-01-007-008}

Comprobar un candidato $A\in\mathbb R$ exige que, para cada $\varepsilon>0$, un corte controle $|a_n-A|<\varepsilon$ en todos los índices posteriores: sirve la definición de C06. Garantizar existencia sin candidato previo requiere construir algún límite; para una sucesión real no decreciente con cota superior, §7.3 lo obtiene como supremo, y para una no creciente con cota inferior, §7.4 lo obtiene como ínfimo. Identificar un límite existente exige determinar su valor: pueden usarse las propiedades del extremo o las reglas de C06 y la unicidad, comprobando previamente las hipótesis de cada operación.

### 58. Solución

[]{#MA-MIC-ANM-01-007-058}

[]{#MA-MSOL-ANM-01-007-058}

Por la definición, $|x_n-1|=1/(n+1)$. Dado $\varepsilon>0$, elige por arquimedianidad $N\in\mathbb N$ con $N>1/\varepsilon$. Para todo $n\ge N$, se tiene $n+1>1/\varepsilon$, luego $|x_n-1|<\varepsilon$; así $x_n\to1$.

Por orden, $x_{n+1}-x_n=1/[(n+1)(n+2)]>0$ y $x_n<1$. El teorema de §7.3 usa completitud para obtener convergencia a $s=\sup S_x$. Si $B<1$, elige un natural $m>1/(1-B)$; entonces $1/(m+1)<1-B$ y $x_m>B$. Ningún $B<1$ es cota superior, mientras que 1 sí lo es, de modo que $s=1$. La primera ruta basta con el control arquimediano del error; esa propiedad ya fue deducida de completitud en C03, por lo que no se afirma independencia de ella.

### 59. Solución

[]{#MA-MIC-ANM-01-007-059}

[]{#MA-MSOL-ANM-01-007-059}

Una vez probado $x_n\to1$, las reglas de escalar y suma de C06 §6.6, junto con la constante de valor $-3$, dan $2x_n-3\to2\cdot1-3=-1$. Sus hipótesis de convergencia están acreditadas. En cambio, pasar al límite en una recurrencia presupone que ese límite existe y que las operaciones están admitidas. Resolver la ecuación resultante sólo identifica candidatos necesarios. Por ejemplo, $w_{n+1}=-w_n$, $w_0=1$, impone $W=-W$ y $W=0$ bajo una suposición de convergencia, pero $w_n=(-1)^n$ no converge.

### 60. Solución

[]{#MA-MIC-ANM-01-007-060}

[]{#MA-MSOL-ANM-01-007-060}

La restricción de $a$ tiene dominio $D=\{n\in\mathbb N:n\ge1\}$ y codominio $\mathbb R$. La reindexación $c:\mathbb N\to\mathbb R$ tiene regla $c_k=a_{1+k}=1-1/(k+1)=x_k$. Como $c$ y $x$ comparten dominio, codominio y cada evaluación, son la misma función. Si $K$ controla el error de $c$ para una tolerancia dada, toma $N=1+K$ para $a$. Para $n\ge N$, el natural $k=n-1$ satisface $k\ge K$ y $|a_n-1|=|c_k-1|$, trasladando el mismo control.

### 61. Solución

[]{#MA-MIC-ANM-01-007-061}

[]{#MA-MSOL-ANM-01-007-061}

El conjunto global $S_a$ contiene 10 y todos los demás términos son menores que 1; por eso $\sup S_a=10$. El conjunto de cola $S_{a,1}=\{a_n:n\ge1\}$ coincide con $S_x$, luego $\sup S_{a,1}=1$. La sucesión original converge a 1 por transferencia desde esa cola. La conclusión correcta es: si la cola desde $T$ es no decreciente y está acotada superiormente en $\mathbb R$, entonces el límite de la sucesión original es $\sup S_{a,T}$. No se sustituye ese conjunto por el global, que conserva el prefijo.

### 62. Solución

[]{#MA-MIC-ANM-01-007-062}

[]{#MA-MSOL-ANM-01-007-062}

$d_n=(-1)^n$ está acotada, pero carece de monotonía incluso eventual: después de cualquier corte aparecen pasos de 1 a $-1$ y de $-1$ a 1. §7.5 ya refutó todos sus candidatos reales, así que no converge. $e_n=(-1)^n/(n+1)$ también carece de monotonía eventual, por pasos alternos de positivo a negativo y de negativo a positivo; sin embargo, C06 acredita $e_n\to0$ mediante el error $1/(n+1)$. En ambos casos falta la dirección exigida para aplicar el teorema monótono; esa falla no decide por sí sola la convergencia.

Para $a_n=n$ sí hay no decrecimiento y cota inferior 0, pero falta la cota superior pertinente. Por arquimedianidad, dada una barrera real $M$, existe $N>M$ y todo $n\ge N$ satisface $a_n=n>M$. Es el escape por arriba de §7.5, que excluye un límite real sin incorporar un infinito al codominio.

### 63. Solución

[]{#MA-MIC-ANM-01-007-063}

[]{#MA-MSOL-ANM-01-007-063}

Para dividir por $y_n$, la inducción de positividad prueba $y_n>0$, luego $y_n\ne0$, antes de cada paso recursivo. Para garantizar un límite real, el invariante $y_n^2>2$ y la positividad permiten demostrar descenso y la cota inferior 1; §7.4 se aplica a esa sucesión no creciente y acotada inferiormente. Para dividir por $L$, se necesita una obligación distinta: una vez acreditado $y_n\to L$, el orden de límites aplicado a $1\le y_n\le2$ da $1\le L\le2$, luego $L\ne0$. Junto con la convergencia y los denominadores no nulos, ese margen habilita la regla del cociente para $2/y_n\to2/L$.

### 64. Solución

[]{#MA-MIC-ANM-01-007-064}

[]{#MA-MSOL-ANM-01-007-064}

La construcción racional es $y:\mathbb N\to\mathbb Q$; la inclusión es $\iota:\mathbb Q\to\mathbb R$ y su composición es $\widetilde y=\iota\circ y:\mathbb N\to\mathbb R$. Comparten índices y valores correspondientes, pero se distinguen por el codominio. El candidato de un límite racional debe pertenecer a $\mathbb Q$; el de un límite real pertenece a $\mathbb R$.

En una prueba de convergencia a un candidato fijo $A$, se fija primero $\varepsilon>0$ y se elige $N$ que puede depender de $\varepsilon$, de $A$ y de la sucesión, pero no del índice posterior $n$; después se controla todo $n\ge N$. En una prueba de escape, se fija la barrera real $M$ y se elige un corte $N$ que puede depender de ella, para controlar todos los índices posteriores. Para refutar un candidato fijo $A$, se elige una tolerancia $\varepsilon_0>0$ que puede depender de $A$; ante cada corte propuesto $K$, se encuentra un índice $n\ge K$, dependiente de $K$, con $|a_n-A|\ge\varepsilon_0$. La tolerancia se mantiene fija al variar $K$. En el caso racional, el error se escribe $|\iota(y_n)-\iota(r)|$ para $r\in\mathbb Q$.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 7](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html) · [Ejercicios](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-microcontroles.html)
