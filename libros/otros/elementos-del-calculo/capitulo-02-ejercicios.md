---
title: Capítulo 2 — Ejercicios
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
source-id: EDC-C02-EJERCICIOS
source-sha256: 606765197763fb7a611d831b1e4c7b9211de58bfbf8e41e06bc2efd7989c0c70
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-02.html) · [Ejercicios](capitulo-02-ejercicios.html) · [Soluciones](capitulo-02-soluciones.html) · [Notas históricas](capitulo-02-notas.html)

Todos los ejercicios están concebidos para resolverse usando únicamente los capítulos 0–2. Las reglas deben emplearse **sobre sus dominios**. Salvo indicación contraria, se pide justificar los pasos esenciales y no limitarse a escribir una fórmula.

## A. Reconocimiento y lenguaje

**Ejercicio 2.1 (`EDC-C02-EXR-001`).** Para $f(x)=(x^2+1)/(x-1)$, determine el dominio real, explique por qué la derivada existe en cada punto de él y calcule $f'(0)$.

**Ejercicio 2.2 (`EDC-C02-EXR-002`).** Determine cuáles de las fórmulas $(f+g)'=f'+g'$, $(fg)'=f'g'$, $(f/g)'=f'/g'$ y $(cf)'=cf'$ son universalmente válidas bajo hipótesis de derivabilidad y dominio apropiadas. Para cada fórmula falsa dé un contraejemplo concreto.

**Ejercicio 2.3 (`EDC-C02-EXR-003`).** Si $p(x)=x^3-2x+5$, obtenga $p'(a)$ a partir de reglas ya demostradas. Verifique separadamente $p'(1)$ por el cociente incremental.

**Ejercicio 2.4 (`EDC-C02-EXR-004`).** En el teorema de la función inversa, distinga las hipótesis «$f$ continua y estrictamente monótona» y «$f'(a)\ne0$». Explique qué garantiza cada una y examine $f(x)=x^3$ en $a=0$.

## B. Derivación algebraica y composición

**Ejercicio 2.5 (`EDC-C02-EXR-005`).** Halle la derivada de $p(x)=(3x^2-2x+1)(x^3+4)$ en $\mathbb R$ de dos maneras: regla del producto y desarrollo polinómico.

**Ejercicio 2.6 (`EDC-C02-EXR-006`).** Derive $q(x)=(x^2+1)/(x-2)$, indique el dominio y determine $q'(3)$.

**Ejercicio 2.7 (`EDC-C02-EXR-007`).** Derive $u(x)=(x^2+1)^5$ e identifique de modo explícito las funciones interior y exterior.

**Ejercicio 2.8 (`EDC-C02-EXR-008`).** Derive $v(x)=\sqrt{1+3x^2}$ y justifique que la expresión derivada está definida para todo real.

**Ejercicio 2.9 (`EDC-C02-EXR-009`).** Derive $w(x)=x^{-3}$, $x\ne0$, y explique por qué no tiene sentido hablar de $w'(0)$.

**Ejercicio 2.10 (`EDC-C02-EXR-010`).** Derive $r(x)=e^x/(1+x^2)$ en $\mathbb R$ y simplifique el numerador de su expresión final.

## C. Exponenciales, logaritmos y trigonometría

**Ejercicio 2.11 (`EDC-C02-EXR-011`).** Halle las derivadas de $f(x)=e^{2x-x^2}$ y $g(x)=\ln(3+x^2)$. Indique sus dominios.

**Ejercicio 2.12 (`EDC-C02-EXR-012`).** Para $0<x<\pi$, halle la derivada de $h(x)=\ln(\sin x)$ y explique por qué el intervalo indicado evita problemas de dominio.

**Ejercicio 2.13 (`EDC-C02-EXR-013`).** Derive $2^x$ para $x\in\mathbb R$ y $\log_2 x$ para $x>0$. Señale por qué $\log_2 x$ no es el recíproco de $2^x$ evaluado en el mismo argumento.

**Ejercicio 2.14 (`EDC-C02-EXR-014`).** Halle la derivada de $a(x)=\arctan(3x)$ en $\mathbb R$.

**Ejercicio 2.15 (`EDC-C02-EXR-015`).** Determine el dominio real de $b(x)=\arcsin(x^2)$ y derive donde exista la derivada bilateral. Discuta por separado $x=\pm1$.

