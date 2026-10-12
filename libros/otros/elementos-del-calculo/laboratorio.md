---
title: Laboratorio de problemas de investigación — *Elementos del cálculo*
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
source-id: EDC_LABORATORIO_PROBLEMAS
source-sha256: affd10532091228d9821a7d612f0a565ba6377007936b79b4a0584588ab866d6
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

Estos problemas complementan, **sin sustituir ni renumerar**, los 338 ejercicios y soluciones del cuerpo del libro. La pregunta se plantea antes de ofrecer un procedimiento, y exige demostrar por qué funciona. Cada solución se encuentra por el mismo identificador en [el solucionario independiente](laboratorio-soluciones.html). Los problemas se proponen con las herramientas disponibles **hasta** el capítulo indicado; ninguno presupone Lebesgue, espacios métricos abstractos o Picard–Lindelöf general.

## Variación y fundamentos

### INV-C00-01 — La iteración de Herón desde la completitud

Sea $s=\sqrt2$, cuya existencia y unicidad se demostraron en C00. Comenzando con $x_0=2$, defina $x_{n+1}=\frac12(x_n+2/x_n)$. Demuestre directamente, **sin derivadas**, que $x_n\ge s$, que $x_n$ es decreciente, que converge a $s$ y que el error verifica

$$
0\le x_{n+1}-s=\frac{(x_n-s)^2}{2x_n}\le\frac{(x_n-s)^2}{2s}.
$$

¿Por qué resulta más informativo el error exacto que observar sólo valores decimales?

### INV-C01-01 — Todas las tangentes a una cúbica por un punto dado

Para $f(x)=x^3$, use sólo el cociente incremental y la definición de tangente de C01. Dado $P=(0,b)$, $b\in\mathbb R$, determine **todas** las tangentes diferenciales a la gráfica que pasan por $P$. Compare el número de tangentes con el caso de la parábola $y=x^2$ del ejercicio 1.22. Explique por qué una intersección única no caracteriza una tangente general.

### INV-C02-01 — Una identidad trigonométrica que no depende de derivar

Para $x>0$, pruebe que $\arctan x+\arctan(1/x)=\pi/2$ utilizando identidades de suma y los intervalos de las funciones inversas. Compruebe también que la derivada de la suma es cero **donde está definida**. ¿Por qué esa última comprobación, por sí sola y antes de demostrar el teorema del valor medio, no constituye la demostración solicitada?

### INV-C03-01 — De la concavidad del logaritmo a AM–GM ponderada

Sean $x_1,\ldots,x_n>0$ y $w_1,\ldots,w_n\ge0$ con $\sum w_i=1$. A partir de la concavidad estricta de $\ln$ demostrada en C03, deduzca por inducción

$$
\prod_{i=1}^n x_i^{w_i}\le\sum_{i=1}^n w_i x_i.
$$

Determine cuándo hay igualdad, excluyendo los pesos nulos. Explique el papel del orden real y de la monotonía de la exponencial.

## Cuadraturas e integración

### INV-C04-01 — ¿Cuántas generaciones bastan?

En la construcción parabólica de C04, las generaciones $0$ a $n-1$ poseen área poligonal $P_n=\frac{4T}{3}(1-4^{-n})$. Sin usar integrales, pruebe que el **error relativo respecto del valor compatible $A=4T/3$** es exactamente $4^{-n}$. Determine el menor entero $n$ que garantiza error relativo menor que $10^{-6}$ y explique por qué una suma finita no debe confundirse con el área de la región curva.

### INV-C05-01 — Una función con infinitas discontinuidades pero integrable

Defina $\tau:[0,1]\to\mathbb R$ por $\tau(x)=0$ si $x$ es irracional, y $\tau(p/q)=1/q$ si $p/q$ es racional en forma irreducible con $q\ge1$. Pruebe que $\tau$ es Riemann–Darboux integrable y que $\int_0^1\tau=0$. Debe construir una partición con diferencia superior–inferior arbitrariamente pequeña, usando la **finitud** de los racionales con denominador $q\le N$. No puede apelar a criterios de medida de conjuntos de discontinuidad.

### INV-C06-01 — Igual integral no significa igual acumulación

