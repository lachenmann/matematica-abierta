---
title: Capítulo 9 — Ejercicios
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
source-id: EDC-C09-EJERCICIOS
source-sha256: baf9d3ccba78229f2fe72b0537de3153d8aac84e2156e61b2a2ef46887a44f0b
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-09.md) · [Ejercicios](capitulo-09-ejercicios.md) · [Soluciones](capitulo-09-soluciones.md) · [Notas históricas](capitulo-09-notas.md)

El propósito de los ejercicios no es memorizar desarrollos: se debe distinguir una identidad polinómica, un polinomio local, una estimación finita y una serie infinita. Justifique en cada caso el intervalo, las hipótesis de derivabilidad y, si corresponde, el paso al límite. Las soluciones independientes aparecen en [el archivo correspondiente](capitulo-09-soluciones.md). Sólo se utilizan C00–C09.

## A. El binomio de Newton y las series binomiales

**Ejercicio 9.1 (`EDC-C09-EXR-001`).** Demuestre por inducción $(1+x)^m=\sum_{k=0}^{m}\binom mkx^k$ para $m\in\mathbb N_0$. Indique dónde interviene la identidad de Pascal y por qué la igualdad no requiere ninguna consideración sobre convergencia.

**Ejercicio 9.2 (`EDC-C09-EXR-002`).** Calcule los coeficientes $\binom{1/2}{k}$, $0\le k\le4$, y escriba el polinomio de orden cuatro de la expansión binomial de $\sqrt{1+x}$. Indique su intervalo interior de representación probado.

**Ejercicio 9.3 (`EDC-C09-EXR-003`).** Para $\alpha=-3/2$ demuestre que $\sum_{n\ge0}\binom\alpha n x^n$ tiene radio exactamente uno y representa $(1+x)^{-3/2}$ para $|x|<1$. ¿Autoriza el radio afirmar convergencia en $x=-1$?

**Ejercicio 9.4 (`EDC-C09-EXR-004`).** Deduzca con el Teorema 9.2 la identidad $(1+x)^{-2}=\sum_{n\ge0}(-1)^n(n+1)x^n$ para $|x|<1$. Verifique la recurrencia de coeficientes y explique la conexión con la serie geométrica derivada en C08.

**Ejercicio 9.5 (`EDC-C09-EXR-005`).** Compare la serie binomial para $\alpha=3$ y para $\alpha=1/2$. Identifique cuál termina, el radio de la otra, y por qué un resultado demostrado sólo para $|x|<1$ no permite evaluar automáticamente el extremo $x=-1$.

**Ejercicio 9.6 (`EDC-C09-EXR-006`).** Sea $F(x)=\sum_{n\ge0}\binom\alpha n x^n$. Demuestre, dentro de su radio positivo, que $(1+x)F'=\alpha F$ y $F(0)=1$; explique por qué estas condiciones identifican $F$ como $(1+x)^\alpha$ en $(-1,1)$ sin utilizar el capítulo 10.

## B. Reconstrucción polinómica desde datos de derivadas

**Ejercicio 9.7 (`EDC-C09-EXR-007`).** Halle $T_{2,0}(e^x)$ y compruebe sus valores de derivadas de órdenes $0,1,2$ en cero.

**Ejercicio 9.8 (`EDC-C09-EXR-008`).** Calcule $T_{4,0}(\sin x)$ y explique por qué carece de término de grado cuatro. Encuentre las derivadas que justifican sus coeficientes.

**Ejercicio 9.9 (`EDC-C09-EXR-009`).** Obtenga $T_{3,1}(\ln x)$ y especifique el dominio real de $\ln x$ y las hipótesis del resto de Lagrange para $x$ en un compacto positivo.

**Ejercicio 9.10 (`EDC-C09-EXR-010`).** Halle $T_{2,1}(\sqrt{x})$ y explique por qué el polinomio no puede utilizarse sin estimación para aproximar $\sqrt{x}$ arbitrariamente lejos de $x=1$.

**Ejercicio 9.11 (`EDC-C09-EXR-011`).** Calcule $T_{3,0}(1/(1-x))$ y el error **exacto** en $x=1/2$; distinga el error exacto de una cota de Lagrange.

**Ejercicio 9.12 (`EDC-C09-EXR-012`).** Determine el único polinomio de grado a lo sumo tres con $P(a)=2$, $P'(a)=-1$, $P''(a)=4$ y $P'''(a)=0$. Pruebe su unicidad, no sólo la fórmula.

## C. Restos, cotas y tolerancias

**Ejercicio 9.13 (`EDC-C09-EXR-013`).** Aproxime $\cos(1/5)$ por $T_{3,0}(\cos x)$ y obtenga una cota explícita con el Teorema 9.4. No use una identidad de series sin justificar el error.

**Ejercicio 9.14 (`EDC-C09-EXR-014`).** Aproxime $e^{1/10}$ por $T_{3,0}(e^x)$ y pruebe un error menor que $1/80000$, utilizando $e<3$ y una cota de Lagrange.

