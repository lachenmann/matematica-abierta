---
content-id: MA-BCH-0244
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-010-SOLUCIONES
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
title: Soluciones — Capítulo 10
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C10_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 10](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html) · [Ejercicios](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-microcontroles.html)

## 10.1. Dos índices universales

[]{#MA-EX-ANM-01-010-001}

[]{#MA-SOL-ANM-01-010-001}

[]{#MA-SEC-ANM-01-010-001}

La definición de Cauchy exige un corte antes de todos los pares posteriores. La segunda condición es verdadera para cualquier sucesión tomando $q=p$, con distancia cero. No impone Cauchy: $(-1)^n$ la satisface y no es de Cauchy.

## 10.2. Un corte recíproco

[]{#MA-EX-ANM-01-010-002}

[]{#MA-SOL-ANM-01-010-002}

Los términos posteriores a $N$ están en $(0,1/(N+1)]$, luego cualquier distancia es a lo sumo $1/(N+1)$. Para $\varepsilon>0$ tomar el mínimo natural con $N+1>1/\varepsilon$; existe por arquimedianidad y garantiza distancia menor que $\varepsilon$. Si $\varepsilon\ge1$, podemos tomar directamente $N=0$, porque todas las distancias son estrictamente menores que uno. Si $\varepsilon<1$, cero no sirve: una distancia $1-1/(n+1)$ lo bastante tardía alcanza esa tolerancia. No es necesario proponer un destino.

Después de la prueba, puede retomarse la [figura 10.1](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f01) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.3. Constantes y repetición

[]{#MA-EX-ANM-01-010-003}

[]{#MA-SOL-ANM-01-010-003}

Si $a_n=c$ para todos los índices, $|a_p-a_q|=0$ para todo par. El corte cero sirve para toda tolerancia positiva. La sucesión sigue siendo una función aunque repita un valor; Cauchy controla distancias, no inyectividad.

## 10.4. Simetría de los pares

[]{#MA-EX-ANM-01-010-004}

[]{#MA-SOL-ANM-01-010-004}

Para pares iguales la distancia es cero. Para $p<q$, intercambiar los índices usa $|a_p-a_q|=|a_q-a_p|$ y reduce al caso comprobado. El corte es el mismo y no se altera el orden de cuantificadores. Esta reducción no permite limitar la separación a un desplazamiento fijo.

Después de la prueba, puede retomarse la [figura 10.1](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f01) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.5. Una escala discreta de tolerancias

[]{#MA-EX-ANM-01-010-005}

[]{#MA-SOL-ANM-01-010-005}

La condición de Cauchy implica cada una de esas condiciones al usar $\varepsilon=1/k$. Recíprocamente, dada $\varepsilon>0$, arquimedianidad da $k\ge1$ con $1/k<\varepsilon$; el corte de esa condición controla cualquier par posterior con distancia menor que $\varepsilon$. No se intercambia el índice universal de par con el corte.

## 10.6. Dos errores

[]{#MA-EX-ANM-01-010-006}

[]{#MA-SOL-ANM-01-010-006}

[]{#MA-SEC-ANM-01-010-002}

Si $a_n\to L$, para $\varepsilon>0$ escoger un corte que haga $|a_n-L|<\varepsilon/2$ en toda la cola. Para $p,q$ posteriores, la desigualdad triangular da $|a_p-a_q|\le|a_p-L|+|a_q-L|<\varepsilon$. La división en dos errores se hace antes de fijar $p,q$. El límite viene dado por hipótesis; no se utiliza completitud.

Después de la prueba, puede retomarse la [figura 10.2](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f02) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.7. Alternancia amortiguada

[]{#MA-EX-ANM-01-010-007}

[]{#MA-SOL-ANM-01-010-007}

$|a_p-a_q|\le1/(p+1)+1/(q+1)\le2/(N+1)$ para pares posteriores a $N$. Tomar cualquier natural con $N+1>2/\varepsilon$ garantiza control. Para términos positivos bastaba $N+1>1/\varepsilon$; aquí pueden sumarse las magnitudes de signos opuestos. Ambos son cortes suficientes, sin afirmar optimalidad.

Después de la prueba, puede retomarse la [figura 10.2](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f02) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.8. Radio no es diámetro

[]{#MA-EX-ANM-01-010-008}

[]{#MA-SOL-ANM-01-010-008}

Por triangular, dos errores menores que $r$ suman menos que $2r$. Los puntos $L-3r/4$ y $L+3r/4$ pertenecen a la ventana y están separados por $3r/2>r$. Una ventana de radio $r$ no proporciona automáticamente tolerancia de Cauchy $r$.

Después de la prueba, puede retomarse la [figura 10.2](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f02) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.9. Transportar un corte conocido

[]{#MA-EX-ANM-01-010-009}

[]{#MA-SOL-ANM-01-010-009}

Si $C=0$, la sucesión es constante $L$ y sirve cero. Si $C>0$, para $p,q\ge N$ la distancia es a lo sumo $2C/(N+1)$. Cualquier $N$ con $N+1>2C/\varepsilon$ garantiza la condición. La cota no estricta inicial se convierte en estricta al escoger el corte.

## 10.10. Una recíproca pendiente

[]{#MA-EX-ANM-01-010-010}

[]{#MA-SOL-ANM-01-010-010}

Falta demostrar que cada sucesión con control interno tiene un destino dentro del codominio. La desigualdad triangular relaciona distancias con un centro ya dado; no crea ese centro. La prueba de §10.4 lo construirá por completitud. El contraste racional de §10.7 mostrará por qué esa obligación no es meramente formal.

## 10.11. Ancla y prefijo

[]{#MA-EX-ANM-01-010-011}

[]{#MA-SOL-ANM-01-010-011}

[]{#MA-SEC-ANM-01-010-003}

Con tolerancia uno obtener $N_0$, fijar el índice ancla en $N_0$ y deducir $|a_n|<|a_{N_0}|+1$ para $n\ge N_0$. Si $N_0=0$, esa cota es global. Si $N_0>0$, el máximo de ella y las finitas magnitudes anteriores acota toda la sucesión. El conjunto del máximo es no vacío y no se usa completitud.

Después de la prueba, puede retomarse la [figura 10.3](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f03) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.12. La cota no basta

[]{#MA-EX-ANM-01-010-012}

[]{#MA-SOL-ANM-01-010-012}

$a_n=(-1)^n$ tiene magnitud uno. Para cualquier corte, $p=N,q=N+1$ dan distancia dos. La tolerancia fija uno impide la condición de Cauchy en cualquier cola. La acotación sólo evita escape; no obliga a proximidad mutua.

## 10.13. Intervalos de cola

[]{#MA-EX-ANM-01-010-013}

[]{#MA-SOL-ANM-01-010-013}

$I_N=[0,1/(N+1)]$ y su anchura es $1/(N+1)$. El extremo superior se alcanza en $N$; el inferior cero no es término. El intervalo encierra toda la cola y también valores que ésta nunca toma. Los extremos se calculan por optimalidad y arquimedianidad.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.14. Ancho no estricto

[]{#MA-EX-ANM-01-010-014}

[]{#MA-SOL-ANM-01-010-014}

Para cada valor fijo $y$ de la cola, todos sus valores $x$ cumplen $x<y+\eta$. Tomando supremo, $u_N\le y+\eta$. Así $u_N-\eta$ acota inferiormente todos los $y$, y $u_N-\eta\le\ell_N$. Restar da anchura a lo sumo $\eta$. No se supone que existan valores extremos alcanzados.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.15. La igualdad puede sobrevivir

[]{#MA-EX-ANM-01-010-015}

[]{#MA-SOL-ANM-01-010-015}

Tomar $a_n=1/(n+1)$. Todos sus valores son positivos y a lo sumo uno, de modo que cada distancia es menor que uno. El supremo es uno y el ínfimo cero, luego anchura uno. La sucesión es de Cauchy por el control recíproco. Se verifica que pasar a extremos puede perder la desigualdad estricta.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.16. Comparar cortes distintos

[]{#MA-EX-ANM-01-010-016}

[]{#MA-SOL-ANM-01-010-016}

[]{#MA-SEC-ANM-01-010-004}

El índice $r=\max\{M,N\}$ pertenece a ambas colas y da $\ell_M\le a_r\le u_N$. Por ello cada $u_N$ acota a todo el conjunto de inferiores. Esto permite deducir $\sup_M\ell_M\le u_N$. La desigualdad de extremos con el mismo corte no proporciona por sí sola esa cota de todo el conjunto.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.17. Existencia y comprobación

[]{#MA-EX-ANM-01-010-017}

[]{#MA-SOL-ANM-01-010-017}

Por acotación existen extremos reales de cada cola. El conjunto no vacío de inferiores es acotado superiormente y tiene supremo $L$ por completitud. La comparación entre cortes da $\ell_N\le L\le u_N$ para todo $N$. Dada $\varepsilon>0$, usar Cauchy con $\varepsilon/2$ para obtener anchura a lo sumo $\varepsilon/2$ en una cola. Todos sus términos y $L$ están en ese intervalo, de modo que $|a_n-L|\le\varepsilon/2<\varepsilon$.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.18. Intersección única

[]{#MA-EX-ANM-01-010-018}

[]{#MA-SOL-ANM-01-010-018}

El real $L$ construido pertenece a todos los intervalos. Si $x,y$ estuvieran en la intersección y su distancia fuera $d>0$, Cauchy con tolerancia $d/2$ daría un intervalo de anchura a lo sumo $d/2$ que contiene a ambos. Eso contradice su distancia $d$. Por tanto sólo contiene a $L$.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.19. Recuperar el criterio desde anchuras

[]{#MA-EX-ANM-01-010-019}

[]{#MA-SOL-ANM-01-010-019}

Cauchy con tolerancia $\varepsilon/2$ fuerza anchura a lo sumo $\varepsilon/2$ en todos los cortes posteriores, por §10.3; así las anchuras tienden a cero. Recíprocamente, dada $\varepsilon>0$, escoger un corte con anchura menor que $\varepsilon$. Todo par posterior está en su intervalo, por lo que su distancia es a lo sumo la anchura y menor que $\varepsilon$. Se compara control de pares y geometría sin usar aún existencia de límite.

Después de la prueba, puede retomarse la [figura 10.4](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.20. Conocer una extracción basta con Cauchy

[]{#MA-EX-ANM-01-010-020}

[]{#MA-SOL-ANM-01-010-020}

Una inducción da $\varphi(k)\ge k$. Para $\varepsilon>0$, tomar el corte $N_1$ de Cauchy con tolerancia $\varepsilon/2$ y el corte $K$ de la extracción para la misma tolerancia respecto de $L$. Fijar $k=\max\{K,N_1\}$, así $\varphi(k)\ge N_1$ y $|a_{\varphi(k)}-L|<\varepsilon/2$. Para todo $n\ge N_1$, $|a_n-L|\le|a_n-a_{\varphi(k)}|+|a_{\varphi(k)}-L|<\varepsilon$. Se necesita una extracción ya dada, no BW.

## 10.21. Negación exacta

[]{#MA-EX-ANM-01-010-021}

[]{#MA-SOL-ANM-01-010-021}

[]{#MA-SEC-ANM-01-010-005}

Existe $\varepsilon_0>0$ tal que para cada $N$ existen $p,q\ge N$ con $|a_p-a_q|\ge\varepsilon_0$. Para la alternancia escoger $\varepsilon_0=1$ y los índices $N,N+1$, cuya distancia es dos. La tolerancia se fija primero; los testigos se escogen después del corte.

## 10.22. Tolerancia móvil

[]{#MA-EX-ANM-01-010-022}

[]{#MA-SOL-ANM-01-010-022}

No. $1/(n+1)$ tiene términos distintos después de cada corte, pero es de Cauchy. La distancia de los testigos puede hacerse tan pequeña como se quiera al mover el corte; no hay una tolerancia positiva fija que todas las colas infrinjan.

## 10.23. Bloques separados

[]{#MA-EX-ANM-01-010-023}

[]{#MA-SOL-ANM-01-010-023}

El salto es $1/(n+2)$ y tiende a cero. Para $m\ge1$, la diferencia $h_{2m-1}-h_{m-1}$ contiene $m$ sumandos, cada uno al menos $1/(2m)$, y por tanto es al menos $1/2$. Dado $N$, tomar $m=N+1$ deja ambos índices posteriores. La tolerancia fija $1/2$ niega Cauchy. Todas las sumas usadas son finitas.

Después de la prueba, puede retomarse la [figura 10.5](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f05) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.24. Vecindad de longitud fija

[]{#MA-EX-ANM-01-010-024}

[]{#MA-SOL-ANM-01-010-024}

Si $r=0$ la diferencia es cero. Si $r>0$, contiene $r$ sumandos con denominadores al menos $n+2$, luego $0\le h_{n+r}-h_n\le r/(n+2)\to0$. El corte suficiente puede depender de $r$. Cauchy exige un único corte para todas las separaciones posibles, y los bloques con longitud creciente mantienen distancia al menos $1/2$.

Después de la prueba, puede retomarse la [figura 10.5](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f05) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.25. Acotada con saltos pequeños

[]{#MA-EX-ANM-01-010-025}

[]{#MA-SOL-ANM-01-010-025}

Concatenar los bloques de la sugerencia y reindexar desde cero. Todos los valores están en $[0,1]$. Dentro del bloque $m$, cada salto es $1/m$; entre bloques ambos valores de unión son cero y el salto es cero. Dada $\varepsilon>0$, después de los finitos bloques con $m$ pequeño todos los saltos son menores que $\varepsilon$. Pero cada bloque tardío contiene cero y uno; después de cualquier corte se puede elegir un bloque completo y dos índices con distancia uno. La tolerancia fija uno niega Cauchy. La acotación no repara el fallo de controlar sólo vecinos.

## 10.26. Álgebra por distancias

[]{#MA-EX-ANM-01-010-026}

[]{#MA-SOL-ANM-01-010-026}

[]{#MA-SEC-ANM-01-010-006}

Para suma y diferencia, triangular acota su diferencia de términos por la suma de las diferencias de cada factor; tomar máximo de cortes con tolerancia $\varepsilon/2$. Para escalar no cero, usar la tolerancia $\varepsilon/|c|$, ya que la nueva distancia es $|c|$ veces la original. Si $c=0$, la sucesión es constante y sirve corte cero.

## 10.27. Producto sin conocer destinos

[]{#MA-EX-ANM-01-010-027}

[]{#MA-SOL-ANM-01-010-027}

Por acotación, fijar $A,B\ge0$ con magnitudes de $a,b$ a lo sumo esos números. La identidad $a_pb_p-a_qb_q=a_p(b_p-b_q)+b_q(a_p-a_q)$ da cota $A|b_p-b_q|+B|a_p-a_q|$. Escoger cortes con tolerancias $\varepsilon/[2(A+1)]$ para $b$ y $\varepsilon/[2(B+1)]$ para $a$. Después del máximo la cota es a lo sumo la suma de dos cantidades menores que $\varepsilon/2$, con casos de cota cero igualmente controlados. No se requiere signo positivo de términos.

## 10.28. Recíprocos y prefijo

[]{#MA-EX-ANM-01-010-028}

[]{#MA-SOL-ANM-01-010-028}

Los recíprocos de esta cola están definidos. Para un corte original $H$ que controle $a$ con tolerancia $c^2\varepsilon$, tomar un corte nuevo $K=\max\{H,N_0\}$. Si $p,q\ge K$, sus índices originales $p+N_0,q+N_0$ superan ambos cortes y la distancia de recíprocos es a lo sumo la distancia de términos dividida por $c^2$, menor que $\varepsilon$. Los ceros previos no afectan a esta cola reindexada, pero impedirían definir recíprocos en todos los índices de $a$.

## 10.29. Diferencia de Cauchy no es error nulo

[]{#MA-EX-ANM-01-010-029}

[]{#MA-SOL-ANM-01-010-029}

No. Las constantes $a_n=0$ y $b_n=1$ son de Cauchy y su diferencia constante menos uno también, con destinos distintos. Basta que $a_n-b_n\to0$: ambos tienen límites reales por el criterio y la regla de resta de C06 da diferencia de límites cero. Ser de Cauchy para la diferencia sólo asegura que ésta tiene algún límite, no que sea cero.

## 10.30. Valor absoluto no tiene recíproca

[]{#MA-EX-ANM-01-010-030}

[]{#MA-SOL-ANM-01-010-030}

La triangular inversa $\big||a_p|-|a_q|\big|\le|a_p-a_q|$ permite usar el mismo corte. Para la vuelta, $a_n=(-1)^n$ no es de Cauchy, mientras $|a_n|=1$ es constante. La operación olvida el signo y puede borrar separaciones.

## 10.31. Tres pasos racionales

[]{#MA-EX-ANM-01-010-031}

[]{#MA-SOL-ANM-01-010-031}

[]{#MA-SEC-ANM-01-010-007}

Los intervalos son $[1,2]$, $[1,3/2]$, $[5/4,3/2]$, $[11/8,3/2]$. Los puntos medios $3/2$, $5/4$, $11/8$ tienen cuadrados $9/4>2$, $25/16<2$, $121/64<2$, respectivamente. Así se elige cada mitad correcta, las anchuras son uno, medio, cuarto y octavo, y los extremos siguen encerrando el valor dos entre sus cuadrados.

Después de la prueba, puede retomarse la [figura 10.6](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f06) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.32. Cauchy racional sin raíz presupuesta

[]{#MA-EX-ANM-01-010-032}

[]{#MA-SOL-ANM-01-010-032}

Los intervalos están encajados y tienen anchura $2^{-N}$. Para $p,q\ge N$, los extremos inferiores posteriores pertenecen a $[l_N,u_N]$, luego su distancia es a lo sumo $2^{-N}$. Escoger por arquimedianidad $N$ con $2^{-N}<\varepsilon$ garantiza todos los pares. La existencia de una raíz real aún no se ha usado: sólo extremos racionales y anchuras conocidas.

Después de la prueba, puede retomarse la [figura 10.6](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f06) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.33. El destino no es racional

[]{#MA-EX-ANM-01-010-033}

[]{#MA-SOL-ANM-01-010-033}

El criterio real proporciona $l_n\to L$, y $u_n-l_n=2^{-n}\to0$ da $u_n\to L$. Por regla de producto y orden, $l_n^2<2<u_n^2$ implica $L^2\le2\le L^2$. Si un racional reducido $s/t$ tuviera cuadrado dos, $s^2=2t^2$ obligaría a que $s$ y luego $t$ fueran pares, contradicción. Un límite racional de $l$ también sería un límite real y por unicidad igual a $L$, imposible.

Después de la prueba, puede retomarse la [figura 10.6](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f06) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.34. Un intervalo retiene el destino

[]{#MA-EX-ANM-01-010-034}

[]{#MA-SOL-ANM-01-010-034}

El criterio real proporciona un límite $L$. Las cotas $A\le a_n\le B$ pasan al límite por C06, luego $A\le L\le B$. En $(0,1)$, la sucesión $1/(n+2)$ es de Cauchy y converge en $\mathbb R$ a cero, fuera del conjunto; unicidad impide otro destino interior. La pertenencia del límite al codominio no se sigue sólo de proximidad.

## 10.35. Conjunto finito

[]{#MA-EX-ANM-01-010-035}

[]{#MA-SOL-ANM-01-010-035}

Si el conjunto tiene un único valor, la afirmación es inmediata. Si tiene varios, sea $\delta>0$ la mínima distancia entre dos valores distintos, existente por finitud. Cauchy con tolerancia $\delta$ fuerza que todos los términos posteriores sean iguales entre sí, pues distintos darían distancia al menos $\delta$. Así la cola es constante. Recíprocamente, una cola constante tiene todas sus distancias cero y prueba Cauchy.

## 10.36. Saltos geométricos

[]{#MA-EX-ANM-01-010-036}

[]{#MA-SOL-ANM-01-010-036}

[]{#MA-SEC-ANM-01-010-008}

La estimación de §10.8 con $C=5,\rho=1/2$ da $|a_p-a_q|\le10\,2^{-q}$ para $p>q$. Escoger $N$ con $10\,2^{-N}<\varepsilon$ garantiza Cauchy. Completitud real aporta $L$ y el paso al límite en el primer índice da $|L-a_n|\le10\,2^{-n}$. El mismo corte suficiente asegura error estricto al límite.

Después de la prueba, puede retomarse la [figura 10.7](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f07) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.37. Sumar antes de tomar un límite

[]{#MA-EX-ANM-01-010-037}

[]{#MA-SOL-ANM-01-010-037}

Para $p>q$, multiplicar $S=\rho^q+\cdots+\rho^{p-1}$ por $1-\rho$ deja $S-\rho S=\rho^q-\rho^p$ tras cancelar términos. Como $1-\rho\ne0$, $S=\rho^q(1-\rho^{p-q})/(1-\rho)$. Todas las operaciones son finitas; el control de pares y luego Cauchy construyen el límite de la sucesión, sin asignar valor a una suma infinita.

Después de la prueba, puede retomarse la [figura 10.7](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f07) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.38. Error exacto en una iteración

[]{#MA-EX-ANM-01-010-038}

[]{#MA-SOL-ANM-01-010-038}

En cero la fórmula da cero. Si vale en $n$, entonces $(3(1-2^{-n})+3)/2=3(1-2^{-(n+1)})$, lo que cierra inducción. Su límite es tres y el error exacto $3\,2^{-n}$. La contracción tiene $\rho=1/2$ y $D=3/2$, por lo que la cota general $D\rho^n/(1-\rho)$ coincide aquí con el error exacto. No todas las iteraciones saturan esa cota.

Después de la prueba, puede retomarse la [figura 10.7](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f07) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.39. Iterar dentro de un intervalo

[]{#MA-EX-ANM-01-010-039}

[]{#MA-SOL-ANM-01-010-039}

La imagen en el mismo intervalo permite definir todos los iterados por recursión. Con $D=|x_1-x_0|$, la inducción de §10.8 da saltos a lo sumo $D\rho^n$, por lo que es de Cauchy y converge en $\mathbb R$. Las cotas $A\le x_n\le B$ pasan al límite y retienen $L$ en el dominio de $F$. La desigualdad $|F(L)-L|\le\rho|L-x_n|+|x_{n+1}-L|$ prueba que es fijo. Dos puntos fijos cumplen distancia a lo sumo $\rho$ veces sí misma, luego coinciden. Si $A=B$, la iteración es constante y la conclusión sigue.

Después de la prueba, puede retomarse la [figura 10.7](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f07) para contrastar el mecanismo con el ejemplo del capítulo.

## 10.40. La misma contracción con codominio incompleto

[]{#MA-EX-ANM-01-010-040}

[]{#MA-SOL-ANM-01-010-040}

Es racional para todo racional no cero. Para $1\le x\le2$, $F(x)-1=(x^2-2x+2)/(2x)=((x-1)^2+1)/(2x)>0$ y $2-F(x)=(4x-x^2-2)/(2x)\ge1/(2x)>0$, pues $4x-x^2-2=2-(x-2)^2\ge1$ en ese intervalo. Así $F(x)\in X$. Además $|F(x)-F(y)|=|x-y|\,|1-2/(xy)|/2$. Como $1\le xy\le4$, $1/2\le2/(xy)\le2$ y el último factor absoluto es a lo sumo uno, dando contracción por $1/2$. Un punto fijo resolvería $x^2=2$, imposible en $\mathbb Q$. Los iterados son de Cauchy y convergen en $\mathbb R$; el centro real no tiene por qué pertenecer a $X$. Falta completitud del codominio, y por eso no se puede evaluar allí $F(L)$ como una función sobre $X$.

Después de la prueba, puede retomarse la [figura 10.6](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html#fig-anm-c10-f06) para contrastar el mecanismo con el ejemplo del capítulo.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 10](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html) · [Ejercicios](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-microcontroles.html)
