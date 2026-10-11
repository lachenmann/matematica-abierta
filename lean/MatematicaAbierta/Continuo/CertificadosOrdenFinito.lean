import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.Tactic

/-!
FOR-11 / M04. A syntactic certificate calculus for finite natural polynomial
inequalities. There is no rule importing arbitrary Lean propositions.
It isolates the arithmetic successor step needed by bounded induction.
It is NOT a full RCA₀ calculus: coding of finite recursion and elimination of
its definitional extension, and the object-language induction instance, remain open.
-/
namespace MatematicaAbierta.Continuo.CertificadosOrdenFinito

noncomputable section

abbrev Poly := MvPolynomial ℕ ℕ
abbrev Context := List (Poly × Poly)

/-- Only order reflexivity/transitivity, additive monotonicity, multiplication
by a natural numeral, hypotheses, and polynomial identity transport. -/
inductive Certificate (Γ : Context) : Poly → Poly → Type where
  | hypothesis {p q : Poly} : (p, q) ∈ Γ → Certificate Γ p q
  | reflexive (p : Poly) : Certificate Γ p p
  | transitive {p q r : Poly} : Certificate Γ p q → Certificate Γ q r → Certificate Γ p r
  | addLeft {p q : Poly} (r : Poly) : Certificate Γ p q → Certificate Γ (r + p) (r + q)
  | scale {p q : Poly} (k : ℕ) : Certificate Γ p q →
      Certificate Γ (MvPolynomial.C k * p) (MvPolynomial.C k * q)
  | transport {p q p' q' : Poly} : p = p' → q = q' →
      Certificate Γ p q → Certificate Γ p' q'

def Holds (ρ : ℕ → ℕ) (Γ : Context) : Prop :=
  ∀ p q, (p, q) ∈ Γ → MvPolynomial.eval ρ p ≤ MvPolynomial.eval ρ q

/-- Uniform interpretation, not restricted to the standard natural numbers.
This verifies the finite rules in any ordered commutative semiring. It is not
a soundness theorem for the still absent second-order RCA₀ calculus. -/
def HoldsIn {R : Type*} [CommSemiring R] [PartialOrder R]
    (ρ : ℕ → R) (Γ : Context) : Prop :=
  ∀ p q, (p, q) ∈ Γ →
    MvPolynomial.eval₂ (Nat.castRingHom R) ρ p ≤
      MvPolynomial.eval₂ (Nat.castRingHom R) ρ q

theorem Certificate.soundIn {R : Type*} [CommSemiring R] [PartialOrder R]
    [IsOrderedRing R] {Γ : Context} {p q : Poly} (c : Certificate Γ p q)
    (ρ : ℕ → R) (h : HoldsIn ρ Γ) :
    MvPolynomial.eval₂ (Nat.castRingHom R) ρ p ≤
      MvPolynomial.eval₂ (Nat.castRingHom R) ρ q := by
  induction c with
  | hypothesis hm => exact h _ _ hm
  | reflexive p => exact le_rfl
  | transitive _ _ ih₁ ih₂ => exact le_trans ih₁ ih₂
  | addLeft r _ ih =>
      simpa [add_comm] using (add_le_add_left ih (MvPolynomial.eval₂ (Nat.castRingHom R) ρ r))
  | scale k _ ih => simpa using mul_le_mul_of_nonneg_left ih (Nat.cast_nonneg (α := R) k)
  | transport hp hq _ ih => simpa only [← hp, ← hq] using ih

theorem Certificate.sound {Γ : Context} {p q : Poly} (c : Certificate Γ p q)
    (ρ : ℕ → ℕ) (h : Holds ρ Γ) : MvPolynomial.eval ρ p ≤ MvPolynomial.eval ρ q := by
  induction c with
  | hypothesis hm => exact h _ _ hm
  | reflexive p => exact le_rfl
  | transitive _ _ ih₁ ih₂ => exact le_trans ih₁ ih₂
  | addLeft r _ ih => simpa using Nat.add_le_add_left ih (MvPolynomial.eval ρ r)
  | scale k _ ih => simpa using Nat.mul_le_mul_left k ih
  | transport hp hq _ ih => simpa only [← hp, ← hq] using ih

def u : Poly := MvPolynomial.X 0
def d : Poly := MvPolynomial.X 1
def b : Poly := MvPolynomial.X 2
def successorContext : Context := [(3 * u + 2, 2 * d), (b, 1)]

/-- A closed finite proof object: 3u+2≤2d, b≤1 ⊢
3(4u+2b)+2≤2(4d). Its leaves are precisely the two listed hypotheses. -/
def successorCertificate : Certificate successorContext
    (3 * (4 * u + 2 * b) + 2) (2 * (4 * d)) := by
  have hu : Certificate successorContext (3 * u + 2) (2 * d) :=
    .hypothesis (by simp [successorContext])
  have hb : Certificate successorContext b 1 :=
    .hypothesis (by simp [successorContext])
  have h₁ : Certificate successorContext (12 * u + 8) (8 * d) :=
    .transport (by norm_num; ring) (by norm_num; ring) (.scale 4 hu)
  have h₂ : Certificate successorContext (6 * b + 2) 8 :=
    .transport (by norm_num; ring) (by norm_num) (.addLeft 2 (.scale 6 hb))
  exact .transport (by ring) (by ring)
    (.transitive (.addLeft (12 * u) h₂) h₁)

/-- Semantic check of the certificate; no target arithmetic fact is an axiom. -/
theorem successor_bound (U D B : ℕ) (hu : 3 * U + 2 ≤ 2 * D) (hb : B ≤ 1) :
    3 * (4 * U + 2 * B) + 2 ≤ 2 * (4 * D) := by
  let ρ : ℕ → ℕ := fun i => if i = 0 then U else if i = 1 then D else B
  have hh : Holds ρ successorContext := by
    intro p q hpq
    simp only [successorContext, List.mem_cons, List.not_mem_nil, or_false] at hpq
    rcases hpq with h | h
    · cases h
      simpa [u, d, ρ] using hu
    · cases h
      simpa [b, ρ] using hb
  simpa [u, d, b, ρ] using successorCertificate.sound ρ hh

#print axioms successorCertificate
#print axioms successor_bound
#print axioms Certificate.soundIn

end
end MatematicaAbierta.Continuo.CertificadosOrdenFinito
