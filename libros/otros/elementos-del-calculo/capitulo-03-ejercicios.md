---
title: Capítulo 3 — Ejercicios
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
source-id: EDC-C03-EJERCICIOS
source-sha256: 89d20c7c920122dfba2655dff9727b5e93b1010aec4d4865253ae3abc68e02dc
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-03.html) · [Ejercicios](capitulo-03-ejercicios.html) · [Soluciones](capitulo-03-soluciones.html) · [Notas históricas](capitulo-03-notas.html)

Los ejercicios se resuelven a partir de C00–C03. En cada caso se deben justificar dominios, hipótesis y resultados, no limitarse a una fórmula. Las referencias `EDC-C03-EXR-nnn` corresponden uno a uno a las soluciones del archivo independiente.

## A. Reconocimiento de hipótesis y conceptos

**Ejercicio 3.1 (`EDC-C03-EXR-001`).** Para $f(x)=x^2$ sobre el dominio $[0,2]$, determine sus extremos absolutos. ¿Puede aplicarse sin modificación el principio de Fermat al extremo en $0$? Discuta su derivada derecha.

**Ejercicio 3.2 (`EDC-C03-EXR-002`).** Explique por qué el principio de Fermat no afirma que $f'(c)=0$ sea suficiente para un extremo. Compruébelo con $f(x)=x^3$ en $c=0$.

**Ejercicio 3.3 (`EDC-C03-EXR-003`).** Compruebe todas las hipótesis del teorema de Rolle para $f(x)=|x|$ sobre $[-1,1]$ y diga cuál falla. ¿Existe allí un punto interior con derivada cero?

**Ejercicio 3.4 (`EDC-C03-EXR-004`).** Aplique Rolle a $f(x)=\sin x$ sobre $[0,\pi]$ e identifique al menos un punto $c$ que satisfaga su conclusión.

## B. Valor medio, extremos e incrementos

**Ejercicio 3.5 (`EDC-C03-EXR-005`).** Para $f(x)=x^2$ en $[-1,2]$, calcule la pendiente secante e identifique el punto $c$ del teorema del valor medio.

**Ejercicio 3.6 (`EDC-C03-EXR-006`).** Para $f(x)=\ln x$ sobre $[1,e]$, encuentre un valor de $c$ que satisfaga el teorema del valor medio y justifique que pertenece a $(1,e)$.

**Ejercicio 3.7 (`EDC-C03-EXR-007`).** Determine el máximo y mínimo absolutos de $f(x)=x^2-4x+1$ en $[-1,5]$. Compare todos los candidatos, incluidos los extremos del intervalo.

**Ejercicio 3.8 (`EDC-C03-EXR-008`).** Demuestre para todos $a,b\in\mathbb R$ que $|\sin b-\sin a|\le|b-a|$, indicando qué hipótesis del valor medio se utilizan.

**Ejercicio 3.9 (`EDC-C03-EXR-009`).** Halle los extremos absolutos de $f(x)=x^3-3x$ en $[-2,2]$ y determine los intervalos de monotonía interiores.

**Ejercicio 3.10 (`EDC-C03-EXR-010`).** Aplicando el valor medio a $f(x)=e^x$ en $[0,1]$, pruebe que $1<e-1<e$ sin sustituir la conclusión por una aproximación decimal.

## C. Criterios globales y convexidad

**Ejercicio 3.11 (`EDC-C03-EXR-011`).** Demuestre que si $f$ es derivable en un intervalo y $f'=0$ en todos sus puntos interiores, entonces $f$ es constante. Explique dónde se utiliza la condición de intervalo.

**Ejercicio 3.12 (`EDC-C03-EXR-012`).** Si $f'(x)>0$ sobre un intervalo abierto $I$, demuestre que $f$ es estrictamente creciente. ¿Es necesario que la derivada tenga límite o sea continua?

**Ejercicio 3.13 (`EDC-C03-EXR-013`).** Sea $f$ dos veces derivable sobre un intervalo $I$ con $f''\ge0$. Demuestre que toda recta tangente está por debajo de su gráfica y precise el dominio donde vale la desigualdad.

**Ejercicio 3.14 (`EDC-C03-EXR-014`).** Pruebe que $\ln x\le x-1$ para $x>0$, con igualdad sólo en $x=1$, empleando el criterio de concavidad.

**Ejercicio 3.15 (`EDC-C03-EXR-015`).** Sea $f:I\to\mathbb R$ derivable en un intervalo abierto con $f'(x)\ge m>0$. Demuestre que su inversa sobre $f(I)$ satisface $|f^{-1}(v)-f^{-1}(u)|\le|v-u|/m$.

## D. Contraejemplos y diagnóstico de errores

