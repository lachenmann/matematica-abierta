import Mathlib

namespace MatematicaAbierta

/-- Desigualdad triangular para el valor absoluto en los números reales. -/
theorem desigualdad_triangular_real (x y : ℝ) :
    |x + y| ≤ |x| + |y| := by
  exact abs_add x y

end MatematicaAbierta
