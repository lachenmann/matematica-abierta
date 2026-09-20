# La naturaleza del continuo — FDC-AUD-022

## Procedencia y trazabilidad

Módulo: `ProgramaTransparente.lean`, incorporado a `MatematicaAbierta.lean` para que Lake lo compile. Fuente canónica: Google Drive, `03_Formalizacion/FDC_T002_programa_transparente.lean`, SHA-256 original `b5893820588c0f0d51887a7eb596436cd9ea0041a0c6d68920216cae19ded786`, blob Git original `aef0754071eb6fdfde0e698737831f81f09e5e4a`. Se preservan los 40 teoremas heredados de AUD-021. La compilación CI inicial de la PR #105 encontró una recursión excesiva de `simp` en el primer teorema nuevo, línea 816; la corrección sustituye la simplificación indiscriminada por la reducción de **un solo paso** de `buscarHasta` y `rw [h]`. El hash del archivo reparado es diferente al original y su nueva versión requiere otra compilación.

## Siete teoremas añadidos — pruebas desarrolladas en el proyecto

| Declaración (namespace `Continuo.Semantica`) | Dependencias directas y contenido |
| --- | --- |
| `programaVisible_estable_succ` | Definición de `programaVisible` y ecuación recursiva de `buscarHasta`: una respuesta permanece al sumar un paso de combustible. |
| `programaVisible_estable` | `programaVisible_estable_succ`, inducción natural y `Nat.add_succ`: estabilidad con cualquier combustible adicional. |
| `programaVisible_grafo_iff` | Definiciones de `programaVisible` y `Responde`: igualdad definicional de los grafos. |
| `programaVisible_estabiliza_iff` | `programaVisible_estable`, testigo existencial y especialización `k=0`: respuesta eventual si y solo si estabilidad eventual. |
| `programaVisible_correcto` | Teorema propio heredado `responde_correcta` y `programaVisible_grafo_iff`: corrección condicionada por decididores correctos y cortes inferiores. |
| `programaVisible_dominio_iff` | Teorema propio heredado `responde_iff_fuera_frontera` y `programaVisible_grafo_iff`: dominio para cortes interpretados en los reales clásicos de Mathlib. |
| `programaVisible_sin_salida_frontera` | Teorema propio heredado `responde_ausente_en_frontera` y `programaVisible_grafo_iff`: no aparece ninguna respuesta exactamente en la frontera. |

**Clasificación:** las siete demostraciones son desarrollos propios del proyecto, con dependencias mixtas en Lean y Mathlib. No se presentan como teoremas originales de Mathlib ni se cuentan las 40 declaraciones heredadas como siete resultados adicionales. La parte del dominio reutiliza la estructura `ℝ` de Mathlib como semántica externa, no construye los reales a partir de cortes.

## Contrato operacional y límites

`programaVisible χA χB p n := buscarHasta χA χB p n` es una familia total de observaciones con combustible `n`; no es un decisor total de pertenencia a la suma. `Responde χA χB p b` significa que alguna observación devuelve `some b`. Las pruebas no establecen la semántica de la antigua rutina opaca `partial def buscarSinCota`, ni la equiparan con la familia transparente; tampoco prueban T002b/T002f, una reducción a la detención o un intérprete completo sin combustible. Para acreditar FOR-07 hay que verificar el código **final** en GitHub Actions con `lake build --wfail`, inspeccionar los enunciados y comprobar ausencia de `sorry`, `admit` y axiomas añadidos. No se modifica el cierre crítico del expediente por una compilación selectiva.
