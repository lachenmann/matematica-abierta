---
title: Capítulo 7 — Ejercicios
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
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C07-EJERCICIOS
source-sha256: cf173c11db642879f7eeb6c60fa641de5bb1351ad0edd425b7c367fd8e1255da
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-07.html) · [Ejercicios](capitulo-07-ejercicios.html) · [Soluciones](capitulo-07-soluciones.html) · [Notas históricas](capitulo-07-notas.html)

Cada enunciado se resuelve utilizando sólo los capítulos C00–C07. Salvo indicación expresa, las integrales son propias, sobre intervalos cerrados donde el integrando está definido. Para las primitivas indefinidas deben identificarse los componentes del dominio y la constante; para las integrales definidas, comprobarse la orientación y los extremos. Las soluciones completas están en [un archivo independiente](capitulo-07-soluciones.html).

## A. Hipótesis, lenguaje y elecciones de método

**Ejercicio 7.1 (`EDC-C07-EXR-001`).** Distinga (a) demostrar que una función continua es Riemann–Darboux integrable, (b) hallar una primitiva y (c) calcular una integral definida a partir de ella. ¿Qué resultado de los capítulos anteriores une (b) y (c)?

**Ejercicio 7.2 (`EDC-C07-EXR-002`).** Explique por qué en el Teorema 7.1 el cambio de variable puede invertir la orientación y no necesita ser monótono. Ilustre con $\phi(t)=1-t$ en $[0,1]$ y $f(u)=u$.

**Ejercicio 7.3 (`EDC-C07-EXR-003`).** Un estudiante propone $\int_{-1}^{1}2t e^{t^2}\,dt=\int_0^1 e^u\,du$ usando $u=t^2$. Encuentre el error y el valor correcto.

**Ejercicio 7.4 (`EDC-C07-EXR-004`).** Determine si las expresiones $\int_{-1}^1(1/x)\,dx$ y $\int_1^2(1/x)\,dx$ tienen sentido como integrales **propias** de C05. Explique por qué una primitiva formal no elimina el problema de dominio.

## B. Sustitución y extremos

**Ejercicio 7.5 (`EDC-C07-EXR-005`).** Calcule $\int_0^2 3x^2(1+x^3)^4\,dx$ mediante un cambio de variable y verifique los nuevos extremos.

**Ejercicio 7.6 (`EDC-C07-EXR-006`).** Calcule $\int_0^1\frac{2x}{1+x^2}\,dx$ justificando que el denominador no se anula.

**Ejercicio 7.7 (`EDC-C07-EXR-007`).** Evalúe $\int_0^{\pi/2}\sin x\cos x\,dx$ con $u=\sin x$, y compruebe después el resultado mediante una identidad trigonométrica.

**Ejercicio 7.8 (`EDC-C07-EXR-008`).** Evalúe $\int_{-1}^1 2x e^{x^2}\,dx$ por sustitución y explique por qué sería incorrecto sustituir $2x$ por $|2x|$.

**Ejercicio 7.9 (`EDC-C07-EXR-009`).** Evalúe $\int_0^1 e^{3x+1}\,dx$ mediante el cambio afín $u=3x+1$, incluyendo el factor de escala.

**Ejercicio 7.10 (`EDC-C07-EXR-010`).** Evalúe $\int_0^1 x\sqrt{1+x^2}\,dx$. Escriba en qué intervalo está definida la raíz y cómo cambian los extremos.

**Ejercicio 7.11 (`EDC-C07-EXR-011`).** Halle $\int_0^\pi\frac{\cos x}{2+\sin x}\,dx$ sin suponer que $2+\sin x$ sea monótona en todo el intervalo.

**Ejercicio 7.12 (`EDC-C07-EXR-012`).** Evalúe $\int_1^e\frac{\ln x}{x}\,dx$ por sustitución; indique el dominio y la primitiva correspondiente.

## C. Integración por partes

**Ejercicio 7.13 (`EDC-C07-EXR-013`).** Calcule $\int_0^1 xe^x\,dx$, indicando los factores $u$ y $v'$ y realizando un control por derivación.

**Ejercicio 7.14 (`EDC-C07-EXR-014`).** Calcule $\int_0^\pi x\sin x\,dx$ y verifique el signo del resultado usando que el integrando es no negativo.

**Ejercicio 7.15 (`EDC-C07-EXR-015`).** Calcule $\int_1^e\ln x\,dx$ mediante partes sin recurrir a una tabla de integrales de logaritmos.

