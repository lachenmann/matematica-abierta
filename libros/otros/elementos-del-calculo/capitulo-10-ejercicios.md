---
title: Capítulo 10 — Ejercicios
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
source-id: EDC-C10-EJERCICIOS
source-sha256: dd5fe3af40a2cbf4cbc733e89217ccc0eeb41095726e45c35e1773b441932065
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-10.md) · [Ejercicios](capitulo-10-ejercicios.md) · [Soluciones](capitulo-10-soluciones.md) · [Notas históricas](capitulo-10-notas.md)

Cada problema debe resolverse con los resultados disponibles hasta C10. Distinga la existencia de una solución, la verificación por sustitución, la demostración de unicidad y el intervalo donde se afirma cada resultado. Las soluciones están en [un archivo independiente](capitulo-10-soluciones.md); la numeración `EDC-C10-EXR-nnn` se corresponde exactamente con `EDC-C10-SOL-nnn`.

## A. Interpretar ecuaciones y condiciones iniciales

**Ejercicio 10.1 (`EDC-C10-EXR-001`).** Clasifique $y'=2t$, $y'+3y=\cos t$, $y'=y^2$ y $y''+4y=0$ por orden, carácter lineal y autonomía. Indique cuál requiere, en general, dos condiciones iniciales escalares.

**Ejercicio 10.2 (`EDC-C10-EXR-002`).** Compruebe que $y(t)=2e^{-3t}+1$ resuelve $y'+3y=3$. Determine el dato en $t=0$ y explique por qué la comprobación sola no demuestra que no existan otras soluciones con el mismo dato.

**Ejercicio 10.3 (`EDC-C10-EXR-003`).** Una función satisface $y'(t)=2t$ en toda $\mathbb R$. Demuestre que tiene la forma $t^2+C$. ¿Cuál es la solución del PVI $y(1)=5$? Justifique unicidad.

**Ejercicio 10.4 (`EDC-C10-EXR-004`).** Interprete rigurosamente la forma integral $y(t)=y_0+\int_{t_0}^{t}F(s,y(s))ds$. Explique por qué ésta no constituye, por sí sola, una prueba de existencia de soluciones para cualquier función continua $F$.

## B. Reconstrucción, crecimiento y coeficientes variables

**Ejercicio 10.5 (`EDC-C10-EXR-005`).** Halle y verifique el único PVI $y'=3t^2-2t$, $y(0)=4$ sobre $\mathbb R$.

**Ejercicio 10.6 (`EDC-C10-EXR-006`).** Resuelva $y'=-2y$, $y(0)=7$, pruebe unicidad sin dividir por $y$ y determine $\lim_{t\to\infty}y(t)$.

**Ejercicio 10.7 (`EDC-C10-EXR-007`).** Sea $a(t)=2t$ en $\mathbb R$. Resuelva $y'=2ty$, $y(1)=3$. Determine el signo de la solución y sus intervalos de crecimiento y decrecimiento.

**Ejercicio 10.8 (`EDC-C10-EXR-008`).** Pruebe que la única solución del PVI $y'=a(t)y$, $y(t_0)=0$ es $y\equiv0$ cuando $a$ es continua, y explique por qué la división por $y$ perdería este caso.

**Ejercicio 10.9 (`EDC-C10-EXR-009`).** Encuentre $y$ si $y'=1/(1+t^2)$, $y(0)=2$. Determine si la solución está definida sobre toda $\mathbb R$ y demuestre su unicidad.

## C. Factor integrante y estabilidad

**Ejercicio 10.10 (`EDC-C10-EXR-010`).** Resuelva y compruebe $y'+2y=3$, $y(0)=1$, mostrando el factor integrante y los límites correctos de la integral.

**Ejercicio 10.11 (`EDC-C10-EXR-011`).** Resuelva $y'+y=t$, $y(0)=0$. Compruebe mediante derivación y diga qué sucede cuando $t\to\infty$.

**Ejercicio 10.12 (`EDC-C10-EXR-012`).** Resuelva $y'+(1/t)y=t$ con $y(1)=2$ sobre $(0,\infty)$. Explique por qué la afirmación de existencia sobre todo $\mathbb R$ no está justificada.

**Ejercicio 10.13 (`EDC-C10-EXR-013`).** Demuestre que toda solución de $y'+p(t)y=q(t)$ sobre un intervalo difiere de una solución particular por $Ce^{-P(t)}$. Identifique la dependencia respecto del dato inicial.

**Ejercicio 10.14 (`EDC-C10-EXR-014`).** Para $y'+y=q_i(t)$, $i=1,2$, sobre $[0,2]$, con $|q_1-q_2|\le1/10$ e iniciales $a_1,a_2$ con $|a_1-a_2|\le1/5$, use el Teorema 10.4 para obtener una cota explícita de $|y_1(2)-y_2(2)|$.

**Ejercicio 10.15 (`EDC-C10-EXR-015`).** Resuelva $y'+(2t)y=2t$ en $\mathbb R$ si $y(0)=0$. Verifique que $y(t)=1-e^{-t^2}$ satisface el dato y la ecuación; justifique su unicidad.

