import MatematicaAbierta.Continuo.PrimerExito

/-!
# FDC-AUD-023 — Computabilidad uniforme del aproximante de detención

El resultado es un programa parcial-recursivo TOTAL que recibe el código de
un programa y la precisión, y devuelve un par explícito (numerador, denominador).
La construcción uniforme de índices usa `exists_code` y `curry` de la versión
fijada de Mathlib. No supone la decidibilidad del problema de parada.
La semántica de `evaln` continúa siendo una cota de evaluación, no tiempo literal.
-/

namespace Continuo.Indices

open Denumerable

/-- Paso de la búsqueda acotada, con el índice y el resultado anterior. -/
def advance (c : Code) (p : ℕ × Option ℕ) : Option ℕ :=
  match p.2 with
  | some t => some t
  | none => if (run c p.1).isSome then some p.1 else none

/-- El evaluador finito es primitivo recursivo uniformemente en código y cota. -/
theorem primrec_run : Primrec₂ run := by
  exact Nat.Partrec.Code.primrec_evaln.comp
    ((Primrec.snd.pair Primrec.fst).pair (Primrec.const fixedInput))

/-- Cada paso de búsqueda es primitivo recursivo. -/
theorem primrec_advance : Primrec₂ advance := by
  have hr : Primrec (fun p : Code × (ℕ × Option ℕ) => run p.1 p.2.1) :=
    primrec_run.comp Primrec.fst (Primrec.fst.comp Primrec.snd)
  have hb : Primrec (fun p : Code × (ℕ × Option ℕ) =>
      if (run p.1 p.2.1).isSome then some p.2.1 else none) := by
    refine (Primrec.cond (Primrec.option_isSome.comp hr)
      (Primrec.option_some.comp (Primrec.fst.comp Primrec.snd))
      (Primrec.const none)).of_eq ?_
    intro p
    cases (run p.1 p.2.1).isSome <;> simp
  exact (Primrec.option_casesOn (Primrec.snd.comp Primrec.snd)
    hb (Primrec.option_some.comp Primrec.snd).to₂).of_eq fun ⟨c, k, old⟩ => by
      cases old <;> rfl

/-- El primer éxito es primitivo recursivo, no solo una definición total de Lean. -/
theorem primrec_firstHit : Primrec₂ firstHit := by
  refine (Primrec.nat_rec (f := fun (_ : Code) => (none : Option ℕ))
    (g := advance) (Primrec.const none) primrec_advance).of_eq ?_
  intro c N
  induction N with
  | zero => rfl
  | succ N ih =>
    change advance c (N, Nat.rec (motive := fun _ => Option ℕ)
      none (fun k old => advance c (k, old)) N) = firstHit c (N + 1)
    rw [ih]
    cases hp : firstHit c N <;> simp [advance, firstHit, hp]

/-- Certificado racional con numerador y denominador naturales explícitos. -/
def rationalPair (c : Code) (N : ℕ) : ℕ × ℕ :=
  match firstHit c N with
  | none => (0, 1)
  | some t => (1, 2 ^ (t + 2))

/-- Interpretación semántica del certificado, sin suponerla computable. -/
def pairValue (p : ℕ × ℕ) : ℚ := (p.1 : ℚ) / (p.2 : ℚ)

/-- El certificado explícito representa exactamente el aproximante anterior. -/
theorem rationalPair_correct (c : Code) (N : ℕ) :
    pairValue (rationalPair c N) = approximant c N := by
  cases h : firstHit c N with
  | none => simp [pairValue, rationalPair, approximant, h]
  | some t => simp [pairValue, rationalPair, approximant, dyadic, h, Nat.cast_pow]

/-- El par racional computado es uniformemente primitivo recursivo. -/
theorem primrec_rationalPair : Primrec₂ rationalPair := by
  have hpow : Primrec (fun t : ℕ => 2 ^ (t + 2)) :=
    (Primrec₂.unpaired'.1 Nat.Primrec.pow).comp
      (Primrec.const 2) (Primrec.nat_add.comp Primrec.id (Primrec.const 2))
  have hsome : Primrec₂ (fun (_ : Code × ℕ) (t : ℕ) =>
      ((1, 2 ^ (t + 2)) : ℕ × ℕ)) :=
    ((Primrec.const (1 : ℕ)).pair (hpow.comp Primrec.snd)).to₂
  exact (Primrec.option_casesOn primrec_firstHit (Primrec.const (0, 1))
    hsome).of_eq fun ⟨c, N⟩ => by
      cases h : firstHit c N <;> simp [rationalPair, h]

/-- Codificación de salida mediante el emparejamiento aritmético de naturales. -/
def packedApprox (c : Code) (N : ℕ) : ℕ :=
  Nat.pair (rationalPair c N).1 (rationalPair c N).2

/-- La función numérica codificada es primitiva recursiva. -/
theorem primrec_packedApprox : Primrec₂ packedApprox := by
  exact (Primrec₂.natPair.comp
    (Primrec.fst.comp primrec_rationalPair)
    (Primrec.snd.comp primrec_rationalPair)).of_eq fun p => rfl

/-- La función total que recibe los dos parámetros como un único natural. -/
def packedNatural (z : ℕ) : ℕ :=
  packedApprox (ofNat Code z.unpair.1) z.unpair.2

/-- Certificado explícito de computabilidad de la función universal empaquetada. -/
theorem primrec_packedNatural : Primrec packedNatural := by
  have hp : Primrec (fun z : ℕ =>
      (ofNat Code z.unpair.1, z.unpair.2)) :=
    ((Primrec.ofNat Code).comp (Primrec.fst.comp Primrec.unpair)).pair
      (Primrec.snd.comp Primrec.unpair)
  exact (show Primrec (fun p : Code × ℕ => packedApprox p.1 p.2)
    from primrec_packedApprox).comp hp

/-- Existe un código universal concreto, cuya evaluación siempre devuelve la salida correcta. -/
theorem exists_packed_program :
    ∃ u : Code, ∀ z : ℕ, packedNatural z ∈ Nat.Partrec.Code.eval u z := by
  have hn : Nat.Primrec packedNatural := Primrec.nat_iff.mp primrec_packedNatural
  obtain ⟨u, hu⟩ := (Nat.Partrec.Code.exists_code).mp (Nat.Partrec.of_primrec hn)
  refine ⟨u, ?_⟩
  intro z
  rw [hu]
  simp

/-- La construcción de índices por especialización es primitiva recursiva. -/
theorem exists_uniform_approximant_codes :
    ∃ index : Code → Code, Primrec index ∧
      ∀ c N, packedApprox c N ∈ Nat.Partrec.Code.eval (index c) N := by
  obtain ⟨u, hu⟩ := exists_packed_program
  refine ⟨fun c => Nat.Partrec.Code.curry u (Encodable.encode c), ?_, ?_⟩
  · exact Nat.Partrec.Code.primrec₂_curry.comp
      (Primrec.const u) Primrec.encode
  · intro c N
    rw [Nat.Partrec.Code.eval_curry]
    have h := hu (Nat.pair (Encodable.encode c) N)
    simpa [packedNatural, packedApprox] using h

/-- Una sola rutina computable produce, para todos los códigos, nombres racionales exactos. -/
theorem packedApprox_correct (c : Code) (N : ℕ) :
    pairValue (Nat.unpair (packedApprox c N)) = approximant c N := by
  simpa [packedApprox] using rationalPair_correct c N

end Continuo.Indices
