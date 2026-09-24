import MatematicaAbierta.Continuo.SumaCortesReduccion
import Mathlib.Computability.Halting

open Set
open scoped Pointwise

namespace Continuo.Indices

/-!
# FDC-AUD-023 — O5: contradicción uniforme

La hipótesis de un transformador parcial recursivo de índices de decididores
para sumas de cortes conduce a un decididor del problema de la parada. La
reducción ya falla cuando el segundo corte es siempre `fixedNegativeCut`.
-/

/-- Un índice decide un corte en la representación racional codificada de O3. -/
def DecidesCut (e : Code) (A : Set ℚ) : Prop :=
  ∀ z : ℕ, ∃ b : Bool,
    Encodable.encode b ∈ Nat.Partrec.Code.eval e z ∧
      (b = true ↔ codedQuery z ∈ A)

/-- Transformador primitivo recursivo de índices para los cortes desplazados. -/
noncomputable def indexA : Code → Code :=
  Classical.choose exists_uniform_shifted_cut_decider_codes

theorem primrec_indexA : Primrec indexA :=
  (Classical.choose_spec exists_uniform_shifted_cut_decider_codes).1

theorem indexA_decides (c : Code) :
    DecidesCut (indexA c) (shiftedLowerCut c) := by
  intro z
  have hO3 :=
    (Classical.choose_spec exists_uniform_shifted_cut_decider_codes).2 c z
  rcases lt_trichotomy (codedQuery z : ℝ) (shiftedReal c) with hlt | heq | hgt
  · refine ⟨true, hO3.1.mpr hlt, ?_⟩
    simpa using (codedQuery_mem_shiftedLowerCut_iff c z).mpr hlt
  · exact False.elim ((shiftedReal_irrational c).ne_rat (codedQuery z) heq.symm)
  · refine ⟨false, hO3.2.mpr hgt, ?_⟩
    constructor
    · intro hfalse
      cases hfalse
    · intro hmem
      have hlt := (codedQuery_mem_shiftedLowerCut_iff c z).mp hmem
      exact False.elim (lt_asymm hlt hgt)

/-- Índice fijo de O3 para el corte de `-√2`. -/
noncomputable def negativeIndex : Code :=
  Classical.choose exists_negative_cut_decider_code

theorem negativeIndex_decides :
    DecidesCut negativeIndex fixedNegativeCut := by
  intro z
  have hO3 := (Classical.choose_spec exists_negative_cut_decider_code) z
  rcases lt_trichotomy (codedQuery z : ℝ) (-Real.sqrt 2) with hlt | heq | hgt
  · refine ⟨true, hO3.1.mpr hlt, ?_⟩
    simpa using (codedQuery_mem_fixedNegativeCut_iff z).mpr hlt
  · exact False.elim (negativeRoot_irrational.ne_rat (codedQuery z) heq.symm)
  · refine ⟨false, hO3.2.mpr hgt, ?_⟩
    constructor
    · intro hfalse
      cases hfalse
    · intro hmem
      have hlt := (codedQuery_mem_fixedNegativeCut_iff z).mp hmem
      exact False.elim (lt_asymm hlt hgt)

/-- Un nombre natural explícito de la consulta racional cero. -/
def zeroQueryCode : ℕ := queryCode ((0, 0), 0)

theorem codedQuery_zeroQueryCode : codedQuery zeroQueryCode = 0 := by
  simp [zeroQueryCode, codedQuery_queryCode]

/-- Subfamilia de cortes inferiores válidos usada en la reducción. -/
def ValidLowerCut (A : Set ℚ) : Prop :=
  ∃ x : ℝ, A = lowerCut x

/-- Contrato uniforme: efectividad, terminación en entradas válidas y
corrección de todo índice producido. No se restringen las entradas inválidas. -/
def UniformSumContract (Transform : Code × Code →. Code) : Prop :=
  Partrec Transform ∧
    ∀ (eA eB : Code) (A B : Set ℚ),
      ValidLowerCut A → ValidLowerCut B →
      DecidesCut eA A → DecidesCut eB B →
        ∃ e : Code, e ∈ Transform (eA, eB) ∧
          ∀ e' : Code, e' ∈ Transform (eA, eB) → DecidesCut e' (A + B)

/-- Forma reforzada: el segundo índice es siempre el mismo. -/
def FixedNegativeSumContract (Transform : Code × Code →. Code) : Prop :=
  Partrec Transform ∧
    ∀ c : Code, ∃ e : Code,
      e ∈ Transform (indexA c, negativeIndex) ∧
        DecidesCut e (shiftedLowerCut c + fixedNegativeCut)

