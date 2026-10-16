---
content-id: MA-BCH-0279
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-019-EJERCICIOS
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
title: Ejercicios — Capítulo 19
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C19_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 19](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html) · [Ejercicios](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html)

Las soluciones completas se encuentran en ANM-C19_SOLUCIONES.md. Declara intervalo, continuidad de bordes y derivabilidad interior. Verifica cada segmento y división; distingue punto existencial de punto predeterminado, desigualdad débil de estricta y existencia de raíz de unicidad. No uses convexidad, segunda derivada, Taylor, integrales o L’Hôpital; no presupongas continuidad de f′.

## 19.1. Signos en un mínimo

[]{#MA-EX-ANM-01-019-001}

[]{#MA-SOL-ANM-01-019-001}

[]{#MA-SEC-ANM-01-019-001}

Prueba Fermat para un mínimo interior usando signos de secantes y dos casos para el signo de la derivada.

## 19.2. El borde no es un centro interior

[]{#MA-EX-ANM-01-019-002}

[]{#MA-SOL-ANM-01-019-002}

Analiza los extremos y derivadas relativas de $f(x)=x$ sobre $[0,1]$. Explica por qué no contradicen Fermat.

## 19.3. Una esquina y un punto estacionario

[]{#MA-EX-ANM-01-019-003}

[]{#MA-SOL-ANM-01-019-003}

Compara $|x|$, $x^2$ y $x^3$ en cero: extremo local, derivabilidad y suficiencia de pendiente nula.

## 19.4. Dos lados sin un intervalo completo

[]{#MA-EX-ANM-01-019-004}

[]{#MA-SOL-ANM-01-019-004}

Prueba que en Fermat puede reemplazarse interioridad por acumulación a ambos lados, manteniendo extremo local y derivada relativa existentes.

## 19.5. Transformar el máximo

[]{#MA-EX-ANM-01-019-005}

[]{#MA-SOL-ANM-01-019-005}

Deduce Fermat para un máximo a partir del caso mínimo y verifica las condiciones de la función auxiliar.

## 19.6. Localizar un extremo interior

[]{#MA-EX-ANM-01-019-006}

[]{#MA-SOL-ANM-01-019-006}

[]{#MA-SEC-ANM-01-019-002}

Si una continua en $[a,b]$ tiene bordes iguales $k$ y algún valor distinto, prueba que alcanza un extremo global interior.

## 19.7. Una parábola que vuelve al borde

[]{#MA-EX-ANM-01-019-007}

[]{#MA-SOL-ANM-01-019-007}

Aplica Rolle a $f(x)=x(1-x)$ en $[0,1]$. Halla todos los puntos de derivada cero y comprueba si son ceros de la función.

## 19.8. Perder continuidad en un borde

[]{#MA-EX-ANM-01-019-008}

[]{#MA-SOL-ANM-01-019-008}

Para $u(x)=x$ si $0\le x<1$ y $u(1)=0$, audita Rolle en $[0,1]$ y prueba que la continuidad interior no basta.

## 19.9. Omitir la derivabilidad

[]{#MA-EX-ANM-01-019-009}

[]{#MA-SOL-ANM-01-019-009}

Analiza Rolle para $|x-1/2|$ en $[0,1]$ y contrasta con eliminar igualdad de borde en la identidad.

## 19.10. Muchos puntos posibles

[]{#MA-EX-ANM-01-019-010}

[]{#MA-SOL-ANM-01-019-010}

Explica por qué Rolle no da unicidad ni una selección simultánea. Trata una función constante y el segmento degenerado.

## 19.11. Construir el residuo de la secante

[]{#MA-EX-ANM-01-019-011}

[]{#MA-SOL-ANM-01-019-011}

[]{#MA-SEC-ANM-01-019-003}

Construye la función auxiliar de Lagrange y verifica todas las hipótesis de Rolle antes de aplicarlo.

## 19.12. Tangente paralela en el cuadrado

[]{#MA-EX-ANM-01-019-012}

[]{#MA-SOL-ANM-01-019-012}

Halla el punto de Lagrange para $x^2$ en $[1,3]$ y calcula la función auxiliar que resta la secante.

## 19.13. El punto medio no es universal

[]{#MA-EX-ANM-01-019-013}

[]{#MA-SOL-ANM-01-019-013}

Una aplicación de Lagrange al cubo en $[0,1]$ usa automáticamente $c=1/2$. Corrígela y explica el origen del error.

## 19.14. Restringir sin llenar un hueco

[]{#MA-EX-ANM-01-019-014}

[]{#MA-SOL-ANM-01-019-014}

Explica qué se necesita para aplicar Lagrange a $f:D\to\mathbb R$ entre $u<v$. Usa un dominio de dos piezas para refutar que basten los extremos.

## 19.15. Igualdad sin continuidad de derivada

[]{#MA-EX-ANM-01-019-015}

[]{#MA-SOL-ANM-01-019-015}

Explica si Lagrange se aplica a la función de bultos de C18 en un segmento cerrado que cruce cero, aunque su derivada sea discontinua allí.

## 19.16. Del signo a cada par

[]{#MA-EX-ANM-01-019-016}

[]{#MA-SOL-ANM-01-019-016}

[]{#MA-SEC-ANM-01-019-004}

Prueba que $f\prime\ge0$ en el interior de un intervalo, con continuidad de $f$ y derivabilidad interior, implica que $f$ es no decreciente.

## 19.17. Crecimiento estricto con una derivada nula

[]{#MA-EX-ANM-01-019-017}

[]{#MA-SOL-ANM-01-019-017}

Prueba que el cubo es estrictamente creciente y tiene derivada nula en cero. ¿Qué recíproca se refuta?

## 19.18. Derivadas iguales, valores fijados

[]{#MA-EX-ANM-01-019-018}

[]{#MA-SOL-ANM-01-019-018}

Sean f,g continuas en un intervalo y derivables en su interior, con derivadas iguales. Prueba que su diferencia es constante y determina qué ocurre si coinciden en un punto.

## 19.19. Constantes distintas en un dominio roto

[]{#MA-EX-ANM-01-019-019}

[]{#MA-SOL-ANM-01-019-019}

Construye una función con derivada relativa cero en todos los puntos de $[0,1]\cup[2,3]$ que no sea constante. Revisa también los bordes.

## 19.20. Signo de una derivada existente

[]{#MA-EX-ANM-01-019-020}

[]{#MA-SOL-ANM-01-019-020}

Si una función es no decreciente y tiene derivada en un punto interior a su intervalo, prueba que esa derivada es no negativa sin aplicar Lagrange.

## 19.21. Dos cotas de incrementos

[]{#MA-EX-ANM-01-019-021}

[]{#MA-SOL-ANM-01-019-021}

[]{#MA-SEC-ANM-01-019-005}

Deriva las cotas $m(y-x)\le f(y)-f(x)\le M(y-x)$ desde cotas de derivada en un intervalo. Indica cómo tratar pares no ordenados para una cota absoluta.

## 19.22. Cubo y radio común

[]{#MA-EX-ANM-01-019-022}

[]{#MA-SOL-ANM-01-019-022}

Da una constante Lipschitz y un radio uniforme para $x^3$ en $[-2,2]$ usando la derivada.

## 19.23. Una frontera rompe el certificado

[]{#MA-EX-ANM-01-019-023}

[]{#MA-SOL-ANM-01-019-023}

Para la función de E008, prueba que la derivada interior acotada por uno no da ninguna cota Lipschitz finita en todo $[0,1]$.

## 19.24. La raíz lejos de cero

[]{#MA-EX-ANM-01-019-024}

[]{#MA-SOL-ANM-01-019-024}

Da una constante Lipschitz para la raíz en $[1/4,4]$ y explica por qué no puede extenderse una cota finita a $[0,1]$.

## 19.25. Una pendiente cercana en todos los centros

[]{#MA-EX-ANM-01-019-025}

[]{#MA-SOL-ANM-01-019-025}

Si $|f\prime(t)-A|\le\eta$ en el interior de un segmento con centro a y extremo x, prueba error de modelo a lo sumo $\eta|x-a|$. ¿Qué dato no basta?

## 19.26. Productos cruzados antes de cocientes

[]{#MA-EX-ANM-01-019-026}

[]{#MA-SOL-ANM-01-019-026}

[]{#MA-SEC-ANM-01-019-006}

Construye la auxiliar de Cauchy y prueba la forma sin divisiones del valor medio.

## 19.27. Tres puntos diferentes

[]{#MA-EX-ANM-01-019-027}

[]{#MA-SOL-ANM-01-019-027}

Para $f=x^2,g=x^3$ en $[0,1]$, compara sus dos puntos de Lagrange con el punto de Cauchy.

## 19.28. Legitimar ambas divisiones

[]{#MA-EX-ANM-01-019-028}

[]{#MA-SOL-ANM-01-019-028}

Bajo $g\prime(t)\ne0$ en todo $(a,b)$, prueba que la forma de cocientes de Cauchy está definida.

## 19.29. Un incremento nulo

[]{#MA-EX-ANM-01-019-029}

[]{#MA-SOL-ANM-01-019-029}

Aplica la forma cruzada a $f(x)=x$, $g(x)=x(1-x)$ en $[0,1]$. Localiza el punto y explica por qué la razón de incrementos no está definida.

## 19.30. Un testigo donde no se puede dividir

[]{#MA-EX-ANM-01-019-030}

[]{#MA-SOL-ANM-01-019-030}

Para $f=g=x^3$ en $[-1,1]$, explica por qué $\Delta g\ne0$ no autoriza dividir la identidad de Cauchy en cualquier punto que la satisfaga.

## 19.31. Excluir los bordes de un mínimo

[]{#MA-EX-ANM-01-019-031}

[]{#MA-SOL-ANM-01-019-031}

[]{#MA-SEC-ANM-01-019-007}

Si $H\prime(u)<0<H\prime(v)$ y H es derivable en un intervalo abierto que contiene $[u,v]$, prueba que alcanza un mínimo interior en ese segmento.

## 19.32. Una derivada intermedia sin suponer continuidad

[]{#MA-EX-ANM-01-019-032}

[]{#MA-SOL-ANM-01-019-032}

Prueba Darboux para $f\prime(u)<\lambda<f\prime(v)$ y explica cómo tratar el orden opuesto.

## 19.33. Continuidad y ausencia de saltos

[]{#MA-EX-ANM-01-019-033}

[]{#MA-SOL-ANM-01-019-033}

Usa la familia de bultos de C18 para distinguir continuidad de derivada y propiedad de Darboux. Explica qué valores deben aparecer entre cero y cada $x_n$.

## 19.34. Una derivada sin ceros tiene un signo

[]{#MA-EX-ANM-01-019-034}

[]{#MA-SOL-ANM-01-019-034}

Prueba que una derivada no nula en un intervalo abierto tiene signo constante, sin asumir continuidad de esa derivada.

## 19.35. Un escalón no puede ser una derivada

[]{#MA-EX-ANM-01-019-035}

[]{#MA-SOL-ANM-01-019-035}

En $(-1,1)$, sea h menos uno para $x<0$ y uno para $x\ge0$. Prueba que no existe una función derivable en todo ese intervalo con derivada h.

## 19.36. Inyectividad desde Rolle

[]{#MA-EX-ANM-01-019-036}

[]{#MA-SOL-ANM-01-019-036}

[]{#MA-SEC-ANM-01-019-008}

Prueba inyectividad de una función continua y derivable interiormente en un intervalo si su derivada nunca se anula. Trata la diferencia entre igualdad de valores y cero de la función.

## 19.37. Contar ceros por segmentos vecinos

[]{#MA-EX-ANM-01-019-037}

[]{#MA-SOL-ANM-01-019-037}

Si $f'$ tiene a lo sumo k ceros en el interior de un intervalo, prueba que f tiene a lo sumo k+1 ceros distintos bajo las hipótesis de R8.

## 19.38. Existencia, unicidad y primera horquilla

[]{#MA-EX-ANM-01-019-038}

[]{#MA-SOL-ANM-01-019-038}

Para $p(x)=x^3+x-1$ en $[0,1]$, prueba existencia y unicidad de un cero y enciérralo entre $1/2$ y $3/4$.

## 19.39. Un máximo de tres ceros que se alcanza

[]{#MA-EX-ANM-01-019-039}

[]{#MA-SOL-ANM-01-019-039}

Usa la derivada de $q(x)=x^3-3x$ para acotar sus ceros y comprueba cuántos tiene. ¿Dos ceros de $f'$ garantizan tres de f?

## 19.40. Residuo convertido en distancia

[]{#MA-EX-ANM-01-019-040}

[]{#MA-SOL-ANM-01-019-040}

Para la raíz única r de E038 y el aproximante $x=2/3$, demuestra las cotas racionales $16/1161\le r-x\le4/189$.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 19](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html) · [Ejercicios](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html)
