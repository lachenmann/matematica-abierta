import MatematicaAbierta.Continuo.ContradiccionUniforme

open Set
open scoped Pointwise

namespace Continuo.Indices

/-!
# FDC-AUD-023 — O6: no pertenencia completa y dovetailing

La no pertenencia incluye el punto frontera del corte suma. Un semidecididor
efectivo uniforme para esa propiedad, combinado con la evaluación positiva
de un programa, decidiría el problema de la parada.
-/

/-- O6-A. La negación de la equivalencia de pertenencia de O4. -/
theorem zero_not_mem_reduction_sum_iff_not_dom (c : Code) :
    (0 : ℚ) ∉ shiftedLowerCut c + fixedNegativeCut ↔
      ¬ (Nat.Partrec.Code.eval c fixedInput).Dom :=
  not_congr (zero_mem_reduction_sum_iff_dom c)

/-- O6-B. Terminación exactamente en la no pertenencia completa para todos
los nombres racionales de pares de cortes válidos con índices correctos. -/
def UniformOutsideContract (Outside : ((Code × Code) × ℕ) →. ℕ) : Prop :=
  Partrec Outside ∧
    ∀ (eA eB : Code) (A B : Set ℚ),
      ValidLowerCut A → ValidLowerCut B →
      DecidesCut eA A → DecidesCut eB B →
        ∀ z : ℕ,
          (Outside ((eA, eB), z)).Dom ↔ codedQuery z ∉ A + B

/-- O6-C. La misma condición en la familia de O4, con el índice de B fijo. -/
def FixedNegativeOutsideContract (Outside : ((Code × Code) × ℕ) →. ℕ) : Prop :=
  Partrec Outside ∧
    ∀ (c : Code) (z : ℕ),
      (Outside ((indexA c, negativeIndex), z)).Dom ↔
        codedQuery z ∉ shiftedLowerCut c + fixedNegativeCut

theorem uniform_outside_implies_fixed {Outside : ((Code × Code) × ℕ) →. ℕ}
    (h : UniformOutsideContract Outside) :
    FixedNegativeOutsideContract Outside := by
  refine ⟨h.1, ?_⟩
  intro c z
  exact h.2 (indexA c) negativeIndex (shiftedLowerCut c) fixedNegativeCut
    ⟨shiftedReal c, rfl⟩ ⟨-Real.sqrt 2, rfl⟩
    (indexA_decides c) negativeIndex_decides z

/-- O6-D. Ejecución exterior sobre la consulta codificada de cero. -/
noncomputable def outsidePipeline (Outside : ((Code × Code) × ℕ) →. ℕ)
    (c : Code) : Part ℕ :=
  Outside ((indexA c, negativeIndex), zeroQueryCode)

theorem partrec_outsidePipeline {Outside : ((Code × Code) × ℕ) →. ℕ}
    (h : Partrec Outside) : Partrec (outsidePipeline Outside) := by
  have harg :
      Computable (fun c : Code => ((indexA c, negativeIndex), zeroQueryCode)) :=
    (primrec_indexA.to_comp.pair (Computable.const negativeIndex)).pair
      (Computable.const zeroQueryCode)
  exact h.comp harg

theorem outsidePipeline_dom_iff_not_halts
    {Outside : ((Code × Code) × ℕ) →. ℕ}
    (h : FixedNegativeOutsideContract Outside) (c : Code) :
    (outsidePipeline Outside c).Dom ↔
      ¬ (Nat.Partrec.Code.eval c fixedInput).Dom := by
  calc
    (outsidePipeline Outside c).Dom ↔
        codedQuery zeroQueryCode ∉ shiftedLowerCut c + fixedNegativeCut :=
      h.2 c zeroQueryCode
    _ ↔ (0 : ℚ) ∉ shiftedLowerCut c + fixedNegativeCut := by
      rw [codedQuery_zeroQueryCode]
    _ ↔ ¬ (Nat.Partrec.Code.eval c fixedInput).Dom :=
      zero_not_mem_reduction_sum_iff_not_dom c

