import Mathlib.Data.Nat.Basic

namespace MatematicaAbierta

/-- Prueba inicial de compilación: conmutatividad de la suma en ℕ. -/
theorem suma_conmutativa_nat (m n : ℕ) : m + n = n + m := by
  exact Nat.add_comm m n

end MatematicaAbierta
