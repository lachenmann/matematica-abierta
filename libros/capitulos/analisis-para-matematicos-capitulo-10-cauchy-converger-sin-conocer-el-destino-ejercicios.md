---
content-id: MA-BCH-0243
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-010-EJERCICIOS
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
title: Ejercicios — Capítulo 10
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C10_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 10](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html) · [Ejercicios](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-soluciones.html)

Las soluciones completas se encuentran en ANM-C10_SOLUCIONES.md. Justifica las respuestas y conserva el orden tolerancia, corte y dos índices. Verifica el codominio al aplicar existencia de límite.

## 10.1. Dos índices universales

[]{#MA-EX-ANM-01-010-001}

[]{#MA-SOL-ANM-01-010-001}

[]{#MA-SEC-ANM-01-010-001}

Compara la definición de Cauchy con la condición: para todo $\varepsilon>0$ y todo $p$, existe $q\ge p$ con $|a_p-a_q|<\varepsilon$. ¿La segunda impone control?

## 10.2. Un corte recíproco

[]{#MA-EX-ANM-01-010-002}

[]{#MA-SOL-ANM-01-010-002}

Prueba directamente que $a_n=1/(n+1)$ es de Cauchy, dando un corte que incluya el índice cero cuando sirva.

## 10.3. Constantes y repetición

[]{#MA-EX-ANM-01-010-003}

[]{#MA-SOL-ANM-01-010-003}

Prueba que toda sucesión constante es de Cauchy y explica por qué no se exigen valores distintos.

## 10.4. Simetría de los pares

[]{#MA-EX-ANM-01-010-004}

[]{#MA-SOL-ANM-01-010-004}

Prueba que en la definición basta exigir el control para $p>q\ge N$, además de recordar el caso de igualdad.

## 10.5. Una escala discreta de tolerancias

[]{#MA-EX-ANM-01-010-005}

[]{#MA-SOL-ANM-01-010-005}

Demuestra que basta probar: para todo entero $k\ge1$ existe $N_k$ que controla todos los pares posteriores con distancia menor que $1/k$.

## 10.6. Dos errores

[]{#MA-EX-ANM-01-010-006}

[]{#MA-SOL-ANM-01-010-006}

[]{#MA-SEC-ANM-01-010-002}

Demuestra convergente implica Cauchy e identifica dónde se reparte la tolerancia.

## 10.7. Alternancia amortiguada

[]{#MA-EX-ANM-01-010-007}

[]{#MA-SOL-ANM-01-010-007}

Prueba Cauchy directamente para $a_n=(-1)^n/(n+1)$ y compara el corte con el de la sucesión positiva.

## 10.8. Radio no es diámetro

[]{#MA-EX-ANM-01-010-008}

[]{#MA-SOL-ANM-01-010-008}

Si todos los términos de una cola están en $(L-r,L+r)$, prueba que sus distancias son menores que $2r$. Da dos puntos de esa ventana separados por más de $r$.

## 10.9. Transportar un corte conocido

[]{#MA-EX-ANM-01-010-009}

[]{#MA-SOL-ANM-01-010-009}

Supón que $|a_n-L|\le C/(n+1)$ para todos los índices y $C\ge0$. Da un corte de Cauchy para cada tolerancia.

## 10.10. Una recíproca pendiente

[]{#MA-EX-ANM-01-010-010}

[]{#MA-SOL-ANM-01-010-010}

Explica qué obligación falta después de demostrar que una convergente es de Cauchy. ¿La desigualdad triangular por sí sola la resuelve?

## 10.11. Ancla y prefijo

[]{#MA-EX-ANM-01-010-011}

[]{#MA-SOL-ANM-01-010-011}

[]{#MA-SEC-ANM-01-010-003}

Reconstruye la prueba de acotación de una sucesión de Cauchy y trata por separado el corte cero.

## 10.12. La cota no basta

[]{#MA-EX-ANM-01-010-012}

[]{#MA-SOL-ANM-01-010-012}

Da una sucesión real acotada que no sea de Cauchy y prueba ambas afirmaciones.

## 10.13. Intervalos de cola

[]{#MA-EX-ANM-01-010-013}

[]{#MA-SOL-ANM-01-010-013}

Para $a_n=1/(n+1)$, calcula $I_N$ y sus anchuras. ¿Son intervalos de valores alcanzados?

## 10.14. Ancho no estricto

[]{#MA-EX-ANM-01-010-014}

[]{#MA-SOL-ANM-01-010-014}

Prueba que si todos los pares de una cola tienen distancia menor que $\eta$, entonces su intervalo de extremos tiene anchura a lo sumo $\eta$.

## 10.15. La igualdad puede sobrevivir

[]{#MA-EX-ANM-01-010-015}

[]{#MA-SOL-ANM-01-010-015}

Construye una sucesión de Cauchy cuya cola de corte cero tenga todas sus distancias menores que uno y anchura exactamente uno.

## 10.16. Comparar cortes distintos

[]{#MA-EX-ANM-01-010-016}

[]{#MA-SOL-ANM-01-010-016}

[]{#MA-SEC-ANM-01-010-004}

Prueba $\ell_M\le u_N$ para cualesquiera cortes $M,N$ y explica por qué se necesita en la construcción del destino.

## 10.17. Existencia y comprobación

[]{#MA-EX-ANM-01-010-017}

[]{#MA-SOL-ANM-01-010-017}

Construye $L$ para una sucesión de Cauchy sin invocar convergencia monótona ni Bolzano–Weierstrass y verifica el límite.

## 10.18. Intersección única

[]{#MA-EX-ANM-01-010-018}

[]{#MA-SOL-ANM-01-010-018}

Demuestra que la intersección de los intervalos de cola de una sucesión real de Cauchy es un singleton.

## 10.19. Recuperar el criterio desde anchuras

[]{#MA-EX-ANM-01-010-019}

[]{#MA-SOL-ANM-01-010-019}

Para una sucesión real acotada, prueba que es de Cauchy si y sólo si $u_N-\ell_N\to0$, sin usar el criterio de convergencia.

## 10.20. Conocer una extracción basta con Cauchy

[]{#MA-EX-ANM-01-010-020}

[]{#MA-SOL-ANM-01-010-020}

Supón que $a$ es de Cauchy y que $a_{\varphi(k)}\to L$, donde $\varphi:\mathbb N\to\mathbb N$ es estrictamente creciente. Demuestra directamente $a_n\to L$.

## 10.21. Negación exacta

[]{#MA-EX-ANM-01-010-021}

[]{#MA-SOL-ANM-01-010-021}

[]{#MA-SEC-ANM-01-010-005}

Escribe la negación de Cauchy y úsala para $a_n=(-1)^n$.

## 10.22. Tolerancia móvil

[]{#MA-EX-ANM-01-010-022}

[]{#MA-SOL-ANM-01-010-022}

¿Niega Cauchy que para cada corte haya dos términos distintos? Da un ejemplo que decida.

## 10.23. Bloques separados

[]{#MA-EX-ANM-01-010-023}

[]{#MA-SOL-ANM-01-010-023}

Prueba que $h_n=\sum_{j=1}^{n+1}1/j$ no es de Cauchy aunque $h_{n+1}-h_n\to0$.

## 10.24. Vecindad de longitud fija

[]{#MA-EX-ANM-01-010-024}

[]{#MA-SOL-ANM-01-010-024}

Prueba que para cada natural fijo $r$, $h_{n+r}-h_n\to0$ en el ejemplo anterior. ¿Por qué sigue fallando Cauchy?

## 10.25. Acotada con saltos pequeños

[]{#MA-EX-ANM-01-010-025}

[]{#MA-SOL-ANM-01-010-025}

Construye una sucesión acotada con saltos que tienden a cero y que no sea de Cauchy. Sugerencia: concatena para $m=1,2,\ldots$ los bloques $0,1/m,\ldots,1,(m-1)/m,\ldots,0$.

## 10.26. Álgebra por distancias

[]{#MA-EX-ANM-01-010-026}

[]{#MA-SOL-ANM-01-010-026}

[]{#MA-SEC-ANM-01-010-006}

Prueba directamente que suma, diferencia y escala real de sucesiones de Cauchy son de Cauchy, tratando el escalar cero.

## 10.27. Producto sin conocer destinos

[]{#MA-EX-ANM-01-010-027}

[]{#MA-SOL-ANM-01-010-027}

Prueba que el producto de dos sucesiones reales de Cauchy es de Cauchy usando sus cotas globales.

## 10.28. Recíprocos y prefijo

[]{#MA-EX-ANM-01-010-028}

[]{#MA-SOL-ANM-01-010-028}

Sea $a$ de Cauchy y $|a_n|\ge c>0$ para $n\ge N_0$. Prueba que la sucesión $b_k=1/a_{k+N_0}$ es de Cauchy. ¿Qué ocurre con términos cero anteriores?

## 10.29. Diferencia de Cauchy no es error nulo

[]{#MA-EX-ANM-01-010-029}

[]{#MA-SOL-ANM-01-010-029}

Si $a,b$ son de Cauchy y $a-b$ también lo es, ¿deben tener el mismo límite? ¿Qué condición basta?

## 10.30. Valor absoluto no tiene recíproca

[]{#MA-EX-ANM-01-010-030}

[]{#MA-SOL-ANM-01-010-030}

Prueba que $a$ de Cauchy implica $|a|$ de Cauchy y muestra que la vuelta falla.

## 10.31. Tres pasos racionales

[]{#MA-EX-ANM-01-010-031}

[]{#MA-SOL-ANM-01-010-031}

[]{#MA-SEC-ANM-01-010-007}

Calcula los intervalos de bisección de §10.7 para $n=0,1,2,3$ y comprueba los cuadrados de sus extremos.

## 10.32. Cauchy racional sin raíz presupuesta

[]{#MA-EX-ANM-01-010-032}

[]{#MA-SOL-ANM-01-010-032}

Demuestra que los extremos inferiores de esa bisección son de Cauchy antes de construir su límite real.

## 10.33. El destino no es racional

[]{#MA-EX-ANM-01-010-033}

[]{#MA-SOL-ANM-01-010-033}

Prueba que el límite real de los extremos inferiores tiene cuadrado dos y no puede ser límite en $\mathbb Q$.

## 10.34. Un intervalo retiene el destino

[]{#MA-EX-ANM-01-010-034}

[]{#MA-SOL-ANM-01-010-034}

Prueba que toda sucesión de Cauchy con valores en $[A,B]$, con $A\le B$ reales, converge a un punto de ese mismo intervalo. Contrasta con $(0,1)$.

## 10.35. Conjunto finito

[]{#MA-EX-ANM-01-010-035}

[]{#MA-SOL-ANM-01-010-035}

Demuestra que una sucesión con valores en un conjunto real finito no vacío es de Cauchy si y sólo si es eventualmente constante.

## 10.36. Saltos geométricos

[]{#MA-EX-ANM-01-010-036}

[]{#MA-SOL-ANM-01-010-036}

[]{#MA-SEC-ANM-01-010-008}

Supón $|a_{n+1}-a_n|\le5\,2^{-n}$. Prueba existencia de límite y da un corte que asegure error menor que $\varepsilon$.

## 10.37. Sumar antes de tomar un límite

[]{#MA-EX-ANM-01-010-037}

[]{#MA-SOL-ANM-01-010-037}

Prueba la identidad geométrica finita usada en §10.8 y explica por qué no presupone una serie convergente.

## 10.38. Error exacto en una iteración

[]{#MA-EX-ANM-01-010-038}

[]{#MA-SOL-ANM-01-010-038}

Para $x_0=0$ y $x_{n+1}=(x_n+3)/2$, demuestra $x_n=3(1-2^{-n})$ y compara su error con la cota general.

## 10.39. Iterar dentro de un intervalo

[]{#MA-EX-ANM-01-010-039}

[]{#MA-SOL-ANM-01-010-039}

Sea $F:[A,B]\to[A,B]$ con $A\le B$ y $|F(x)-F(y)|\le\rho|x-y|$, $0<\rho<1$. Prueba que desde cualquier $x_0\in[A,B]$ la iteración converge a un único punto fijo en ese intervalo.

## 10.40. La misma contracción con codominio incompleto

[]{#MA-EX-ANM-01-010-040}

[]{#MA-SOL-ANM-01-010-040}

En $X=\mathbb Q\cap[1,2]$, define $F(x)=(x+2/x)/2$. Prueba que $F:X\to X$ contrae distancias con factor $1/2$ pero no tiene punto fijo en $X$. Explica qué falla al trasladar el resultado anterior.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 10](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html) · [Ejercicios](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino-soluciones.html)
