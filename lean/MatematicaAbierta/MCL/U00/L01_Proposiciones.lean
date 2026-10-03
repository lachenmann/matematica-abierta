import Mathlib

/-!
# MCL-U00-L01 — Qué es una proposición

Objetivo matemático:
reconocer una proposición matemática, distinguirla de su demostración
y comenzar a leer una meta elemental de Lean.

Estado pedagógico: REVIEW
Fuente humana: MCL-U00-L01_QUE_ES_UNA_PROPOSICION_v02.md
MA-Lean mapping: MA-Lean/mapeos/MCL/MCL-U00-L01.json
-/

namespace MatematicaAbierta.MCL.U00.L01

/-- MCL-U00-L01-E01 · example
Una primera proposición verdadera. La prueba es reflexiva. -/
theorem dos_es_dos : (2 : ℕ) = 2 := by
  rfl

/-- MCL-U00-L01-E02 · example
La misma idea no depende del número 2. -/
theorem siete_es_siete : (7 : ℕ) = 7 := by
  rfl

/-- MCL-U00-L01-E03 · generalization
Todo natural es igual a sí mismo. -/
theorem natural_igual_a_si_mismo (n : ℕ) : n = n := by
  rfl

end MatematicaAbierta.MCL.U00.L01
