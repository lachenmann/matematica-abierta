---
content-id: MA-BCH-0307
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-026-EJERCICIOS
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
title: Ejercicios — Capítulo 26
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C26_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-microcontroles.html)

Soluciones completas en ANM-C26_SOLUCIONES.md. Declara dominio común, entrada fija, dependencia del corte y existencia de cada operación comparada. Distingue refutación puntual, infractor móvil y diagonal dada.

## 26.1. Fila y columna

[]{#MA-EX-ANM-01-026-001}

[]{#MA-SOL-ANM-01-026-001}

[]{#MA-SEC-ANM-01-026-001}

Para $F(n,x)=(n+1)x$ en $\mathbb N\times\mathbb R$, identifica filas, columnas y las entradas donde hay límite real.

## 26.2. El dominio que se conserva

[]{#MA-EX-ANM-01-026-002}

[]{#MA-SOL-ANM-01-026-002}

Las fórmulas $f_n(x)=1/(x-n)$ tienen dominio $\mathbb R\setminus\{n\}$. Encuentra un dominio común y el límite allí.

## 26.3. Alternancia dependiente de la entrada

[]{#MA-EX-ANM-01-026-003}

[]{#MA-SOL-ANM-01-026-003}

Calcula el conjunto de convergencia de $f_n(x)=(-1)^n(x-2)$ en $\mathbb R$.

## 26.4. Grafo del límite

[]{#MA-EX-ANM-01-026-004}

[]{#MA-SOL-ANM-01-026-004}

Explica por qué la existencia de límite real en cada columna de $X$ define una función sin escoger un límite arbitrario por entrada.

## 26.5. Toda entrada salvo una

[]{#MA-EX-ANM-01-026-005}

[]{#MA-SOL-ANM-01-026-005}

Define $f_n(x)=1$ si $x=n$ y $0$ en otro caso, en $\mathbb R$. Determina su límite y explica por qué las gráficas no bastan.

## 26.6. Certificado explícito

[]{#MA-EX-ANM-01-026-006}

[]{#MA-SOL-ANM-01-026-006}

[]{#MA-SEC-ANM-01-026-002}

Da un corte para $f_n(x)=(x^2+1)/(n+1)\to0$ en $\mathbb R$ con error estricto menor que $\varepsilon$.

## 26.7. Negar en el orden correcto

[]{#MA-EX-ANM-01-026-007}

[]{#MA-SOL-ANM-01-026-007}

Escribe la negación de convergencia puntual hacia una candidata $f$ y úsala para refutar $f_n(x)=(-1)^n$ hacia cero en un dominio no vacío.

## 26.8. Un infractor móvil

[]{#MA-EX-ANM-01-026-008}

[]{#MA-SOL-ANM-01-026-008}

Para $f_n(x)=x/(n+1)$ en $\mathbb R$, elige ante cada corte una entrada con error1. ¿Qué queda refutado?

## 26.9. Reunión finita de obligaciones

[]{#MA-EX-ANM-01-026-009}

[]{#MA-SOL-ANM-01-026-009}

Para $f_n(x)=x/(n+1)$ y $A=\{-3,0,5\}$, produce un corte simultáneo y justifica la generalización a un conjunto finito.

## 26.10. Umbral mínimo

[]{#MA-EX-ANM-01-026-010}

[]{#MA-SOL-ANM-01-026-010}

Para $f_n(x)=x/(n+1)$ calcula $\tau(x,\varepsilon)$ y comprueba la frontera estricta.

## 26.11. Dos errores y una cota

[]{#MA-EX-ANM-01-026-011}

[]{#MA-SOL-ANM-01-026-011}

[]{#MA-SEC-ANM-01-026-003}

Prueba directamente que el producto de dos familias puntualmente convergentes converge al producto de sus límites.

## 26.12. Ceros por filas

[]{#MA-EX-ANM-01-026-012}

[]{#MA-SOL-ANM-01-026-012}

En $X=(0,1]$ sea $g_n(x)=x-1/(n+1)$. Prueba convergencia puntual y explica por qué $1/g_n$ no define una familia en todo $X$.

## 26.13. Orden eventual

[]{#MA-EX-ANM-01-026-013}

[]{#MA-SOL-ANM-01-026-013}

Si $f_n\to f$, $g_n\to g$ puntualmente y para cada $x$ hay un corte con $f_n(x)\le g_n(x)$ después de él, demuestra $f\le g$.

## 26.14. Filas acotadas, límite sin cota

[]{#MA-EX-ANM-01-026-014}

[]{#MA-SOL-ANM-01-026-014}

Analiza $u_n(x)=\min(n,x)$ en $[0,\infty)$ respecto de acotación de filas, columnas, límite y familia completa.

## 26.15. Componer dentro del tipo

[]{#MA-EX-ANM-01-026-015}

[]{#MA-SOL-ANM-01-026-015}

Si $f_n\to f$ puntualmente y todos sus valores y los de $f$ son no negativos, demuestra $\sqrt{f_n}\to\sqrt f$ sin suponer continuidad de las filas.

## 26.16. Potencias y extremos

[]{#MA-EX-ANM-01-026-016}

[]{#MA-SOL-ANM-01-026-016}

[]{#MA-SEC-ANM-01-026-004}

Demuestra el límite puntual de $p_0=1$, $p_n(x)=x^n$ para $n\ge1$, en $[0,1]$, sin logaritmos.

## 26.17. Discontinuidad relativa

[]{#MA-EX-ANM-01-026-017}

[]{#MA-SOL-ANM-01-026-017}

Refuta continuidad del límite de las potencias en1 con un testigo para cada radio.

## 26.18. Una infracción en cada etapa

[]{#MA-EX-ANM-01-026-018}

[]{#MA-SOL-ANM-01-026-018}

Con $x_n=1-1/[2(n+1)]$, prueba $p_n(x_n)>1/2$ y determina el alcance de la conclusión.

## 26.19. Cambiar el dominio

[]{#MA-EX-ANM-01-026-019}

[]{#MA-SOL-ANM-01-026-019}

Compara las potencias en $[0,c]$, $0<c<1$, y en $[0,1)$.

## 26.20. Dominio ampliado

[]{#MA-EX-ANM-01-026-020}

[]{#MA-SOL-ANM-01-026-020}

Calcula el conjunto de convergencia real de la misma familia de potencias en $[-1,1]$.

## 26.21. Capa racional

[]{#MA-EX-ANM-01-026-021}

[]{#MA-SOL-ANM-01-026-021}

[]{#MA-SEC-ANM-01-026-005}

Para $a_n(x)=(n+1)x/[1+(n+1)x]$ en $[0,1]$, prueba el límite y su fallo de continuidad en0.

## 26.22. Dos rutas, dos destinos

[]{#MA-EX-ANM-01-026-022}

[]{#MA-SOL-ANM-01-026-022}

Calcula $a_n(1/(n+1))$ y $a_n(1/(n+1)^2)$ y explica por qué no contradicen el límite puntual.

## 26.23. Una escala intermedia

[]{#MA-EX-ANM-01-026-023}

[]{#MA-SOL-ANM-01-026-023}

Para $w_n=1/\sqrt{n+1}$ calcula el destino de $a_n(w_n)$ y justifica las raíces y la convergencia.

## 26.24. Límites iterados

[]{#MA-EX-ANM-01-026-024}

[]{#MA-SOL-ANM-01-026-024}

Calcula las dos operaciones iteradas en $n\to\infty$ y $x\to0^+$ para $a_n$.

## 26.25. Reparar un prefijo fuera del dominio

[]{#MA-EX-ANM-01-026-025}

[]{#MA-SOL-ANM-01-026-025}

Para $c>0$ construye una ruta en $[0,1]$ que coincida eventualmente con $c/(n+1)$ y calcula las salidas de $a_n$.

## 26.26. Tiendas continuas

[]{#MA-EX-ANM-01-026-026}

[]{#MA-SOL-ANM-01-026-026}

[]{#MA-SEC-ANM-01-026-006}

Para $k=n+3$ demuestra continuidad, soporte y convergencia puntual a cero de $t_n(x)=\max(0,1-|kx-2|)$ en $[0,1]$.

## 26.27. Seguir el centro

[]{#MA-EX-ANM-01-026-027}

[]{#MA-SOL-ANM-01-026-027}

Encuentra una ruta convergente al origen que produzca salidas constantes1 en las tiendas. ¿Bastan límite continuo y cota común para evitarlo?

## 26.28. Certificar el área

[]{#MA-EX-ANM-01-026-028}

[]{#MA-SOL-ANM-01-026-028}

Calcula $\int_0^1t_n$ por ramas, acreditando existencia antes del valor.

## 26.29. Altura que compensa anchura

[]{#MA-EX-ANM-01-026-029}

[]{#MA-SOL-ANM-01-026-029}

Para $b_n=(n+3)t_n$ demuestra convergencia puntual y compara límite de integrales e integral del límite.

## 26.30. Pendientes sin constante común

[]{#MA-EX-ANM-01-026-030}

[]{#MA-SOL-ANM-01-026-030}

Demuestra que las tiendas $t_n$ no satisfacen una cota Lipschitz con la misma constante para todas las filas.

## 26.31. Límite sin integral propia

[]{#MA-EX-ANM-01-026-031}

[]{#MA-SOL-ANM-01-026-031}

[]{#MA-SEC-ANM-01-026-007}

Con $d_n=\mathbf1_{E_{n+1}}$ de C25, prueba límite puntual y explica qué comparación integral está mal tipada.

## 26.32. Calcular las derivadas

[]{#MA-EX-ANM-01-026-032}

[]{#MA-SOL-ANM-01-026-032}

Para $h_n(x)=x/[1+(n+1)x^2]$ en $\mathbb R$, calcula derivadas y demuestra convergencia puntual de valores y derivadas.

## 26.33. Un máximo exacto de error

[]{#MA-EX-ANM-01-026-033}

[]{#MA-SOL-ANM-01-026-033}

Prueba la cota global $|h_n(x)|\le1/[2\sqrt{n+1}]$ y que se alcanza.

## 26.34. Auditar la prueba triangular

[]{#MA-EX-ANM-01-026-034}

[]{#MA-SOL-ANM-01-026-034}

En el intento de deducir continuidad del límite puntual de funciones continuas, identifica el paso no autorizado.

## 26.35. Clasificar tres fracasos

[]{#MA-EX-ANM-01-026-035}

[]{#MA-SOL-ANM-01-026-035}

Compara potencias, tiendas normalizadas y $d_n$ según qué propiedad falla y qué objetos existen.

## 26.36. Transportar una cota común de proximidad

[]{#MA-EX-ANM-01-026-036}

[]{#MA-SOL-ANM-01-026-036}

[]{#MA-SEC-ANM-01-026-008}

Si $f_n\to f$ puntualmente y todas las filas son Lipschitz con la misma constante $L\ge0$, prueba que $f$ lo es y es continua.

## 26.37. Diagonal con presupuesto común

[]{#MA-EX-ANM-01-026-037}

[]{#MA-SOL-ANM-01-026-037}

Bajo la hipótesis del ejercicio anterior, si una ruta dada $x_n\to x\in X$ permanece en $X$, prueba $f_n(x_n)\to f(x)$.

## 26.38. Monotonía sin barrera universal

[]{#MA-EX-ANM-01-026-038}

[]{#MA-SOL-ANM-01-026-038}

Prueba existencia de límite puntual para columnas crecientes acotadas por una barrera que puede depender de la entrada.

## 26.39. Monotonía del índice y de la variable

[]{#MA-EX-ANM-01-026-039}

[]{#MA-SOL-ANM-01-026-039}

Construye una familia creciente por columnas cuyas filas no sean crecientes ni decrecientes en su variable.

## 26.40. Un certificado y su límite de alcance

[]{#MA-EX-ANM-01-026-040}

[]{#MA-SOL-ANM-01-026-040}

Para $f_n(x)=x+1/(n+1)$ en $\mathbb R$, verifica límite puntual, cota Lipschitz común y toda diagonal $x_n\to x$. Compáralo con $t_n$.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-microcontroles.html)
