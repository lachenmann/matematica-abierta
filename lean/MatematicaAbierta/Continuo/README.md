# La naturaleza del continuo — FDC-AUD-022

## Fuente, integración y compilación

Fuente canónica de Drive: `03_Formalizacion/FDC_T002_programa_transparente.lean`. La primera transferencia fue idéntica en bytes: SHA-256 `b5893820588c0f0d51887a7eb596436cd9ea0041a0c6d68920216cae19ded786`, Git blob `aef0754071eb6fdfde0e698737831f81f09e5e4a`. Las reparaciones siguientes modifican las pruebas pero conservan los enunciados: el archivo final requiere su propia compilación. Ubicación en GitHub: `lean/MatematicaAbierta/Continuo/ProgramaTransparente.lean`; importado desde `lean/MatematicaAbierta.lean`.

La PR #105 tuvo comprobación satisfactoria tanto de Lean 4.34.0 (`lake build --wfail`) como de Quarto sobre `9bb5afd2eb68837b2cf2cbb31eea0e2919dc33aa`: [Lean](https://github.com/lachenmann/matematica-abierta/actions/runs/35487548407), [Quarto](https://github.com/lachenmann/matematica-abierta/actions/runs/35487548388). Al fusionar se descubrió que `main` había recibido nuevos módulos concurrentes; la PR integró el `main` actualizado conservando **todas** las importaciones existentes y la nueva importación del continuo. La versión combinada requiere **nuevos checks para su propio SHA** antes de ser fusionada.

Historial de diagnóstico: el primer CI detectó desbordamiento de recursión de `simp` en `programaVisible_estable_succ` (línea 816); una reescritura ordinaria volvió a desbordar (línea 818). La prueba se corrigió mediante `congrArg` aplicado directamente a un único paso de la búsqueda. La prueba inductiva de `programaVisible_estable` también desbordaba por una simplificación innecesaria (línea 821): se reemplazó por igualdades definicionales de la suma natural. El caso `k=0` de `programaVisible_estabiliza_iff` usa directamente el testigo, sin simplificador general. El control textual del CI señaló inicialmente palabras presentes en la documentación y no en el código: la documentación se corrigió sin relajar el control. Los workflows auxiliares de transferencia, reparaciones y resolución de conflictos se eliminaron de la rama.

## Siete teoremas nuevos de `Continuo.Semantica`

| Teorema | Demostración y dependencias |
| --- | --- |
| `programaVisible_estable_succ` | Demostración propia: ecuación recursiva de `buscarHasta` y `congrArg`; persistencia de una salida tras un paso más de combustible. |
| `programaVisible_estable` | Demostración propia: inducción sobre combustible adicional; utiliza `programaVisible_estable_succ` e igualdades definicionales de `Nat`. |
| `programaVisible_grafo_iff` | Demostración propia por `rfl`: grafo existencial de `programaVisible` coincide con `Responde` por definición. |
| `programaVisible_estabiliza_iff` | Demostración propia: `programaVisible_estable` y especialización en combustible adicional cero. |
| `programaVisible_correcto` | Demostración mixta: reutiliza el teorema anterior del proyecto `responde_correcta` y `programaVisible_grafo_iff`; requiere decididores correctos y cortes inferiores. |
| `programaVisible_dominio_iff` | Demostración mixta: reutiliza el teorema anterior `responde_iff_fuera_frontera` y `programaVisible_grafo_iff`; utiliza `ℝ` de Mathlib como semántica externa. |
| `programaVisible_sin_salida_frontera` | Demostración mixta: reutiliza `responde_ausente_en_frontera` y `programaVisible_grafo_iff`. |

Las otras **40 declaraciones theorem son heredadas de AUD-021**, no son nuevas de AUD-022. Las siete pruebas se desarrollaron en el proyecto, con infraestructura y resultados de Mathlib en la cadena heredada; no se atribuyen como demostraciones íntegramente contenidas en Mathlib.

## Contrato matemático y obligaciones abiertas

`programaVisible χA χB p n := buscarHasta χA χB p n` es una familia total **con combustible**, no un decisor total de la suma. `Responde` significa que existe un combustible que produce `some b`. Bajo las hipótesis exactas sobre los decididores, la respuesta es correcta y el dominio excluye exactamente la igualdad con `x+y` para los cortes `corteReal` interpretados en los reales clásicos de Mathlib. El hito FOR-07 queda satisfecho por **sustitución operacional transparente**, no por una equivalencia con la antigua `partial def buscarSinCota`, cuya semántica sigue sin demostrarse. No hay prueba aquí de T002b, T002f, de la reducción al problema de detención, de un decisor universal total ni de la construcción independiente de los números reales. La compilación selectiva no constituye cierre crítico del expediente FDC-002.
