import Mathlib

/-!
# Cauchy–Schwarz: caso elemental de dos términos

Correspondencia editorial: MA-ART-0004, `teoria/resultados/_cauchy-1.qmd`, §2.
La desigualdad se deduce de una identidad algebraica y la no negatividad
explícita de un cuadrado; no se invoca el teorema general de Mathlib.
-/

namespace MatematicaAbierta

/-- MA-ART-0004, §2: identidad algebraica que explica Cauchy–Schwarz en dimensión dos. -/
theorem identidad_lagrange_dos_terminos (a₁ a₂ b₁ b₂ : ℝ) :
    (a₁ ^ 2 + a₂ ^ 2) * (b₁ ^ 2 + b₂ ^ 2) -
      (a₁ * b₁ + a₂ * b₂) ^ 2 = (a₁ * b₂ - a₂ * b₁) ^ 2 := by
  ring

/-- MA-ART-0004, §2: caso de dos términos de Cauchy–Schwarz, demostrado por un cuadrado. -/
theorem cauchy_schwarz_dos_terminos (a₁ a₂ b₁ b₂ : ℝ) :
    (a₁ * b₁ + a₂ * b₂) ^ 2 ≤
      (a₁ ^ 2 + a₂ ^ 2) * (b₁ ^ 2 + b₂ ^ 2) := by
  have hid := identidad_lagrange_dos_terminos a₁ a₂ b₁ b₂
  have hcuadrado : 0 ≤ (a₁ * b₂ - a₂ * b₁) ^ 2 := sq_nonneg _
  linarith

end MatematicaAbierta
