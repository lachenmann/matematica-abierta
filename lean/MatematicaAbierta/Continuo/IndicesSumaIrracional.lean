import MatematicaAbierta.Continuo.CompletitudCertificadosSuma

/-!
# FDC-AUD-025-M04c — Índices uniformes para la suma con frontera irracional

B5: se instancia el puente computacional de EtapasUniformes con la etapa
primitivamente recursiva de certificados de suma. La función de índices
obtenida es primitiva recursiva y NO depende de las fronteras reales:
las fronteras intervienen solo en la hipótesis semántica de corrección.

La condición de irracionalidad se usa únicamente para excluir que alguna
consulta racional coincida con la frontera de la suma. No se exige ni se
construye un procedimiento que reconozca esa promesa.
-/

namespace Continuo.Indices

open Set
open scoped Pointwise

/-- Cualquier respuesta emitida por la etapa posee la semántica correcta
de pertenencia a la suma puntual de los dos cortes principales. -/
set_option maxHeartbeats 1200000 in
theorem sumCertificateStage_answer_correct
    (eA eB : Code) (x y : ℝ)
    (hA : DecidesCut eA (lowerCut x))
    (hB : DecidesCut eB (lowerCut y))
    (z n : ℕ) (b : Bool)
    (h : sumCertificateStage (((eA, eB), z), n) = some b) :
    b = true ↔ codedQuery z ∈ lowerCut x + lowerCut y := by
  cases b with
  | true =>
      constructor
      · intro _
        exact sumCertificateStage_true_correct
          (((eA, eB), z), n) x y hA hB h
      · intro _
        rfl
  | false =>
      constructor
      · intro hfalse
        cases hfalse
      · intro hmem
        have hstrict : x + y < (codedQuery z : ℝ) :=
          sumCertificateStage_false_correct
            (((eA, eB), z), n) x y hA hB h
        rw [lowerCut_add] at hmem
        have hbelow : (codedQuery z : ℝ) < x + y :=
          (lowerCut_mem_iff _ (x + y)).mp hmem
        exact (lt_asymm hstrict hbelow).elim

/-- B5: un único transformador primitivamente recursivo de códigos
construye un decididor total de la suma para CUALQUIER pareja de índices
correctos de cortes principales, cuando la suma de sus fronteras es
irracional. No se introduce un índice dependiente de x o de y. -/
theorem exists_primrec_irrational_sum_decider :
    ∃ index : (Code × Code) → Code,
      Primrec index ∧
      ∀ (eA eB : Code) (x y : ℝ),
        DecidesCut eA (lowerCut x) →
        DecidesCut eB (lowerCut y) →
        Irrational (x + y) →
        DecidesCut (index (eA, eB)) (lowerCut x + lowerCut y) := by
  obtain ⟨index, hprim, heval⟩ :=
    exists_uniform_stage_codes
      sumCertificateStage primrec_sumCertificateStage
  refine ⟨index, hprim, ?_⟩
  intro eA eB x y hA hB hirr z
  have hne : x + y ≠ (codedQuery z : ℝ) :=
    hirr.ne_rat (codedQuery z)
  obtain ⟨n, b, hstage⟩ :=
    sumCertificateStage_eventually eA eB x y hA hB z hne
  have hdom :
      (uniformStageSearch sumCertificateStage ((eA, eB), z)).Dom :=
    uniformStageSearch_dom sumCertificateStage ((eA, eB), z)
      ⟨n, b, hstage⟩
  obtain ⟨answer, hanswer⟩ := Part.dom_iff_mem.mp hdom
  refine ⟨answer, ?_, ?_⟩
  · rw [heval (eA, eB) z]
    exact (Part.mem_map_iff Encodable.encode).mpr
      ⟨answer, hanswer, rfl⟩
  · exact uniformStageSearch_sound sumCertificateStage
      ((eA, eB), z) (codedQuery z ∈ lowerCut x + lowerCut y)
      (fun n' b' h' =>
        sumCertificateStage_answer_correct eA eB x y hA hB
          z n' b' h')
      answer hanswer

end Continuo.Indices
