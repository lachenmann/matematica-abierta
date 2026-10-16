---
content-id: MA-BCH-0247
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-011-EJERCICIOS
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
title: Ejercicios — Capítulo 11
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C11_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html)

Las soluciones completas se encuentran en ANM-C11_SOLUCIONES.md. Justifica las respuestas y distingue términos, totales, suma y resto. Conserva el orden tolerancia, corte y extremos de bloque.

## 11.1. Aportes y totales

[]{#MA-EX-ANM-01-011-001}

[]{#MA-SOL-ANM-01-011-001}

[]{#MA-SEC-ANM-01-011-001}

Calcula $s_0,s_1,s_2,s_3$ para $a_n=2^{-n}$. Distingue ambos objetos.

## 11.2. Recuperar una serie

[]{#MA-EX-ANM-01-011-002}

[]{#MA-SOL-ANM-01-011-002}

Si se prescribe $s_n=(n+1)/(n+2)$, encuentra la única sucesión de términos que produce esos totales y decide convergencia.

## 11.3. Misma suma, distinto proceso

[]{#MA-EX-ANM-01-011-003}

[]{#MA-SOL-ANM-01-011-003}

Construye dos sucesiones distintas de soporte finito con la misma suma y prueba que sus procesos son distintos.

## 11.4. Una transformación reversible

[]{#MA-EX-ANM-01-011-004}

[]{#MA-SOL-ANM-01-011-004}

Prueba que toda sucesión real $s$ es el proceso de sumación de una única sucesión real $a$.

## 11.5. Totales acotados y término nulo

[]{#MA-EX-ANM-01-011-005}

[]{#MA-SOL-ANM-01-011-005}

Construye una serie con términos que tienden a cero y sumas parciales acotadas que no convergen.

## 11.6. Identidad de bloques

[]{#MA-EX-ANM-01-011-006}

[]{#MA-SOL-ANM-01-011-006}

[]{#MA-SEC-ANM-01-011-002}

Prueba por inducción que $s_p-s_q=\sum_{j=q+1}^pa_j$ cuando $p>q$.

## 11.7. La longitud no puede elegir el corte

[]{#MA-EX-ANM-01-011-007}

[]{#MA-SOL-ANM-01-011-007}

En la armónica $a_n=1/(n+1)$, muestra que los bloques de cualquier longitud fija tienden a cero al alejar su inicio. Explica por qué la serie diverge.

## 11.8. Términos que no desaparecen

[]{#MA-EX-ANM-01-011-008}

[]{#MA-SOL-ANM-01-011-008}

Descarta convergencia de las series con términos $a_n=(-1)^n$ y $b_n=(n+1)/(n+2)$.

## 11.9. Acumulación en potencias de dos

[]{#MA-EX-ANM-01-011-009}

[]{#MA-SOL-ANM-01-011-009}

Prueba $s_{2^m-1}\ge1+m/2$ para las sumas parciales armónicas, con $m\in\mathbb N$.

## 11.10. Reparar una falsa prueba

[]{#MA-EX-ANM-01-011-010}

[]{#MA-SOL-ANM-01-011-010}

Diagnostica: «Como $a_n\to0$, cada término de un bloque tardío es menor que $\varepsilon$; por tanto su suma es menor que $\varepsilon$». Repara el argumento cuando todo bloque tiene longitud a lo sumo $M\ge1$.

## 11.11. Telescopaje y corte

[]{#MA-EX-ANM-01-011-011}

[]{#MA-SOL-ANM-01-011-011}

[]{#MA-SEC-ANM-01-011-003}

Para $a_n=1/((n+1)(n+2))$, calcula el total, suma y resto; encuentra un corte que garantice error menor que $1/100$.

## 11.12. Razón negativa

[]{#MA-EX-ANM-01-011-012}

[]{#MA-SOL-ANM-01-011-012}

Calcula la suma y resto de la geométrica $r=-1/2$. Encuentra un corte que certifique error menor que $1/100$.

## 11.13. Todos los casos geométricos

[]{#MA-EX-ANM-01-011-013}

[]{#MA-SOL-ANM-01-011-013}

Clasifica la convergencia de $\sum r^n$ para todos los reales $r$, incluyendo cero y ambos extremos.

## 11.14. La diferencia puede sumar sin magnitudes

[]{#MA-EX-ANM-01-011-014}

[]{#MA-SOL-ANM-01-011-014}

Para $c_n=(-1)^n/(n+1)$, prueba convergencia de la serie $a_n=c_n-c_{n+1}$ y decide si la serie de magnitudes $|a_n|$ converge.

## 11.15. Telescopar no crea destino

[]{#MA-EX-ANM-01-011-015}

[]{#MA-SOL-ANM-01-011-015}

Sea $a_n=c_n-c_{n+1}$. Prueba que su serie converge si y sólo si $c_n$ converge, y relaciona ambos límites.

## 11.16. Dónde se usa la barrera

[]{#MA-EX-ANM-01-011-016}

[]{#MA-SOL-ANM-01-011-016}

[]{#MA-SEC-ANM-01-011-004}

Reconstruye desde el supremo la convergencia de una serie no negativa con totales acotados superiormente.

## 11.17. Comparar y estimar

[]{#MA-EX-ANM-01-011-017}

[]{#MA-SOL-ANM-01-011-017}

Prueba convergencia de $\sum1/(n+2)^2$ y una cota de resto usando el telescopaje de §11.3.

## 11.18. Comparación eventual

[]{#MA-EX-ANM-01-011-018}

[]{#MA-SOL-ANM-01-011-018}

Sea $a_0=100$ y $a_n=2^{-n}$ para $n\ge1$, y sea $b_n=2^{-n}$ en todos los índices. Compara las convergencias y las sumas.

## 11.19. Una barrera para series con signos

[]{#MA-EX-ANM-01-011-019}

[]{#MA-SOL-ANM-01-011-019}

Explica por qué la prueba positiva no se aplica a una serie arbitraria cuyas sumas parciales son acotadas superiormente; aporta un contraejemplo.

## 11.20. Barrera sin fórmula de suma

[]{#MA-EX-ANM-01-011-020}

[]{#MA-SOL-ANM-01-011-020}

Para cualquier sucesión $0\le\theta_n\le1$, prueba convergencia de $a_n=\theta_n/((n+1)(n+2))$ y estima su resto sin identificar su suma.

## 11.21. Triangular finita

[]{#MA-EX-ANM-01-011-021}

[]{#MA-SOL-ANM-01-011-021}

[]{#MA-SEC-ANM-01-011-005}

Prueba la desigualdad $|\sum_{j=q+1}^pa_j|\le\sum_{j=q+1}^p|a_j|$ sin suponer convergencia.

## 11.22. Signos libres

[]{#MA-EX-ANM-01-011-022}

[]{#MA-SOL-ANM-01-011-022}

Sea $\sigma_n\in\{-1,1\}$ en cada índice. Prueba convergencia absoluta de $a_n=\sigma_n2^{-n}$ y estima el resto.

## 11.23. Orden de las hipótesis

[]{#MA-EX-ANM-01-011-023}

[]{#MA-SOL-ANM-01-011-023}

Diagnostica: «Como $|s_n|\le u_n$ y $u_n$ converge, $s_n$ converge». Escribe una prueba correcta de convergencia absoluta implica convergencia.

## 11.24. Sumas y restos

[]{#MA-EX-ANM-01-011-024}

[]{#MA-SOL-ANM-01-011-024}

Si las series de $a$ y $|a|$ tienen sumas $S,A$, demuestra $|S|\le A$ y $|S-s_n|\le A-u_n$.

## 11.25. Localizar igualdad

[]{#MA-EX-ANM-01-011-025}

[]{#MA-SOL-ANM-01-011-025}

Supón que la serie de $a$ converge absolutamente. Prueba que $|S|=A$ si y sólo si todos los términos tienen un signo común, permitiendo ceros.

## 11.26. Lema alternado

[]{#MA-EX-ANM-01-011-026}

[]{#MA-SOL-ANM-01-011-026}

[]{#MA-SEC-ANM-01-011-006}

Prueba que una suma finita alternada de magnitudes decrecientes no negativas está entre cero y la primera magnitud.

## 11.27. Un corte alternado

[]{#MA-EX-ANM-01-011-027}

[]{#MA-SOL-ANM-01-011-027}

Para $a_n=(-1)^n/(n+1)$, prueba convergencia y encuentra un corte que garantice error menor que $1/100$.

## 11.28. El signo del resto

[]{#MA-EX-ANM-01-011-028}

[]{#MA-SOL-ANM-01-011-028}

Para una serie $(-1)^nb_n$ bajo las hipótesis de §11.6, demuestra que $s_n$ queda por encima de la suma si $n$ es par y por debajo si es impar.

## 11.29. Borrar el decrecimiento

[]{#MA-EX-ANM-01-011-029}

[]{#MA-SOL-ANM-01-011-029}

Construye una serie de signos alternados y términos nulos que diverja; explica la hipótesis que falla.

## 11.30. Alternancia eventual

[]{#MA-EX-ANM-01-011-030}

[]{#MA-SOL-ANM-01-011-030}

Supón que desde un índice $m$ los términos son $a_{m+k}=\eta(-1)^kb_k$, con $\eta\in\{-1,1\}$ y $b_k$ decreciente no negativa hacia cero. Prueba convergencia y estima el error en cortes $n\ge m$.

## 11.31. Extremos de grupos

[]{#MA-EX-ANM-01-011-031}

[]{#MA-SOL-ANM-01-011-031}

[]{#MA-SEC-ANM-01-011-007}

Prueba la identidad $t_k=s_{\phi(k)}$ para los grupos consecutivos de §11.7.

## 11.32. Una agrupación engañosa

[]{#MA-EX-ANM-01-011-032}

[]{#MA-SOL-ANM-01-011-032}

Agrupa por parejas la serie $(-1)^n$ y compara su convergencia con la original.

## 11.33. Grupos de longitud acotada

[]{#MA-EX-ANM-01-011-033}

[]{#MA-SOL-ANM-01-011-033}

Prueba que si $a_n\to0$, los grupos tienen longitud a lo sumo $M\ge1$ y la serie agrupada converge, entonces la original converge a la misma suma.

## 11.34. Longitud no necesaria

[]{#MA-EX-ANM-01-011-034}

[]{#MA-SOL-ANM-01-011-034}

Construye una serie convergente agrupada en bloques de longitud no acotada y explica por qué eso no contradice la condición suficiente de grupos cortos.

## 11.35. Excursiones que se reducen

[]{#MA-EX-ANM-01-011-035}

[]{#MA-SOL-ANM-01-011-035}

En el bloque $m\ge1$, coloca $m$ términos $h_m/m$ y luego $m$ términos $-h_m/m$, donde $0\le h_m\le1$. Demuestra que la serie converge si y sólo si $h_m\to0$, y decide su suma.

## 11.36. Una tolerancia estricta

[]{#MA-EX-ANM-01-011-036}

[]{#MA-SOL-ANM-01-011-036}

[]{#MA-SEC-ANM-01-011-008}

Para $\sum2^{-n}$, encuentra el primer índice de corte que garantiza error estrictamente menor que $1/16$, y el número de términos utilizados.

## 11.37. Certificado sin suma conocida

[]{#MA-EX-ANM-01-011-037}

[]{#MA-SOL-ANM-01-011-037}

En la armónica alternada, usa $s_4,s_5$ para obtener un intervalo y una aproximación de error menor que $1/10$.

## 11.38. Linealidad con dominio de validez

[]{#MA-EX-ANM-01-011-038}

[]{#MA-SOL-ANM-01-011-038}

Prueba linealidad de la suma para dos series convergentes. Muestra por qué no permite asignar sumas a dos series divergentes.

## 11.39. Cambiar sólo un prefijo

[]{#MA-EX-ANM-01-011-039}

[]{#MA-SOL-ANM-01-011-039}

Si $a$ y $b$ coinciden para $n\ge m$, demuestra equivalencia de convergencia y relaciona sus sumas, incluyendo $m=0$.

## 11.40. Dos mecanismos en una sola serie

[]{#MA-EX-ANM-01-011-040}

[]{#MA-SOL-ANM-01-011-040}

Sea $a_n=(-1)^n/(n+1)+e_n$ con $|e_n|\le2^{-n}$. Prueba convergencia, una cota de resto y que la convergencia es condicional.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html)
