import Mathlib

/-!
# MCL-U00-L01 — Qué es una proposición

Objetivo matemático:
reconocer una proposición matemática, distinguirla de su demostración
y comenzar a leer una meta elemental de Lean.

Estado pedagógico: REVIEW

Documento humano:
Obsidian/Vault/Matemática/Matemática Abierta/Aprender matemáticas con Lean/
MCL-U00-L01_QUE_ES_UNA_PROPOSICION_v01.md
-/

namespace MCL.U00.L01

/-- MCL-U00-L01-E01:
Una primera proposición verdadera. La prueba es reflexiva. -/
theorem dos_es_dos : (2 : ℕ) = 2 := by
  rfl

/-- MCL-U00-L01-E02:
La misma idea no depende del número 2. -/
theorem siete_es_siete : (7 : ℕ) = 7 := by
  rfl

/-- MCL-U00-L01-E03:
Generalización: todo natural es igual a sí mismo. -/
theorem natural_igual_a_si_mismo (n : ℕ) : n = n := by
  rfl

/-!
Error productivo propuesto para el estudiante:

```lean
example : (2 : ℕ) = 3 := by
  rfl
```

Lean rechaza esta prueba: la reflexividad no transforma una proposición falsa
en verdadera. El error debe interpretarse matemáticamente, no sólo como
un problema de sintaxis.
-/

end MCL.U00.L01
