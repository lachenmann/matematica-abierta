---
title: Capítulo 6 — Ejercicios
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
source-id: EDC-C06-EJERCICIOS
source-sha256: 22ca43a5a0b071e6603f672df24e6d4fbb8ff72f9aa2683422d731eed798b2ec
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-06.html) · [Ejercicios](capitulo-06-ejercicios.html) · [Soluciones](capitulo-06-soluciones.html)

El propósito es utilizar el Teorema Fundamental como una afirmación **demostrada y condicionada**, no como una regla de cancelación formal. En cada cálculo, indique continuidad, intervalo y primitiva empleada cuando corresponda. Los ejercicios dependen de C00–C06; ninguno requiere técnicas de sustitución o integración por partes del capítulo 7.

## A. Interpretación y control de hipótesis

**Ejercicio 6.1 (`EDC-C06-EXR-001`).** Enuncie separadamente las dos partes del Teorema Fundamental para $f$ continua en $[a,b]$. Indique qué objeto se construye en cada parte y qué resultados previos necesita cada demostración.

**Ejercicio 6.2 (`EDC-C06-EXR-002`).** Sea $f(t)=t^2$ en $[0,2]$ y $F(x)=\int_0^x f(t)\,dt$. Calcule $F'_+(0)$ y $F'_-(2)$ y explique por qué ninguna de estas dos expresiones constituye por sí misma una derivada bilateral en los extremos del dominio.

**Ejercicio 6.3 (`EDC-C06-EXR-003`).** Demuestre, sin derivar $F$, que si $f$ es integrable y no negativa en $[a,b]$, entonces $F(x)=\int_a^x f$ es no decreciente; determine cuándo la conclusión «estrictamente creciente» está justificada si, además, $f$ es continua y positiva en cada punto del intervalo.

**Ejercicio 6.4 (`EDC-C06-EXR-004`).** Un móvil tiene velocidad $v(t)=3t^2$ para $0\le t\le2$. Calcule su desplazamiento. Si $t$ se mide en segundos y $v$ en metros por segundo, especifique las unidades físicas del coeficiente numérico $3$.

**Ejercicio 6.5 (`EDC-C06-EXR-005`).** Para $f$ integrable en $[a,b]$ y $c\in[a,b]$, pruebe que $F_a(x)=\int_a^x f(t)\,dt$ y $F_c(x)=\int_c^x f(u)\,du$ difieren en una constante. ¿Qué papel desempeña que $t$ y $u$ sean variables mudas?

## B. Acumulaciones construidas desde la integral

**Ejercicio 6.6 (`EDC-C06-EXR-006`).** Para $0\le x\le2$, obtenga una expresión para $F(x)=\int_0^x t^2\,dt$. Compruebe por derivación en el interior y por la condición inicial $F(0)=0$.

**Ejercicio 6.7 (`EDC-C06-EXR-007`).** En $[-1,4]$ defina $F(x)=\int_1^x(t-3)\,dt$. Determine $F(x)$, sus intervalos de crecimiento/decrecimiento y los valores $F(1)$ y $F(4)$.

**Ejercicio 6.8 (`EDC-C06-EXR-008`).** Para $-1\le x\le2$, calcule $F(x)=\int_{-1}^x|t|\,dt$ mediante una fórmula por tramos. Compruebe expresamente la derivabilidad de $F$ en $x=0$ y halle $F(2)$.

**Ejercicio 6.9 (`EDC-C06-EXR-009`).** Para $0\le x\le1$, encuentre $F(x)=\int_0^x\frac{dt}{1+t^2}$ y demuestre que $F'(x)>0$ para $0<x<1$. ¿Cuál es $F(1)$?

**Ejercicio 6.10 (`EDC-C06-EXR-010`).** Sea $F(x)=\int_0^x e^{-t^2}\,dt$, con $0\le x\le1$. Sin recurrir a una fórmula elemental de primitiva, pruebe que $F'(x)=e^{-x^2}$ en $(0,1)$, que $F$ es creciente y que $0\le F(x)\le x$.

**Ejercicio 6.11 (`EDC-C06-EXR-011`).** En $[-1,1]$, sea $s(t)=0$ si $t<0$ y $s(t)=1$ si $t\ge0$. Calcule $S(x)=\int_{-1}^x s(t)\,dt$, sus derivadas laterales en $0$ y $S(1)$. Distinga integrabilidad de derivabilidad de la acumulación.

## C. Evaluación de integrales definidas

**Ejercicio 6.12 (`EDC-C06-EXR-012`).** Calcule $\int_{-1}^{2}(3t^2-2t+1)\,dt$ e identifique una primitiva válida sobre el intervalo completo.

**Ejercicio 6.13 (`EDC-C06-EXR-013`).** Calcule $\int_0^\pi\sin t\,dt$ y explique por qué el resultado coincide aquí con un área geométrica no negativa.

**Ejercicio 6.14 (`EDC-C06-EXR-014`).** Calcule $\int_1^e\frac{dt}{t}$, justificando el dominio del logaritmo.

**Ejercicio 6.15 (`EDC-C06-EXR-015`).** Calcule $\int_0^1 e^{2t}\,dt$ mostrando directamente que $\frac12 e^{2t}$ es una primitiva en $[0,1]$.

