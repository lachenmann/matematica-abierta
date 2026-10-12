---
content-id: MA-BCH-0319
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-029-EJERCICIOS
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
title: Ejercicios — Capítulo 29
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C29_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-microcontroles.html)

Soluciones completas en ANM-C29_SOLUCIONES.md.

Declara dominio, cola y margen interior antes de operar. Comprueba mayorantes, anclas, coeficientes y extremos según la tarea.

## 29.1. La geométrica en dos dominios

[]{#MA-EX-ANM-01-029-001}

[]{#MA-SOL-ANM-01-029-001}

[]{#MA-SEC-ANM-01-029-001}

Para $u_j(x)=x^j$, encuentre dominio, suma y una envolvente en $[-r,r]$, $0<r<1$. Decida uniformidad en $(-1,1)$.

## 29.2. Un término necesario

[]{#MA-EX-ANM-01-029-002}

[]{#MA-SOL-ANM-01-029-002}

Pruebe que la convergencia uniforme de una serie implica que sus términos tienden uniformemente a cero. Refute la recíproca.

## 29.3. Cortes dependientes de la entrada

[]{#MA-EX-ANM-01-029-003}

[]{#MA-SOL-ANM-01-029-003}

Diagnostique: «para todo $x$ existe un corte geométrico, así que hay un corte para todo $(-1,1)$». Exhiba entradas que impiden un corte dado.

## 29.4. Prefijo no acotado

[]{#MA-EX-ANM-01-029-004}

[]{#MA-SOL-ANM-01-029-004}

En $\mathbb R$ tome $u_0(x)=x^2$ y $u_j(x)=2^{-j}$ para $j\ge1$. Pruebe uniformidad y explique por qué no puede haber mayorante global finito para $u_0$.

## 29.5. Cauchy sin suma conocida

[]{#MA-EX-ANM-01-029-005}

[]{#MA-SOL-ANM-01-029-005}

Suponga $|\sum_{j=n+1}^m u_j(x)|\le\eta_n$ para todos $m>n$ y $x\in X$, con $\eta_n\to0$. Construya la suma y un certificado.

## 29.6. Mayorante dyádico

[]{#MA-EX-ANM-01-029-006}

[]{#MA-SOL-ANM-01-029-006}

[]{#MA-SEC-ANM-01-029-002}

Si $|u_j(x)|\le3\,2^{-j}$, dé cota de suma y cola y el primer índice garantizado para error estrictamente menor que $3/8$.

## 29.7. La serie de magnitudes

[]{#MA-EX-ANM-01-029-007}

[]{#MA-SOL-ANM-01-029-007}

Pruebe directamente que las hipótesis M hacen uniforme $\sum|u_j|$ y acotan su destino por $\sum M_j$.

## 29.8. Uniformidad sin criterio M

[]{#MA-EX-ANM-01-029-008}

[]{#MA-SOL-ANM-01-029-008}

Use $u_j(x)=\mathbf1_{\{j\}}(x)/(j+1)$ en $X=\mathbb N_0$ para refutar que el criterio M sea necesario incluso para uniformidad de las magnitudes.

## 29.9. Cancelación uniforme

[]{#MA-EX-ANM-01-029-009}

[]{#MA-SOL-ANM-01-029-009}

Considere $u_j(x)=(-1)^j/(j+1)$ en cualquier conjunto no vacío $X$. Decida uniformidad, absoluta y posibilidad de M.

## 29.10. Cambio de parámetro

[]{#MA-EX-ANM-01-029-010}

[]{#MA-SOL-ANM-01-029-010}

En $Y=[0,1]$ sea $u_j(x)=x^j/3^j$. Encuentre una suma explícita y compare el resto exacto con M.

## 29.11. Integrales y orientación

[]{#MA-EX-ANM-01-029-011}

[]{#MA-SOL-ANM-01-029-011}

[]{#MA-SEC-ANM-01-029-003}

Si una serie integrable en $[-2,3]$ tiene $|R_n|\le2^{-n}$, acote error de su integral completa y de las acumuladas desde $1$.

## 29.12. Serie derivada con ancla

[]{#MA-EX-ANM-01-029-012}

[]{#MA-SOL-ANM-01-029-012}

Formule y pruebe el teorema derivativo de §29.3 usando sólo el teorema de sucesiones de C28.

## 29.13. Telescopio suave con esquina

[]{#MA-EX-ANM-01-029-013}

[]{#MA-SOL-ANM-01-029-013}

Para $h_n(x)=\sqrt{x^2+1/(n+1)^2}$ forme la serie telescópica de §29.3. Pruebe uniformidad y la falla de derivación en cero.

## 29.14. Constantes invisibles

[]{#MA-EX-ANM-01-029-014}

[]{#MA-SOL-ANM-01-029-014}

Dé una serie cuya serie de derivadas converja uniformemente, pero cuya serie de valores diverja. Identifique la hipótesis perdida.

## 29.15. Serie polinómica integrada

[]{#MA-EX-ANM-01-029-015}

[]{#MA-SOL-ANM-01-029-015}

En $[-1,1]$ tome $u_j(x)=2^{-j}x^2$. Calcule suma, derivada, integral desde cero y sus errores uniformes.

## 29.16. Convergencia en una entrada

[]{#MA-EX-ANM-01-029-016}

[]{#MA-SOL-ANM-01-029-016}

[]{#MA-SEC-ANM-01-029-004}

Una serie de centro $2$ converge en $t=-1$ y satisface $|a_j(-3)^j|\le5$. Dé una ventana protegida y cota de cola sobre $[0,4]$.

## 29.17. Supremo sin pertenencia

[]{#MA-EX-ANM-01-029-017}

[]{#MA-SOL-ANM-01-029-017}

Reconstruya el radio a partir de $H$ y pruebe interior y exterior. Evite afirmar convergencia en la distancia $R$.

## 29.18. El término constante

[]{#MA-EX-ANM-01-029-018}

[]{#MA-SOL-ANM-01-029-018}

Diagnostique «una serie de potencias da cero en su centro». Dé un ejemplo y trate $R=0$.

## 29.19. Compactos interiores

[]{#MA-EX-ANM-01-029-019}

[]{#MA-SOL-ANM-01-029-019}

Pruebe que una serie de radio $R>0$ converge uniformemente en todo compacto $K\subset(c-R,c+R)$.

## 29.20. Radios iguales no dan cortes iguales

[]{#MA-EX-ANM-01-029-020}

[]{#MA-SOL-ANM-01-029-020}

Compare la geométrica y $\sum x^j/(j+1)^2$, ambas de radio $1$, en todo $[-1,1]$ y en $(-1,1)$.

## 29.21. Cocientes acreditados

[]{#MA-EX-ANM-01-029-021}

[]{#MA-SOL-ANM-01-029-021}

[]{#MA-SEC-ANM-01-029-005}

Pruebe el criterio de cociente cuando el límite es menor que $1$ y cuando es mayor que $1$, indicando el tratamiento de un prefijo.

## 29.22. Trasladar y escalar

[]{#MA-EX-ANM-01-029-022}

[]{#MA-SOL-ANM-01-029-022}

Encuentre radio y dominio de $\sum_{j=1}^{\infty}((x-2)/3)^j/j$.

## 29.23. Ceros en los coeficientes

[]{#MA-EX-ANM-01-029-023}

[]{#MA-SOL-ANM-01-029-023}

Encuentre el radio de $\sum_{k=0}^{\infty}(x-1)^{2k}$ y explique por qué no sirve el cociente consecutivo de sus coeficientes.

## 29.24. Raíz sin cociente

[]{#MA-EX-ANM-01-029-024}

[]{#MA-SOL-ANM-01-029-024}

Para $a_j=2^j$ si $j$ es par y $a_j=2^j/(j+1)$ si es impar, calcule $R$. Justifique el límite de raíces usado.

## 29.25. Todos los extremos

[]{#MA-EX-ANM-01-029-025}

[]{#MA-SOL-ANM-01-029-025}

Construya series de radio $2$ y centro $-3$ con cada uno de los cuatro posibles dominios de extremos.

## 29.26. La cola derivada

[]{#MA-EX-ANM-01-029-026}

[]{#MA-SOL-ANM-01-029-026}

[]{#MA-SEC-ANM-01-029-006}

Deduzca $\sum_{j>n}j\rho^{j-1}$, $0<\rho<1$, sin derivar una serie infinita.

## 29.27. Presupuesto derivativo concreto

[]{#MA-EX-ANM-01-029-027}

[]{#MA-SOL-ANM-01-029-027}

Si $|a_j|\le3\,2^{-j}$, acote en $[-1,1]$ el resto de la serie derivada y evalúe la cota en $n=4$.

## 29.28. Una frontera no derivable por la serie

[]{#MA-EX-ANM-01-029-028}

[]{#MA-SOL-ANM-01-029-028}

Para $F(x)=\sum_{j\ge1}x^j/j$, explique por qué la convergencia en $-1$ no autoriza la fórmula de serie derivada allí.

## 29.29. Integral y radio

[]{#MA-EX-ANM-01-029-029}

[]{#MA-SOL-ANM-01-029-029}

Pruebe que dividir los coeficientes por $j+1$ e incrementar el grado no aumenta el radio de una serie de radio positivo.

## 29.30. Orden finito y ancla

[]{#MA-EX-ANM-01-029-030}

[]{#MA-SOL-ANM-01-029-030}

Obtenga $F^{(3)}$ y $a_3$ para una serie de centro $c$ y radio positivo. Precise la región válida.

## 29.31. Certificado factorial

[]{#MA-EX-ANM-01-029-031}

[]{#MA-SOL-ANM-01-029-031}

[]{#MA-SEC-ANM-01-029-007}

Calcule la cota factorial para $E$ en $[-1,1]$ con $n=4$ y compruebe tolerancia estricta $1/50$.

## 29.32. Ecuación y positividad

[]{#MA-EX-ANM-01-029-032}

[]{#MA-SOL-ANM-01-029-032}

Pruebe $E^{\prime}=E$, $E(x)E(-x)=1$ y $E(x)>0$ usando las operaciones ya acreditadas.

## 29.33. Unicidad de coeficientes

[]{#MA-EX-ANM-01-029-033}

[]{#MA-SOL-ANM-01-029-033}

Dos series del mismo centro representan la misma función cerca del centro y tienen radios positivos. Pruebe que sus coeficientes coinciden.

## 29.34. Integral geométrica

[]{#MA-EX-ANM-01-029-034}

[]{#MA-SOL-ANM-01-029-034}

Defina $L(x)=\int_0^x(1-t)^{-1}\,dt$ en $(-1,1)$. Encuentre su serie y su derivada sin nombrar un logaritmo.

## 29.35. Ley de adición y unicidad concreta

[]{#MA-EX-ANM-01-029-035}

[]{#MA-SOL-ANM-01-029-035}

Pruebe la ley de adición de $E$ y la unicidad de $y^{\prime}=y$, $y(0)=1$, en un intervalo que contiene cero.

## 29.36. Triángulo de coeficientes

[]{#MA-EX-ANM-01-029-036}

[]{#MA-SOL-ANM-01-029-036}

[]{#MA-SEC-ANM-01-029-008}

Encuentre los coeficientes del producto de dos geométricas centradas en cero e identifique la función resultante dentro de radio $1$.

## 29.37. Colas del producto

[]{#MA-EX-ANM-01-029-037}

[]{#MA-SOL-ANM-01-029-037}

Pruebe la cota triangular del producto numérico y explique el orden de sus dos límites.

## 29.38. El radio del producto puede crecer

[]{#MA-EX-ANM-01-029-038}

[]{#MA-SOL-ANM-01-029-038}

Use la geométrica y $1-x$ para refutar que el radio del producto sea siempre exactamente el mínimo de los radios.

## 29.39. Uniformidad del producto funcional

[]{#MA-EX-ANM-01-029-039}

[]{#MA-SOL-ANM-01-029-039}

Si dos series de magnitudes son uniformes en $Y$ con totales acotados por $A_*,B_*$, demuestre uniformidad de su producto de Cauchy.

## 29.40. Un certificado reutilizable y su alcance

[]{#MA-EX-ANM-01-029-040}

[]{#MA-SOL-ANM-01-029-040}

Para el cuadrado de la geométrica en $[-1/2,1/2]$, obtenga una cota de cola de producto por triángulos y compárela con la cola exacta de coeficientes. Indique qué parte anticipa ACM.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-microcontroles.html)