**Ejercicio 2.16 (`EDC-C02-EXR-016`).** Derive la función positiva $k(x)=(1+x^2)^{\sin x}$ utilizando su representación exponencial; justifique su dominio.

## D. Diagnóstico de inferencias inválidas

**Ejercicio 2.17 (`EDC-C02-EXR-017`).** Un estudiante afirma que $(fg)'=f'g'$. Refute la afirmación con $f(x)=x$ y $g(x)=x^2$; escriba la fórmula correcta.

**Ejercicio 2.18 (`EDC-C02-EXR-018`).** Otro estudiante sostiene: «Si $f\circ g$ es derivable en $a$, necesariamente $f$ es derivable en $g(a)$». Analice $f(t)=|t|$ y $g(x)=x^2$.

**Ejercicio 2.19 (`EDC-C02-EXR-019`).** Refute «Toda función derivable tiene derivada continua» utilizando $f(x)=x^2\sin(1/x)$ si $x\ne0$, $f(0)=0$. Escriba dos sucesiones testigo.

**Ejercicio 2.20 (`EDC-C02-EXR-020`).** Sea $f(x)=2x$ si $x<0$ y $f(x)=x^2$ si $x\ge0$. Decida si es continua y si es derivable en $0$. ¿Qué papel desempeñan las derivadas laterales?

## E. Demostraciones

**Ejercicio 2.21 (`EDC-C02-EXR-021`).** Demuestre directamente que si $f$ es derivable en $a$ y $f(a)\ne0$, entonces $(1/f)'(a)=-f'(a)/f(a)^2$. Controle que $f$ no se anula cerca de $a$.

**Ejercicio 2.22 (`EDC-C02-EXR-022`).** Sea $f$ derivable en un intervalo abierto $I$. Demuestre por inducción que para $n\in\mathbb N$ se cumple $(f^n)'=nf^{n-1}f'$ en $I$.

**Ejercicio 2.23 (`EDC-C02-EXR-023`).** Si $g:I\to\mathbb R$ es derivable y no se anula en $I$, demuestre que $\ln|g(x)|$ es derivable y que $(\ln|g|)'=g'/g$.

**Ejercicio 2.24 (`EDC-C02-EXR-024`).** Con la identidad $E(x+y)=E(x)E(y)$ y $E(x)>0$, pruebe que $E(-x)=1/E(x)$. Junto con $E(h)>1$ para $h>0$ y continuidad, deduzca que $E$ es creciente y que su recorrido es $(0,\infty)$, sin usar el teorema del valor medio.

## F. Descubrimiento guiado

**Ejercicio 2.25 (`EDC-C02-EXR-025`).** Considere $F(x)=\sqrt{x^2}=|x|$. Una aplicación mecánica de la cadena para $x\ne0$ parece dar $F'(x)=x/\sqrt{x^2}$. Compruebe la fórmula y explique por qué ese cálculo no define la derivada en $0$.

**Ejercicio 2.26 (`EDC-C02-EXR-026`).** Para $r\in\mathbb R$ demuestre, sin desarrollar series binomiales, que $\lim_{h\to0}((1+h)^r-1)/h=r$; recuerde que $1+h>0$ cerca de cero.

**Ejercicio 2.27 (`EDC-C02-EXR-027`).** Sea $a,b>0$. En la rama superior de la elipse $x^2/a^2+y^2/b^2=1$, halle $y'(x)$ para $-a<x<a$ y evalúe la pendiente en $(a/\sqrt2,b/\sqrt2)$. Justifique la existencia de esa rama derivable.

## G. Desafío de síntesis

**Ejercicio 2.28 (`EDC-C02-EXR-028`).** Sean $\alpha,\beta\in\mathbb R$ y $y(x)=e^{\alpha x}\cos(\beta x)$. Calcule $y'$ y $y''$ mediante reglas ya demostradas y verifique la identidad

$$
y''-2\alpha y'+(\alpha^2+\beta^2)y=0.
$$

No se pide una teoría de ecuaciones diferenciales ni una afirmación de unicidad: sólo la verificación de esta identidad para la función indicada.

---

**Correspondencia editorial:** los ejercicios `EDC-C02-EXR-001--028` se desarrollan, con la misma numeración, en [las soluciones del capítulo](capitulo-02-soluciones.html).