**Ejercicio 6.16 (`EDC-C06-EXR-016`).** Calcule $\int_0^{\pi/4}\frac{dt}{\cos^2 t}$ e indique por qué el denominador es no nulo en el intervalo.

**Ejercicio 6.17 (`EDC-C06-EXR-017`).** Demuestre que $\int_{-2}^{2}t^3\,dt=0$ de dos maneras: por una primitiva y por simetría de la función impar con la aditividad de C05.

**Ejercicio 6.18 (`EDC-C06-EXR-018`).** Calcule $\int_{-1}^{1}|t|\,dt$ y explique por qué la función $|t|$ sí tiene una primitiva en todo el intervalo aunque no sea derivable en $t=0$.

**Ejercicio 6.19 (`EDC-C06-EXR-019`).** Calcule la integral orientada $\int_2^0(2t+1)\,dt$. ¿Qué signo obtiene y por qué?

## D. Extremos variables

**Ejercicio 6.20 (`EDC-C06-EXR-020`).** Para $-1<x<1$, derive $H(x)=\int_0^{x^2}e^{t^2}\,dt$ sin hallar ninguna primitiva elemental de $e^{t^2}$.

**Ejercicio 6.21 (`EDC-C06-EXR-021`).** Para $-1<x<1$, derive $K(x)=\int_{\sin x}^{x^2+1}\ln(1+t^2)\,dt$. Compruebe que los dos límites de integración pertenecen a un intervalo compacto fijo sobre el que el integrando es continuo.

**Ejercicio 6.22 (`EDC-C06-EXR-022`).** Para $-1<x<2$, derive $L(x)=\int_x^2(t^2+1)\,dt$ y calcule $L(2)$ por continuidad de la fórmula.

**Ejercicio 6.23 (`EDC-C06-EXR-023`).** Para $-1<x<1$, derive $M(x)=\int_0^{x^3}\cos(t^2)\,dt$. Explique la diferencia entre derivar el extremo variable y realizar una sustitución integral general.

**Ejercicio 6.24 (`EDC-C06-EXR-024`).** Sea $N(x)=\int_{-1}^x(t^2+1)\,dt+\int_x^1(t^2+1)\,dt$ para $-1\le x\le1$. Demuestre mediante aditividad que $N$ es constante, calcule su valor y compruebe que $N'(x)=0$ en el interior.

## E. Diagnóstico de afirmaciones inválidas

**Ejercicio 6.25 (`EDC-C06-EXR-025`).** Sea $r(t)=1$ si $t\ne0$ y $r(0)=0$ sobre $[-1,1]$. Demuestre que $r$ es integrable, calcule $R(x)=\int_{-1}^x r(t)\,dt$ y compare $R'(0)$ con $r(0)$. Identifique exactamente qué hipótesis de la primera parte del Teorema Fundamental falla en ese punto.

**Ejercicio 6.26 (`EDC-C06-EXR-026`).** La función $G(x)=\sqrt{x}$ es continua en $[0,1]$ y derivable en $(0,1)$. ¿Por qué no se puede aplicar directamente la versión de la segunda parte para derivadas Riemann-integrables a $G'(x)=1/(2\sqrt{x})$ sobre $[0,1]$? Distinga la existencia de $G(1)-G(0)$ de la definición de una integral **propia** de Darboux.

**Ejercicio 6.27 (`EDC-C06-EXR-027`).** Sea $f(x)=x$ en $[0,1]$ y defina $G(x)=x^2/2$ cuando $x>0$, pero $G(0)=100$. Aunque $G'(x)=f(x)$ para todo $x\in(0,1)$, ¿es lícito concluir que $\int_0^1 f=G(1)-G(0)$? Explique el papel de la continuidad de $G$ en el extremo.

## F. Pruebas y síntesis

**Ejercicio 6.28 (`EDC-C06-EXR-028`).** Sean $G,H$ continuas en $[a,b]$, derivables en $(a,b)$ y tales que $G'=H'$ en ese intervalo. Pruebe por el teorema del valor medio que $G-H$ es constante. Indique por qué no basta conocer una igualdad de derivadas en dos intervalos separados para obtener una única constante global.

**Ejercicio 6.29 (`EDC-C06-EXR-029`).** Reconstruya la prueba directa por sumas de la fórmula $\int_a^b f=G(b)-G(a)$ bajo las hipótesis: $G$ continua en $[a,b]$, derivable en $(a,b)$; $f$ integrable en $[a,b]$ y $f=G'$ en el interior. Identifique el papel distinto del valor medio y de la equivalencia Riemann–Darboux.

**Ejercicio 6.30 (`EDC-C06-EXR-030`).** **Desafío:** si $s\in C^1([a,b])$ (es decir, $s$ es continua en $[a,b]$, derivable en $(a,b)$ y $s'$ se prolonga continuamente a $[a,b]$), defina la variación total de $s$ como el supremo de $\sum_i|s(t_i)-s(t_{i-1})|$ sobre particiones finitas. Pruebe que ese supremo es exactamente $\int_a^b|s'(t)|\,dt$. Utilice la segunda parte del Teorema Fundamental, la desigualdad triangular y el valor medio para obtener ambas desigualdades.

---

Cada `EDC-C06-EXR-nnn` tiene una única solución razonada `EDC-C06-SOL-nnn` en [el archivo independiente de soluciones](capitulo-06-soluciones.html).
