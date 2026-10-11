# Estado del proyecto

**Actualización:** 2026-09-16. **Naturaleza:** traducción española abierta NO OFICIAL de Axler, cuarta edición, bajo CC BY-NC 4.0. Edición de fuente canónica: [PDF oficial 16-08-2026](https://linear.axler.net/LADR4e.pdf); [errata](https://linear.axler.net/LADRErrata4e.html). La copia de 2024 es secundaria.

## Avance por unidad

| Unidad | Texto | Ejercicios | Estado de soluciones |
|---|---|---:|---|
| 1A — $\mathbf R^n$ y $\mathbf C^n$ | Primera pasada cotejada | 15/15 | Verificadas en el registro anterior |
| 1B — Definición de espacio vectorial | Primera pasada cotejada | 8/8 | Verificadas en el registro anterior |
| 1C — Subespacios | Primera pasada cotejada | 24/24 | Verificadas en el registro anterior |
| 2A — Span e independencia | Primera pasada cotejada | 20/20 | Verificadas en el registro anterior |
| 2B — Bases | Primera pasada cotejada | 11/11 | Verificadas en el registro anterior |
| 2C — Dimensión | Primera pasada cotejada | 20/20 | Verificadas en el registro anterior |
| 3A — Espacio vectorial de aplicaciones lineales | Primera pasada cotejada | 17/17 | Verificadas en el registro anterior |
| 3B — Espacios nulos e imágenes | Primera pasada cotejada | 33/33 | Verificadas en el registro anterior |
| 3C — Matrices | Primera pasada cotejada | 17/17 | Verificadas en el registro anterior |
| 3D — Invertibilidad e isomorfismos | 3.59–3.86 y enunciados traducidos | 24/24 | Redactadas y en primera revisión; QA independiente pendiente |
| 3E — Productos y cocientes | 3.87–3.107 y enunciados traducidos | 19/19 | Redactadas y en primera revisión; QA independiente pendiente |

**Acumulado:** $47+51+67+24+19=208$ soluciones redactadas; 165 previas verificadas según registro; 43 nuevas (3D y 3E) pendientes de QA final. «Primera pasada publicada» no equivale a `CERRADO` ni a revisión comunitaria completada.

## Control de fuente y QA

- Correcciones oficiales pp. 28 (`F`→`R`), 35 (`w_m`→`w_n`) y p. 85 / 3.68 (intercambio `V`/`W`) incorporadas. Sin entradas de errata específicas en pp. 96–104 al 16-09-2026.
- En 3C, diferencias de versiones 2024→2026: caso $c=0$ en 3.57 y espacios no nulos en ejercicio 2; no confundir con errata publicada.
- La fotografía de un tercero en la apertura de capítulo 3 no se reproduce. En 3E, la figura de 3.96 se acompaña de equivalente textual accesible; dibujo editorial propio pendiente si se quiere conservar el apoyo visual.
- Se preservan los números de resultado 3.87–3.107, la prueba de que suma y producto escalar en $V/U$ no dependen de representantes y la distinción entre producto externo y suma directa interna.

### QA por capítulos

- [Capítulo 1](CHAPTER1_QA.md): total 47; estados de primera pasada, no cierre definitivo.
- [Capítulo 2](CHAPTER2_QA.md): total 51; se incorporaron las dos erratas oficiales tempranas.
- Capítulo 3A–3C: 17+33+17=67 soluciones; teorema 3.21, factorización columna–fila 3.56 e igualdad rango fila/columna 3.57. Se conserva $\operatorname{null}T$ y $\operatorname{range}T$ en fórmulas, «espacio nulo» e «imagen» en prosa.
- [3D](CHAPTER3D_QA.md): el ejercicio 22 tiene **alcance matricial explícito $n\ge1$ bajo la definición 3.79**. Para $n=0$, existe un único operador sobre $\{0\}$ y la matriz $0\times0$; considerarla identidad e invertible es una **convención adicional propia, marcada `[NOTA]`**. Esta aclaración resuelve el conflicto editorial pero no convierte automáticamente las 24 soluciones en verificadas. Ejercicios 19 y 20 distinguen matrices invariantes y evaluación $p(3)$; 3.68 sigue la errata oficial.
- [3E](CHAPTER3E_QA.md): 19 soluciones; ejercicios 3–5, 13 y 16–19 sin hipótesis extra de finitud; ejercicio 9 requiere $1/2\in\mathbf F$ (aquí $\mathbf F=\mathbf R$ o $\mathbf C$); ejercicio 11 usa soportes infinitos disjuntos para probar infinitud del cociente; ejercicio 18 contempla cociente de dimensión cero. Pendientes revisión cruzada independiente y render.

## Terminología y colaboración

- [GLOSARIO.md](GLOSARIO.md) **v0.10** es la versión principal aún vigente; [suplemento 3D](GLOSARIO_3D.md) y [suplemento 3E](GLOSARIO_3E.md) provisionales, sin incremento ficticio de versión.
- Capas: `[AXLER]` original; `[TRAD]` traducción; `[SOL]` soluciones originales; `[NOTA]` añadidos originales; `[ERRATA]` intervención documentada.
- Issues y Pull Requests abiertos a revisión; separar traducción, decisiones propias y correcciones de la fuente.

## Estados y próximo paso

`PENDIENTE → BORRADOR → COTEJADO → VERIFICADO → CERRADO`. Para cada unidad se exige cotejo con fuente, control de hipótesis, fórmulas, glosario, soluciones y QA antes del cierre. **Siguiente: segunda lectura independiente de 3D y 3E; posteriormente 3F — Dualidad.**