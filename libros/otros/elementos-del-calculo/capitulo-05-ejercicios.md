---
title: Capítulo 5 — Ejercicios
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-12'
license: GFDL-1.3-or-later
areas:
- calculo
- analisis
- fundamentos
level: intermedio
topics:
- calculo-de-una-variable
- historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
  - role: idea
    note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra
      independiente.'
source-id: EDC-C05-EJERCICIOS
source-sha256: f1b753e17b2e842ed7694c0b37d67a3fa9b687dcb657fc09ce8c5537e5986f3d
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-05.html) · [Ejercicios](capitulo-05-ejercicios.html) · [Soluciones](capitulo-05-soluciones.html) · [Notas históricas](capitulo-05-notas.html)

Cada ejercicio se resuelve con los resultados de C00–C05, **sin invocar el Teorema Fundamental del Cálculo**, que aparecerá en C06. Es necesario distinguir particiones, etiquetas, integrabilidad, signo de la función y existencia de primitivas. Toda respuesta tiene un desarrollo independiente con ID correspondiente en [el solucionario](capitulo-05-soluciones.html).

## A. Definiciones, supremos y lenguaje

**Ejercicio 5.1 (`EDC-C05-EXR-001`).** Escriba las definiciones de $L(f,P)$, $U(f,P)$, $\underline{\mathcal I}(f)$ y $\overline{\mathcal I}(f)$. ¿Por qué la acotación de $f$ es importante? Distinga supremo e ínfimo de máximo y mínimo.

**Ejercicio 5.2 (`EDC-C05-EXR-002`).** Sea $f:[0,1]\to\mathbb R$ dada por $f(0)=2$ y $f(x)=x$ si $0<x\le1$. Calcule el ínfimo y el supremo de $f$ en $[0,1]$, e indique cuáles son alcanzados.

**Ejercicio 5.3 (`EDC-C05-EXR-003`).** Para $f(x)=x^2$ en $[0,1]$ y $P=\{0,1/2,1\}$, calcule $L(f,P)$, $U(f,P)$ y $U-L$. ¿Cuál de estas cantidades cambia si se eligen otras etiquetas?

**Ejercicio 5.4 (`EDC-C05-EXR-004`).** Para $f(x)=x$ en $[0,1]$, use $P=\{0,1/3,2/3,1\}$ y etiquetas $\xi=(0,1/2,1)$. Calcule $S(f;P,\xi)$, $L(f,P)$ y $U(f,P)$.

## B. Refinamientos y compatibilidad

**Ejercicio 5.5 (`EDC-C05-EXR-005`).** Parta de $P=\{0,1\}$ para $f(x)=x^2$. Inserte $1/2$ y compruebe numéricamente las cuatro desigualdades del Lema 5.1.

**Ejercicio 5.6 (`EDC-C05-EXR-006`).** Encuentre el refinamiento común de $P=\{0,1/2,1\}$ y $Q=\{0,1/3,2/3,1\}$. Demuestre que $L(f,P)\le U(f,Q)$ para una función acotada arbitraria, sin suponer monotonía.

**Ejercicio 5.7 (`EDC-C05-EXR-007`).** Para $d=\mathbf 1_{\mathbb Q\cap[0,1]}$, encuentre $L(d,P)$ y $U(d,P)$ para cualquier partición y determine ambas integrales de Darboux. ¿Por qué no es integrable?

**Ejercicio 5.8 (`EDC-C05-EXR-008`).** Sea $h(x)=5$ si $x=1/2$ y $h(x)=0$ en los demás puntos de $[0,1]$. Encuentre su integral y una cota explícita para $U(h,P)-L(h,P)$ en función de $\|P\|$.

## C. Criterios de existencia y ejemplos

**Ejercicio 5.9 (`EDC-C05-EXR-009`).** Sea $s(x)=0$ para $x<1/3$ y $s(x)=1$ para $x\ge1/3$ en $[0,1]$. Pruebe su integrabilidad y determine la integral usando particiones adaptadas al salto.

**Ejercicio 5.10 (`EDC-C05-EXR-010`).** Para $f(x)=-x$ en $[0,1]$, calcule la diferencia $U(f,P)-L(f,P)$ para una partición arbitraria y deduzca su integrabilidad.

**Ejercicio 5.11 (`EDC-C05-EXR-011`).** Demuestre que $f(x)=\sin x$ es integrable en $[0,\pi]$ sin calcular su integral. Indique el teorema preciso usado y por qué no hace falta una primitiva.

**Ejercicio 5.12 (`EDC-C05-EXR-012`).** Suponga que $f:[0,2]\to\mathbb R$ es derivable, continua hasta los extremos, y $|f'(x)|\le3$ para $0<x<2$. Obtenga una cota de $U(f,P)-L(f,P)$ en términos de la finura y dé una condición suficiente para que sea menor que $10^{-3}$.

**Ejercicio 5.13 (`EDC-C05-EXR-013`).** Explique por qué la convergencia a $0$ de las sumas de la función de Dirichlet sobre particiones uniformes con **todas** las muestras irracionales no demuestra que esa función sea integrable.

**Ejercicio 5.14 (`EDC-C05-EXR-014`).** Construya una sucesión de particiones con número de intervalos tendiendo a infinito pero finura constante $1/2$. Explique qué cuantificador del Teorema 5.3 no se cumple.

