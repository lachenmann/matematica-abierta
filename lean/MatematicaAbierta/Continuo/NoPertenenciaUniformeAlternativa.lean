import MatematicaAbierta.Continuo.ContradiccionUniforme
import Mathlib.Computability.Halting

open Set
open scoped Pointwise

namespace Continuo.Indices

/-!
# FDC-AUD-023 — O6, demostración independiente para revisión

Esta fuente es una reconstrucción autónoma a partir de los contratos de O3–O5.
NO es el archivo histórico NoPertenenciaUniforme.lean de O6-E2: ese
archivo aún debe recuperarse y cotejarse antes de una integración canónica.

La tesis es la imposibilidad de semidecidir uniformemente la NO pertenencia
completa a la suma de dos cortes decidibles, incluido su punto frontera.
El contrato se refiere a programas y a todos los índices de consulta racional.
La prueba reutiliza la familia con segundo corte fijo de O5 y el teorema
de Mathlib que excluye la enumerabilidad recursiva del complemento de parada.
-/

/-- Un índice e semidecide exactamente el complemento del corte A.
Se exige terminación si y solo si la consulta racional codificada NO pertenece
al corte; el valor concreto devuelto por eval resulta irrelevante. -/
def SemiDecidesNonmem (e : Code) (A : Set ℚ) : Prop :=
  ∀ z : ℕ, (Nat.Partrec.Code.eval e z).Dom ↔ codedQuery z ∉ A

/-- Contrato uniforme con promesa de entradas válidas. Un transformador
parcial recursivo termina sobre cada par de índices de cortes correctos;
sus índices de salida semideciden la no pertenencia completa a la suma. -/
def UniformNonmemContract (Transform : Code × Code →. Code) : Prop :=
  Partrec Transform ∧
    ∀ (eA eB : Code) (A B : Set ℚ),
      ValidLowerCut A → ValidLowerCut B →
      DecidesCut eA A → DecidesCut eB B →
        ∃ e : Code, e ∈ Transform (eA, eB) ∧
          ∀ e' : Code, e' ∈ Transform (eA, eB) →
            SemiDecidesNonmem e' (A + B)

/-- Contrato restringido a los cortes A_c de la reducción, con el segundo
índice fijo y válido negativeIndex. -/
def FixedNegativeNonmemContract (Transform : Code × Code →. Code) : Prop :=
  Partrec Transform ∧
    ∀ c : Code, ∃ e : Code,
      e ∈ Transform (indexA c, negativeIndex) ∧
        ∀ e' : Code, e' ∈ Transform (indexA c, negativeIndex) →
          SemiDecidesNonmem e' (shiftedLowerCut c + fixedNegativeCut)

/-- La hipótesis uniforme implicaría ya la hipótesis con un sumando fijo. -/
theorem uniformNonmem_implies_fixed {Transform : Code × Code →. Code}
    (h : UniformNonmemContract Transform) :
    FixedNegativeNonmemContract Transform := by
  refine ⟨h.1, ?_⟩
  intro c
  obtain ⟨e, he, hcorrect⟩ :=
    h.2 (indexA c) negativeIndex (shiftedLowerCut c) fixedNegativeCut
      ⟨shiftedReal c, rfl⟩ ⟨-Real.sqrt 2, rfl⟩
      (indexA_decides c) negativeIndex_decides
  exact ⟨e, he, hcorrect⟩

/-- En cero, la semidecisión de la no pertenencia equivale a reconocer
la ausencia de detención del programa original. -/
theorem output_nonmem_zero_iff_nonhalt
    {Transform : Code × Code →. Code}
    (h : FixedNegativeNonmemContract Transform)
    (c e : Code) (he : e ∈ Transform (indexA c, negativeIndex)) :
    (Nat.Partrec.Code.eval e zeroQueryCode).Dom ↔
      ¬(Nat.Partrec.Code.eval c fixedInput).Dom := by
  obtain ⟨_e0, _he0, hall⟩ := h.2 c
  have hcorrect := hall e he zeroQueryCode
  have hboundary :
      codedQuery zeroQueryCode ∉ (shiftedLowerCut c + fixedNegativeCut) ↔
        ¬(Nat.Partrec.Code.eval c fixedInput).Dom := by
    rw [codedQuery_zeroQueryCode]
    exact not_congr (zero_mem_reduction_sum_iff_dom c)
  exact hcorrect.trans hboundary

/-- La composición parcial reutilizada de O5 tiene como dominio
precisamente el complemento del problema de parada. -/
theorem reductionPipeline_dom_iff_nonhalt
    {Transform : Code × Code →. Code}
    (h : FixedNegativeNonmemContract Transform) (c : Code) :
    (reductionPipeline Transform c).Dom ↔
      ¬(Nat.Partrec.Code.eval c fixedInput).Dom := by
  obtain ⟨e, he, _hall⟩ := h.2 c
  change
    ((Transform (indexA c, negativeIndex)).bind
      (fun e' => Nat.Partrec.Code.eval e' zeroQueryCode)).Dom ↔
        ¬(Nat.Partrec.Code.eval c fixedInput).Dom
  constructor
  · intro hp
    obtain ⟨v, hv⟩ := (Part.dom_iff_mem).mp hp
    obtain ⟨e', he', hval⟩ := (Part.mem_bind_iff).mp hv
    exact (output_nonmem_zero_iff_nonhalt h c e' he').mp
      ((Part.dom_iff_mem).mpr ⟨v, hval⟩)
  · intro hnot
    have heval : (Nat.Partrec.Code.eval e zeroQueryCode).Dom :=
      (output_nonmem_zero_iff_nonhalt h c e he).mpr hnot
    obtain ⟨v, hv⟩ := (Part.dom_iff_mem).mp heval
    exact (Part.dom_iff_mem).mpr
      ⟨v, (Part.mem_bind_iff).mpr ⟨e, he, hv⟩⟩

/-- Ni siquiera con segundo corte fijo existe tal transformador efectivo. -/
theorem no_fixed_negative_nonmem_transform :
    ¬ ∃ Transform : Code × Code →. Code,
      FixedNegativeNonmemContract Transform := by
  rintro ⟨Transform, h⟩
  have hre :
      REPred (fun c : Code => ¬(Nat.Partrec.Code.eval c fixedInput).Dom) :=
    ((partrec_reductionPipeline h.1).dom_re).of_eq
      (fun c => reductionPipeline_dom_iff_nonhalt h c)
  exact (ComputablePred.halting_problem_not_re fixedInput) hre

/-- T002f: la no pertenencia completa a la suma de cortes inferiores
no admite un semidecidor uniforme en los códigos de los dos decididores. -/
theorem no_uniform_sum_nonmem_semidecider_transform :
    ¬ ∃ Transform : Code × Code →. Code,
      UniformNonmemContract Transform := by
  rintro ⟨Transform, h⟩
  exact no_fixed_negative_nonmem_transform
    ⟨Transform, uniformNonmem_implies_fixed h⟩

end Continuo.Indices