/-- O6-E. La evaluación ordinaria semidecide la detención. -/
def haltsPipeline (c : Code) : Part ℕ :=
  Nat.Partrec.Code.eval c fixedInput

theorem partrec_haltsPipeline : Partrec haltsPipeline :=
  Nat.Partrec.Code.eval_part.comp Computable.id
    (Computable.const fixedInput)

theorem haltsPipeline_dom_iff (c : Code) :
    (haltsPipeline c).Dom ↔ (Nat.Partrec.Code.eval c fixedInput).Dom :=
  Iff.rfl

/-- O6-F. Dos semidecididores contrapuestos dan una decisión total.
`Partrec.merge` usa en Mathlib el dovetailing de `evaln`: busca de forma
intercalada hasta que uno de los dos cálculos termina. -/
theorem computablePred_of_dovetail
    {α σ : Type*} [Primcodable α] [Primcodable σ]
    {p : α → Prop} (positive negative : α →. σ)
    (hpositive : Partrec positive) (hnegative : Partrec negative)
    (hpos : ∀ a, (positive a).Dom ↔ p a)
    (hneg : ∀ a, (negative a).Dom ↔ ¬ p a) :
    ComputablePred p := by
  classical
  have hcompat :
      ∀ a, ∀ x ∈ (positive a).map (fun _ => true),
        ∀ y ∈ (negative a).map (fun _ => false), x = y := by
    intro a x hx y hy
    simp only [Part.mem_map_iff] at hx hy
    obtain ⟨u, hu, _⟩ := hx
    obtain ⟨v, hv, _⟩ := hy
    have hp : p a := (hpos a).mp (Part.dom_iff_mem.mpr ⟨u, hu⟩)
    have hnp : ¬ p a := (hneg a).mp (Part.dom_iff_mem.mpr ⟨v, hv⟩)
    exact False.elim (hnp hp)
  obtain ⟨merged, hmerged, hmem⟩ :=
    Partrec.merge
      (hpositive.map (Computable.const true).to₂)
      (hnegative.map (Computable.const false).to₂)
      hcompat
  have hvalue (a : α) : decide (p a) ∈ merged a := by
    apply (hmem a _).mpr
    by_cases hp : p a
    · left
      obtain ⟨u, hu⟩ := Part.dom_iff_mem.mp ((hpos a).mpr hp)
      simp only [hp, Part.mem_map_iff]
      exact ⟨u, hu, rfl⟩
    · right
      obtain ⟨v, hv⟩ := Part.dom_iff_mem.mp ((hneg a).mpr hp)
      simp only [hp, Part.mem_map_iff]
      exact ⟨v, hv, rfl⟩
  exact Computable.computablePred (hmerged.of_eq_tot hvalue)

/-- O6-G. La familia de B fijo ya prohibe la semidecisión exterior completa. -/
theorem no_fixed_negative_complete_outside_semidecider :
    ¬ ∃ Outside : ((Code × Code) × ℕ) →. ℕ,
      FixedNegativeOutsideContract Outside := by
  rintro ⟨Outside, hOutside⟩
  have hdec : ComputablePred
      (fun c : Code => (Nat.Partrec.Code.eval c fixedInput).Dom) :=
    computablePred_of_dovetail
      haltsPipeline (outsidePipeline Outside)
      partrec_haltsPipeline (partrec_outsidePipeline hOutside.1)
      haltsPipeline_dom_iff (outsidePipeline_dom_iff_not_halts hOutside)
  exact (ComputablePred.halting_problem fixedInput) hdec

/-- O6-H. No existe un semidecididor exterior completo uniforme. -/
theorem no_uniform_complete_outside_semidecider :
    ¬ ∃ Outside : ((Code × Code) × ℕ) →. ℕ,
      UniformOutsideContract Outside := by
  rintro ⟨Outside, hOutside⟩
  exact no_fixed_negative_complete_outside_semidecider
    ⟨Outside, uniform_outside_implies_fixed hOutside⟩

end Continuo.Indices
