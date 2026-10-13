---
title: Capítulo 0 — Ejercicios
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
source-id: EDC-C00-EJERCICIOS
source-sha256: ef7d075ad08492bbb0e0def39d9d54f966b666aa8668f64300a525d4e411c3bf
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-00.html) · [Ejercicios](capitulo-00-ejercicios.html) · [Soluciones](capitulo-00-soluciones.html) · [Notas históricas](capitulo-00-notas.html)

Los problemas de [Del límite a la pregunta por el cálculo](capitulo-00.html) permiten trabajar con las decisiones que sostienen sus argumentos: elegir una tolerancia, construir una sucesión, encontrar una cota o comprobar qué ocurre al suprimir una hipótesis. En todos los casos se pide justificar las afirmaciones; una gráfica o una aproximación decimal puede orientar la búsqueda, pero la respuesta necesita un argumento. Las respuestas desarrolladas figuran, por los mismos números, en [Soluciones del capítulo 0](capitulo-00-soluciones.html).

## A. Lenguaje y lectura conceptual

### Ejercicio 0.1 — Cuantificadores de una convergencia (`EDC-C00-EXR-001`)

Escriba mediante cuantificadores y desigualdades la negación exacta de la afirmación «$x_n\to L$». Explique por qué no es suficiente decir que algún término de la sucesión está lejos de $L$.

### Ejercicio 0.2 — Continuidad en un punto aislado (`EDC-C00-EXR-002`)

Sea $D=\{0\}\cup[1,2]$ y $f:D\to\mathbb R$ una función cualquiera. Demuestre que $f$ es continua en $0$ con respecto a su dominio. ¿Tiene sentido, bajo nuestra Definición 0.3, la expresión $\lim_{x\to0,\,x\in D}f(x)$? Razone la diferencia.

### Ejercicio 0.3 — La pendiente secante no es una sustitución (`EDC-C00-EXR-003`)

Para $f(x)=x^2+3x$ y $h\ne0$, calcule $[f(a+h)-f(a)]/h$ y su límite cuando $h\to0$. Identifique el paso que dejaría de tener sentido si se sustituyera $h=0$ antes de simplificar.

### Ejercicio 0.4 — Rectángulos para una recta (`EDC-C00-EXR-004`)

En el intervalo $[0,1]$, tome $f(x)=x$. Calcule, para una partición en $n$ subintervalos iguales, la suma de rectángulos de extremos izquierdos y la de extremos derechos. Halle su diferencia y sus límites, sin emplear la notación de integral.

## B. Límites, continuidad y cálculos justificados

### Ejercicio 0.5 — Un umbral elegido a partir de la tolerancia (`EDC-C00-EXR-005`)

Dado $\varepsilon>0$, encuentre una condición explícita suficiente sobre $N$ para garantizar $|3+2/n-3|<\varepsilon$ para todo $n\ge N$. Deduzca el límite de la sucesión.

### Ejercicio 0.6 — Otro número que no es racional (`EDC-C00-EXR-006`)

Demuestre que $\sqrt3\notin\mathbb Q$. Puede usar que, para un entero $m$, la divisibilidad de $m^2$ por $3$ implica la divisibilidad de $m$ por $3$, pero deberá justificar este hecho.

### Ejercicio 0.7 — Monotonía y supremo (`EDC-C00-EXR-007`)

Considere $x_n=1-1/n$ para $n\ge1$. Compruebe que la sucesión es no decreciente, que su conjunto de valores tiene supremo $1$ y que $x_n\to1$, identificando el uso de la propiedad arquimediana.

### Ejercicio 0.8 — Límite en un punto fuera del dominio (`EDC-C00-EXR-008`)

Defina $g:\mathbb R\setminus\{1\}\to\mathbb R$ mediante $g(x)=(x^3-1)/(x-1)$. Calcule $\lim_{x\to1}g(x)$ y explique por qué el límite no obliga a que $g(1)$ esté definido.

### Ejercicio 0.9 — Persistencia local del signo (`EDC-C00-EXR-009`)

Sea $f:D\to\mathbb R$ continua en $a\in D$ y suponga $f(a)>0$. Demuestre que existe $\delta>0$ tal que $f(x)>0$ para todo $x\in D$ con $|x-a|<\delta$. ¿Es indispensable suponer que $a$ sea punto de acumulación?

## C. Construcción y combinación

### Ejercicio 0.10 — Existencia de raíces cuadradas (`EDC-C00-EXR-010`)

