import MatematicaAbierta.Continuo.DecididoresCortesEfectivos
import Mathlib.Algebra.Order.CompleteField

open Set
open scoped Pointwise

namespace Continuo.Indices

/-!
# FDC-AUD-023 — O4: identidad de suma y reducción semántica

Este módulo formaliza la obligación O4 de la reducción T002b.

Establece la identidad de suma de cortes racionales inferiores,
la especializa a la familia `shiftedReal c` y al corte fijo `-√2`,
y conecta la pertenencia de cero a la suma con la positividad de
`delta c` y con el dominio de la evaluación parcial del programa.

No formaliza todavía O5 ni O6.

La representación de un real x como corte racional inferior será
el cutMap de Mathlib especializado de ℝ a ℚ.
-/

/-- Corte racional inferior estricto asociado al real externo `x`. -/
def lowerCut (x : ℝ) : Set ℚ :=
  LinearOrderedField.cutMap ℚ x


/-- Pertenecer al corte significa exactamente estar estrictamente
    por debajo de la frontera real. -/
theorem lowerCut_mem_iff (q : ℚ) (x : ℝ) :
    q ∈ lowerCut x ↔ (q : ℝ) < x := by
  change
    q ∈ LinearOrderedField.cutMap ℚ x ↔
      (q : ℝ) < x

  exact
    LinearOrderedField.coe_mem_cutMap_iff
      (α := ℝ)
      (β := ℚ)
      (a := x)
      (q := q)


/-- O4-A.
    La suma conjuntista puntual de dos cortes inferiores principales
    es exactamente el corte de la suma de sus fronteras. -/
theorem lowerCut_add (x y : ℝ) :
    lowerCut x + lowerCut y =
      lowerCut (x + y) := by
  unfold lowerCut

  exact
    (LinearOrderedField.cutMap_add
      (β := ℚ) x y).symm


/-- Corte variable A_c usado en la reducción. -/
def shiftedLowerCut (c : Code) : Set ℚ :=
  lowerCut (shiftedReal c)


/-- Corte fijo B = L_{-√2}. -/
def fixedNegativeCut : Set ℚ :=
  lowerCut (-Real.sqrt 2)


/-- O4-B.
    A_c + B es exactamente L_{δ_c}. -/
theorem shiftedLowerCut_add_fixedNegativeCut
    (c : Code) :
    shiftedLowerCut c + fixedNegativeCut =
      lowerCut (deltaReal c) := by

  rw [shiftedLowerCut, fixedNegativeCut, lowerCut_add]

  apply congrArg lowerCut

  unfold shiftedReal

  ring


/-- Puente explícito con la semántica del decididor O3 variable. -/
theorem codedQuery_mem_shiftedLowerCut_iff
    (c : Code) (z : ℕ) :
    codedQuery z ∈ shiftedLowerCut c ↔
      (codedQuery z : ℝ) < shiftedReal c := by

  exact lowerCut_mem_iff
    (codedQuery z) (shiftedReal c)


/-- Puente explícito con el decididor O3 fijo. -/
theorem codedQuery_mem_fixedNegativeCut_iff
    (z : ℕ) :
    codedQuery z ∈ fixedNegativeCut ↔
      (codedQuery z : ℝ) < -Real.sqrt 2 := by

  exact lowerCut_mem_iff
    (codedQuery z) (-Real.sqrt 2)


/-- O4-C.
    Cero pertenece al corte de δ_c exactamente cuando δ_c es positivo. -/
theorem zero_mem_deltaLowerCut_iff
    (c : Code) :
    (0 : ℚ) ∈ lowerCut (deltaReal c) ↔
      0 < delta c := by

  rw [lowerCut_mem_iff]

  unfold deltaReal

  norm_cast


/-- O4-D.
    Caracterización de cero en la suma mediante la positividad de δ_c. -/
theorem zero_mem_reduction_sum_iff_delta_pos
    (c : Code) :
    (0 : ℚ) ∈ shiftedLowerCut c + fixedNegativeCut ↔
      0 < delta c := by

  rw [shiftedLowerCut_add_fixedNegativeCut]

  exact zero_mem_deltaLowerCut_iff c


/-- O4-E.
    Forma en términos de la semántica de parada ya demostrada en O1. -/
theorem zero_mem_reduction_sum_iff_halts
    (c : Code) :
    (0 : ℚ) ∈ shiftedLowerCut c + fixedNegativeCut ↔
      ∃ x : ℕ,
        x ∈ Nat.Partrec.Code.eval c fixedInput := by

  rw [zero_mem_reduction_sum_iff_delta_pos]

  exact delta_pos_iff_halts c


/-- O4-F.
    La misma equivalencia expresada directamente mediante el dominio
    de la evaluación parcial. -/
theorem zero_mem_reduction_sum_iff_dom
    (c : Code) :
    (0 : ℚ) ∈ shiftedLowerCut c + fixedNegativeCut ↔
      (Nat.Partrec.Code.eval c fixedInput).Dom := by

  rw [zero_mem_reduction_sum_iff_delta_pos]

  exact delta_pos_iff_dom c


end Continuo.Indices