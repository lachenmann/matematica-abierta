# Estado del proyecto

Última actualización: 2026-09-13

## Fuente

- Obra: Sheldon Axler, *Linear Algebra Done Right*, 4.ª edición.
- Fuente canónica: PDF oficial de Sheldon Axler, versión **16-08-2026**.
- Copia de trabajo inicial: 25-03-2024.
- Capítulos 1–2 y apertura/Secciones 3A–3B cotejados contra el PDF oficial de 16-08-2026.
- Errata oficial revisada: las correcciones de p. 28 (`F` → `R`) y p. 35 (`w_m` → `w_n`) afectan a 2A y ya están incorporadas; no se listan correcciones específicas para las pp. 39–68 de 2B–2C y 3A–3B.

## Avance público

- Prefacio para estudiantes: `BORRADOR COTEJADO`.
- Apertura del capítulo 1: `BORRADOR COTEJADO`.
- Sección 1A — $\mathbf R^n$ y $\mathbf C^n$: `COTEJADO`; **15/15 ejercicios resueltos**.
- Sección 1B — Definición de espacio vectorial: `COTEJADO`; **8/8 ejercicios resueltos**.
- Sección 1C — Subespacios: `COTEJADO`; **24/24 ejercicios resueltos**.
- Capítulo 1: **47/47 ejercicios**, primera pasada pública completa; QA global en `CHAPTER1_QA.md`.
- Apertura del capítulo 2 — Espacios vectoriales de dimensión finita: `COTEJADO`.
- Sección 2A — Span e independencia lineal: `COTEJADO`; **20/20 ejercicios resueltos**, soluciones `VERIFICADO`.
- Sección 2B — Bases: `COTEJADO`; **11/11 ejercicios resueltos**, soluciones `VERIFICADO`.
- Sección 2C — Dimensión: `COTEJADO`; **20/20 ejercicios resueltos**, soluciones `VERIFICADO`.
- Capítulo 2: **51/51 ejercicios**, primera pasada pública completa; QA global en `CHAPTER2_QA.md`.
- Apertura del capítulo 3 — Aplicaciones lineales: `COTEJADO`.
- Sección 3A — Espacio vectorial de aplicaciones lineales: `COTEJADO`; **17/17 ejercicios resueltos**, soluciones `VERIFICADO`.
- Sección 3B — Espacios nulos e imágenes: `COTEJADO`; **33/33 ejercicios resueltos**, soluciones `VERIFICADO`.
- Total acumulado de ejercicios resueltos: **148**.
- Glosario terminológico: **v0.9**.
- Siguiente bloque activo: **3C — Matrices**.

## QA de 1A

- numeración 1.1–1.18 preservada;
- ejercicios 1–15 preservados;
- fórmulas cotejadas con la fuente 2026;
- soluciones sin uso de resultados posteriores.

## QA de 1B

- numeración 1.19–1.32 preservada;
- ejercicios 1–8 preservados;
- diferencia entre $0\in\mathbf F$ y el vector $0\in V$ mantenida explícitamente;
- ejercicio 5 resuelto en ambas direcciones;
- ejercicio 8 verifica la estructura compleja de la complexificación sin teoría posterior.

## QA de 1C

- numeración 1.33–1.46 preservada;
- ejercicios 1–24 preservados y resueltos;
- separación entre suma de subespacios y suma directa;
- criterios 1.45 y 1.46 usados en las soluciones;
- ejercicio 24 prueba existencia y unicidad de la descomposición par/impar.

## QA de 2A

- numeración 2.1–2.25 preservada;
- ecuación numerada 2.20 preservada;
- definiciones de span, dimensión finita/infinita, independencia y dependencia lineal cotejadas;
- lema de dependencia lineal 2.19 y teorema 2.22 incluidos con demostración;
- correcciones oficiales de pp. 28 y 35 incorporadas;
- 20/20 ejercicios resueltos;
- ejercicio 20 resuelto sin recurrir a división/factorización polinómica posterior.

## QA de 2B

