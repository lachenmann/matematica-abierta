---
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0006
status: published
draft: false
date-created: '2026-10-21'
date-modified: '2026-10-21'
areas:
  - algebra
level: intermedio
topics:
  - algebra-lineal
solution-status: complete
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
number-sections: false
toc: true
toc-depth: 3
title: Convenciones de lectura
subtitle: Álgebra para matemáticos · Tomo II
content-id: MA-BCH-0392
related:
  - MA-BOK-0006
---

[Índice del tomo II](/libros/para-matematicos/algebra-para-matematicos-tomo-ii.md)

Los resultados se formulan sobre el cuerpo que se declara en cada pasaje. Los ejemplos numéricos ordinarios se interpretan sobre los reales cuando el capítulo así lo establece; las cuentas en cuerpos finitos se señalan expresamente. En el capítulo 20 todos los espacios tienen dimensión finita: la primera unidad admite un cuerpo conmutativo y las tres restantes trabajan sobre los reales o los complejos.

| Símbolo | Significado |
|---|---|
| $\operatorname{rg}T$, $\operatorname{rg}A$ | Rango de una aplicación o de su matriz. |
| $\operatorname{nul}T$ | Dimensión del núcleo. |
| $[T]_{\mathcal C\leftarrow\mathcal B}$ | Matriz que recibe coordenadas en $\mathcal B$ y entrega coordenadas en $\mathcal C$. |
| $P_{\mathcal C\leftarrow\mathcal B}$ | Matriz de transición de coordenadas de $\mathcal B$ a coordenadas de $\mathcal C$. |
| $A^{\mathsf T}$ | Transpuesta, sin conjugación. |
| $V^*$ | Dual algebraico. |
| $T'$ | Aplicación dual: $T'g=g\circ T$. |
| $A^\dagger=\overline A^{\mathsf T}$ | Conjugada transpuesta de una matriz. |
| $T^*$ | Adjunto respecto de los productos internos elegidos. |
| $A^+$ | Pseudoinversa de Moore–Penrose. |
| $\langle v,w\rangle$ | Producto interno lineal en la primera entrada. |
| $\chi_T(t)$, $m_T(t)$ | Polinomio característico $\det(tI-[T])$ y polinomio mínimo mónico. |

Las bases son ordenadas al escribir coordenadas, que se organizan en columnas. Si una transición $P$ convierte coordenadas nuevas en antiguas, el cambio de matriz de un operador es $P^{-1}AP$. Para una forma bilineal se cambian simultáneamente sus dos entradas y la regla es $P^{\mathsf T}MP$; para una forma hermitiana es $P^\dagger HP$.

La base del espacio cero es la lista vacía; su columna de coordenadas también es vacía. Las sumas vacías valen cero y los productos vacíos, uno. El determinante de orden cero y los polinomios característico y mínimo del único operador sobre el espacio cero valen uno. La traza de ese operador vale cero.

El uso del teorema fundamental del álgebra conserva el alcance declarado en el tomo I: es un resultado externo admitido. La clasificación de Jordan exige escisión en el cuerpo elegido. La diagonalización exige además factores lineales distintos en el polinomio mínimo.