**Ejercicio 9.15 (`EDC-C09-EXR-015`).** Para $f(x)=1/(1+x)$ en $[0,1/2]$, compare el resto exacto del polinomio $T_{2,0}f=1-x+x^2$ con la cota de Lagrange obtenida de $|f'''|\le6$. Evalúe ambas cotas en $x=1/2$.

**Ejercicio 9.16 (`EDC-C09-EXR-016`).** A partir de Taylor–Peano, pruebe $\sin x=x-x^3/6+o(|x|^3)$ cuando $x\to0$. Explique por qué el símbolo $o$ no permite concluir por sí solo una identidad de series para todo $x$.

**Ejercicio 9.17 (`EDC-C09-EXR-017`).** Demuestre con el resto integral $e^x-1-x=\int_0^x e^t(x-t)\,dt$, también para $x<0$. Compruebe la orientación y el signo del resto.

**Ejercicio 9.18 (`EDC-C09-EXR-018`).** Si $f\in C^{n+1}([a,b])$ y $|f^{(n+1)}|\le M$, deduzca desde la fórmula integral que $|f(x)-T_{n,a}f(x)|\le M|x-a|^{n+1}/(n+1)!$ para cualquier $x\in[a,b]$.

## D. Series representativas, radio y no analiticidad

**Ejercicio 9.19 (`EDC-C09-EXR-019`).** Deduzca los desarrollos de $\sin x$ y $\cos x$ desde las cotas finitas del capítulo. Aclare por qué la representación es válida para todo $x\in\mathbb R$.

**Ejercicio 9.20 (`EDC-C09-EXR-020`).** Use $T_{4,0}(e^x)$ para aproximar $e^{-1}$ y demuestre que el error absoluto es a lo sumo $1/120$. Escriba el valor racional aproximante.

**Ejercicio 9.21 (`EDC-C09-EXR-021`).** Identifique los coeficientes de Maclaurin de $\ln(1+x)$ para $|x|<1$. Dé una cota de error al sumar los primeros $N$ términos en $x=1/2$, sin invocar un teorema de Taylor de borde.

**Ejercicio 9.22 (`EDC-C09-EXR-022`).** Compare el radio de Taylor en $0$ de $(1+x)^{-1}$ y el de $(1+x)^3$. Demuestre por qué un exponente entero no negativo produce una excepción al radio uno.

**Ejercicio 9.23 (`EDC-C09-EXR-023`).** Para $g(0)=0$ y $g(x)=e^{-1/x^2}$ si $x\ne0$, demuestre que $g'(0)=g''(0)=0$ y explique la inducción general que produce $g^{(k)}(0)=0$ para todo $k$.

**Ejercicio 9.24 (`EDC-C09-EXR-024`).** Muestre que la serie de Maclaurin de $g$ del problema anterior converge en todo punto, pero no representa a $g$ fuera de cero. Explique con cuantificadores por qué ello no contradice el resto de Peano.

## E. Algoritmos de aproximación y control de inferencias

**Ejercicio 9.25 (`EDC-C09-EXR-025`).** Aplique dos iteraciones de Newton a $f(x)=x^2-2$ empezando por $x_0=3/2$. Obtenga $x_1,x_2$ exactamente y deduzca una cota local del error hacia $r=\sqrt2$ bajo las hipótesis de $[r-2/5,r+2/5]$.

**Ejercicio 9.26 (`EDC-C09-EXR-026`).** Estudie por qué la fórmula de Newton no puede iniciarse en $x_0=0$ para $f(x)=x^3-1$. Señale qué hipótesis del Teorema 9.10 falla y qué conclusión **no** se puede extraer sobre todas las semillas posibles.

**Ejercicio 9.27 (`EDC-C09-EXR-027`).** Refute cada afirmación: (a) «si $f\in C^\infty$, la serie de Taylor coincide con $f$»; (b) «si $f$ está definida en $x$, su serie de Taylor en cero converge en $x$»; (c) «el polinomio de Taylor de orden $n$ siempre tiene grado exactamente $n$».

**Ejercicio 9.28 (`EDC-C09-EXR-028`).** Demuestre la unicidad de los coeficientes de una representación $f(x)=\sum_{n\ge0}a_n(x-c)^n$ de radio positivo y explique por qué este resultado es una implicación **condicionada** y no una prueba de que toda función suave admite serie convergente.

## F. Desafíos de síntesis

**Ejercicio 9.29 (`EDC-C09-EXR-029`).** Para $f(x)=\sqrt{1+x}$, calcule $T_{2,0}f(1/4)$, pruebe con Lagrange que el error es a lo sumo $1/1024$ y explique cómo la igualdad binomial de Newton garantiza también representación por la serie completa en ese punto.

**Ejercicio 9.30 (`EDC-C09-EXR-030`).** **Síntesis:** sea $f(x)=e^x\cos x$. (a) Calcule $T_{3,0}f$. (b) Demuestre para $0\le x\le1/2$ que $|f(x)-T_{3,0}f(x)|\le e^{1/2}x^4/6$. (c) Explique por qué esta **cota finita** no afirma automáticamente que la serie de Taylor de una función arbitraria converja a ella; indique cuál de los teoremas de C09 aporta el paso lógico faltante.

---

**Correspondencia editorial:** Los IDs `EDC-C09-EXR-001--030` se resuelven uno por uno en [EDC-C09-SOLUCIONES](capitulo-09-soluciones.md), sin utilizar C10 ni C11.