- numeración 2.26–2.33 preservada, incluida la ecuación 2.29;
- definición y criterio de base cotejados;
- teoremas 2.30–2.33 incluidos con demostración;
- sin erratas específicas registradas para 2B;
- 11/11 ejercicios resueltos;
- ejercicios 3 y 4 construyen explícitamente bases, extensiones y complementos directos;
- ejercicios 6 y 8 incluyen contraejemplos explícitos;
- ejercicio 11 usa la complexificación definida en 1B.

## QA de 2C

- numeración 2.34–2.43 preservada;
- ecuaciones numeradas 2.44 y 2.45 preservadas;
- definición de dimensión y resultados 2.37–2.43 incluidos con demostración;
- analogía cardinalidad/dimensión preservada;
- sin erratas específicas registradas para las pp. 44–50;
- 20/20 ejercicios resueltos;
- ejercicios 3–7 resueltos sin anticipar el capítulo 4;
- ejercicio 10 verifica la base asociada a los polinomios de Bernstein por triangularidad de coeficientes;
- ejercicios 14–16 desarrollan cotas de dimensión de intersecciones;
- ejercicio 19 aporta contraejemplo explícito a la falsa inclusión–exclusión de tres subespacios;
- ejercicio 20 demuestra la identidad simétrica correcta sumando tres aplicaciones de 2.43.

## QA de 3A

- apertura del capítulo 3 preservada, incluidos los supuestos permanentes sobre $\mathbf F,U,V,W$;
- la fotografía de la apertura, material de tercero bajo CC BY-SA, no se reproduce y queda señalada editorialmente;
- numeración 3.1–3.10 preservada;
- definición de aplicación lineal, notación $\mathcal L(V,W)$ y ejemplos 3.3 cotejados;
- lema de la aplicación lineal 3.4 incluido con demostración completa;
- suma, multiplicación por escalares y producto/composición de aplicaciones lineales preservados;
- propiedades 3.8 y resultado 3.10 preservados;
- errata oficial revisada: sin correcciones específicas para las pp. 51–58;
- 17/17 ejercicios resueltos;
- ejercicios 5 y 6 desarrollan las demostraciones que Axler deja al lector en 3.6 y 3.8;
- ejercicio 11 demuestra que el centro de $\mathcal L(V)$ está formado por los múltiplos escalares de $I$ sin usar matrices;
- ejercicio 17 demuestra que los únicos ideales bilaterales de $\mathcal L(V)$ son $\{0\}$ y $\mathcal L(V)$ mediante aplicaciones elementales definidas sobre una base, sin anticipar 3C.

## QA de 3B

- numeración 3.11–3.28 preservada, incluidas las ecuaciones/sistemas 3.25 y 3.27;
- espacio nulo, inyectividad, imagen y sobreyectividad cotejados con ejemplos y demostraciones;
- teorema fundamental de las aplicaciones lineales 3.21 preservado con demostración completa;
- resultados dimensionales 3.22 y 3.24 y aplicaciones a sistemas lineales 3.26 y 3.28 preservados;
- notación original $\operatorname{null}T$ y $\operatorname{range}T$ conservada en fórmulas, con «espacio nulo» e «imagen» en la prosa;
- errata oficial revisada: sin correcciones específicas para las pp. 59–68;
- 33/33 ejercicios resueltos y verificados;
- ejercicios 19–20 construyen inversas laterales sin anticipar invertibilidad de 3D;
- ejercicios 21–26 desarrollan preimágenes, cotas de dimensión y factorización de aplicaciones usando sólo 3B y resultados anteriores;
- ejercicio 28 demuestra sobreyectividad mediante restricciones a $\mathcal P_n(\mathbf R)$ y 3.21;
- ejercicio 29 aplica esa herramienta a $5q''+3q'=p$;
- ejercicio 32 usa la clasificación de ideales bilaterales de 3A;
- ejercicio 33 verifica la complexificación de una aplicación lineal y conecta con el Ejercicio 8 de 1B.

## Estados

`PENDIENTE → BORRADOR → COTEJADO → VERIFICADO → CERRADO`

Una unidad `CERRADA` ha superado cotejo con la fuente canónica, control matemático, terminológico y editorial. Los capítulos 1 y 2 y las Secciones 3A–3B permanecen abiertos a revisión comunitaria antes de la promoción definitiva a `CERRADO`.