Usando sólo la estructura de cuerpo ordenado completo de $\mathbb R$, demuestre que para cada $c>0$ existe un único $r>0$ con $r^2=c$. Deberá definir un conjunto al cual aplicar el axioma del supremo, justificar que no es vacío ni está desprovisto de cota superior, y excluir los casos $r^2<c$ y $r^2>c$.

### Ejercicio 0.11 — Dos subsucesiones incompatibles (`EDC-C00-EXR-011`)

Sea $x_n=(-1)^n+1/n$. Demuestre que está acotada, determine los límites de las subsucesiones de índices pares e impares y concluya que $(x_n)$ no es convergente.

### Ejercicio 0.12 — Continuidad que no depende del punto (`EDC-C00-EXR-012`)

Pruebe directamente a partir de $||x|-|y||\le|x-y|$ que $f(x)=|x|$ es continua en todo $\mathbb R$. Demuestre además que es uniformemente continua en toda la recta, aunque ésta no sea un intervalo acotado.

### Ejercicio 0.13 — Existencia y unicidad sin derivadas (`EDC-C00-EXR-013`)

Demuestre que la ecuación $x^3+x-1=0$ tiene exactamente una solución en $(0,1)$, usando el teorema del valor intermedio y propiedades algebraicas de la función $x\mapsto x^3+x$. No invoque la derivada.

## D. Hipótesis y contraejemplos

### Ejercicio 0.14 — Dos hipótesis que no se deben borrar (`EDC-C00-EXR-014`)

(a) Dé un ejemplo de función continua y acotada en $(0,1)$ que no alcance ni su supremo ni su ínfimo. (b) Defina una función sobre $[0,1]$ que tome los valores $0$ y $1$, pero no tome el valor $1/2$. Indique con exactitud qué hipótesis del teorema del valor intermedio no se cumple.

### Ejercicio 0.15 — Una suma, dos elecciones de muestras (`EDC-C00-EXR-015`)

Sea $d(x)=1$ si $x\in\mathbb Q$ y $d(x)=0$ si $x\notin\mathbb Q$, para $x\in[0,1]$. Dada una partición cualquiera $0=x_0<\cdots<x_n=1$, elija un punto $t_k\in(x_{k-1},x_k)$ en cada subintervalo y considere $S=\sum_{k=1}^n d(t_k)(x_k-x_{k-1})$. Muestre que se puede obtener tanto $S=0$ como $S=1$, sin modificar la partición.

### Ejercicio 0.16 — Una sucesión testigo no basta (`EDC-C00-EXR-016`)

Construya una función $f:\mathbb R\to\mathbb R$ y una sucesión $x_n\to0$ tales que $f(x_n)\to f(0)$, aunque $f$ no sea continua en $0$. Explique qué palabra de la Proposición 0.2 impide inferir continuidad a partir de su ejemplo.

## E. Demostraciones y descubrimiento

### Ejercicio 0.17 — Bisección, existencia y control del error (`EDC-C00-EXR-017`)

Parta de $I_0=[1,2]$, cuya imagen por $p(x)=x^2-2$ cambia de signo. Construya por bisección una sucesión de intervalos cerrados $I_n=[a_n,b_n]$ tales que $p(a_n)\le0\le p(b_n)$ y $|I_n|=2^{-n}$. Demuestre que sus extremos convergen a un mismo número $r$ que satisface $r^2=2$ y que $|a_n-r|,|b_n-r|\le2^{-n}$. No dé por demostrada la convergencia por el mero hecho de dibujar intervalos cada vez menores.

### Ejercicio 0.18 — La misma potencia desde dos problemas (`EDC-C00-EXR-018`)

Para $r>0$, en $[0,r]$ y con $f(x)=x^2$, calcule las sumas izquierda y derecha de rectángulos correspondientes a $n$ subintervalos iguales, y demuestre que ambas convergen a $r^3/3$. Compruebe además que el cociente incremental de $F(x)=x^3/3$ tiende a $x^2$ cuando el incremento tiende a cero. Explique por qué estas igualdades particulares no constituyen todavía una demostración del Teorema Fundamental del Cálculo.

---

**Trazabilidad:** 18 enunciados propios, `EDC-C00-EXR-001` a `EDC-C00-EXR-018`; 18 soluciones correspondientes, en [EDC-C00-SOLUCIONES](capitulo-00-soluciones.html). Los ejercicios no suman nuevas unidades al indicador global de capítulos.