Sea $f(x)=x$ y $g(x)=1-x$ sobre $[0,1]$. Verifique que las integrales en todo el intervalo son iguales, pero que sus funciones acumuladoras $F(t)=\int_0^t f$ y $G(t)=\int_0^t g$ son distintas para cada $0<t<1$. Interprete el resultado por la primera parte del Teorema Fundamental del Cálculo.

### INV-C07-01 — Un área logarítmica por dos caminos

Calcule $I=\int_0^1\ln(1+x)\,dx$ mediante (a) integración por partes y (b) un cambio de variable seguido de la verificación directa de una primitiva. Compare los dos razonamientos y justifique que no existe una singularidad en $[0,1]$.

### INV-C07-02 — Sustitución con una trayectoria que retrocede

Sea $\phi(t)=t^2$ en $[-1,1]$. Compruebe, **sin exigir monotonía**,

$$
\int_{-1}^{1}\phi(t)\phi'(t)\,dt=0
$$

por la sustitución orientada de C07 y, de forma independiente, por la paridad de un polinomio. Explique por qué sustituir arbitrariamente por una integral no orientada con límites ordenados perdería información.

## Series, aproximación y dinámica

### INV-C08-01 — La misma identidad obtenida dos veces

Para $|x|<1$, pruebe $\sum_{n=0}^{\infty}(n+1)x^n=(1-x)^{-2}$ de dos formas: producto de Cauchy de series geométricas y derivación término a término. Luego, para $0\le r<1$ y $|x|\le r$, demuestre la cota de cola

$$
\left|\sum_{n=N+1}^{\infty}(n+1)x^n\right|\le\frac{r^{N+1}[(N+2)-(N+1)r]}{(1-r)^2}.
$$

### INV-C09-01 — De Herón a la convergencia cuadrática de Newton

Reexamine la iteración de INV-C00-01 como método de Newton para $f(x)=x^2-2$. Demuestre que la fórmula de Newton coincide exactamente con la de Herón y que el error satisface la relación cuadrática obtenida **antes de disponer del cálculo**. Identifique qué aporta adicionalmente el teorema local general de C09.

### INV-C10-01 — El tiempo para alcanzar la mitad de la capacidad

En la ecuación logística $y'=r y(1-y/K)$ con $r,K>0$, suponga $0<y_0<K/2$ en el instante $t_0$. Determine el **único** instante futuro en que $y(t)=K/2$, expresando la respuesta en términos de $r,K,y_0$. Justifique signo, dominio y unidades; discuta por qué la fórmula de tiempo no daría un evento futuro si $y_0>K/2$.

### INV-C10-02 — Una identidad de energía sin resolver una EDO nueva

Sean $x_1,x_2$ dos soluciones $C^2$ de $x''+\omega^2x=0$ en un intervalo, con $\omega>0$. Construya una magnitud no negativa, en términos de la diferencia $w=x_1-x_2$, cuya derivada sea idénticamente cero. Deduzca unicidad para posición y velocidad iniciales coincidentes, y explique por qué el procedimiento constituye una prueba distinta de la verificación explícita de las fórmulas trigonométricas.

### INV-C11-01 — Dos certificados independientes para una acumulación

Para $y(t)=e^{-t}$ en $[0,1]$, llamemos $I=\int_0^1y(t)\,dt$. Por un lado, tome cualquier suma etiquetada $S_n$ sobre $n$ intervalos iguales; por otro, defina $T_N=\sum_{k=0}^N(-1)^k/k!$ y $A_N=1-T_N$. Demuestre, con los teoremas de C06, C09 y C11,

$$
|S_n-I|\le\frac1{2n},\qquad
|A_N-I|\le\frac1{(N+1)!},\qquad
|S_n-A_N|\le\frac1{2n}+\frac1{(N+1)!}.
$$

¿Por qué las dos cotas pueden contrastarse sin depender de observaciones decimales?

---

**Regla editorial:** 14 problemas `INV-C00-01` a `INV-C11-01` (con dos de C07 y C10), originales y adicionales a los 338 pares de ejercicios existentes. La elección de problemas clásicos como Herón, AM–GM o la función de Thomae no constituye reclamación de originalidad histórica de tales objetos; son **nuevos enunciados y desarrollos didácticos de EDC**.
