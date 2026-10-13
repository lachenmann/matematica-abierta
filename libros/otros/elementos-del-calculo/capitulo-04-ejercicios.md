---
title: Capítulo 4 — Ejercicios
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-13'
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
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C04-EJERCICIOS
source-sha256: 6dc787319ded4c1f8d24408b3ef843c8bef2d75c2444103f53cba10c060612c7
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-04.html) · [Ejercicios](capitulo-04-ejercicios.html) · [Soluciones](capitulo-04-soluciones.html) · [Notas históricas](capitulo-04-notas.html)

El objetivo de estos problemas es justificar aproximaciones geométricas mediante cálculos finitos, estimaciones del resto y argumentos de límite. **No** se debe emplear la definición de integral de Riemann–Darboux ni el Teorema Fundamental del Cálculo. Pueden utilizarse los resultados demostrados en C00–C04. Cada ejercicio tiene una solución independiente identificada con el mismo número.

## A. Lectura geométrica y precisión conceptual

**Ejercicio 4.1 (`EDC-C04-EXR-001`).** Explique qué condiciones tendría que cumplir un número propuesto como área de una región curva cuando se conocen polígonos interiores y exteriores. ¿Basta encontrar dos sucesiones $L_n\le U_n$ con $U_n-L_n\to0$ para demostrar la existencia de un número común? Distinga existencia y unicidad.

**Ejercicio 4.2 (`EDC-C04-EXR-002`).** Para una región parabólica descrita por $y=k(x-a)(b-x)$ con $k>0$ y $a<b$, determine la longitud de base, la altura máxima y el área del triángulo principal. Compruebe las dimensiones físicas de $k$ si $x$ e $y$ son longitudes.

**Ejercicio 4.3 (`EDC-C04-EXR-003`).** ¿Por qué un polígono inscrito de área $P$ no permite afirmar que una región curva tenga área $P$? Construya un argumento mediante cotas y diga qué tendría que cambiar para conseguir precisión arbitraria.

**Ejercicio 4.4 (`EDC-C04-EXR-004`).** Describa la diferencia matemática entre un método de agotamiento que hace un resto menor que cualquier tolerancia y una afirmación no justificada de que una región «es la suma de infinitos segmentos». Indique qué resultado de C00 fundamenta el primero.

## B. Triángulos parabólicos y agotamiento

**Ejercicio 4.5 (`EDC-C04-EXR-005`).** Considere $f(x)=2x(3-x)$ en $[0,3]$. Calcule la altura máxima, el área $T$ del triángulo principal y el candidato $4T/3$ para la región bajo el arco.

**Ejercicio 4.6 (`EDC-C04-EXR-006`).** Para $f(x)=3(x+1)(1-x)$ sobre $[-1,1]$, encuentre $T$ y el área determinada por el agotamiento.

**Ejercicio 4.7 (`EDC-C04-EXR-007`).** En una cuadratura parabólica con triángulo inicial de área $T$, halle el área del polígono tras incluir las generaciones $0$ y $1$, la cota $B_2$ del resto y los extremos del intervalo de encaje de área.

**Ejercicio 4.8 (`EDC-C04-EXR-008`).** Si $T=3/2$, determine el menor entero $n\ge1$ para el cual el error $4T/(3\cdot4^n)$ de los polígonos inscritos respecto del valor $4T/3$ es menor que $10^{-3}$.

**Ejercicio 4.9 (`EDC-C04-EXR-009`).** Demuestre sin emplear sumas infinitas que cada triángulo nuevo de la primera generación tiene $1/8$ del área del triángulo original y que el total agregado equivale a $1/4$.

**Ejercicio 4.10 (`EDC-C04-EXR-010`).** Si $T=1$, calcule el número de triángulos y su área individual en la generación $n$, empezando con la generación cero. Compruebe que el área total de esa generación es $4^{-n}$.

## C. Rectángulos, particiones y potencias

**Ejercicio 4.11 (`EDC-C04-EXR-011`).** Para $f(x)=x^2$ en $[0,1]$ y cuatro subintervalos uniformes, calcule las sumas con extremos izquierdo y derecho y verifique que $1/3$ queda entre ambas.

**Ejercicio 4.12 (`EDC-C04-EXR-012`).** Para $f(x)=x^2$ en $[0,1]$, use la partición $0,1/4,3/4,1$. Calcule $L(P)$, $U(P)$, su diferencia y la finura; compárela con la cota de la Proposición 4.2.

**Ejercicio 4.13 (`EDC-C04-EXR-013`).** Calcule las sumas de puntos medios y trapecios para $f(x)=x^2$ con dos subintervalos iguales. Contraste sus errores respecto del valor candidato $1/3$.

**Ejercicio 4.14 (`EDC-C04-EXR-014`).** Para $f(x)=x$ en $[0,1]$ y una partición arbitraria, demuestre que la suma de trapecios es exactamente $1/2$, y calcule la diferencia entre las sumas por extremos.

**Ejercicio 4.15 (`EDC-C04-EXR-015`).** Para $f(x)=x^3$ en $[0,1]$, use dos subintervalos iguales. Calcule las sumas extremas y compruebe que el candidato $1/4$ queda entre ellas.

