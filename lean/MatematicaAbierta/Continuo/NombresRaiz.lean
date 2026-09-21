import MatematicaAbierta.Continuo.ComputabilidadAproximante
import Mathlib.Analysis.Rat.NatSqrt.Real
import Mathlib.Computability.Primrec.List

/-!
# FDC-AUD-023 — O2: nombres racionales efectivos de raíces desplazadas

Construimos nombres racionales de `√2`, `-√2` y `√2 + δ_c`. El último nombre
se representa por dos naturales obtenidos por una función primitiva recursiva.
La construcción uniforme de índices se basa en `exists_code` y `curry`; no
decide la parada. Las cotas de error se expresan en los reales de Mathlib.
-/

namespace Continuo.Indices

/-- Precisión entera positiva, con dos bits de margen. -/
def sqrtPrecision (n : ℕ) : ℕ := 2 ^ (n + 2)

/-- Nombre racional finito de la raíz de dos. -/
def sqrtTwoName (n : ℕ) : ℚ := Nat.ratSqrt 2 (sqrtPrecision n)

/-- Representación aritmética explícita del nombre racional. -/
def sqrtTwoPair (n : ℕ) : ℕ × ℕ :=
  (Nat.sqrt (2 * (sqrtPrecision n) ^ 2), sqrtPrecision n)

/-- Los pares de naturales representan exactamente los racionales elegidos. -/
theorem sqrtTwoPair_correct (n : ℕ) :
    pairValue (sqrtTwoPair n) = sqrtTwoName n := by
  simp [pairValue, sqrtTwoPair, sqrtTwoName, Nat.ratSqrt]

