import Mathlib

/-!
# Desigualdad triangular: pruebas algebraicas explícitas

Correspondencia editorial: MA-ART-0003, `teoria/resultados/desigualdad-triangular.qmd`,
§2 (cotas bilaterales) y §4 (desigualdad triangular inversa).
No se necesita completitud de los reales: basta un cuerpo linealmente ordenado.
-/

namespace MatematicaAbierta

variable {F : Type*} [LinearOrderedField F]

/-- MA-ART-0003, §2: la desigualdad triangular se deduce de las cuatro cotas
`-|x| ≤ x ≤ |x|` y `-|y| ≤ y ≤ |y|`, sin invocar `abs_add_le`. -/
theorem desigualdad_triangular_cuerpo_ordenado (x y : F) :
    |x + y| ≤ |x| + |y| := by
  apply abs_le.mpr
  constructor
  · have hx : -|x| ≤ x := neg_abs_le x
    have hy : -|y| ≤ y := neg_abs_le y
    linarith
  · have hx : x ≤ |x| := le_abs_self x
    have hy : y ≤ |y| := le_abs_self y
    linarith

/-- MA-ART-0003, §2, especialización del teorema general a ℝ. -/
theorem desigualdad_triangular_real (x y : ℝ) :
    |x + y| ≤ |x| + |y| := by
  exact desigualdad_triangular_cuerpo_ordenado x y

/-- MA-ART-0003, §4: desigualdad triangular inversa.
Se obtiene aplicando dos veces la desigualdad triangular anterior. -/
theorem desigualdad_triangular_inversa_cuerpo_ordenado (x y : F) :
    ||x| - |y|| ≤ |x - y| := by
  apply abs_le.mpr
  constructor
  · have h := desigualdad_triangular_cuerpo_ordenado (y - x) x
    have hy : (y - x) + x = y := by ring
    rw [hy, abs_sub_comm] at h
    linarith
  · have h := desigualdad_triangular_cuerpo_ordenado (x - y) y
    have hx : (x - y) + y = x := by ring
    rw [hx] at h
    linarith

end MatematicaAbierta
