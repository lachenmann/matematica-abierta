---
content-id: MA-BCH-0287
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-021-EJERCICIOS
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
title: Ejercicios — Capítulo 21
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C21_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-microcontroles.html)

Las soluciones completas están en ANM-C21_SOLUCIONES.md. Declara centro, orden, dominio y contrato diferencial. Justifica cada aplicación de Rolle/Cauchy y cada denominador; distingue resto exacto, error normalizado y certificado uniforme. No uses integrales o sumas infinitas ni derives un símbolo o sin hipótesis.

## 21.1. Los coeficientes no se eligen a ojo

[]{#MA-EX-ANM-01-021-001}

[]{#MA-SOL-ANM-01-021-001}

[]{#MA-SEC-ANM-01-021-001}

Para $P(t)=\sum_{k=0}^n a_k(t-c)^k$, demuestra $P^{(j)}(c)=j!a_j$ y deduce existencia y unicidad del polinomio que conserva los datos de órdenes0 a$n$.

## 21.2. El cubo visto desde uno

[]{#MA-EX-ANM-01-021-002}

[]{#MA-SOL-ANM-01-021-002}

Construye los polinomios de Taylor de órdenes1,2,3 de $t^3$ en$c=1$, usando$h=t-1$. Calcula sus restos exactos.

## 21.3. Orden mayor que el grado

[]{#MA-EX-ANM-01-021-003}

[]{#MA-SOL-ANM-01-021-003}

Encuentra el Taylor de orden4 de$2-3t+t^2$ en cero y explica por qué la palabra orden no exige grado4.

## 21.4. Mismos datos, salidas diferentes

[]{#MA-EX-ANM-01-021-004}

[]{#MA-SOL-ANM-01-021-004}

Para$n$ fijo y un polinomio$P$ de grado a lo sumo$n$, prueba que$P+A(t-c)^{n+1}$ conserva sus datos centrales hasta orden$n$ y puede alcanzar cualquier valor prescrito en una entrada$x\ne c$.

## 21.5. Centro, dominio y factorial

[]{#MA-EX-ANM-01-021-005}

[]{#MA-SOL-ANM-01-021-005}

Explica los tres controles necesarios para escribir Taylor de$1/(1-t)$ en$c=0$ y por qué la definición del polinomio no certifica su error cerca de$t=1$.

## 21.6. El invariante de Rolle repetido

[]{#MA-EX-ANM-01-021-006}

[]{#MA-SOL-ANM-01-021-006}

[]{#MA-SEC-ANM-01-021-002}

Escribe una prueba por inducción finita del lema de21.2, declarando el invariante y el número de aplicaciones.

## 21.7. Una cadena de tres puntos

[]{#MA-EX-ANM-01-021-007}

[]{#MA-SOL-ANM-01-021-007}

Para$H(t)=t^3(1-t)$ entre0 y1, comprueba los ceros centrales hasta orden2 y la cadena de puntos$3/4,1/2,1/4$ de Rolle.

## 21.8. Un dato central que no puede perderse

[]{#MA-EX-ANM-01-021-008}

[]{#MA-SOL-ANM-01-021-008}

Para$n=1$, muestra que$H(0)=H(1)=0$ sin exigir$H\prime(0)=0$ no garantiza un cero de$H\prime\prime$ interior.

## 21.9. Rolle hacia la izquierda

[]{#MA-EX-ANM-01-021-009}

[]{#MA-SOL-ANM-01-021-009}

Aplica el esquema de$n=1$ a$H(t)=t^2(t+1)$ entre$c=0$ y$x=-1$. Calcula una cadena de testigos y explica la orientación.

## 21.10. Qué continuidad consume cada paso

[]{#MA-EX-ANM-01-021-010}

[]{#MA-SOL-ANM-01-021-010}

Distingue las hipótesis de continuidad de$H_0,\ldots,H_n$ y la hipótesis sobre$H_n\prime$. Explica por qué no hace falta una familia infinita de puntos.

## 21.11. El auxiliar que obliga a la igualdad

[]{#MA-EX-ANM-01-021-011}

[]{#MA-SOL-ANM-01-021-011}

[]{#MA-SEC-ANM-01-021-003}

Demuestra Taylor–Lagrange a orden$n$ mediante$H=f-T_{n,c}f-A(t-c)^{n+1}$, justificando cada división y el caso$x=c$.

## 21.12. Un testigo que no es el medio

[]{#MA-EX-ANM-01-021-012}

[]{#MA-SOL-ANM-01-021-012}

Para$f(t)=t^3$, centro0, entrada1 y Taylor de orden1, calcula el testigo de Lagrange y compáralo con el punto medio.

## 21.13. Una derivada constante deja muchos testigos

[]{#MA-EX-ANM-01-021-013}

[]{#MA-SOL-ANM-01-021-013}

Para$t^3$ a orden2 y centro1, muestra que cualquier punto interior entre1 y$x\ne1$ verifica el resto. ¿Qué demuestra sobre la unicidad?

## 21.14. Un centro fronterizo sin última derivada

[]{#MA-EX-ANM-01-021-014}

[]{#MA-SOL-ANM-01-021-014}

En$[0,1]$, usa$f(t)=t^{5/2}=t^2\sqrt t$ para Taylor de orden2 y centro0 mediante el contrato cerrado. Verifica los miembros continuos y explica qué pasa con la tercera derivada en el borde.

## 21.15. El caso de orden cero

[]{#MA-EX-ANM-01-021-015}

[]{#MA-SOL-ANM-01-021-015}

Reduce Taylor–Lagrange de orden0 al valor medio de C19 y señala las hipótesis que siguen siendo necesarias.

## 21.16. Una cota que no necesita máximo

[]{#MA-EX-ANM-01-021-016}

[]{#MA-SOL-ANM-01-021-016}

[]{#MA-SEC-ANM-01-021-004}

Deriva la cota absoluta de resto desde Lagrange con$|f^{(n+1)}|\le M$. Incluye$x=c$ y$M=0$ y explica por qué no se requiere derivada final continua.

## 21.17. La cancelación de Cauchy

[]{#MA-EX-ANM-01-021-017}

[]{#MA-SOL-ANM-01-021-017}

Calcula la derivada de$G(t)=f(x)-\sum_{k=0}^n f^{(k)}(t)(x-t)^k/k!$ con$x$ fijado y deduce su forma de resto.

## 21.18. Una banda que cambia de orientación

[]{#MA-EX-ANM-01-021-018}

[]{#MA-SOL-ANM-01-021-018}

Si$2\le f^{(3)}\le6$ entre$c$ y$x$, escribe las bandas firmadas para el resto de orden2 cuando$x>c$ y cuando$x<c$.

## 21.19. Testigos diferentes para el mismo error

[]{#MA-EX-ANM-01-021-019}

[]{#MA-SOL-ANM-01-021-019}

Para$t^3$, centro0, entrada1 y orden1, encuentra un testigo de Cauchy y compáralo con el de Lagrange. Compara sus cotas con$|f\prime\prime|\le6$.

## 21.20. Una región antes de una entrada

[]{#MA-EX-ANM-01-021-020}

[]{#MA-SOL-ANM-01-021-020}

Supón$|f^{(n+1)}|\le M$ en el interior de$[c-\rho,c+\rho]$ bajo el contrato cerrado. Demuestra un control uniforme y explica por qué una muestra de esa derivada no lo sustituye.

## 21.21. Peano por Cauchy e inducción

[]{#MA-EX-ANM-01-021-021}

[]{#MA-SOL-ANM-01-021-021}

[]{#MA-SEC-ANM-01-021-005}

Prueba el paso inductivo de Peano de orden$n\ge2$ a partir del resultado para$H\prime$, con$H=f-T_{n,c}f$. Declara el denominador no nulo.

## 21.22. Peano sin un orden cúbico de error

[]{#MA-EX-ANM-01-021-022}

[]{#MA-SOL-ANM-01-021-022}

Para$f(h)=h^2\sqrt{|h|}$, verifica los datos centrales hasta orden2 y demuestra$o(|h|^2)$ pero ausencia de cota$C|h|^3$ cerca de cero.

## 21.23. Error absoluto y error normalizado

[]{#MA-EX-ANM-01-021-023}

[]{#MA-SOL-ANM-01-021-023}

Para$n\ge1$, compara$r(h)=h^n$ y$s(h)=h^{n+1}$ cerca de cero. Decide qué errores son$o(|h|^n)$ y muestra por qué tender a cero no basta.

## 21.24. Un modelo asintótico también es único

[]{#MA-EX-ANM-01-021-024}

[]{#MA-SOL-ANM-01-021-024}

Si$P,Q$ tienen grado a lo sumo$n$ y$f-P=o(|h|^n)$ y$f-Q=o(|h|^n)$ en centro0, demuestra$P=Q$ sin derivar los restos.

## 21.25. Un radio para un error de raíz

[]{#MA-EX-ANM-01-021-025}

[]{#MA-SOL-ANM-01-021-025}

Para el ejemplo de E022, produce un radio explícito que haga$|f(h)|<\varepsilon|h|^2$. Explica qué no prueba ese radio sobre una cota cúbica.

## 21.26. Dominar el resto para decidir un signo

[]{#MA-EX-ANM-01-021-026}

[]{#MA-SOL-ANM-01-021-026}

[]{#MA-SEC-ANM-01-021-006}

Demuestra el criterio de la primera derivada no nula usando$ah^m+o(|h|^m)$ y una tolerancia explícita.

## 21.27. Cuarto poder frente a cubo

[]{#MA-EX-ANM-01-021-027}

[]{#MA-SOL-ANM-01-021-027}

Compara$x^4$ y$x^3$ en cero por el primer orden diferencial no nulo y verifica las conclusiones directamente.

## 21.28. Datos nulos con tres respuestas

[]{#MA-EX-ANM-01-021-028}

[]{#MA-SOL-ANM-01-021-028}

Para$n$ fijo, construye tres polinomios con iguales datos centrales hasta orden$n$ en0 y con mínimo, máximo y ningún extremo local allí.

## 21.29. El mínimo que no gobierna toda la recta

[]{#MA-EX-ANM-01-021-029}

[]{#MA-SOL-ANM-01-021-029}

Para$q(h)=h^2-h^4$, prueba mínimo local estricto en0 y falla de mínimo global. Compara con la hipótesis de C20.

## 21.30. El orden impar en una frontera

[]{#MA-EX-ANM-01-021-030}

[]{#MA-SOL-ANM-01-021-030}

Explica por qué el criterio impar no excluye un mínimo de$x$ en0 sobre$[0,1]$. Declara una versión unilateral de la comparación de signos.

## 21.31. Una identidad geométrica todavía finita

[]{#MA-EX-ANM-01-021-031}

[]{#MA-SOL-ANM-01-021-031}

[]{#MA-SEC-ANM-01-021-007}

Demuestra$T_{n,0}(1/(1-h))=\sum_{k=0}^n h^k$ y calcula su resto exacto sin usar series.

## 21.32. La raíz y su tercera derivada

[]{#MA-EX-ANM-01-021-032}

[]{#MA-SOL-ANM-01-021-032}

Calcula$T_{2,0}\sqrt{1+h}$ y justifica la cota$0<g^{(3)}\le8/9$ en$|h|\le1/4$ con productos y raíces.

## 21.33. Un intervalo racional para una raíz

[]{#MA-EX-ANM-01-021-033}

[]{#MA-SOL-ANM-01-021-033}

Usa E032 y Taylor–Lagrange para certificar$\sqrt{5/4}$ por un intervalo racional. Explica la inclusión estricta o débil de cada borde.

## 21.34. Un cotejo por racionalización

[]{#MA-EX-ANM-01-021-034}

[]{#MA-SOL-ANM-01-021-034}

Calcula un certificado de error para$143/128$ como aproximante de$\sqrt{5/4}$ mediante diferencia de cuadrados, y compáralo con$1/432$.

## 21.35. La singularidad impone el margen

[]{#MA-EX-ANM-01-021-035}

[]{#MA-SOL-ANM-01-021-035}

Para$1/(1-h)$ con centro0 y$n$ fijo, demuestra la cota en$|h|\le\rho<1$ y explica por qué no se conserva una cota uniforme al acercarse a$h=1$.

## 21.36. Multiplicar modelos sin derivar errores

[]{#MA-EX-ANM-01-021-036}

[]{#MA-SOL-ANM-01-021-036}

[]{#MA-SEC-ANM-01-021-008}

Si$f=P+u$ y$g=Q+v$ con$u,v=o(|h|^n)$ y$n\ge1$, demuestra que el producto truncado de$PQ$ a grado$n$ es un modelo del mismo orden.

## 21.37. Sustitución con denominador protegido

[]{#MA-EX-ANM-01-021-037}

[]{#MA-SOL-ANM-01-021-037}

Construye el Taylor de orden2 de$F(h)=1/(1-h-h^2)$ y una cota cúbica válida en$|h|\le1/4$.

## 21.38. Elegir el menor grado certificado

[]{#MA-EX-ANM-01-021-038}

[]{#MA-SOL-ANM-01-021-038}

Para$1/(1-h)$ en$|h|\le1/4$, encuentra el menor orden que garantiza error menor que$1/1000$ usando la fórmula geométrica. Comprueba el valor en$h=1/4$.

## 21.39. Trasladar un centro conocido

[]{#MA-EX-ANM-01-021-039}

[]{#MA-SOL-ANM-01-021-039}

Reexpande$t^3$ en centro2 y compara con centro1. Explica por qué este traslado exacto no autoriza trasladar sin datos los coeficientes de una función general.

## 21.40. Muestras y datos que no determinan otra salida

[]{#MA-EX-ANM-01-021-040}

[]{#MA-SOL-ANM-01-021-040}

Prueba que$P(h)+A h^{n+1}\prod_{j=1}^m(h-h_j)^2$ conserva datos centrales hasta orden$n$ y valores en muestras no nulas$h_j$. Muestra que en otra entrada$h_*\ne0$ distinta de ellas puede imponerse cualquier salida.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-microcontroles.html)