**Ejercicio 3.16 (`EDC-C03-EXR-016`).** Refute «Si $f'(c)=0$, entonces $c$ es un extremo local» usando una función polinómica concreta.

**Ejercicio 3.17 (`EDC-C03-EXR-017`).** Refute «Si una función continua toma valores iguales en los extremos de un intervalo, tiene derivada cero en un punto interior» sin omitir el análisis de derivabilidad.

**Ejercicio 3.18 (`EDC-C03-EXR-018`).** Construya una función derivable en $\mathbb R$ con $f'\ge0$ en todas partes que, sin embargo, no sea estrictamente creciente. Justifique el empalme donde corresponda.

**Ejercicio 3.19 (`EDC-C03-EXR-019`).** Una persona deduce de $f'(0)>0$ que $f$ es creciente en toda $\mathbb R$. Dé un contraejemplo polinómico y explique qué información local sí permite la derivada positiva.

**Ejercicio 3.20 (`EDC-C03-EXR-020`).** Estudie $f(x)=|x|^{2/3}$ en $[-1,1]$. ¿Dónde alcanza su mínimo? ¿Es derivable en ese punto? ¿Por qué esto no contradice Fermat?

## E. Demostraciones estructurales

**Ejercicio 3.21 (`EDC-C03-EXR-021`).** Demuestre el **valor medio de Cauchy**: si $f,g$ son continuas en $[a,b]$ y derivables en $(a,b)$, existe $c\in(a,b)$ tal que

$$
(f(b)-f(a))g'(c)=(g(b)-g(a))f'(c).
$$

No divida por $g'$ sin hipótesis de que sea diferente de cero.

**Ejercicio 3.22 (`EDC-C03-EXR-022`).** Demuestre que si $f$ es continua en $[a,b]$, derivable en $(a,b)$ y $|f'|\le K$ en $(a,b)$, entonces $f$ es $K$-Lipschitz en $[a,b]$.

**Ejercicio 3.23 (`EDC-C03-EXR-023`).** Sea $f$ derivable en un intervalo abierto y suponga $f'(x)\le -m<0$ en todo él. Demuestre que $f$ es estrictamente decreciente y que su inversa, definida sobre la imagen, tiene variaciones acotadas por $|u-v|/m$.

**Ejercicio 3.24 (`EDC-C03-EXR-024`).** Suponga que $f'$ es no decreciente sobre un intervalo abierto. Demuestre, mediante el valor medio, que $f(y)\ge f(x)+f'(x)(y-x)$ para cualesquiera $x,y$ del intervalo y deduzca la convexidad de $f$.

**Ejercicio 3.25 (`EDC-C03-EXR-025`).** Sea $f$ continua en $[a,b]$, derivable en $(a,b)$ y $f'(x)\le-m<0$ allí. Si $f(a)>0>f(b)$, pruebe que $f$ tiene exactamente un cero en $(a,b)$.

## F. Descubrimiento y optimización

**Ejercicio 3.26 (`EDC-C03-EXR-026`).** Entre los rectángulos de perímetro $P>0$, determine cuál tiene área máxima. Justifique la existencia y el carácter global del máximo sin permitir lados negativos.

**Ejercicio 3.27 (`EDC-C03-EXR-027`).** Un cilindro circular recto **cerrado** tiene área total $S>0$. Determine la relación entre altura $h$ y radio $r$ que maximiza el volumen. Controle el dominio y los límites en sus extremos.

**Ejercicio 3.28 (`EDC-C03-EXR-028`).** Para $\alpha,\lambda>0$ encuentre y justifique el máximo global de $F(x)=x^{\alpha}e^{-\lambda x}$ sobre $x>0$. Estudie sus intervalos de crecimiento y decrecimiento.

**Ejercicio 3.29 (`EDC-C03-EXR-029`).** ¿Qué puntos de la parábola $y=x^2$ están a distancia mínima del punto $(0,1)$? Trabaje con la distancia al cuadrado, justifique que existe un mínimo global y controle los puntos estacionarios que no son mínimos.

## G. Desafío de síntesis

**Ejercicio 3.30 (`EDC-C03-EXR-030`).** Suponga $f$ dos veces derivable sobre un intervalo abierto que contiene el segmento entre $a$ y $b$, con $|f''(x)|\le M$. Demuestre, mediante **dos aplicaciones** del teorema del valor medio y sin usar Taylor, que

$$
|f(b)-f(a)-f'(a)(b-a)|\le M(b-a)^2.
$$

Indique si la cota tiene que ser la mejor posible y proporcione un ejemplo donde no sea óptima.

---

**Correspondencia editorial:** `EDC-C03-EXR-001--030` ↔ `EDC-C03-SOL-001--030`. Todos los enunciados serán resueltos en [el archivo independiente de soluciones](capitulo-03-soluciones.html).
