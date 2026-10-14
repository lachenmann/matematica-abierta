---
title: Capítulo 11 — Ejercicios de síntesis
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
source-id: EDC-C11-EJERCICIOS
source-sha256: 1f685d1728cde17f3e6c58d2c3ba36e8c76b6b2854dc08f8073fe8ba71686c3f
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-11.html) · [Ejercicios](capitulo-11-ejercicios.html) · [Soluciones](capitulo-11-soluciones.html)

Los treinta problemas recorren las cinco convergencias conceptuales del libro y exigen **demostrar**, no sólo recordar fórmulas. Los problemas `EDC-C11-EXR-001--030` corresponden uno por uno a [EDC-C11-SOLUCIONES](capitulo-11-soluciones.html).

## A. Qué constituye una prueba en cálculo

**Ejercicio 11.1 (`EDC-C11-EXR-001`).** Exponga la diferencia entre una expresión finita, una sucesión convergente y una aproximación certificada. Pruebe que $A_n=2-2^{-n}$ certifica el valor $2$, indicando una cota de error.

**Ejercicio 11.2 (`EDC-C11-EXR-002`).** Señale el límite o cuantificador que falta en cada frase: (a) «los términos de una serie tienden a cero; luego hay suma»; (b) «una función tiene derivadas de todo orden; luego coincide con Taylor»; (c) «Euler tiene un error local $O(h^2)$; luego su error global es $O(h^2)$». Ofrezca para (a) y (b) contraejemplos de C08–C09.

**Ejercicio 11.3 (`EDC-C11-EXR-003`).** Sean $f,g$ continuas en $[0,2]$ y derivables en $(0,2)$, con $f'=g'$ allí y $f(0)=g(0)+3$. Demuestre $f(x)=g(x)+3$ para todo $x\in[0,2]$.

**Ejercicio 11.4 (`EDC-C11-EXR-004`).** Para $f(x)=x^2$ y $g(x)=0$, compruebe $f'(0)=g'(0)$ y demuestre que ello no permite concluir $f-g$ constante en ningún intervalo abierto alrededor de cero.

**Ejercicio 11.5 (`EDC-C11-EXR-005`).** Distinga una condición de continuidad de una de derivabilidad usando $|x|$, y explique dónde falla exactamente aplicar Rolle a $|x|$ en $[-1,1]$.

## B. Reconstruir mediante integral y cotas de error

**Ejercicio 11.6 (`EDC-C11-EXR-006`).** Desde C06, pruebe $f(x)=f(0)+\int_0^x f'(t)dt$ para $f\in C^1([0,1])$. Identifique cuál parte del Teorema Fundamental se usa.

**Ejercicio 11.7 (`EDC-C11-EXR-007`).** Sea $g(t)=3t^2$ en $[0,2]$. Construya la única solución continua hasta los extremos de $y'=g$, $y(0)=4$, y compruebe la fórmula sin dividir por $y$.

**Ejercicio 11.8 (`EDC-C11-EXR-008`).** Sea $f$ cero en $[0,1]$ salvo $f(1/2)=7$. Pruebe su integrabilidad de Darboux y el valor de su integral mediante particiones, no mediante un principio de medida no demostrado.

**Ejercicio 11.9 (`EDC-C11-EXR-009`).** Para la función de Dirichlet $d(x)=1$ si $x\in\mathbb Q$ y $0$ en otro caso, sobre $[0,1]$, halle $L(d,P)$ y $U(d,P)$ para toda partición $P$ y determine la integrabilidad.

**Ejercicio 11.10 (`EDC-C11-EXR-010`).** Para $f(x)=x^2$ en $[0,1]$, obtenga la cota del Teorema 11.3 para cualquier suma de $n$ rectángulos de igual ancho, y determine un $n$ que garantice error menor que $10^{-3}$.

**Ejercicio 11.11 (`EDC-C11-EXR-011`).** Considere $f(x)=2x$ en $[0,1]$. Calcule la suma de extremos derechos de $n$ rectángulos, su error **exacto** frente a la integral, y compárelo con la cota universal del Teorema 11.3.

**Ejercicio 11.12 (`EDC-C11-EXR-012`).** Si $f\in C^1([0,1])$, $f(0)=3$ y $|f'|\le4$, pruebe $\left|\int_0^h f(t)dt-3h\right|\le2h^2$ para $0\le h\le1$. Explique qué papel cumple el valor medio.

## C. La frontera de las series y los desarrollos locales

**Ejercicio 11.13 (`EDC-C11-EXR-013`).** Justifique la divergencia de $\sum_{n=1}^{\infty}1/n$ aun cuando su término general tienda a cero, utilizando bloques diádicos.

**Ejercicio 11.14 (`EDC-C11-EXR-014`).** Para $\sum_{n=0}^{\infty}x^n$, determine radio y comportamiento en $x=-1$ y $x=1$; explique por qué la igualdad con $1/(1-x)$ no autoriza sustituir esos puntos.

**Ejercicio 11.15 (`EDC-C11-EXR-015`).** Explique por qué C08 permite derivar término a término $\sum x^n$ para $|x|<1$ y pruebe $\sum_{n=1}^{\infty}nx^{n-1}=1/(1-x)^2$ allí. ¿Puede asegurarse la igualdad en $x=-1$?

