# Auditoría matemática inicial — MA-Práctica v0.1

**Fecha:** 2026-09-22. **Ámbito:** cuatro ejercicios provisionales `MAP-DEMO-001`–`004` de `practica/exercises.mjs`. **Estado:** revisión estática inicial y pruebas de consistencia añadidas; revisión editorial final, QA de interfaz y publicación todavía pendientes. Ningún resultado está verificado formalmente en Lean.

## Revisión por ejercicio

| ID | Revisión de razonamiento | Hallazgo / acción |
| --- | --- | --- |
| MAP-DEMO-001 (fracciones) | m.c.m.(2,3)=6; 1/2=3/6; 1/3=2/6; suma 5/6. | Se eliminó el distractor `2/6 + 3/6` porque también suma 5/6 (conmutatividad): el enunciado anterior admitía dos respuestas matemáticamente equivalentes. Sustituido por `2/6 + 2/6`. Prueba automática comprueba unicidad del valor correcto entre opciones. |
| MAP-DEMO-002 (ecuación) | Distribuir y restar x a ambos miembros lleva a x−6=5 y x=11; sustitución 16=16. | La solución es única; se añadió comprobación numérica de la solución y de los distractores del paso final. |
| MAP-DEMO-003 (derivada) | Para u=x²+1 y g(u)=u³, (g∘u)'=3(x²+1)²·2x=6x(x²+1)². | Se añadió comprobación independiente por diferencias centradas en siete valores reales; es prueba de consistencia numérica, **no demostración** de la identidad para todo x. |
| MAP-DEMO-004 (contraposición) | Para n entero par, n=2k implica n²=2(2k²), que es par; por contraposición, n² impar implica n impar. | Se precisó el enunciado de la representación de paridad y el distractor `n=k/2` (verdadero para cualquier n entero si k=2n) pasó a `n=k/2 para algún k impar`, falso para n entero. Se añadió muestra computacional de enteros positivos y negativos; la justificación general sigue siendo la demostración algebraica descrita. |

## Alcance y cautelas

- Los IDs `MAP-DEMO-*` identifican material de demostración; no sustituyen problemas canónicos `MA-PRB-*` ni documentos maestros de Obsidian/Drive.
- Seleccionar pasos de una demostración de opción múltiple **no** implica haber redactado ni verificado formalmente la prueba.
- Los ratings de dificultad y Elo continúan siendo inventarios experimentales no calibrados, sin rankings ni medición comparable entre estudiantes.
- Las pruebas adicionales comprueban validación de entradas, máquina de estados, preservación de traza, cierre de sesiones, comportamiento Elo matemático y consistencia de los cuatro ejercicios; **no** cubren aún persistencia `localStorage`, duplicación de puntuaciones a nivel UI, borrado de datos, QA visual ni accesibilidad.
- La puerta M1 solo se considerará cerrada tras revisión matemática/editorial final y QA funcional/visual/accesibilidad, más CI verde para el último commit; integrar en Quarto exige después una puerta M2 independiente.
