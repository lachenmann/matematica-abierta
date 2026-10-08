import MatematicaAbierta.Continuo.NoPertenenciaUniforme

/-!
# FDC-AUD-025-M04 — Puente computacional de etapas a índices

Un procedimiento primitivo recursivo por etapas que produce respuestas correctas
y termina en toda consulta de una subfamilia prometida determina, de manera
uniforme y primitivo recursiva, un índice de decididor para esa subfamilia.

Este módulo demuestra el puente general. La construcción de la etapa específica
de suma de cortes bajo promesa de frontera irracional es una obligación distinta.
-/

namespace Continuo.Indices

/-- Búsqueda efectiva de la primera etapa que emite una respuesta booleana. -/
def uniformStageSearch
    (stage : (((Code × Code) × ℕ) × ℕ) → Option Bool)
    (input : (Code × Code) × ℕ) : Part Bool :=
  Nat.rfindOpt (fun n => stage (input, n))

/-- La búsqueda es parcial recursiva si cada etapa es primitiva recursiva. -/
theorem partrec_uniformStageSearch
    (stage : (((Code × Code) × ℕ) × ℕ) → Option Bool)
    (hstage : Primrec stage) :
    Partrec (uniformStageSearch stage) := by
  unfold uniformStageSearch
  exact Partrec.rfindOpt (hstage.to_comp.to₂)

/-- Un testigo de respuesta finita garantiza la terminación de la búsqueda. -/
theorem uniformStageSearch_dom
    (stage : (((Code × Code) × ℕ) × ℕ) → Option Bool)
    (input : (Code × Code) × ℕ)
    (h : ∃ n : ℕ, ∃ b : Bool, stage (input, n) = some b) :
    (uniformStageSearch stage input).Dom := by
  unfold uniformStageSearch
  apply Nat.rfindOpt_dom.mpr
  obtain ⟨n, b, hn⟩ := h
  refine ⟨n, b, ?_⟩
  simpa only [Option.mem_def] using hn

/-- La primera respuesta hereda cualquier propiedad satisfecha por todas
las respuestas emitidas en las etapas finitas. -/
theorem uniformStageSearch_sound
    (stage : (((Code × Code) × ℕ) × ℕ) → Option Bool)
    (input : (Code × Code) × ℕ) (P : Prop)
    (hsound : ∀ n b, stage (input, n) = some b → (b = true ↔ P))
    (b : Bool) (hb : b ∈ uniformStageSearch stage input) :
    b = true ↔ P := by
  obtain ⟨n, hn⟩ := Nat.rfindOpt_spec hb
  apply hsound n b
  simpa only [Option.mem_def] using hn

/-- Versión codificada como función parcial de naturales para extraer un
programa universal mediante la API de Mathlib. -/
private def packedUniformStageSearch
    (stage : (((Code × Code) × ℕ) × ℕ) → Option Bool)
    (w : ℕ) : Part ℕ :=
  (uniformStageSearch stage
    (ofNat (Code × Code) w.unpair.1, w.unpair.2)).map Encodable.encode

private theorem partrec_packedUniformStageSearch
    (stage : (((Code × Code) × ℕ) × ℕ) → Option Bool)
    (hstage : Primrec stage) :
    Partrec (packedUniformStageSearch stage) := by
  change Partrec (fun w : ℕ =>
    (uniformStageSearch stage
      (ofNat (Code × Code) w.unpair.1, w.unpair.2)).map Encodable.encode)
  have hin : Computable (fun w : ℕ =>
      (ofNat (Code × Code) w.unpair.1, w.unpair.2)) :=
    ((Computable.ofNat (Code × Code)).comp
      (Computable.fst.comp Computable.unpair)).pair
      (Computable.snd.comp Computable.unpair)
  have hs : Partrec (fun w : ℕ =>
      uniformStageSearch stage
        (ofNat (Code × Code) w.unpair.1, w.unpair.2)) :=
    (partrec_uniformStageSearch stage hstage).comp hin
  have henc :
      Computable₂ (fun (_ : ℕ) (b : Bool) => Encodable.encode b) :=
    (Computable.encode.comp Computable.snd).to₂
  exact hs.map henc

/-- Extracción uniforme de índices a partir de una etapa computable.
La función que especializa el programa en los dos códigos de entrada es PR. -/
theorem exists_uniform_stage_codes
    (stage : (((Code × Code) × ℕ) × ℕ) → Option Bool)
    (hstage : Primrec stage) :
    ∃ index : (Code × Code) → Code,
      Primrec index ∧
      ∀ p z,
        Nat.Partrec.Code.eval (index p) z =
          (uniformStageSearch stage (p, z)).map Encodable.encode := by
  have hn : Nat.Partrec (packedUniformStageSearch stage) :=
    Partrec.nat_iff.mp (partrec_packedUniformStageSearch stage hstage)
  obtain ⟨u, hu⟩ := (Nat.Partrec.Code.exists_code).mp hn
  refine ⟨fun p => Nat.Partrec.Code.curry u (Encodable.encode p), ?_, ?_⟩
  · exact Nat.Partrec.Code.primrec₂_curry.comp
      (Primrec.const u) Primrec.encode
  · intro p z
    rw [Nat.Partrec.Code.eval_curry]
    rw [hu]
    simp [packedUniformStageSearch]

/-- Transferencia al contrato de decididores del continuo:
si las etapas son correctas y aparecen para todas las consultas prometidas,
los índices de los dos datos determinan computablemente el índice de salida. -/
theorem exists_uniform_stage_deciders
    (stage : (((Code × Code) × ℕ) × ℕ) → Option Bool)
    (hstage : Primrec stage)
    (Good : Code × Code → Prop)
    (sumCut : Code × Code → Set ℚ)
    (hready : ∀ p, Good p → ∀ z,
      ∃ n : ℕ, ∃ b : Bool, stage ((p, z), n) = some b)
    (hsound : ∀ p z n b, Good p →
      stage ((p, z), n) = some b →
        (b = true ↔ codedQuery z ∈ sumCut p)) :
    ∃ index : (Code × Code) → Code,
      Primrec index ∧ ∀ p, Good p → DecidesCut (index p) (sumCut p) := by
  obtain ⟨index, hprim, heval⟩ :=
    exists_uniform_stage_codes stage hstage
  refine ⟨index, hprim, ?_⟩
  intro p hp z
  obtain ⟨n, b, hstageb⟩ := hready p hp z
  have hdom : (uniformStageSearch stage (p, z)).Dom :=
    uniformStageSearch_dom stage (p, z) ⟨n, b, hstageb⟩
  obtain ⟨answer, hanswer⟩ := Part.dom_iff_mem.mp hdom
  refine ⟨answer, ?_, ?_⟩
  · rw [heval p z]
    exact (Part.mem_map_iff Encodable.encode).mpr
      ⟨answer, hanswer, rfl⟩
  · exact uniformStageSearch_sound stage (p, z)
      (codedQuery z ∈ sumCut p)
      (fun n' b' h => hsound p z n' b' hp h)
      answer hanswer

end Continuo.Indices