**Ejercicio 11.16 (`EDC-C11-EXR-016`).** Construya $T_{2,0}e^x$, y mediante Taylor–Lagrange demuestre para $0\le x\le1/2$ la cota $|e^x-T_{2,0}e^x|\le e^{1/2}x^3/6$.

**Ejercicio 11.17 (`EDC-C11-EXR-017`).** Dé una función $C^\infty$ que no sea analítica en cero, pruebe que su Taylor converge para todo $x$, y que no la representa para $x\ne0$.

**Ejercicio 11.18 (`EDC-C11-EXR-018`).** Formule con cuantificadores la distinción entre (i) $f(x)=T_{n,a}f(x)+o(|x-a|^n)$ al acercarse $x$ a $a$ con $n$ fijo y (ii) $R_n(x)\to0$ con $x$ fijo y $n\to\infty$.

## D. De las leyes diferenciales a las trayectorias

**Ejercicio 11.19 (`EDC-C11-EXR-019`).** Resuelva $y'+2y=4$, $y(0)=1$ y pruebe existencia y unicidad sobre $\mathbb R$, identificando qué teorema del libro se utiliza.

**Ejercicio 11.20 (`EDC-C11-EXR-020`).** Exhiba para $y'=\sqrt{|y|}$, $y(0)=0$, dos soluciones globales distintas; verifique su unión $C^1$ y por qué no contradicen el Teorema 10.6.

**Ejercicio 11.21 (`EDC-C11-EXR-021`).** Resuelva $y'=y^2$, $y(0)=1$ sobre la rama positiva y demuestre que no admite prolongación real continua a través de $t=1$.

**Ejercicio 11.22 (`EDC-C11-EXR-022`).** Para $y'=y$, $y(0)=1$, obtenga el paso de Euler de longitud $h>0$ y el error local exacto. Demuestre $0\le e^h-(1+h)\le e^h h^2/2$ y explique qué falta para controlar los pasos sucesivos.

**Ejercicio 11.23 (`EDC-C11-EXR-023`).** Aplique el Teorema 10.3 para construir la solución de $y'+y=t$, $y(0)=0$. Compruebe por derivación y distinga la fórmula explícita de una presunción de existencia general de EDO.

## E. Reconstruir la historia sin anacronismos

**Ejercicio 11.24 (`EDC-C11-EXR-024`).** Compare el agotamiento geométrico de Arquímedes y los comentarios de Liu Hui: identifique un parecido matemático y una atribución anacrónica que deba evitarse, según las fuentes consultadas.

**Ejercicio 11.25 (`EDC-C11-EXR-025`).** Explique qué significa decir que la escuela de Kerala trabajó con identidades equivalentes a ciertas series de trigonometría y $\pi$. Distinga reconstrucción moderna, transmisión textual indirecta y prueba de una teoría $\varepsilon$–$N$.

**Ejercicio 11.26 (`EDC-C11-EXR-026`).** Distinga la genealogía de fluxiones de Newton y la notación operatoria de Leibniz. ¿Por qué una prueba actual del Teorema Fundamental no puede atribuirse literalmente a uno de ellos sin cotejo?

**Ejercicio 11.27 (`EDC-C11-EXR-027`).** Coloque en orden cronológico la publicación de *Cours d'analyse* de Cauchy (1821), el artículo de Darboux sobre funciones discontinuas (1875) y *Methodus incrementorum* de Brook Taylor (1715). Indique cuáles de esas fechas están respaldadas documentalmente en las notas.

## F. Un examen de cierre matemático e histórico

**Ejercicio 11.28 (`EDC-C11-EXR-028`).** Dé cinco implicaciones matemáticas falsas, cada una de capítulos distintos, y un contraejemplo válido. Añada una hipótesis suficiente **cuando se haya demostrado en EDC**, sin inventar un teorema general.

**Ejercicio 11.29 (`EDC-C11-EXR-029`).** Una sucesión de funciones continuas $f_n(x)=x^n$ en $[0,1]$ converge puntualmente a $f$. Halle $f$ y pruebe que no existe una sucesión $\varepsilon_n\to0$ con $|f_n(x)-f(x)|\le\varepsilon_n$ para todo $x\in[0,1]$. Relaciónelo con la cota interior de C08.

**Ejercicio 11.30 (`EDC-C11-EXR-030`).** **Síntesis final.** Sea $y(t)=e^{-t}$, $t\in[0,1]$, y $A(x)=\int_0^x y(t)dt$. (a) Determine $A$ mediante C06 y compruebe $A'=y$. (b) Obtenga una cota de error para cualquier suma de $n$ rectángulos uniformes de $\int_0^1y$. (c) Demuestre $|A(x)-x|\le x^2/2$ para $0\le x\le1$. (d) Verifique que $y$ es la única solución del PVI $y'=-y$, $y(0)=1$. (e) Explique el significado y los límites de las cuatro pruebas; no confunda ninguna de ellas con evidencia empírica de un modelo de decaimiento.
