---
content-id: MA-BCH-0299
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-024-EJERCICIOS
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
title: Ejercicios — Capítulo 24
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C24_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html)

Las soluciones completas están en ANM-C24_SOLUCIONES.md. Declara dominio, sentido de cada derivada, existencia de cada integral y dónde se gasta continuidad. Conserva los bordes de las primitivas y el signo de la orientación.

## 24.1. Acumular una tasa afín

[]{#MA-EX-ANM-01-024-001}

[]{#MA-SOL-ANM-01-024-001}

[]{#MA-SEC-ANM-01-024-001}

En $[0,1]$, calcula $A_f(x)$ para $f(t)=2t-1$ usando la fórmula por sumas de C22, e identifica sus valores en $0,1/2,1$.

## 24.2. Cambiar de origen

[]{#MA-EX-ANM-01-024-002}

[]{#MA-SOL-ANM-01-024-002}

Demuestra para una integrable que $A_{f,c}(x)=A_f(x)-A_f(c)$ para toda entrada, y aplícalo a $f=1$ con $c=3/4$ en $[0,1]$.

## 24.3. Grafo sin selección

[]{#MA-EX-ANM-01-024-003}

[]{#MA-SOL-ANM-01-024-003}

Justifica que la relación que define $A_f$ tiene dominio exacto $[a,b]$ y codominio real, separando el borde.

## 24.4. Incremento orientado

[]{#MA-EX-ANM-01-024-004}

[]{#MA-SOL-ANM-01-024-004}

Prueba $A_f(y)-A_f(x)=\int_x^y f$ también cuando $y<x$ y cuando son iguales.

## 24.5. Acumular un escalón

[]{#MA-EX-ANM-01-024-005}

[]{#MA-SOL-ANM-01-024-005}

Para el escalón de corte $1/2$, deduce la acumulada, incluido el valor en el corte, mediante restricciones y cambios finitos.

## 24.6. Lipschitz de la acumulada

[]{#MA-EX-ANM-01-024-006}

[]{#MA-SOL-ANM-01-024-006}

[]{#MA-SEC-ANM-01-024-002}

Si $|f|\le3$ en $[-1,2]$, prueba continuidad uniforme de $A_f$ con radio explícito y una cota de su valor.

## 24.7. El caso de cota nula

[]{#MA-EX-ANM-01-024-007}

[]{#MA-SOL-ANM-01-024-007}

Explica por qué el radio $\varepsilon/(B+1)$ prueba continuidad uniforme incluso con $B=0$.

## 24.8. Signo y orden

[]{#MA-EX-ANM-01-024-008}

[]{#MA-SOL-ANM-01-024-008}

Demuestra que $f\ge m>0$ implica crecimiento estricto de su acumulada y una cota inferior de cada incremento.

## 24.9. Positivo en un punto

[]{#MA-EX-ANM-01-024-009}

[]{#MA-SOL-ANM-01-024-009}

Refuta que una tasa integrable no negativa, positiva en algún punto, tenga acumulada estrictamente creciente.

## 24.10. Cociente encerrado

[]{#MA-EX-ANM-01-024-010}

[]{#MA-SOL-ANM-01-024-010}

Si $-2\le f\le5$ sobre $[x,y]$, $x<y$, encierra el incremento y el cociente de su acumulada. ¿Hace falta alcanzar esas cotas?

## 24.11. El lado negativo del cociente

[]{#MA-EX-ANM-01-024-011}

[]{#MA-SOL-ANM-01-024-011}

[]{#MA-SEC-ANM-01-024-003}

Prueba el lema del promedio local cuando $y<x$, sin dividir una desigualdad por un negativo.

## 24.12. Radio puntual completo

[]{#MA-EX-ANM-01-024-012}

[]{#MA-SOL-ANM-01-024-012}

Escribe la prueba $\varepsilon$–$\delta$ de $A_f'(x)=f(x)$ para una integrable continua en un centro interior.

## 24.13. Cociente exacto del cuadrado

[]{#MA-EX-ANM-01-024-013}

[]{#MA-SOL-ANM-01-024-013}

Para $f(t)=t^2$ en $[0,1]$ y centro $1/2$, calcula el cociente con incremento $h$ admisible y no nulo, usando $A_f(x)=x^3/3$ de C22.

## 24.14. Residuo cuadrático sin Taylor

[]{#MA-EX-ANM-01-024-014}

[]{#MA-SOL-ANM-01-024-014}

Si $f$ es Lipschitz de constante $L$, demuestra la cota $|A_f(y)-A_f(x)-f(x)(y-x)|\le L|y-x|^2/2$.

## 24.15. Continuidad local y global

[]{#MA-EX-ANM-01-024-015}

[]{#MA-SOL-ANM-01-024-015}

Explica qué hipótesis locales y globales se gastan al derivar la acumulada en un único centro.

## 24.16. Derivada en el borde

[]{#MA-EX-ANM-01-024-016}

[]{#MA-SOL-ANM-01-024-016}

[]{#MA-SEC-ANM-01-024-004}

Para una integrable continua relativamente en $a$, demuestra que la derivada derecha de $A_f$ vale $f(a)$.

## 24.17. Dos pendientes incompatibles

[]{#MA-EX-ANM-01-024-017}

[]{#MA-SOL-ANM-01-024-017}

Prueba por contradicción cuantificada que la acumulada del escalón no tiene derivada en $1/2$.

## 24.18. Derivada existente, valor no recuperado

[]{#MA-EX-ANM-01-024-018}

[]{#MA-SOL-ANM-01-024-018}

Para el pico aislado de altura uno, calcula su acumulada y su derivada en el pico; identifica la hipótesis fallida.

## 24.19. Modificar un extremo

[]{#MA-EX-ANM-01-024-019}

[]{#MA-SOL-ANM-01-024-019}

En $[0,1]$, toma $f(0)=1$ y $f(t)=0$ para $t>0$. Evalúa $A_f$ y su derivada derecha en cero.

## 24.20. Corolario de tasa continua

[]{#MA-EX-ANM-01-024-020}

[]{#MA-SOL-ANM-01-024-020}

Justifica que una continua sobre todo $[a,b]$ produce una acumulada continua y derivable con los valores relativos correctos.

## 24.21. Telescopía de una primitiva

[]{#MA-EX-ANM-01-024-021}

[]{#MA-SOL-ANM-01-024-021}

[]{#MA-SEC-ANM-01-024-005}

Para una acotada $f$ y primitiva $H$, prueba el encierro de $H(b)-H(a)$ por $L(f,P),U(f,P)$ sin formar etiquetas de Lagrange.

## 24.22. Encierro y evaluación

[]{#MA-EX-ANM-01-024-022}

[]{#MA-SOL-ANM-01-024-022}

Añade integrabilidad a la tarea anterior y deriva Newton–Leibniz mediante una tolerancia arbitraria.

## 24.23. Borde discontinuo de la candidata

[]{#MA-EX-ANM-01-024-023}

[]{#MA-SOL-ANM-01-024-023}

En $[0,1]$, $f=0$, $H(0)=1$ y $H(x)=0$ para $x>0$. ¿Basta $H'=f$ interior para evaluar la integral?

## 24.24. Subintervalo y orientación

[]{#MA-EX-ANM-01-024-024}

[]{#MA-SOL-ANM-01-024-024}

Si $H$ es una primitiva de una integrable, demuestra la fórmula de evaluación para todos los pares $u,v$ del dominio.

## 24.25. Hipótesis independientes

[]{#MA-EX-ANM-01-024-025}

[]{#MA-SOL-ANM-01-024-025}

Distingue las premisas de la primera y la segunda parte del teorema.

## 24.26. Constante de primitivas

[]{#MA-EX-ANM-01-024-026}

[]{#MA-SOL-ANM-01-024-026}

[]{#MA-SEC-ANM-01-024-006}

Prueba unicidad salvo constante y determina la constante si $H(a)=3$ y $K(a)=-2$.

## 24.27. Un dato inicial

[]{#MA-EX-ANM-01-024-027}

[]{#MA-SOL-ANM-01-024-027}

Para $f(t)=2t-1$ en $[0,1]$ y $H(0)=2$, encuentra y justifica la solución única del problema $H'=f$.

## 24.28. Potencia entera

[]{#MA-EX-ANM-01-024-028}

[]{#MA-SOL-ANM-01-024-028}

Calcula $\int_{-1}^2 t^3\,dt$ y justifica la primitiva con herramientas anteriores.

## 24.29. Cancelación y absoluto

[]{#MA-EX-ANM-01-024-029}

[]{#MA-SOL-ANM-01-024-029}

Calcula las integrales de $2t-1$ y de su absoluto en $[0,1]$, sin confundirlas.

## 24.30. Estacionario sin extremo

[]{#MA-EX-ANM-01-024-030}

[]{#MA-SOL-ANM-01-024-030}

En $[-1,1]$, toma $f(t)=3t^2$. Calcula su acumulada y demuestra que cero es estacionario sin ser extremo.

## 24.31. Partes desde producto

[]{#MA-EX-ANM-01-024-031}

[]{#MA-SOL-ANM-01-024-031}

[]{#MA-SEC-ANM-01-024-007}

Demuestra integración por partes bajo las hipótesis de R7a, explicando por qué existen ambas integrales.

## 24.32. Comprobar una integración por partes

[]{#MA-EX-ANM-01-024-032}

[]{#MA-SOL-ANM-01-024-032}

Con $p(t)=t$, $q(t)=t^2/2$ en $[0,1]$, verifica la fórmula y sus hipótesis.

## 24.33. Cambio de variable decreciente

[]{#MA-EX-ANM-01-024-033}

[]{#MA-SOL-ANM-01-024-033}

Aplica R7b a $f(s)=s$, $g(t)=1-t$ en $[0,1]$ y explica el signo.

## 24.34. Ida y vuelta sin monotonía

[]{#MA-EX-ANM-01-024-034}

[]{#MA-SOL-ANM-01-024-034}

Usa $f(s)=s$ en $[0,1]$ y $g(t)=t^2$ en $[-1,1]$ para verificar el cambio de variable y mostrar qué sucede con $|g'|$.

## 24.35. La imagen toca un borde

[]{#MA-EX-ANM-01-024-035}

[]{#MA-SOL-ANM-01-024-035}

Explica por qué la prueba con $A_f\circ g$ sigue válida si una entrada interior de $g$ tiene imagen en $a$ o $b$, o si su incremento es cero.

## 24.36. Error uniforme de la tasa

[]{#MA-EX-ANM-01-024-036}

[]{#MA-SOL-ANM-01-024-036}

[]{#MA-SEC-ANM-01-024-008}

Si $|f-g|\le1/100$ en $[0,3]$ y ambas son integrables, certifica el error entre sus acumuladas en cualquier entrada y en $3$.

## 24.37. Dato inicial y tasa

[]{#MA-EX-ANM-01-024-037}

[]{#MA-SOL-ANM-01-024-037}

Si primitivas admisibles $H,K$ tienen datos iniciales con distancia $1/10$ en $0$ y sus tasas integrables difieren a lo sumo $1/100$ en $[0,2]$, certifica la diferencia de salidas.

## 24.38. Misma acumulada, distintas tasas

[]{#MA-EX-ANM-01-024-038}

[]{#MA-SOL-ANM-01-024-038}

Construye dos integrables diferentes con acumuladas iguales y explica por qué no contradicen la primera parte.

## 24.39. Promedio alcanzado

[]{#MA-EX-ANM-01-024-039}

[]{#MA-SOL-ANM-01-024-039}

Demuestra el valor medio integral para una continua en un cerrado y refuta su extensión a toda integrable mediante el escalón.

## 24.40. Dos operaciones y una constante

[]{#MA-EX-ANM-01-024-040}

[]{#MA-SOL-ANM-01-024-040}

Formula qué recupera cada composición de derivar e integrar, e identifica una afirmación no habilitada por el capítulo.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html)