## D. Demostraciones y auditoría de hipótesis

**Ejercicio 5.15 (`EDC-C05-EXR-015`).** Pruebe la dirección difícil del criterio de Darboux: si $\sup_P L(f,P)=\inf_P U(f,P)$, explique cómo obtener una **única partición** con $U-L<\varepsilon$ a partir de dos particiones iniciales distintas.

**Ejercicio 5.16 (`EDC-C05-EXR-016`).** Para la función de salto $s_c$ del §5.6, demuestre directamente que toda suma etiquetada sobre una partición de finura $\delta$ difiere de $b-c$ en no más de $2\delta$. ¿Qué muestra sobre el requisito de muestras arbitrarias?

**Ejercicio 5.17 (`EDC-C05-EXR-017`).** Demuestre desde la definición por sumas etiquetadas que $\int_a^b(f+g)=\int_a^bf+\int_a^bg$ para funciones integrables. Controle el orden de los cuantificadores de $\varepsilon$ y $\delta$.

**Ejercicio 5.18 (`EDC-C05-EXR-018`).** Demuestre que, aunque $f,g$ sean integrables, la fórmula $\int_0^1fg=(\int_0^1f)(\int_0^1g)$ no es universalmente válida; tome $f(x)=g(x)=x$.

**Ejercicio 5.19 (`EDC-C05-EXR-019`).** Calcule $\int_0^1|2x-1|\,dx$ sin emplear primitivas. Justifique la partición usada y el resultado geométrico/lineal necesario.

**Ejercicio 5.20 (`EDC-C05-EXR-020`).** Si $f,g$ son integrables en $[0,4]$ y $|f(x)-g(x)|\le0.01$ para todo $x$, obtenga la mejor cota que se deduce inmediatamente de la Proposición 5.2 para la diferencia de sus integrales.

## E. Aditividad, orientación y cálculo

**Ejercicio 5.21 (`EDC-C05-EXR-021`).** En $[0,2]$, sea $s(x)=0$ para $x<1$ y $s(x)=3$ para $x\ge1$. Calcule las integrales en $[0,1]$, $[1,2]$ y $[0,2]$, y compruebe la aditividad con cuidado del valor en el punto de salto.

**Ejercicio 5.22 (`EDC-C05-EXR-022`).** Demuestre que una función integrable en $[a,b]$ lo es en cada subintervalo $[u,v]\subset[a,b]$, controlando qué ocurre si $u=a$ o $v=b$.

**Ejercicio 5.23 (`EDC-C05-EXR-023`).** Evalúe $\int_3^1 2x\,dx$ sin usar el Teorema Fundamental. Construya la integral de la función afín en $[1,3]$ mediante sumas o geometría elemental y aplique la convención de orientación.

**Ejercicio 5.24 (`EDC-C05-EXR-024`).** Calcule $\int_0^1(1-x)^2\,dx$ mediante expansión polinómica y las cuadraturas ya demostradas en C04 y C05.

## F. Valor medio, contraejemplos y estabilidad

**Ejercicio 5.25 (`EDC-C05-EXR-025`).** Para $f(x)=x^2$ en $[0,1]$, encuentre un punto $c$ que cumpla el teorema del valor medio integral y justifique su existencia sin resolver una ecuación integral por primitivas.

**Ejercicio 5.26 (`EDC-C05-EXR-026`).** Sea $f(x)=0$ para $x\le1/2$ y $f(x)=1$ para $x>1/2$ en $[0,1]$. Demuestre su integrabilidad, calcule el promedio integral y explique por qué ningún $c$ satisface $f(c)$ igual a ese promedio.

**Ejercicio 5.27 (`EDC-C05-EXR-027`).** Modifique $f(x)=x^2$ sólo en $x=1/2$, asignando allí el valor $100$. Pruebe que la nueva función sigue siendo integrable y tiene integral $1/3$.

**Ejercicio 5.28 (`EDC-C05-EXR-028`).** Reconstruya el argumento del producto de funciones integrables. ¿Por qué basta la cota $\operatorname{osc}_I(fg)\le A\operatorname{osc}_I(g)+B\operatorname{osc}_I(f)$ y para qué sirve un refinamiento común?

**Ejercicio 5.29 (`EDC-C05-EXR-029`).** Explique por qué $\int_0^3(-2)\,dx=-6$ no contradice que toda área geométrica sea no negativa. Indique también las unidades si $-2$ representa metros por segundo y el intervalo mide segundos.

## G. Síntesis rigurosa

**Ejercicio 5.30 (`EDC-C05-EXR-030`).** Para $\lambda\ge0$ defina en $[0,1]$ la función $f_\lambda(x)=x^2+\lambda\mathbf1_{[1/2,1]}(x)$. Pruebe su integrabilidad, calcule su integral **sin primitivas** y obtenga una cota del error de una suma etiquetada que dependa de $\lambda$ y $\|P\|$ y tienda a cero para toda familia de particiones finas.

---

**Correspondencia canónica:** `EDC-C05-EXR-001--030` con `EDC-C05-SOL-001--030`. El banco no incrementa el contador de capítulos; sus soluciones se publican en archivo independiente.