**Ejercicio 7.16 (`EDC-C07-EXR-016`).** Calcule $\int_0^1x^2e^x\,dx$ por dos aplicaciones de partes; compruebe el resultado derivando la primitiva obtenida.

**Ejercicio 7.17 (`EDC-C07-EXR-017`).** Encuentre la familia de primitivas de $e^x\cos x$ por integración por partes **dos veces**. Justifique el factor numérico final y compruebe la derivada.

**Ejercicio 7.18 (`EDC-C07-EXR-018`).** Calcule $\int_0^1x\cos(2x)\,dx$ y presente el resultado en términos de $\sin2$ y $\cos2$.

**Ejercicio 7.19 (`EDC-C07-EXR-019`).** Refute la regla falsa $\int_0^1u(x)v(x)\,dx=(\int_0^1u)(\int_0^1v)$ con $u(x)=v(x)=x$. Señale qué identidad correcta permite integrar ciertos productos.

## D. Fracciones racionales y controles de dominio

**Ejercicio 7.20 (`EDC-C07-EXR-020`).** Descomponga $1/[x(x-1)]$ en fracciones parciales y encuentre sus primitivas sobre cada intervalo del dominio.

**Ejercicio 7.21 (`EDC-C07-EXR-021`).** Verifique por denominador común la descomposición de $1/[x(x-1)^2]$ y calcule su primitiva donde esté definida.

**Ejercicio 7.22 (`EDC-C07-EXR-022`).** Calcule una primitiva de $(2x+3)/(x^2+2x+2)$ sobre $\mathbb R$, mostrando cómo se completa el cuadrado.

**Ejercicio 7.23 (`EDC-C07-EXR-023`).** Calcule $\int_2^3\frac{x^3+1}{x^2-1}\,dx$ mediante división y cancelación racional. Explique por qué el punto $x=-1$ continúa excluido del dominio original.

**Ejercicio 7.24 (`EDC-C07-EXR-024`).** Utilice el Teorema 7.3 para descomponer $1/[(x-1)(x-2)(x-3)]$. Obtenga una primitiva en cada intervalo de su dominio y compruebe los coeficientes.

## E. Aplicaciones y significado de la integral

**Ejercicio 7.25 (`EDC-C07-EXR-025`).** Calcule el área entre las curvas $y=2x$ y $y=x^2$ sobre $[0,2]$, justificando cuál es la superior.

**Ejercicio 7.26 (`EDC-C07-EXR-026`).** Calcule el **área total** entre $y=x$ e $y=x^2$ en $[-1,2]$. Separe el intervalo en los puntos de cruce y compare con el valor absoluto de la integral orientada de $x-x^2$.

**Ejercicio 7.27 (`EDC-C07-EXR-027`).** Un resorte lineal con constante $k>0$ se estira cuasiestáticamente desde $0$ hasta $L>0$. Halle el trabajo realizado por una fuerza externa $F_{\mathrm{ext}}(x)=kx$ y el trabajo de la fuerza de restitución $F_{\mathrm{res}}(x)=-kx$. Justifique sus unidades.

**Ejercicio 7.28 (`EDC-C07-EXR-028`).** La tasa de acumulación de una cantidad es $r(t)=2t+3$ para $1\le t\le4$. Calcule $Q(4)-Q(1)$ si $Q'=r$ y diga qué información adicional haría falta para conocer $Q(4)$.

## F. Demostraciones y desafío de síntesis

**Ejercicio 7.29 (`EDC-C07-EXR-029`).** Sea $f$ continua en un intervalo que contiene $[a,b]$. Demuestre mediante el Teorema 7.1 la identidad de reflexión $\int_{-b}^{-a}f(-t)\,dt=\int_a^bf(u)\,du$ para $a<b$. Explique por qué el signo negativo de la derivada del cambio de variable no produce un signo final negativo.

**Ejercicio 7.30 (`EDC-C07-EXR-030`).** **Desafío integrador.** Evalúe exactamente

$$
\int_0^1\left(2xe^{x^2}+x\ln(1+x^2)+\frac1{(x+1)(x+2)}\right)\,dx.
$$

Utilice sustitución, integración por partes y fracciones parciales, respectivamente, para los tres sumandos; controle continuidad, positividad de los argumentos logarítmicos y extremos. Verifique el resultado final por diferenciación de una primitiva explícita.

---

**Correspondencia editorial:** Los treinta identificadores `EDC-C07-EXR-001--030` tienen desarrollos únicos `EDC-C07-SOL-001--030` en [las soluciones del capítulo 7](capitulo-07-soluciones.html).
