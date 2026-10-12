---
content-id: MA-BCH-0231
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-007-EJERCICIOS
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
title: Ejercicios — Capítulo 7
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C07_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 7](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html) · [Ejercicios](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-microcontroles.html)

Se conserva $\mathbb N=\{0,1,2,\ldots\}$. Los ejercicios utilizan las herramientas disponibles hasta su sección. Justifica las propiedades de las funciones completas y declara los dominios al construir nuevos objetos.

## §7.1

### 1. Comparaciones y alcance de los cuantificadores

[]{#MA-EX-ANM-01-007-001}

[]{#MA-SOL-ANM-01-007-001}

[]{#MA-SEC-ANM-01-007-001}

Para una sucesión $a:\mathbb N\to\mathbb R$, considera estas afirmaciones:

- $P$: para todo $n\in\mathbb N$, $a_n\le a_{n+1}$.
- $Q$: para todos $n,m\in\mathbb N$, si $n\le m$, entonces $a_n\le a_m$.
- $R$: para todo $n\in\mathbb N$, $a_n<a_{n+1}$.
- $S$: para todos $n,m\in\mathbb N$, si $n<m$, entonces $a_n<a_m$.
- $M$: $(\forall n\in\mathbb N,\ a_n\le a_{n+1})\ \lor\ (\forall n\in\mathbb N,\ a_{n+1}\le a_n)$.
- $V$: para todo $n\in\mathbb N$, $a_n\le a_{n+1}\ \lor\ a_{n+1}\le a_n$.

Demuestra $P\Leftrightarrow Q$ y $R\Leftrightarrow S$, y explica el cambio de $n\le m$ a $n<m$. Determina cuáles caracterizan el no decrecimiento y cuáles el crecimiento estricto. Justifica $R\Rightarrow P$ y refuta la implicación inversa con una constante. ¿Qué propiedad expresa $M$? Decide si $M$ y $V$ son equivalentes, justificando tu respuesta con un ejemplo cuando haga falta. En las comparaciones, distingue índices y términos.

### 2. Las mismas alturas en otro orden

[]{#MA-EX-ANM-01-007-002}

[]{#MA-SOL-ANM-01-007-002}

Sea $E=\{2j:j\in\mathbb N\}\subseteq\mathbb R$. Construye dos funciones $a,b:\mathbb N\to\mathbb R$ cuyo conjunto de valores sea $E$: una estrictamente creciente y otra que no sea monótona. Puedes partir de la enumeración natural de $E$ e intercambiar vecinos. Define ambas para todos los índices, prueba las dos igualdades de conjuntos y acredita cada afirmación sobre dirección. Explica por qué $a(\mathbb N)=b(\mathbb N)$ no implica $a=b$ ni igualdad de sus gráficas discretas.

### 3. Bloques de longitud variable

[]{#MA-EX-ANM-01-007-003}

[]{#MA-SOL-ANM-01-007-003}

Fija $m\in\mathbb N$ con $m\ge2$. Construye una sucesión $a^{(m)}:\mathbb N\to\mathbb R$ que tome el valor $k$ exactamente en los $m$ índices del bloque $mk,mk+1,\ldots,mk+m-1$, para cada $k\in\mathbb N$. Justifica que la regla asigna un único valor a cada índice. Demuestra el no decrecimiento distinguiendo el interior de un bloque de su frontera y prueba que los valores no tienen cota superior real. Decide si la sucesión es estrictamente creciente o no creciente, y explica por qué las repeticiones no impiden que sea función.

### 4. Una suma que no cambia

[]{#MA-EX-ANM-01-007-004}

[]{#MA-SOL-ANM-01-007-004}

Sean $a,b:\mathbb N\to\mathbb R$ dos sucesiones no decrecientes y sea $c\in\mathbb R$. Supón que $a_n+b_n=c$ para todo $n\in\mathbb N$. Demuestra que cada sucesión es constante. Localiza dónde se usa la dirección común. Si se sustituye esa hipótesis por «cada sucesión es monótona, con direcciones posiblemente distintas», decide si la conclusión sigue siendo válida y justifica tu decisión. ¿Las hipótesis originales obligan además a que $a=b$ como funciones?

## §7.2

### 5. Cota, barrera mínima y posición de alcanzamiento

[]{#MA-EX-ANM-01-007-005}

[]{#MA-SOL-ANM-01-007-005}

[]{#MA-SEC-ANM-01-007-002}

Sean $a:\mathbb N\to\mathbb R$, $S_a=a(\mathbb N)$ y $U,s\in\mathbb R$. Justifica la equivalencia entre $a_n\le U$ para todo $n$, $S_a\subseteq(-\infty,U]$ y $S_a\cap(U,\infty)=\varnothing$. Escribe con cuantificadores qué obligación adicional convierte una cota $s$ en $\sup S_a$. Demuestra que $s$ es máximo de $S_a$ si y sólo si es su supremo y el conjunto de índices $I_s=\{j\in\mathbb N:a_j=s\}$ es no vacío.

Aplica estas distinciones a $d_0=-1$ y $d_n=4$ para $n\ge1$: determina $S_d$, clasifica la cota superior 6, calcula el supremo y el máximo, y describe $I_4$. Distingue el tipo del número 4, del conjunto de valores, del conjunto de índices y de la función $d$.

### 6. Una barrera prescrita, con y sin alcanzamiento

[]{#MA-EX-ANM-01-007-006}

[]{#MA-SOL-ANM-01-007-006}

Para cada $s\in\mathbb R$ y $h\ge0$, construye dos sucesiones reales $a^{s,h}$ y $b^{s,h}$ con todos sus términos en $[s-h,s]$ y con supremo del conjunto de valores igual a $s$. Si $h>0$, exige que la primera no alcance $s$ y que la segunda lo alcance en un único índice. Si $h=0$, determina qué funciones permite la condición sobre el intervalo y qué ocurre con el alcanzamiento. Verifica cota y aproximación para tus construcciones y declara sus dominios; no necesitas calcular límites.

### 7. Aproximar con una escala numerable

[]{#MA-EX-ANM-01-007-007}

[]{#MA-SOL-ANM-01-007-007}

Supón que $a:\mathbb N\to\mathbb R$ y que $s\in\mathbb R$ es cota superior de $S_a$. Demuestra que $s=\sup S_a$ equivale a la condición

$$
\forall k\in\mathbb N\ \exists j\in\mathbb N:\quad 0\le s-a_j<\frac1{k+1}.
$$

Señala cómo se pasa de una tolerancia real arbitraria a una de las tolerancias indicadas y de qué dato puede depender el índice $j$. Decide si la condición mostrada, por sí sola, seguiría caracterizando el supremo al omitir la hipótesis global de cota. No uses el teorema de convergencia monótona.

### 8. Igual imagen acotada, distinto comportamiento

[]{#MA-EX-ANM-01-007-008}

[]{#MA-SOL-ANM-01-007-008}

Sea $E=\{0\}\cup\{1/(j+1):j\in\mathbb N\}$. Construye $a,b:\mathbb N\to\mathbb R$ con $a(\mathbb N)=b(\mathbb N)=E$, tales que $a$ converja a 0 y $b$ no converja a ningún real. Puedes cambiar cuántas veces aparece cada valor. Prueba la igualdad de ambas imágenes, da cotas comunes y justifica las afirmaciones de convergencia desde los cuantificadores de C06. Explica por qué tu construcción no representa una permutación biyectiva de los índices de la sucesión convergente.

### 9. Un testigo convertido indebidamente en corte

[]{#MA-EX-ANM-01-007-009}

[]{#MA-SOL-ANM-01-007-009}

La siguiente es una **prueba defectuosa**: «Como $s=\sup S_a$, para cada $\varepsilon>0$ hay un índice $j$ con $s-\varepsilon<a_j\le s$. Tomo $N=j$; entonces $|a_n-s|<\varepsilon$ para todo $n\ge N$, y por tanto $a_n\to s$».

Localiza la inferencia sin justificación y compara los cuantificadores de la premisa con los de la conclusión. Refútala mediante una sucesión cuyo supremo sea 3, no se alcance y para la que el candidato 3 falle como límite. Construye la sucesión usando, para cada $k\in\mathbb N$, tres posiciones consecutivas: un valor que se aproxime a 3, un valor 0 y un valor 1. Justifica el supremo y da una tolerancia fija con un infractor posterior a cada corte. Repara después el argumento general incorporando una hipótesis de comparación entre términos que permita usar §7.1; demuestra el paso reparado directamente, sin invocar el teorema de §7.3.

## §7.3

### 10. Reensamblar el argumento y localizar las hipótesis

[]{#MA-EX-ANM-01-007-010}

[]{#MA-SOL-ANM-01-007-010}

[]{#MA-SEC-ANM-01-007-003}

Sea $a:\mathbb N\to\mathbb R$ no decreciente y supón que $a_n\le U$ para todo $n$, con $U\in\mathbb R$. Los siguientes fragmentos de prueba están desordenados:

- A: para todo $n\ge N$, $s-\varepsilon<a_N\le a_n\le s$; por tanto $|a_n-s|<\varepsilon$.
- B: se forma $S_a=\{a_n:n\in\mathbb N\}$ y se verifica que es no vacío y acotado superiormente.
- C: dada $\varepsilon>0$, se obtiene un índice $N$ con $s-\varepsilon<a_N$.
- D: existe un real $s=\sup S_a$.

Ordénalos, completa sus justificaciones e identifica qué dato o hipótesis autoriza cada paso. Distingue el papel de $U$ del de $s$, y registra el orden en que se fijan $s$, $\varepsilon$, $N$ y $n$. Para $w_n=2-1/(n+1)$, acredita las hipótesis y el supremo, y comprueba que $N=0$ sirve con tolerancia 2. Decide si sigue sirviendo con tolerancia 1 y proporciona un corte válido en ese caso.

### 11. Una familia con denominador desplazado

[]{#MA-EX-ANM-01-007-011}

[]{#MA-SOL-ANM-01-007-011}

Sean $\alpha,\beta,q\in\mathbb R$, con $\beta\ge0$ y $q>0$. Estudia la sucesión $a_n=\alpha-\beta/(n+q)$ para $n\in\mathbb N$: verifica su buena definición, dirección, cotas y existencia de límite mediante §7.3. Identifica después su supremo y su límite. Separa $\beta=0$ de $\beta>0$, indica cuándo la dirección es estricta y justifica la elección de un índice para cada tolerancia. Explica por qué hay que controlar el denominador también en $n=0$.

### 12. Reconocer el supremo desde un límite ya conocido

[]{#MA-EX-ANM-01-007-012}

[]{#MA-SOL-ANM-01-007-012}

Sea $a:\mathbb N\to\mathbb R$ no decreciente y supón que $a_n\to L\in\mathbb R$. Sin aplicar el teorema de §7.3 para obtener una cota, demuestra que $a_k\le L$ para todo $k\in\mathbb N$. Usa esa cota y la convergencia para demostrar que $L=\sup S_a$. En el primer paso, explica cómo se coordina un índice $k$ previamente fijado con un corte de convergencia elegido después de una tolerancia. ¿Hace falta suponer de entrada una cota superior adicional?

### 13. Recuperar la desigualdad estricta

[]{#MA-EX-ANM-01-007-013}

[]{#MA-SOL-ANM-01-007-013}

Supón que $a:\mathbb N\to\mathbb R$ es no decreciente, que $s\in\mathbb R$ domina todos sus términos y que para cada $\delta>0$ puedes obtener un índice $N_\delta$ con $s-\delta\le a_{N_\delta}$. Adapta la prueba ε–N para concluir $a_n\to s$, aunque el testigo sólo dé una desigualdad no estricta. Justifica también que $s=\sup S_a$. Explica por qué usar $\delta=\varepsilon$ y conservar cualquier testigo recibido no garantiza el error estricto; ilústralo con una sucesión no decreciente cuyo supremo sea 0, tolerancia 1 y testigo inicial situado en la frontera. Da una elección auxiliar que repare la prueba para toda tolerancia, no sólo para ese ejemplo.

### 14. Sumar valores con el mismo índice

[]{#MA-EX-ANM-01-007-014}

[]{#MA-SOL-ANM-01-007-014}

Sean $a,b:\mathbb N\to\mathbb R$ no decrecientes y acotadas superiormente. Escribe $s=\sup S_a$ y $t=\sup S_b$, y define $c_n=a_n+b_n$. Demuestra que $\sup S_c=s+t$, coordinando los testigos de aproximación de ambas sucesiones. Verifica las hipótesis de §7.3 para $c$ y deduce su límite.

Distingue $S_c=\{a_n+b_n:n\in\mathbb N\}$ del conjunto $T=\{x+y:x\in S_a,\ y\in S_b\}$. ¿Son necesariamente iguales? Justifica la inclusión que siempre vale y construye un ejemplo con las hipótesis indicadas en el que la inclusión sea estricta.

### 15. Promedios finitos que conservan el destino

[]{#MA-EX-ANM-01-007-015}

[]{#MA-SOL-ANM-01-007-015}

Sea $a:\mathbb N\to\mathbb R$ no decreciente y acotada superiormente. Define $s=\sup S_a$ y la sucesión de promedios finitos $c_n=(a_0+\cdots+a_n)/(n+1)$. Prueba que está definida, que $a_0\le c_n\le a_n\le s$ y que no decrece. Obtén la existencia de su límite con §7.3 y demuestra que ese límite coincide con el de $a$.

Para identificarlo, compara los términos de un bloque final con un término $a_K$ previamente fijado y separa la contribución de los $K$ términos anteriores. Controla el error desde la definición ε–N, incluido el caso $K=0$. No invoques un teorema general sobre promedios de sucesiones convergentes ni teoría de series.

## §7.4

### 16. Reflexión con una altura de referencia

[]{#MA-EX-ANM-01-007-016}

[]{#MA-SOL-ANM-01-007-016}

[]{#MA-SEC-ANM-01-007-004}

Sean $a:\mathbb N\to\mathbb R$ y $c\in\mathbb R$ fijo. Define $b_n=c-a_n$. Describe el dominio, codominio y conjunto de valores de $b$, y demuestra las equivalencias que transportan no decrecimiento a no crecimiento y viceversa. Transporta una cota inferior $\ell$ y una superior $U$ de $a$. Cuando los extremos correspondientes existan, prueba $\sup S_b=c-\inf S_a$ y $\inf S_b=c-\sup S_a$.

Si $a_n\to L$, identifica el límite de $b$ mediante una igualdad de errores. Describe qué cambia en los puntos de la gráfica y qué se conserva en sus coordenadas de índice. ¿Las funciones $a$ y $b$ son necesariamente iguales?

### 17. Un prefijo arbitrario y una barrera no alcanzada

[]{#MA-EX-ANM-01-007-017}

[]{#MA-SOL-ANM-01-007-017}

Fija $T\in\mathbb N$, $L\in\mathbb R$, $h>0$ y datos reales $x_0,\ldots,x_{T-1}$, entendiendo que no hay datos si $T=0$. Construye una sucesión $a:\mathbb N\to\mathbb R$ con ese prefijo y una cola cuyo término de posición reindexada $k$ esté a distancia $h/(k+1)$ por debajo de $L$.

Define la restricción a $D_T=\{n\in\mathbb N:n\ge T\}$ y la sucesión reindexada. Comprueba la dirección y el supremo de la cola, determina el límite de $a$ y calcula el supremo global. Si $T>0$, clasifica el alcanzamiento según el máximo del prefijo sea menor, igual o mayor que $L$. Trata también $T=0$, sin tomar el máximo de un conjunto vacío.

### 18. Incorporar el prefijo a los extremos

[]{#MA-EX-ANM-01-007-018}

[]{#MA-SOL-ANM-01-007-018}

Sea $a:\mathbb N\to\mathbb R$ y sea $T\in\mathbb N$. Supón que $Q=\{a_n:n\ge T\}$ está acotado por ambos lados y escribe $s=\sup Q$, $t=\inf Q$ y $P=\{a_n:n<T\}$. Prueba que

$$
\sup S_a=\max\bigl(\{s\}\cup P\bigr),
\qquad
\inf S_a=\min\bigl(\{t\}\cup P\bigr).
$$

Justifica que las expresiones están definidas y demuestra sus propiedades extremales, no sólo que proporcionan cotas. Explica el caso $T=0$ y por qué no hace falta que la cola sea monótona. Distingue los conjuntos $P,Q$ de sus extremos reales, que pueden no pertenecer a $Q$.

### 19. Dos extensiones de la misma cola

[]{#MA-EX-ANM-01-007-019}

[]{#MA-SOL-ANM-01-007-019}

Sea $u:\mathbb N\to\mathbb R$ una sucesión monótona y acotada por ambos lados. Fija $T\in\mathbb N$ con $T\ge2$. Construye $a,b:\mathbb N\to\mathbb R$ tales que $a_{T+k}=b_{T+k}=u_k$ para todo $k\in\mathbb N$, con $a$ globalmente monótona y $b$ globalmente no monótona. La construcción debe servir también cuando $u$ sea constante.

Verifica todas las comparaciones de los prefijos y las fronteras necesarias, demuestra que ambas extensiones tienen el mismo límite e identifica ese límite según la dirección de $u$. Explica por qué un único término de prefijo no permitiría garantizar la construcción de $b$ para toda cola constante. Distingue igualdad de cola, igualdad de límite e igualdad de funciones.

### 20. Mínimo y máximo de dos colas alineadas

[]{#MA-EX-ANM-01-007-020}

[]{#MA-SOL-ANM-01-007-020}

Sean $a,b:\mathbb N\to\mathbb R$ eventualmente no decrecientes y acotadas superiormente. Define $m_n=\min\{a_n,b_n\}$ y $M_n=\max\{a_n,b_n\}$. Demuestra que ambas sucesiones son eventualmente no decrecientes y tienen cota superior, y determina sus límites en términos de los límites de $a$ y $b$.

Reúne los cortes de monotonía, reindexa las dos colas desde un corte común y usa aproximaciones a sus supremos para identificar los supremos de los valores alineados de mínimo y máximo. Justifica la transferencia a las funciones originales. No uses continuidad de mínimo o máximo ni fórmulas de límites que se hayan supuesto antes de acreditar existencia.

## §7.5

### 21. Superar una barrera y controlar una cola

[]{#MA-EX-ANM-01-007-021}

[]{#MA-SOL-ANM-01-007-021}

[]{#MA-SEC-ANM-01-007-005}

Para $a:\mathbb N\to\mathbb R$, escribe con todos sus dominios estas cuatro afirmaciones: no tiene cota superior, escapa eventualmente por arriba, no tiene cota inferior y escapa eventualmente por abajo. Obtén las negaciones de las dos afirmaciones de escape. Compara las obligaciones sobre índices en ausencia de cota y en escape, e indica qué propiedad de comparación permite pasar de una a otra en cada dirección.

Demuestra que escape implica ausencia de la cota correspondiente. ¿Puede el corte de escape depender de la barrera real? ¿Podría existir un único corte válido para todas las barreras? Explica por qué los cuantificadores deben incluir barreras de ambos signos.

### 22. Valores grandes con retornos arbitrariamente tardíos

[]{#MA-EX-ANM-01-007-022}

[]{#MA-SOL-ANM-01-007-022}

Fijado $r\in\mathbb R$, construye $a:\mathbb N\to\mathbb R$ sin cota superior que vuelva al valor $r$ después de cualquier corte. Da una definición completa por paridades y justifica ambas propiedades con sus cuantificadores. Refuta el escape eventual por arriba mediante una barrera real explícita y un índice infractor construido después de cada corte. ¿Qué paso de la prueba de escape monótono queda sin justificación en tu ejemplo? No uses resultados sobre subsucesiones.

### 23. Dos garantías de convergencia defectuosas

[]{#MA-EX-ANM-01-007-023}

[]{#MA-SOL-ANM-01-007-023}

Audita estas dos afirmaciones defectuosas:

1. «Si una sucesión real no decrece y tiene cota inferior, entonces converge a un real por el teorema monótono».
2. «Si todos los términos de una sucesión real están en un intervalo cerrado acotado, entonces converge a un real».

Refuta la primera con una familia de la forma $r+hn$, donde $r\in\mathbb R$ y $h>0$. Refuta la segunda mediante una sucesión periódica de tres valores distintos en $[r-h,r+h]$, excluyendo todos los candidatos reales a límite. Identifica la hipótesis ausente y formula una reparación suficiente para cada afirmación. Explica por qué la falta de una garantía no permite declarar divergente a toda sucesión que no sea eventualmente monótona; construye una familia convergente que lo demuestre y verifica su convergencia y sus infractores de dirección.

### 24. Una tolerancia de refutación prescrita

[]{#MA-EX-ANM-01-007-024}

[]{#MA-SOL-ANM-01-007-024}

Fija de antemano $\varepsilon_0>0$. Supón que $a:\mathbb N\to\mathbb R$ escapa eventualmente por arriba. Para cada candidato $A\in\mathbb R$, usa la barrera $A+\varepsilon_0$ para construir, después de cualquier corte propuesto $K\in\mathbb N$, un índice $n\ge K$ con $|a_n-A|\ge\varepsilon_0$. Formula y demuestra la versión de escape por abajo con la barrera $A-\varepsilon_0$.

Registra el orden de los datos y elecciones, y concluye la ausencia de límite real en ambos casos. ¿La refutación exige error estrictamente mayor que la tolerancia o también admite igualdad? ¿Necesitas monotonía una vez que el escape ya está acreditado?

### 25. Escape y monotonía eventual no son conversas

[]{#MA-EX-ANM-01-007-025}

[]{#MA-SOL-ANM-01-007-025}

Para cada $c\in\mathbb R$, define $a^{(c)}_n=n+c(-1)^n$ en $\mathbb N$. Demuestra el escape eventual por arriba para todo parámetro y clasifica cuándo la sucesión es no decreciente o estrictamente creciente. Decide si puede ser no creciente, y si las clasificaciones cambian al exigir las propiedades sólo eventualmente.

Trata los valores frontera $c=1/2$ y $c=-1/2$, indicando dónde hay pasos de igualdad. Para los parámetros fuera del intervalo que admite no decrecimiento, construye después de cualquier corte infractores de ambas direcciones. Usa la familia para decidir si el escape eventual por arriba implica monotonía eventual, y distingue ese escape de la convergencia a un número real.

## §7.6

### 26. Una combinación que conserva el lado de una barrera

[]{#MA-EX-ANM-01-007-026}

[]{#MA-SOL-ANM-01-007-026}

[]{#MA-SEC-ANM-01-007-006}

Sean $c,r\in\mathbb R$ y $0<\lambda<1$. Define $v:\mathbb N\to\mathbb R$ por $v_0=r$ y $v_{n+1}=\lambda v_n+(1-\lambda)c$. Estudia por separado $r<c$, $r>c$ y $r=c$: buena definición, posición respecto de $c$, dirección, cotas y existencia de límite. Identifica después ese límite usando la recurrencia. No necesitas obtener una fórmula geométrica para $v_n$.

### 27. Una ecuación necesaria presentada como garantía

[]{#MA-EX-ANM-01-007-027}

[]{#MA-SOL-ANM-01-007-027}

Sean $c\in\mathbb R$ y $h>0$. Se prescribe $a_0=c+h$ y $a_{n+1}=2c-a_n$. Audita el razonamiento: «La ecuación del límite es $A=2c-A$; tiene la única solución $A=c$, de modo que $a_n\to c$». Localiza la obligación omitida, determina todos los términos y refuta la convergencia a cualquier real mediante una tolerancia explícita y un índice posterior a cualquier corte. ¿Qué cambiaría con dato inicial $a_0=c$?

### 28. Descenso desde un dato inicial variable

[]{#MA-EX-ANM-01-007-028}

[]{#MA-SOL-ANM-01-007-028}

Sea $r\in\mathbb R$ con $r>0$ y $r^2>2$. Para $y_0=r$ y $y_{n+1}=(y_n+2/y_n)/2$, demuestra que la prescripción define $y:\mathbb N\to\mathbb R$. Reconstruye la conservación estricta de $y_n^2>2$, una cota inferior positiva conocida y el descenso. Demuestra la existencia de límite antes de calcularlo, identifica su destino y decide si algún término puede alcanzarlo. No deduzcas propiedades universales de una tabla de valores.

### 29. Cruzar la barrera en el primer paso

[]{#MA-EX-ANM-01-007-029}

[]{#MA-SOL-ANM-01-007-029}

Mantén la recurrencia del ejercicio 28 y toma ahora $r>0$. Resuelve los casos $r^2<2$ y $r^2=2$. En el primer caso, sitúa el primer término respecto de $r$ y de la raíz positiva de 2, determina la dirección desde el índice 1 y justifica la existencia y el destino del límite. Decide si la sucesión completa es monótona. En el segundo caso, prueba que la sucesión es constante. Reúne estos casos con el ejercicio 28 para clasificar todos los datos iniciales positivos.

### 30. Construir la raíz de un parámetro positivo

[]{#MA-EX-ANM-01-007-030}

[]{#MA-SOL-ANM-01-007-030}

Sean $\rho>0$ y $r>0$ reales con $r^2>\rho$. Define $x_0=r$ y $x_{n+1}=(x_n+\rho/x_n)/2$. Construye la sucesión, conserva una desigualdad cuadrática estricta y deduce descenso. Justifica la cota inferior $m=\min\{1,\rho\}>0$ sin presuponer una raíz de $\rho$. Obtén existencia de límite, comprueba su no anulación antes de usar cocientes y demuestra que es el único real positivo cuyo cuadrado es $\rho$. Sitúa cada término respecto de ese límite.

### 31. Datos negativos y una prescripción que no define sucesión

[]{#MA-EX-ANM-01-007-031}

[]{#MA-SOL-ANM-01-007-031}

Para la prescripción $y_0=r$, $y_{n+1}=(y_n+2/y_n)/2$, considera todos los datos reales $r<0$ y el dato $r=0$. En el caso negativo, construye una sucesión positiva auxiliar por reflexión y clasifica posición, dirección y límite según $r^2>2$, $r^2<2$ y $r^2=2$. Distingue dirección global de dirección desde el índice 1. En el caso cero, identifica el primer paso que falla y explica por qué no corresponde llamar divergente a una sucesión definida por esta prescripción.

### 32. Dos trayectorias ordenadas con un destino común

[]{#MA-EX-ANM-01-007-032}

[]{#MA-SOL-ANM-01-007-032}

Sea $R>0$ la raíz de 2 ya construida en §7.6, y sean $R<r<s$. Define dos sucesiones $y,z:\mathbb N\to\mathbb R$ con datos iniciales $y_0=r$, $z_0=s$ y la regla del ejercicio 28. Para la función de paso $F:(0,\infty)\to(0,\infty)$, $F(t)=(t+2/t)/2$, deriva

$$
F(x)-F(t)=\frac{x-t}{2}\left(1-\frac{2}{xt}\right).
$$

Determina el signo relevante cuando $x,t>R$ y demuestra que $y_n<z_n$ para todo índice. Justifica que ambas sucesiones tienen el mismo límite y, sin embargo, son funciones distintas. ¿Qué ocurre si $r=s$? No estimes velocidades de aproximación.

## §7.7

### 33. Una iteración racional y su inclusión real

[]{#MA-EX-ANM-01-007-033}

[]{#MA-SOL-ANM-01-007-033}

[]{#MA-SEC-ANM-01-007-007}

Sean $\rho,r\in\mathbb Q$ con $\rho>0$, $r>0$ y $r^2>\rho$. Construye en $\mathbb Q$ la iteración $q_0=r$, $q_{n+1}=(q_n+\rho/q_n)/2$. Declara los tipos de $q$, de la inclusión $\iota:\mathbb Q\to\mathbb R$ y de $\widetilde q=\iota\circ q$. Justifica racionalidad, positividad, invariante cuadrático y dirección; explica qué conserva la inclusión. Demuestra que $\widetilde q$ coincide como función real con la iteración de parámetros $\iota(\rho),\iota(r)$ del ejercicio 30 y declara su límite real. ¿Se ha demostrado con ello que ese límite sea racional?

### 34. Una nueva ecuación y la misma obstrucción de paridad

[]{#MA-EX-ANM-01-007-034}

[]{#MA-SOL-ANM-01-007-034}

Construye $q:\mathbb N\to\mathbb Q$ mediante $q_0=3$ y $q_{n+1}=(q_n+8/q_n)/2$. Usa el ejercicio 33 para acreditar un límite real positivo $L$ de $\widetilde q=\iota\circ q$ con $L^2=8$. Demuestra que $L$ no pertenece a $\iota(\mathbb Q)$ reduciendo la ecuación a un cuadrado igual a 2 y reconstruyendo la contradicción de paridad. Deduce que $q$ no tiene límite racional. No importes una teoría nueva de divisibilidad.

### 35. Dos destinos para sucesiones de términos racionales

[]{#MA-EX-ANM-01-007-035}

[]{#MA-SOL-ANM-01-007-035}

Se afirma: «Como todos los términos de una sucesión pertenecen a $\mathbb Q$, su límite real, si existe, pertenece a $\mathbb Q$». Se propone además la corrección: «Si todos los términos son racionales y ninguno alcanza el límite, entonces éste es irracional». Audita ambas afirmaciones comparando estas construcciones en $\mathbb Q$:

$$
u_0=0,\quad u_{n+1}=\frac{u_n+1}{2};\qquad
q_0=3,\quad q_{n+1}=\frac{q_n+8/q_n}{2}.
$$

Justifica su buena definición racional, sus límites después de la inclusión real y el no alcanzamiento de esos límites. Explica qué permite y qué no permite concluir el codominio racional de los términos. Distingue la existencia de límite real de la existencia de límite racional.

### 36. Excluir candidatos con tolerancias racionales

[]{#MA-EX-ANM-01-007-036}

[]{#MA-SOL-ANM-01-007-036}

Sea $a:\mathbb N\to\mathbb Q$, sea $\widetilde a=\iota\circ a$ y supón que $\widetilde a_n\to L\in\mathbb R\setminus\iota(\mathbb Q)$. Define «límite racional con tolerancias racionales» por

$$
\forall\eta\in\mathbb Q,\ \eta>0\quad\exists N\in\mathbb N\quad
\forall n\ge N,\quad |\iota(a_n)-\iota(r)|<\iota(\eta),
$$

para un candidato $r\in\mathbb Q$. Prueba que, para un candidato racional fijo, usar todas las tolerancias racionales positivas equivale a usar todas las tolerancias reales positivas. Construye las tolerancias necesarias mediante arquimedianidad. Refuta después cada candidato racional mediante una tolerancia racional explícitamente elegida por debajo de la distancia al límite real y un índice posterior a cualquier corte propuesto. Declara el orden de dependencia de las elecciones. No uses topología de $\mathbb Q$.

## §7.8

### 37. Qué conclusión cierra cada argumento

[]{#MA-EX-ANM-01-007-037}

[]{#MA-SOL-ANM-01-007-037}

[]{#MA-SEC-ANM-01-007-008}

Audita este dossier de argumentos. En cada entrada decide si la conclusión está acreditada, identifica la hipótesis que falta cuando corresponda y repara el argumento o su conclusión con una prueba. No uses una muestra finita como garantía universal.

1. Para $a_n=2n+1$, se observa que es no decreciente y que $a_n\ge1$; se concluye que tiene límite real por el teorema monótono.
2. Para $b_0=7$ y $b_n=2-1/n$ cuando $n\ge1$, se observa que la cola desde 1 es creciente y acotada; se concluye que el límite es $\sup S_b=7$.
3. Para $c_0=0$ y $c_{n+1}=3-c_n$, se resuelve $C=3-C$ y se concluye $c_n\to3/2$.
4. Para $d_n=4-1/(n+2)$, se verifica no decrecimiento y cota superior 4, y se propone concluir $d_n\to4$ después de demostrar que ningún real menor que 4 es cota superior.

Declara dominio y codominio de las sucesiones, el conjunto sobre el que se toma cada extremo y el orden lógico entre existencia e identificación.

### 38. Dos recorridos hacia una misma barrera

[]{#MA-EX-ANM-01-007-038}

[]{#MA-SOL-ANM-01-007-038}

Sean $c\in\mathbb R$ y $h>0$. Para la familia $x:\mathbb N\to\mathbb R$, $x_n=c-h/(n+1)^2$, demuestra $x_n\to c$ por dos recorridos completos: estimación del error con un corte $N(\varepsilon)$ explícitamente construido y teorema monótono con identificación del supremo. Justifica dirección, cotas y no alcanzamiento del destino. Señala dónde se usa directamente completitud y dónde se recibe su consecuencia arquimediana. No invoques el límite ya obtenido por una ruta para cerrar la otra.

### 39. Dos barreras que se encuentran

[]{#MA-EX-ANM-01-007-039}

[]{#MA-SOL-ANM-01-007-039}

Sean $a,b:\mathbb N\to\mathbb R$ con $a$ no decreciente, $b$ no creciente y $a_n\le b_n$ para todo $n$. No se supone que sus términos sean positivos. Supón además $b_n-a_n\to0$. Demuestra que ambas sucesiones tienen límite real y que sus límites coinciden. Si $c:\mathbb N\to\mathbb R$ satisface $a_n\le c_n\le b_n$ desde un índice $T$, demuestra que $c$ converge a ese mismo destino y construye un corte común para una tolerancia dada. Distingue lo que se obtiene sin la hipótesis sobre la distancia y da un ejemplo que muestre su necesidad para la igualdad de límites. No uses un teorema de intervalos encajados.

### 40. Medias simultáneas y un producto conservado

[]{#MA-EX-ANM-01-007-040}

[]{#MA-SOL-ANM-01-007-040}

Sean $0<a_0\le b_0$ reales. Construye simultáneamente $a,b:\mathbb N\to\mathbb R$ mediante

$$
a_{n+1}=\frac{2a_nb_n}{a_n+b_n},\qquad
b_{n+1}=\frac{a_n+b_n}{2}.
$$

Demuestra buena definición, positividad y conservación de $a_n\le b_n$. Obtén las dos direcciones monótonas, cotas y conservación del producto. Acredita existencia de los dos límites antes de usar las recurrencias para identificarlos; demuestra que tienen un destino común y caracteriza éste por una ecuación y su signo. Trata el caso $a_0=b_0$ y decide si, partiendo de desigualdad estricta, alguna evaluación alcanza el destino.

Si $a_0,b_0$ son racionales, declara las dos construcciones con codominio $\mathbb Q$ y sus composiciones reales. Para $a_0=1$, $b_0=2$, determina si existe un límite racional y justifica tu conclusión. No uses continuidad, compactitud ni teoría general de iteraciones.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 7](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites.html) · [Ejercicios](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-7-monotonia-cotas-y-existencia-de-limites-microcontroles.html)
