# Estado del proyecto

Última actualización: 2026-09-16

## Fuente

- Obra: Sheldon Axler, *Linear Algebra Done Right*, 4.ª edición.
- Fuente canónica: PDF oficial de Sheldon Axler, versión **16-08-2026**.
- Copia de trabajo inicial: 25-03-2024, testimonio secundario.
- Capítulos 1–2 y apertura/Secciones 3A–3D cotejados en primera pasada contra el PDF oficial.
- Errata oficial: correcciones de p. 28 (`F` → `R`) y p. 35 (`w_m` → `w_n`) incorporadas en 2A. Para 3D, la entrada de p. 85 corrige el intercambio de $V,W$ en 3.68; la formulación del PDF actual se incorpora. No hay entradas específicas para pp. 39–81.
- Variantes 2024→2026 en 3C: el PDF actual trata $c=0$ en 3.57 y añade no nulidad de $V,W$ en el ejercicio 2; no se confunden variantes con erratas propias.

## Avance público

- Prefacio para estudiantes: `BORRADOR COTEJADO`.
- Apertura del capítulo 1: `BORRADOR COTEJADO`.
- 1A — $\mathbf R^n$ y $\mathbf C^n$: `COTEJADO`; **15/15** ejercicios.
- 1B — Definición de espacio vectorial: `COTEJADO`; **8/8** ejercicios.
- 1C — Subespacios: `COTEJADO`; **24/24** ejercicios.
- Capítulo 1: **47/47 ejercicios**, primera pasada pública completa; QA en `CHAPTER1_QA.md`.
- Apertura del capítulo 2: `COTEJADO`.
- 2A — Span e independencia: `COTEJADO`; **20/20** ejercicios verificados.
- 2B — Bases: `COTEJADO`; **11/11** ejercicios verificados.
- 2C — Dimensión: `COTEJADO`; **20/20** ejercicios verificados.
- Capítulo 2: **51/51 ejercicios**, primera pasada pública completa; QA en `CHAPTER2_QA.md`.
- Apertura del capítulo 3: `COTEJADO`.
- 3A — Espacio vectorial de aplicaciones lineales: `COTEJADO`; **17/17** ejercicios verificados.
- 3B — Espacios nulos e imágenes: `COTEJADO`; **33/33** ejercicios verificados.
- 3C — Matrices: `COTEJADO`; **17/17** ejercicios verificados.
- 3D — Invertibilidad e isomorfismos: **traducción de resultados 3.59–3.86 y enunciados 1–24 publicados**, **24/24 soluciones originales redactadas y sometidas a primera revisión**, con un punto de convención editorial abierto en ejercicio 22.
- Total: **189 soluciones redactadas**; las **165 anteriores verificadas**, las 24 de 3D todavía en primera revisión.
- Glosario base: **v0.10** y suplemento 3D [`GLOSARIO_3D.md`](GLOSARIO_3D.md), candidato a integración v0.11.
- Bloque siguiente después del control de 3D: **3E — Productos y cocientes de espacios vectoriales**.

## QA de 1A

- Numeración 1.1–1.18; ejercicios 1–15; fórmulas cotejadas contra 2026; soluciones sin resultados posteriores.

## QA de 1B

- Numeración 1.19–1.32; ejercicios 1–8; diferencia $0\in\mathbf F$ y $0\in V$; ejercicio 5 ambas direcciones; ejercicio 8 verifica complexificación sin teoría posterior.

## QA de 1C

- Numeración 1.33–1.46; ejercicios 1–24; separación suma/suma directa; criterios 1.45–1.46; ejercicio 24 prueba descomposición par/impar.

## QA de 2A

- Numeración 2.1–2.25 y ecuación 2.20; span, dimensión finita/infinita, independencia, lema 2.19 y teorema 2.22; erratas oficiales pp. 28 y 35 incorporadas; 20/20 ejercicios, incluido 20 sin división polinómica posterior.

## QA de 2B

- Numeración 2.26–2.33 y ecuación 2.29; criterio para base, reducción, existencia, extensión y complemento directo; 11/11 ejercicios; ejercicios 3–4 bases y complementos explícitos; 6 y 8 contraejemplos; 11 complexificación.

## QA de 2C

- Numeración 2.34–2.43 y ecuaciones 2.44–2.45; teoremas y analogía cardinalidad/dimensión; 20/20 ejercicios; 3–7 sin capítulo 4; 10 Bernstein; 14–16 cotas de intersección; 19 contraejemplo a inclusión–exclusión; 20 identidad simétrica.

## QA de 3A

- Apertura del capítulo, supuestos permanentes sobre $\mathbf F,U,V,W$, fotografía de tercero no reproducida por licencia distinta; numeración 3.1–3.10; definición, lema 3.4 y operaciones; 17/17 ejercicios; demostraciones 3.6/3.8 desarrolladas como `[SOL]`; ejercicio 11 centro $\mathcal L(V)$, 17 ideales bilaterales, sin matrices.

## QA de 3B

- Numeración 3.11–3.28 y sistemas 3.25/3.27; espacio nulo, imagen, inyectividad, sobreyectividad, teorema 3.21; 33/33 ejercicios. Se conserva $\operatorname{null}$ y $\operatorname{range}$; ejercicios 7,16,32 revisados para dependencias; 19–20 inversas laterales; 21–26 factorizaciones; 28–29 polinomios; 33 complexificación.

## QA de 3C

- Numeración 3.29–3.58, ecuación 3.47; matriz de $T$ y dependencia de bases, estructura $\mathbf F^{m,n}$, producto matricial, factorización columna–fila 3.56 y rango fila = columna 3.57; 17/17 ejercicios; ejercicio 12 asociatividad por composición; 16 rango uno; 17 criterios de inyectividad; variantes 2024→2026 en 3.57 y ejercicio 2 registradas.

## QA de 3D · primera revisión

- Fuente oficial 2026 pp. 82–95; resultados 3.59–3.86 y ecuaciones numeradas 3.66, 3.77 y 3.85; 24 enunciados íntegros traducidos en archivo separado, soluciones 1–24 en archivo `[SOL]`.
- Errata oficial p. 85, última línea de 3.68, registrada y corregida según autor: $ST=I_V\iff TS=I_W$.
- Separación de aplicaciones y matrices invertibles, isomorfismos, matrices de coordenadas y orientación de matrices de cambio de base.
- Ejercicios 5–8 usan bases adaptadas; 12–13 distinguen dimensión finita e infinita; 19 emplea escalamiento y permutación de bases sin determinantes; 20 mantiene $p(3)$ como evaluación; 24 argumenta mediante aplicaciones lineales.
- **Pendiente:** decisión explícita sobre matriz identidad $0\times0$ en ejercicio 22: 3.79 define $I_n$ para $n\ge1$; el caso de base vacía no debe corregirse silenciosamente. Segunda lectura editorial y revisión comunitaria antes de `CERRADO`.

## Estados

`PENDIENTE → BORRADOR → COTEJADO → VERIFICADO → CERRADO`

Los capítulos 1 y 2 y las secciones 3A–3C están completos en primera pasada y abiertos a revisión comunitaria antes de `CERRADO`. 3D está publicado en primera pasada, con 24 soluciones aún pendientes de promoción a `VERIFICADO` por QA final.
