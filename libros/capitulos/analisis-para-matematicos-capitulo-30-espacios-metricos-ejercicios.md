---
content-id: MA-BCH-0323
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-030-EJERCICIOS
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
title: Ejercicios — Capítulo 30
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C30_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)

Soluciones completas en ANM-C30_SOLUCIONES.md.

Declara espacio, métrica y ambiente de cada conjunto. Comprueba axiomas, radios, cortes, codominios y selección de testigos según la tarea.

## 30.1. Tres distancias de Hamming

[]{#MA-EX-ANM-01-030-001}

[]{#MA-SOL-ANM-01-030-001}

[]{#MA-SEC-ANM-01-030-001}

En palabras binarias de longitud tres, calcule las distancias entre $x=000$, $y=101$ y $z=111$, y compruebe las tres triangulares de este triple.

## 30.2. Separación de una pseudométrica

[]{#MA-EX-ANM-01-030-002}

[]{#MA-SOL-ANM-01-030-002}

Pruebe que $p((a,b),(c,e))=|a-c|$ cumple simetría y triangular, y refute que sea métrica. Exhiba una sucesión con dos destinos diferentes para sus distancias.

## 30.3. La distancia al cuadrado

[]{#MA-EX-ANM-01-030-003}

[]{#MA-SOL-ANM-01-030-003}

Identifique exactamente el axioma que falla para $s(x,y)=|x-y|^2$ en $\mathbb R$. Compare con $2|x-y|$.

## 30.4. Un triple finito completo

[]{#MA-EX-ANM-01-030-004}

[]{#MA-SOL-ANM-01-030-004}

En $X=\{a,b,c\}$ fije distancias simétricas $d(a,b)=2$, $d(b,c)=3$, $d(a,c)=t>0$ y diagonal cero. Determine exactamente los valores de $t$ que dan métrica.

## 30.5. Triangular inversa a dos centros

[]{#MA-EX-ANM-01-030-005}

[]{#MA-SOL-ANM-01-030-005}

Demuestre $|d(x,y)-d(a,b)|\le d(x,a)+d(y,b)$ y señale qué objetos se restan.

## 30.6. Bolas con dos formas

[]{#MA-EX-ANM-01-030-006}

[]{#MA-SOL-ANM-01-030-006}

[]{#MA-SEC-ANM-01-030-002}

Describa las bolas abiertas de radio $2$ centradas en $(1,-1)$ para $d_1$ y $d_\infty$. Decida pertenencia de $(2,0)$ y $(3,-1)$.

## 30.7. El radio de margen

[]{#MA-EX-ANM-01-030-007}

[]{#MA-SOL-ANM-01-030-007}

Si $d(a,y)=3/5$ y $r=1$, pruebe $B(y,2/5)\subset B(a,1)$. ¿Puede incluirse el borde de la bola pequeña sin más información?

## 30.8. Clausura de una bola discreta

[]{#MA-EX-ANM-01-030-008}

[]{#MA-SOL-ANM-01-030-008}

En un espacio discreto con al menos dos puntos, compare $B_D(a,1)$, $C_D(a,1)$ y $\operatorname{cl} B_D(a,1)$.

## 30.9. Dos ventanas separadas

[]{#MA-EX-ANM-01-030-009}

[]{#MA-SOL-ANM-01-030-009}

Si $D=d(a,b)>0$, pruebe que $B(a,D/3)$ y $B(b,D/3)$ son disjuntas. Generalice a radios positivos cuya suma es a lo sumo $D$.

## 30.10. Una bola cerrada es cerrada

[]{#MA-EX-ANM-01-030-010}

[]{#MA-SOL-ANM-01-030-010}

Reconstruya la prueba del cierre de $C_d(a,r)$ y explique por qué no demuestra que sea la clausura de $B_d(a,r)$.

## 30.11. Un borde que depende del ambiente

[]{#MA-EX-ANM-01-030-011}

[]{#MA-SOL-ANM-01-030-011}

[]{#MA-SEC-ANM-01-030-003}

Para $A=[0,1/2)$ calcule interior, clausura y frontera en $\mathbb R$ y en $Y=[0,1]$.

## 30.12. Uniones e intersecciones

[]{#MA-EX-ANM-01-030-012}

[]{#MA-SOL-ANM-01-030-012}

Pruebe unión arbitraria e intersección finita de abiertos. Refute la extensión a intersecciones infinitas con un ejemplo exacto.

## 30.13. Todo abierto y todo cerrado

[]{#MA-EX-ANM-01-030-013}

[]{#MA-SOL-ANM-01-030-013}

Demuestre que en un espacio discreto todos los subconjuntos son abiertos y cerrados. Calcule su frontera.

## 30.14. Clausura por ventanas

[]{#MA-EX-ANM-01-030-014}

[]{#MA-SOL-ANM-01-030-014}

Pruebe que $\operatorname{cl}_X A$ es cerrada y el menor cerrado que contiene a $A$, directamente por bolas.

## 30.15. Intersecar la clausura, no el interior

[]{#MA-EX-ANM-01-030-015}

[]{#MA-SOL-ANM-01-030-015}

Pruebe $\operatorname{cl}_Y A=Y\cap\operatorname{cl}_X A$ para $A\subset Y\subset X$. Refute la fórmula análoga para interiores.

## 30.16. Mismos términos, distinta captura

[]{#MA-EX-ANM-01-030-016}

[]{#MA-SOL-ANM-01-030-016}

[]{#MA-SEC-ANM-01-030-004}

Estudie $x_n=1/(n+1)$ en la recta con métrica usual y con métrica discreta. Considere cualquier posible destino discreto.

## 30.17. Un destino único

[]{#MA-EX-ANM-01-030-017}

[]{#MA-SOL-ANM-01-030-017}

Pruebe unicidad de límites métricos sin usar coordenadas, orden de puntos ni completitud.

## 30.18. Dos referencias acotan el mismo conjunto

[]{#MA-EX-ANM-01-030-018}

[]{#MA-SOL-ANM-01-030-018}

Si $A\subset X$ cumple $d(x,a)\le R$ para todo $x\in A$, dé una cota respecto de otro centro $b$ y un radio abierto que contenga $A$.

## 30.19. Un criterio secuencial con su interfaz

[]{#MA-EX-ANM-01-030-019}

[]{#MA-SOL-ANM-01-030-019}

Formule la relación entre clausura y límites de sucesiones de $A$. Separe la dirección incondicional de la que necesita testigos.

## 30.20. Perturbación y dos distancias

[]{#MA-EX-ANM-01-030-020}

[]{#MA-SOL-ANM-01-030-020}

Si $x_n\to a$ y $y_n\to b$, pruebe $d(x_n,y_n)\to d(a,b)$ y deduzca la regla cuando $d(x_n,y_n)\to0$.

## 30.21. Cauchy sin cero admisible

[]{#MA-EX-ANM-01-030-021}

[]{#MA-SOL-ANM-01-030-021}

[]{#MA-SEC-ANM-01-030-005}

Pruebe que $x_n=1/(n+2)$ es de Cauchy en $(0,1)$ y no converge a ningún elemento de ese espacio.

## 30.22. Cauchy y captura constante

[]{#MA-EX-ANM-01-030-022}

[]{#MA-SOL-ANM-01-030-022}

Caracterice todas las sucesiones de Cauchy de una métrica discreta y sus límites.

## 30.23. Vecinos pequeños no bastan

[]{#MA-EX-ANM-01-030-023}

[]{#MA-SOL-ANM-01-030-023}

Para $h_n=\sum_{j=1}^{n+1}1/j$ en $\mathbb R$, pruebe saltos vecinos nulos y refute Cauchy mediante pares dados después de cualquier corte.

## 30.24. Subsucesión y cola completa

[]{#MA-EX-ANM-01-030-024}

[]{#MA-SOL-ANM-01-030-024}

Pruebe que una sucesión de Cauchy con una subsucesión convergente en $X$ converge al mismo destino. Identifique el índice fijado como referencia.

## 30.25. Saltos geométricos y tres obligaciones

[]{#MA-EX-ANM-01-030-025}

[]{#MA-SOL-ANM-01-030-025}

Si $d(x_{n+1},x_n)\le3\,2^{-n}$, acredite Cauchy y una cota de error si el destino ya existe. Indique qué corte certifica error estrictamente menor que $3/8$.

## 30.26. Preimagen de una banda

[]{#MA-EX-ANM-01-030-026}

[]{#MA-SOL-ANM-01-030-026}

[]{#MA-SEC-ANM-01-030-006}

Para $f(x)=|x|$ en la recta usual, calcule $f^{-1}[(1,2)]$ y pruebe continuidad usando una desigualdad métrica.

## 30.27. La equivalencia por abiertos

[]{#MA-EX-ANM-01-030-027}

[]{#MA-SOL-ANM-01-030-027}

Pruebe continuidad global equivalente a preimágenes abiertas, con espacios métricos distintos y sin construir sucesiones.

## 30.28. Identidad con inversa fallida

[]{#MA-EX-ANM-01-030-028}

[]{#MA-SOL-ANM-01-030-028}

Pruebe que la identidad de $\mathbb R$ discreto hacia $\mathbb R$ usual es una biyección continua y que su inversa falla en cero.

## 30.29. Un fracaso secuencial condicionado

[]{#MA-EX-ANM-01-030-029}

[]{#MA-SOL-ANM-01-030-029}

Si $f$ no es continua en $a$, construya una sucesión infractora bajo $\mathrm{CC}(X)$ y explique el papel de ese supuesto.

## 30.30. Transportar el dominio de un nivel

[]{#MA-EX-ANM-01-030-030}

[]{#MA-SOL-ANM-01-030-030}

Para $b\in X$ pruebe continuidad de $F(x)=d(x,b)$ y determine si $\{x:d(x,b)=r\}$ es cerrado y $\{x:d(x,b)<r\}$ es abierto.

## 30.31. Un radio Lipschitz

[]{#MA-EX-ANM-01-030-031}

[]{#MA-SOL-ANM-01-030-031}

[]{#MA-SEC-ANM-01-030-007}

Para una función $L$-Lipschitz entre métricas, dé radios de continuidad uniforme y pruebe que transporta sucesiones de Cauchy. Separe $L=0$.

## 30.32. Distancia cero sin pertenencia

[]{#MA-EX-ANM-01-030-032}

[]{#MA-SOL-ANM-01-030-032}

Para $A=(0,1)$ dentro de $\mathbb R$, calcule $\operatorname{dist}(x,A)$ en toda la recta y decida dónde vale cero y dónde se alcanza el ínfimo.

## 30.33. Continuidad que destruye Cauchy

[]{#MA-EX-ANM-01-030-033}

[]{#MA-SOL-ANM-01-030-033}

Pruebe continuidad de $1/x$ en $(0,1)$, niegue su uniformidad con pares explícitos y muestre una Cauchy cuya imagen no lo es.

## 30.34. Un supremo que no se alcanza

[]{#MA-EX-ANM-01-030-034}

[]{#MA-SOL-ANM-01-030-034}

En $T=[0,1]$ tome $f_n(t)=t^{n+1}$ y su destino puntual $f(t)=0$ para $t<1$, $f(1)=1$. Calcule $D_\infty(f_n,f)$ y compare con $g_n(t)=t/(n+1)$.

## 30.35. Una distancia de funciones bien definida

[]{#MA-EX-ANM-01-030-035}

[]{#MA-SOL-ANM-01-030-035}

Pruebe los axiomas de $D_\infty$ en $\mathcal B(T)$ con $T$ no vacío y la equivalencia con convergencia uniforme. Indique dónde se usa completitud real.

## 30.36. Un par y dos métricas

[]{#MA-EX-ANM-01-030-036}

[]{#MA-SOL-ANM-01-030-036}

[]{#MA-SEC-ANM-01-030-008}

Para $x=(1,2)$ e $y=(4,-2)$, calcule $d_1,d_\infty$ y pruebe las desigualdades generales entre ambas métricas.

## 30.37. Recortar una métrica

[]{#MA-EX-ANM-01-030-037}

[]{#MA-SOL-ANM-01-030-037}

Pruebe que $e=\min\{1,d\}$ es métrica y que conserva convergencia y Cauchy, aunque puede cambiar acotación.

## 30.38. Una métrica con los mismos abiertos

[]{#MA-EX-ANM-01-030-038}

[]{#MA-SOL-ANM-01-030-038}

Pruebe que $e_\phi(x,y)=|\phi(x)-\phi(y)|$, $\phi(x)=x/(1+|x|)$, es métrica y tiene los mismos abiertos que la usual.

## 30.39. Misma topología, otra Cauchy

[]{#MA-EX-ANM-01-030-039}

[]{#MA-SOL-ANM-01-030-039}

Para $x_n=n$ compare Cauchy, convergencia y acotación en la usual y en $e_\phi$.

## 30.40. Auditar la identidad inversa

[]{#MA-EX-ANM-01-030-040}

[]{#MA-SOL-ANM-01-030-040}

Muestre explícitamente que la identidad desde $(\mathbb R,e_\phi)$ hacia la usual es continua pero no uniformemente continua. Compare con la identidad entre $d_1$ y $d_\infty$.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)