## D. Separación, equilibrios y unicidad

**Ejercicio 10.16 (`EDC-C10-EXR-016`).** Resuelva en la rama $y>0$ el PVI $y'=t y^2$, $y(0)=1$. Indique el intervalo máximo que contiene cero en el que su fórmula permanece positiva y explique la singularidad de borde.

**Ejercicio 10.17 (`EDC-C10-EXR-017`).** Determine los equilibrios de $y'=y(2-y)$. Para $y(0)=1$, halle y compruebe una solución explícita; indique si aumenta o disminuye cuando $t\ge0$.

**Ejercicio 10.18 (`EDC-C10-EXR-018`).** Resuelva el PVI $y'=\cos t\, y$, $y(0)=-2$. Explique por qué el signo no cambia aun cuando $\cos t$ cambia de signo.

**Ejercicio 10.19 (`EDC-C10-EXR-019`).** El PVI $y'=\sqrt{|y|}$, $y(0)=0$ admite la solución nula. Construya dos soluciones adicionales distintas, verificando continuidad de sus derivadas en los tiempos de partida.

**Ejercicio 10.20 (`EDC-C10-EXR-020`).** Justifique la desigualdad $|u(1-u/K)-v(1-v/K)|\le(1+2M/K)|u-v|$ cuando $|u|,|v|\le M$, $K>0$. Deduzca unicidad **entre soluciones existentes y acotadas sobre un compacto** para la ecuación logística.

**Ejercicio 10.21 (`EDC-C10-EXR-021`).** Para $r=2$, $K=10$, $y(0)=2$, halle la solución logística exacta y el límite a tiempo futuro. Calcule el instante en el que alcanza $5$.

**Ejercicio 10.22 (`EDC-C10-EXR-022`).** Estudie $y'=2y(1-y/10)$ con dato $y(0)=-5$. Calcule el tiempo positivo en que se anula el denominador de la fórmula logística y explique por qué no puede proclamarse solución global para ese dato.

## E. Modelos y segundo orden

**Ejercicio 10.23 (`EDC-C10-EXR-023`).** En el modelo de enfriamiento con $T_a=20$, $k=1/2$ por hora y $T(0)=80$, obtenga $T(t)$ para $t\ge0$ y el tiempo exacto en que $T=35$. Compruebe las unidades del exponente.

**Ejercicio 10.24 (`EDC-C10-EXR-024`).** Una temperatura satisface $T'=-T+10+\sin t$, $T(0)=0$. Resuelva mediante factor integrante y verifique que la solución satisface el dato.

**Ejercicio 10.25 (`EDC-C10-EXR-025`).** Un cuerpo obedece $mv'=mg-\gamma v$, con $m=2$, $g=10$, $\gamma=4$ en unidades coherentes, y $v(0)=0$. Halle su velocidad terminal, su fórmula $v(t)$ y el instante en que alcanza la mitad de la velocidad terminal.

**Ejercicio 10.26 (`EDC-C10-EXR-026`).** Resuelva $x''+9x=0$ con $x(0)=2$, $x'(0)=-3$. Verifique ambas condiciones iniciales y pruebe la unicidad mediante la energía de la diferencia de dos soluciones.

**Ejercicio 10.27 (`EDC-C10-EXR-027`).** Para $x''+\omega^2x=0$, demuestre que $(x')^2+\omega^2 x^2$ es constante. Explique qué combinación de datos iniciales fuerza la solución nula y por qué este argumento no es un teorema general para cualquier ecuación de segundo orden.

## F. Diagnóstico fundacional y aproximación

**Ejercicio 10.28 (`EDC-C10-EXR-028`).** Distinga con ejemplos concretos las afirmaciones: «existe solución», «es única en un PVI», «está definida globalmente», «su fórmula tiene una singularidad». Use tres ecuaciones de C10 y no invoque un teorema general de existencia.

**Ejercicio 10.29 (`EDC-C10-EXR-029`).** Sea $y'=y$, $y(0)=1$. Compare el paso de Euler desde $t=0$ hasta $h>0$ con la solución exacta y demuestre mediante Taylor que el error local es a lo sumo $e^h h^2/2$. Explique por qué no se trata de un control automático del error tras $N$ pasos.

**Ejercicio 10.30 (`EDC-C10-EXR-030`).** **Síntesis.** Considere la EDO lineal $y'+2y=1+t$, $y(0)=1$. (a) Construya una solución exacta por factor integrante. (b) Compruebe la ecuación y la unicidad. (c) Calcule $y'(0)$ y $y''(0)$, construya $T_{2,0}y$. (d) Deduzca una cota explícita del error de Taylor en $0\le t\le1$ usando Lagrange y una cota de la tercera derivada. Identifique los resultados previos que legitiman cada paso.

---

**Correspondencia:** los treinta problemas `EDC-C10-EXR-001--030` poseen las treinta soluciones `EDC-C10-SOL-001--030` en [el archivo de resoluciones](capitulo-10-soluciones.md), sin exigir C11.
