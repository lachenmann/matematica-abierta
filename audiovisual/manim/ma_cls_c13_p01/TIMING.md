# Temporización de voz — MA-CLS-C13-P01

## Resultado

La narración queda temporalmente modelada en **185,0 s**.

El cálculo se hizo sobre una versión hablada de las expresiones matemáticas:

- **353 palabras equivalentes**;
- ritmo de referencia: **115 palabras/minuto**;
- voz estimada: **184,1 s**;
- permanencia final: **0,9 s**;
- duración total objetivo: **185,0 s = 3:05**.

Este ritmo es deliberadamente más lento que una locución informativa ordinaria porque las expresiones matemáticas requieren articulación y tiempo de inspección visual.

## Distribución

| Unidad | Palabras habladas | Voz objetivo | Intervalo |
|---|---:|---:|---:|
| Apertura | 42 | 21,9 s | 0,0–21,9 |
| MA-VIZ-C13-002 | 66 | 34,4 s | 21,9–56,3 |
| Puente 1 | 14 | 7,3 s | 56,3–63,6 |
| MA-VIZ-C13-003 | 77 | 40,2 s | 63,6–103,8 |
| Puente 2 | 14 | 7,3 s | 103,8–111,1 |
| MA-VIZ-C13-004 | 78 | 40,7 s | 111,1–151,8 |
| Cierre | 62 | 32,3 s + 0,9 s | 151,8–185,0 |

## Criterio de sincronización

Las fórmulas **no deben aparecer completas antes de que la narración haya presentado sus componentes**.

Por tanto:

1. concepto verbal;
2. aparición del objeto o símbolo;
3. relación matemática;
4. breve permanencia visual.

La animación puede completar un movimiento durante una pausa natural, pero no debe obligar a acelerar la voz.

## Diferencia respecto del preview silencioso

El preview aprobado dura **49,799 s**. No hay que multiplicar todos sus tiempos por un factor uniforme.

La expansión será **semántica**, no proporcional:

- más permanencia cuando se lee una fórmula;
- más tiempo en la construcción de una relación;
- menos expansión en fades y transiciones;
- puentes ajustados casi exactamente a la voz.

## Próximo paso

Incorporar estos tiempos como parámetros de \`MAClsC13P01\` y producir un **timed preview de 185 s**, todavía sin audio. Después de ese QA podrá grabarse o generarse una voz de referencia y hacer el ajuste fino.