theorem uniform_implies_fixed {Transform : Code × Code →. Code}
    (h : UniformSumContract Transform) : FixedNegativeSumContract Transform := by
  refine ⟨h.1, ?_⟩
  intro c
  obtain ⟨e, he, hcorrect⟩ :=
    h.2 (indexA c) negativeIndex (shiftedLowerCut c) fixedNegativeCut
      ⟨shiftedReal c, rfl⟩ ⟨-Real.sqrt 2, rfl⟩
      (indexA_decides c) negativeIndex_decides
  exact ⟨e, he, hcorrect e he⟩

/-- Pipeline parcial: transformar los dos índices y evaluar el resultado en
la consulta explícita de cero. -/
noncomputable def reductionPipeline (Transform : Code × Code →. Code)
    (c : Code) : Part ℕ :=
  (Transform (indexA c, negativeIndex)).bind fun e =>
    Nat.Partrec.Code.eval e zeroQueryCode

theorem partrec_reductionPipeline {Transform : Code × Code →. Code}
    (h : Partrec Transform) : Partrec (reductionPipeline Transform) := by
  have hpair : Computable (fun c : Code => (indexA c, negativeIndex)) :=
    primrec_indexA.to_comp.pair (Computable.const negativeIndex)
  have hfirst : Partrec (fun c : Code => Transform (indexA c, negativeIndex)) :=
    h.comp hpair
  have hsecond :
      Partrec (fun p : Code × Code => Nat.Partrec.Code.eval p.2 zeroQueryCode) :=
    Nat.Partrec.Code.eval_part.comp Computable.snd
      (Computable.const zeroQueryCode)
  exact Partrec.bind hfirst hsecond.to₂

/-- Toda entrada del pipeline termina con el código de un booleano cuya
respuesta positiva equivale a la detención original. -/
theorem reductionPipeline_spec {Transform : Code × Code →. Code}
    (h : FixedNegativeSumContract Transform) (c : Code) :
    ∃ b : Bool, Encodable.encode b ∈ reductionPipeline Transform c ∧
      (b = true ↔ (Nat.Partrec.Code.eval c fixedInput).Dom) := by
  obtain ⟨e, he, hdec⟩ := h.2 c
  obtain ⟨b, hb, hiff⟩ := hdec zeroQueryCode
  refine ⟨b, ?_, ?_⟩
  · exact Part.mem_bind_iff.mpr ⟨e, he, hb⟩
  · calc
      b = true ↔ codedQuery zeroQueryCode ∈
          shiftedLowerCut c + fixedNegativeCut := hiff
      _ ↔ (0 : ℚ) ∈ shiftedLowerCut c + fixedNegativeCut := by
        rw [codedQuery_zeroQueryCode]
      _ ↔ (Nat.Partrec.Code.eval c fixedInput).Dom :=
        zero_mem_reduction_sum_iff_dom c

/-- Ni siquiera existe un transformador efectivo que funcione en la familia
`A_c` con el segundo índice fijo `negativeIndex`. -/
theorem no_fixed_negative_sum_transform :
    ¬ ∃ Transform : Code × Code →. Code,
      FixedNegativeSumContract Transform := by
  rintro ⟨Transform, hTransform⟩
  classical
  let hspec (c : Code) := reductionPipeline_spec hTransform c
  let answer (c : Code) : Bool := Classical.choose (hspec c)
  have hanswer (c : Code) :
      Encodable.encode (answer c) ∈ reductionPipeline Transform c ∧
        (answer c = true ↔ (Nat.Partrec.Code.eval c fixedInput).Dom) :=
    Classical.choose_spec (hspec c)
  have hcomputable : Computable answer :=
    Computable.encode_iff.mp
      ((partrec_reductionPipeline hTransform.1).of_eq_tot
        (fun c => (hanswer c).1))
  have hpred : ComputablePred (fun c : Code => (answer c : Prop)) :=
    ComputablePred.computable_iff.mpr ⟨answer, hcomputable, rfl⟩
  exact (ComputablePred.halting_problem fixedInput)
    (hpred.of_eq (fun c => by simpa using (hanswer c).2))

/-- Un procedimiento parcial recursivo uniforme para decidir sumas de cortes
válidos contradice el problema de la parada. -/
theorem no_uniform_sum_decider_transform :
    ¬ ∃ Transform : Code × Code →. Code,
      UniformSumContract Transform := by
  rintro ⟨Transform, hTransform⟩
  exact no_fixed_negative_sum_transform
    ⟨Transform, uniform_implies_fixed hTransform⟩

end Continuo.Indices