/-- La precisión es primitiva recursiva. -/
theorem primrec_sqrtPrecision : Primrec sqrtPrecision := by
  exact (Primrec₂.unpaired'.1 Nat.Primrec.pow).comp
    (Primrec.const 2) (Primrec.nat_add.comp Primrec.id (Primrec.const 2))

/-- Numerador y denominador se obtienen por un único algoritmo primitivo recursivo. -/
theorem primrec_sqrtTwoPair : Primrec sqrtTwoPair := by
  have hsq : Primrec (fun n : ℕ => (sqrtPrecision n) ^ 2) :=
    (Primrec₂.unpaired'.1 Nat.Primrec.pow).comp
      primrec_sqrtPrecision (Primrec.const 2)
  have hprod : Primrec (fun n : ℕ => 2 * (sqrtPrecision n) ^ 2) :=
    Primrec.nat_mul.comp (Primrec.const 2) hsq
  exact (Primrec.nat_sqrt.comp hprod).pair primrec_sqrtPrecision

/-- Cota estricta para un nombre racional de raíz de dos. -/
theorem sqrtTwoName_error (n : ℕ) :
    |(sqrtTwoName n : ℝ) - Real.sqrt 2| < 1 / (2 : ℝ) ^ (n + 2) := by
  have hp : 0 < sqrtPrecision n := by
    unfold sqrtPrecision
    positivity
  have hlow : (sqrtTwoName n : ℝ) ≤ Real.sqrt 2 := by
    simpa [sqrtTwoName] using Nat.ratSqrt_le_realSqrt 2 hp
  have hhigh : Real.sqrt 2 < (sqrtTwoName n : ℝ) + 1 / (2 : ℝ) ^ (n + 2) := by
    simpa [sqrtTwoName, sqrtPrecision, Nat.cast_pow] using
      Nat.realSqrt_lt_ratSqrt_add_inv_prec 2 hp
  rw [abs_of_nonpos (sub_nonpos.mpr hlow)]
  linarith

/-- El mismo nombre con signo cambiado aproxima menos raíz de dos. -/
def negSqrtTwoName (n : ℕ) : ℚ := -sqrtTwoName n

theorem negSqrtTwoName_error (n : ℕ) :
    |(negSqrtTwoName n : ℝ) - (-Real.sqrt 2)| < 1 / (2 : ℝ) ^ (n + 2) := by
  have heq : (negSqrtTwoName n : ℝ) - (-Real.sqrt 2) =
      -((sqrtTwoName n : ℝ) - Real.sqrt 2) := by
    simp only [negSqrtTwoName, Rat.cast_neg]
    ring
  rw [heq, abs_neg]
  exact sqrtTwoName_error n

/-- Suma exacta de racionales representados por pares con denominador positivo. -/
def addPair (p q : ℕ × ℕ) : ℕ × ℕ :=
  (p.1 * q.2 + q.1 * p.2, p.2 * q.2)

theorem addPair_correct (p q : ℕ × ℕ)
    (hp : p.2 ≠ 0) (hq : q.2 ≠ 0) :
    pairValue (addPair p q) = pairValue p + pairValue q := by
  have hp' : (p.2 : ℚ) ≠ 0 := by exact_mod_cast hp
  have hq' : (q.2 : ℚ) ≠ 0 := by exact_mod_cast hq
  simp only [pairValue, addPair, Nat.cast_add, Nat.cast_mul]
  field_simp [hp', hq']
  ring

/-- La suma aritmética de pares es primitiva recursiva. -/
theorem primrec_addPair : Primrec₂ addPair := by
  have hn : Primrec (fun pq : (ℕ × ℕ) × (ℕ × ℕ) =>
      pq.1.1 * pq.2.2 + pq.2.1 * pq.1.2) :=
    Primrec.nat_add.comp
      (Primrec.nat_mul.comp (Primrec.fst.comp Primrec.fst)
        (Primrec.snd.comp Primrec.snd))
      (Primrec.nat_mul.comp (Primrec.fst.comp Primrec.snd)
        (Primrec.snd.comp Primrec.fst))
  have hd : Primrec (fun pq : (ℕ × ℕ) × (ℕ × ℕ) =>
      pq.1.2 * pq.2.2) :=
    Primrec.nat_mul.comp (Primrec.snd.comp Primrec.fst)
      (Primrec.snd.comp Primrec.snd)
  exact (hn.pair hd).of_eq (fun _ => rfl)

/-- El denominador del nombre radical nunca se anula. -/
theorem sqrtTwoPair_den_ne_zero (n : ℕ) : (sqrtTwoPair n).2 ≠ 0 := by
  have hp : 0 < sqrtPrecision n := by unfold sqrtPrecision; positivity
  exact Nat.ne_of_gt hp

/-- El denominador del aproximante de detención nunca se anula. -/
theorem rationalPair_den_ne_zero (c : Code) (N : ℕ) :
    (rationalPair c N).2 ≠ 0 := by
  cases h : firstHit c N with
  | none => simp [rationalPair, h]
  | some t => simp [rationalPair, h]

/-- El número real semántico: un irracional fijo más el peso de detención. -/
noncomputable def shiftedReal (c : Code) : ℝ := Real.sqrt 2 + deltaReal c

/-- Nombre racional efectivo, con dos etapas de margen para el desplazamiento. -/
def shiftedName (c : Code) (n : ℕ) : ℚ :=
  sqrtTwoName n + approximant c (n + 2)

/-- Un par explícito de naturales representa el nombre racional desplazado. -/
def shiftedPair (c : Code) (n : ℕ) : ℕ × ℕ :=
  addPair (sqrtTwoPair n) (rationalPair c (n + 2))

theorem shiftedPair_correct (c : Code) (n : ℕ) :
    pairValue (shiftedPair c n) = shiftedName c n := by
  rw [shiftedPair, addPair_correct _ _ (sqrtTwoPair_den_ne_zero n)
    (rationalPair_den_ne_zero c (n + 2)), sqrtTwoPair_correct,
    rationalPair_correct]
  rfl

/-- Los dos naturales de cada aproximante se calculan primitiva recursivamente. -/
theorem primrec_shiftedPair : Primrec₂ shiftedPair := by
  have hs : Primrec (fun p : Code × ℕ => sqrtTwoPair p.2) :=
    primrec_sqrtTwoPair.comp Primrec.snd
  have hn : Primrec (fun p : Code × ℕ => p.2 + 2) :=
    Primrec.nat_add.comp Primrec.snd (Primrec.const 2)
  have hd : Primrec (fun p : Code × ℕ => rationalPair p.1 (p.2 + 2)) :=
    primrec_rationalPair.comp Primrec.fst hn
  exact (primrec_addPair.comp hs hd).of_eq (fun _ => rfl)

/-- Código natural de un nombre racional desplazado. -/
def shiftedPacked (c : Code) (n : ℕ) : ℕ :=
  Nat.pair (shiftedPair c n).1 (shiftedPair c n).2

theorem primrec_shiftedPacked : Primrec₂ shiftedPacked := by
  exact (Primrec₂.natPair.comp
    (Primrec.fst.comp primrec_shiftedPair)
    (Primrec.snd.comp primrec_shiftedPair)).of_eq fun p => rfl

/-- Universal de una entrada: programa, precisión, salida empaquetados. -/
def shiftedPackedNatural (z : ℕ) : ℕ :=
  shiftedPacked (ofNat Code z.unpair.1) z.unpair.2

theorem primrec_shiftedPackedNatural : Primrec shiftedPackedNatural := by
  have hp : Primrec (fun z : ℕ =>
      (ofNat Code z.unpair.1, z.unpair.2)) :=
    ((Primrec.ofNat Code).comp (Primrec.fst.comp Primrec.unpair)).pair
      (Primrec.snd.comp Primrec.unpair)
  exact (show Primrec (fun p : Code × ℕ => shiftedPacked p.1 p.2)
    from primrec_shiftedPacked).comp hp

/-- Un único índice universal computa todos los nombres racionales desplazados. -/
theorem exists_shifted_packed_program :
    ∃ u : Code, ∀ z : ℕ,
      shiftedPackedNatural z ∈ Nat.Partrec.Code.eval u z := by
  have hn : Nat.Primrec shiftedPackedNatural :=
    Primrec.nat_iff.mp primrec_shiftedPackedNatural
  obtain ⟨u, hu⟩ := (Nat.Partrec.Code.exists_code).mp (Nat.Partrec.of_primrec hn)
  refine ⟨u, ?_⟩
  intro z
  rw [hu]
  simp

/-- Especialización uniforme y computable del índice según el programa inicial. -/
theorem exists_uniform_shifted_codes :
    ∃ index : Code → Code, Primrec index ∧
      ∀ c n, shiftedPacked c n ∈ Nat.Partrec.Code.eval (index c) n := by
  obtain ⟨u, hu⟩ := exists_shifted_packed_program
  refine ⟨fun c => Nat.Partrec.Code.curry u (Encodable.encode c), ?_, ?_⟩
  · exact Nat.Partrec.Code.primrec₂_curry.comp
      (Primrec.const u) Primrec.encode
  · intro c n
    rw [Nat.Partrec.Code.eval_curry]
    have h := hu (Nat.pair (Encodable.encode c) n)
    simpa [shiftedPackedNatural, shiftedPacked] using h

/-- La salida de cada programa especializado representa el racional exacto. -/
theorem shiftedPacked_correct (c : Code) (n : ℕ) :
    pairValue (Nat.unpair (shiftedPacked c n)) = shiftedName c n := by
  simpa [shiftedPacked] using shiftedPair_correct c n

/-- El error total es estrictamente menor que `2⁻ⁿ`, con margen `5/16`. -/
theorem shiftedName_error (c : Code) (n : ℕ) :
    |(shiftedName c n : ℝ) - shiftedReal c| < 1 / (2 : ℝ) ^ n := by
  have hdyadic : (dyadic (n + 2) : ℝ) = 1 / (2 : ℝ) ^ (n + 4) := by
    simp [dyadic, Nat.cast_pow, show n + 2 + 2 = n + 4 by omega]
  have hscale2 : (2 : ℝ) ^ (n + 2) = (2 : ℝ) ^ n * 4 := by
    rw [pow_add]
    norm_num
  have hscale4 : (2 : ℝ) ^ (n + 4) = (2 : ℝ) ^ n * 16 := by
    rw [pow_add]
    norm_num
  have hsmall : 1 / (2 : ℝ) ^ (n + 2) + 1 / (2 : ℝ) ^ (n + 4) <
      1 / (2 : ℝ) ^ n := by
    rw [hscale2, hscale4]
    have hp : 0 < (2 : ℝ) ^ n := by positivity
    have hne : (2 : ℝ) ^ n ≠ 0 := ne_of_gt hp
    have heq : 1 / ((2 : ℝ) ^ n * 4) + 1 / ((2 : ℝ) ^ n * 16) =
        (5 / 16 : ℝ) * (1 / (2 : ℝ) ^ n) := by
      field_simp [hne]
      ring
    rw [heq]
    have hi : 0 < 1 / (2 : ℝ) ^ n := one_div_pos.mpr hp
    nlinarith
  calc
    |(shiftedName c n : ℝ) - shiftedReal c| =
        |((sqrtTwoName n : ℝ) - Real.sqrt 2) +
          ((approximant c (n + 2) : ℝ) - deltaReal c)| := by
            simp only [shiftedName, shiftedReal, Rat.cast_add]
            congr 1
            ring
    _ ≤ |(sqrtTwoName n : ℝ) - Real.sqrt 2| +
        |(approximant c (n + 2) : ℝ) - deltaReal c| := abs_add_le _ _
    _ < 1 / (2 : ℝ) ^ (n + 2) + (dyadic (n + 2) : ℝ) :=
        add_lt_add_of_lt_of_le (sqrtTwoName_error n)
          (approximant_error_real c (n + 2))
    _ = 1 / (2 : ℝ) ^ (n + 2) + 1 / (2 : ℝ) ^ (n + 4) := by rw [hdyadic]
    _ < 1 / (2 : ℝ) ^ n := hsmall

end Continuo.Indices