**Ejercicio 4.16 (`EDC-C04-EXR-016`).** Aplique la fórmula del segmento parabólico a $f(x)=2x(2-x)$ en $[0,2]$. Identifique el triángulo principal y el área determinada.

## D. Diagnóstico de razonamientos inválidos

**Ejercicio 4.17 (`EDC-C04-EXR-017`).** Refute la afirmación «toda función acotada sobre $[0,1]$ determina un área común al refinar sumas rectangulares». Utilice una función que tome valores distintos en racionales e irracionales.

**Ejercicio 4.18 (`EDC-C04-EXR-018`).** Un alumno afirma que cada línea tiene área cero y, por tanto, una figura descrita mediante «todas sus líneas» tiene área cero. Explique por qué la aditividad para un número **finito** de polígonos o regiones no demuestra esa afirmación sobre una colección infinita.

**Ejercicio 4.19 (`EDC-C04-EXR-019`).** Otra alumna calcula $P_n=T\sum_{j=0}^{n-1}4^{-j}$ y deduce que el área del segmento parabólico es $4T/3$ sin estudiar la región no cubierta. Identifique la laguna y el lema que la repara.

**Ejercicio 4.20 (`EDC-C04-EXR-020`).** Dé un ejemplo de particiones de $[0,1]$ con un número de subintervalos que tiende a infinito, pero cuya finura no tiende a cero. ¿Por qué el número de subintervalos no es por sí solo una medida suficiente de precisión?

**Ejercicio 4.21 (`EDC-C04-EXR-021`).** Explique por qué invocar $\int_0^1x^2\,dx=1/3$ como justificación de todas las cuadraturas discutidas en este capítulo sería circular dentro de la arquitectura actual del libro. Distinga el área geométrica y la futura integral.

## E. Demostraciones y control de hipótesis

**Ejercicio 4.22 (`EDC-C04-EXR-022`).** Demuestre por multiplicación y resta la identidad finita $\sum_{j=0}^{n-1}q^j=(1-q^n)/(1-q)$ para $0<q<1$. Calcule el resto respecto de $1/(1-q)$ sin usar la teoría general de series.

**Ejercicio 4.23 (`EDC-C04-EXR-023`).** Si $f:[a,b]\to\mathbb R$ es no decreciente y $P$ es una partición finita, pruebe que la diferencia entre la suma derecha y la izquierda satisface $0\le U(P)-L(P)\le\|P\|(f(b)-f(a))$.

**Ejercicio 4.24 (`EDC-C04-EXR-024`).** Sea $f:[a,b]\to\mathbb R$ continua. Reconstruya la prueba de que para cada $\varepsilon>0$ existe $\delta>0$ tal que $\|P\|<\delta$ implica $A_+(P)-A_-(P)<\varepsilon$. Justifique dónde se emplean los teoremas de valores extremos y continuidad uniforme.

**Ejercicio 4.25 (`EDC-C04-EXR-025`).** Suponga $R_n\ge0$ y $R_{n+1}\le(2/3)R_n$. Pruebe que el resto puede hacerse menor que cualquier $\varepsilon>0$ sin suponer una fórmula para la suma de una serie infinita.

**Ejercicio 4.26 (`EDC-C04-EXR-026`).** Generalice el laboratorio de potencias a una partición arbitraria $P$ de $[0,1]$: para $p\ge1$ entero, pruebe con el teorema del valor medio que el número $1/(p+1)$ queda entre las sumas por extremos de $x^p$ y que la diferencia de éstas no supera $\|P\|$.

## F. Descubrimiento y síntesis

**Ejercicio 4.27 (`EDC-C04-EXR-027`).** Diseñe una partición uniforme de $[0,1]$ que garantice, para $f(x)=x^2$, que la diferencia entre sumas por extremos sea menor que $10^{-3}$. Puede escoger un número de subintervalos que sea potencia de dos. Justifique la elección.

**Ejercicio 4.28 (`EDC-C04-EXR-028`).** Considere $f(x)=-2x^2+5x+1$ en $[1,3]$ y la región comprendida entre su arco y la cuerda que une los extremos. Demuestre que la diferencia vertical entre arco y cuerda es $2(x-1)(3-x)$ y calcule el área por agotamiento parabólico.

**Ejercicio 4.29 (`EDC-C04-EXR-029`).** Si el triángulo principal tiene área $T=1$, calcule el encaje entre polígono interior y exterior tras tres generaciones y compruebe que $4/3$ queda estrictamente entre sus extremos. Calcule ambos errores respecto de $4/3$.

## G. Desafío de conjunto

**Ejercicio 4.30 (`EDC-C04-EXR-030`).** Para $\lambda\ge0$ defina $f_\lambda(x)=x^2+\lambda x(1-x)$ en $[0,1]$. Sin usar integrales, pruebe que las sumas rectangulares con **cualquier** elección de muestras y particiones cuya finura tienda a cero se aproximan al número $1/3+\lambda/6$. Obtenga una cota explícita del error en función de $\lambda$ y $\|P\|$.

---

Las soluciones independientes de `EDC-C04-EXR-001--030` se encuentran en [EDC-C04-SOLUCIONES](capitulo-04-soluciones.html). Los incisos conceptuales, numéricos y demostrativos se auditan con el mismo nivel de rigor; el banco de ejercicios no constituye capítulos adicionales.
