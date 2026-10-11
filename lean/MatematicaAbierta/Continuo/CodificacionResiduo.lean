import MatematicaAbierta.Continuo.ReversionModular
import MatematicaAbierta.Continuo.SintaxisAritmetica

/-!
FOR-11 / M03: a bounded natural formula for the signed rational residue.
All correctness theorems below are in ambient Lean. No RCA₀ derivation is claimed.
The denominator is d+1; p-m is a redundant signed numerator.
-/
namespace MatematicaAbierta.Continuo.CodificacionResiduo
open ReversionModular SintaxisAritmetica

def rational (p m d : ℕ) : ℚ := ((p : ℚ) - m) / (d + 1)
def numerator (p m d : ℕ) : ℕ := 8*p + (d+1) + 32*(d+1)*(m+1)
def offset (m : ℕ) : ℕ := 8*m
def divisor (d : ℕ) : ℕ := 8*(d+1)
def adjusted (p m d : ℕ) : ℕ := numerator p m d - offset m
def quotient (p m d : ℕ) : ℕ := adjusted p m d / divisor d

theorem offset_le (p m d : ℕ) : offset m ≤ numerator p m d := by
  unfold offset numerator
  nlinarith

theorem signed_shift (p m d : ℕ) :
    rational p m d + 1/8 =
    (adjusted p m d : ℚ) / divisor d - (4*(m+1) : ℕ) := by
  have hs : (adjusted p m d : ℚ) =
      (numerator p m d : ℚ) - offset m := by
    exact Nat.cast_sub (offset_le p m d)
  rw [hs]
  unfold rational numerator offset divisor
  push_cast
  field_simp
  ring

theorem residue_quotient (p m d : ℕ) :
    residue (rational p m d) = (quotient p m d : ℤ) % 4 := by
  unfold residue
  rw [signed_shift, Int.floor_sub_natCast, Rat.floor_natCast_div_natCast]
  unfold quotient
  push_cast
  omega

/-- A formula using only +, ×, =, < and bounded natural quantifiers. -/
def ResidueTwo (p m d : ℕ) : Prop :=
  ∃ h, h < numerator p m d + 1 ∧
    ∃ r, r < divisor d ∧
      numerator p m d = offset m + divisor d * (4*h+2) + r

theorem residueTwo_iff_quotient (p m d : ℕ) :
    ResidueTwo p m d ↔ quotient p m d % 4 = 2 := by
  have hd : 0 < divisor d := by unfold divisor; omega
  have had : adjusted p m d + offset m = numerator p m d :=
    Nat.sub_add_cancel (offset_le p m d)
  constructor
  · rintro ⟨h, _, r, hr, he⟩
    have ha : adjusted p m d = divisor d * (4*h+2) + r := by omega
    have hq : quotient p m d = 4*h+2 := by
      unfold quotient
      rw [ha, Nat.mul_add_div hd, Nat.div_eq_of_lt hr]
    omega
  · intro hq
    let q := quotient p m d
    let r := adjusted p m d % divisor d
    have hqr : divisor d * q + r = adjusted p m d :=
      Nat.div_add_mod (adjusted p m d) (divisor d)
    have hr : r < divisor d := Nat.mod_lt _ hd
    have hform : q = 4*(q/4)+2 := by
      have he := Nat.div_add_mod q 4
      omega
    have hb : q/4 < numerator p m d + 1 := by
      have hle : q ≤ adjusted p m d := Nat.div_le_self (adjusted p m d) (divisor d)
      have ha := Nat.sub_le (numerator p m d) (offset m)
      have hsmall := Nat.div_le_self q 4
      omega
    rw [hform] at hqr
    exact ⟨q/4, hb, r, hr, by omega⟩

theorem residueTwo_iff_residue (p m d : ℕ) :
    ResidueTwo p m d ↔ residue (rational p m d) = 2 := by
  rw [residueTwo_iff_quotient, residue_quotient]
  omega

def numeral {n : ℕ} : ℕ → Term n
  | 0 => .zero
  | k+1 => .succ (numeral k)

@[simp] theorem eval_num {n : ℕ} (ρ : Fin n → ℕ) (k : ℕ) :
    (numeral k).eval ρ = k := by
  induction k with
  | zero => rfl
  | succ k ih => simp [numeral, Term.eval, ih]

def numeratorTerm {n : ℕ} (p m d : Term n) : Term n :=
  .add (.add (.mul ((numeral 8)) p) (.succ d))
    (.mul (.mul ((numeral 32)) (.succ d)) (.succ m))
def divisorTerm {n : ℕ} (d : Term n) : Term n := .mul ((numeral 8)) (.succ d)

/-- Under two binders, r has index zero and h has index one. -/
def residueMatrix {n s : ℕ} (p m d : Term n) : BoundedFormula n s :=
  .existsLt (.succ (numeratorTerm p m d))
    (.existsLt (divisorTerm (d.rename Fin.succ))
      (.equal
        (numeratorTerm (p.rename (Fin.succ ∘ Fin.succ))
          (m.rename (Fin.succ ∘ Fin.succ)) (d.rename (Fin.succ ∘ Fin.succ)))
        (.add
          (.add (.mul ((numeral 8)) (m.rename (Fin.succ ∘ Fin.succ)))
            (.mul (divisorTerm (d.rename (Fin.succ ∘ Fin.succ)))
              (.add (.mul ((numeral 4)) (.var (Fin.succ 0))) ((numeral 2)))))
          (.var 0))))

theorem residueMatrix_correct {n s : ℕ} (p m d : Term n)
    (ρ : Fin n → ℕ) (σ : Fin s → Set ℕ) :
    (residueMatrix p m d).eval ρ σ ↔
      residue (rational (p.eval ρ) (m.eval ρ) (d.eval ρ)) = 2 := by
  rw [← residueTwo_iff_residue]
  simp only [residueMatrix, BoundedFormula.eval, numeratorTerm, divisorTerm,
    Term.eval, eval_num, eval_rename, Function.comp_def, extend,
    Fin.cases_zero, Fin.cases_succ, ResidueTwo, numerator, divisor, offset]

#print axioms signed_shift
#print axioms residueTwo_iff_residue
#print axioms residueMatrix_correct
end MatematicaAbierta.Continuo.CodificacionResiduo
