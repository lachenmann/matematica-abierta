import Mathlib.Data.Fin.Basic
import Mathlib.Tactic

/-!
FOR-11: an explicit bounded arithmetic syntax with natural variables and set parameters.
Bounded number quantifiers preserve Δ⁰₀; Σ⁰₁/Π⁰₁ add one outer number quantifier.
No second-order comprehension or proof calculus is postulated here.
-/
namespace MatematicaAbierta.Continuo.SintaxisAritmetica

inductive Term (n : ℕ) where
  | zero : Term n
  | var : Fin n → Term n
  | succ : Term n → Term n
  | add : Term n → Term n → Term n
  | mul : Term n → Term n → Term n

def Term.eval {n : ℕ} (ρ : Fin n → ℕ) : Term n → ℕ
  | .zero => 0
  | .var i => ρ i
  | .succ t => t.eval ρ + 1
  | .add t u => t.eval ρ + u.eval ρ
  | .mul t u => t.eval ρ * u.eval ρ

def Term.rename {n k : ℕ} (r : Fin n → Fin k) : Term n → Term k
  | .zero => .zero
  | .var i => .var (r i)
  | .succ t => .succ (t.rename r)
  | .add t u => .add (t.rename r) (u.rename r)
  | .mul t u => .mul (t.rename r) (u.rename r)

 theorem eval_rename {n k : ℕ} (r : Fin n → Fin k) (ρ : Fin k → ℕ) (t : Term n) :
    (t.rename r).eval ρ = t.eval (ρ ∘ r) := by
  induction t with
  | zero => rfl
  | var i => rfl
  | succ t ih => simp [Term.rename, Term.eval, ih]
  | add t u iht ihu => simp [Term.rename, Term.eval, iht, ihu]
  | mul t u iht ihu => simp [Term.rename, Term.eval, iht, ihu]

/-- The newly bound natural variable has index zero; existing variables are shifted. -/
def extend {n : ℕ} (x : ℕ) (ρ : Fin n → ℕ) : Fin (n + 1) → ℕ := Fin.cases x ρ

 theorem extend_zero {n : ℕ} (x : ℕ) (ρ : Fin n → ℕ) : extend x ρ 0 = x := rfl

 theorem extend_succ {n : ℕ} (x : ℕ) (ρ : Fin n → ℕ) (i : Fin n) :
    extend x ρ i.succ = ρ i := by simp [extend]

inductive BoundedFormula : ℕ → ℕ → Type where
  | falsum {n s : ℕ} : BoundedFormula n s
  | equal {n s : ℕ} : Term n → Term n → BoundedFormula n s
  | less {n s : ℕ} : Term n → Term n → BoundedFormula n s
  | member {n s : ℕ} : Term n → Fin s → BoundedFormula n s
  | neg {n s : ℕ} : BoundedFormula n s → BoundedFormula n s
  | conj {n s : ℕ} : BoundedFormula n s → BoundedFormula n s → BoundedFormula n s
  | disj {n s : ℕ} : BoundedFormula n s → BoundedFormula n s → BoundedFormula n s
  | existsLt {n s : ℕ} : Term n → BoundedFormula (n + 1) s → BoundedFormula n s
  | forallLt {n s : ℕ} : Term n → BoundedFormula (n + 1) s → BoundedFormula n s

def BoundedFormula.eval {n s : ℕ} (φ : BoundedFormula n s)
    (ρ : Fin n → ℕ) (σ : Fin s → Set ℕ) : Prop :=
  match φ with
  | .falsum => False
  | .equal t u => t.eval ρ = u.eval ρ
  | .less t u => t.eval ρ < u.eval ρ
  | .member t i => t.eval ρ ∈ σ i
  | .neg ψ => ¬ ψ.eval ρ σ
  | .conj ψ χ => ψ.eval ρ σ ∧ χ.eval ρ σ
  | .disj ψ χ => ψ.eval ρ σ ∨ χ.eval ρ σ
  | .existsLt t ψ => ∃ x, x < t.eval ρ ∧ ψ.eval (extend x ρ) σ
  | .forallLt t ψ => ∀ x, x < t.eval ρ → ψ.eval (extend x ρ) σ

/-- Normal forms: one outer unbounded number quantifier and a bounded matrix. -/
def sigma1 {n s : ℕ} (matrix : BoundedFormula (n + 1) s)
    (ρ : Fin n → ℕ) (σ : Fin s → Set ℕ) : Prop := ∃ x, matrix.eval (extend x ρ) σ

def pi1 {n s : ℕ} (matrix : BoundedFormula (n + 1) s)
    (ρ : Fin n → ℕ) (σ : Fin s → Set ℕ) : Prop := ∀ x, matrix.eval (extend x ρ) σ

 theorem pi1_neg_iff_not_sigma1 {n s : ℕ} (matrix : BoundedFormula (n + 1) s)
    (ρ : Fin n → ℕ) (σ : Fin s → Set ℕ) :
    pi1 (.neg matrix) ρ σ ↔ ¬ sigma1 matrix ρ σ := by
  simp [pi1, sigma1, BoundedFormula.eval]

 theorem sigma1_neg_iff_not_pi1 {n s : ℕ} (matrix : BoundedFormula (n + 1) s)
    (ρ : Fin n → ℕ) (σ : Fin s → Set ℕ) :
    sigma1 (.neg matrix) ρ σ ↔ ¬ pi1 matrix ρ σ := by
  classical
  simp [sigma1, pi1, BoundedFormula.eval]

/-- Complementarity is an explicit hypothesis at an assignment, not a new axiom. -/
theorem complementary_matrices_delta1 {n s : ℕ}
    (positive negative : BoundedFormula (n + 1) s)
    (ρ : Fin n → ℕ) (σ : Fin s → Set ℕ)
    (h : sigma1 positive ρ σ ↔ ¬ sigma1 negative ρ σ) :
    sigma1 positive ρ σ ↔ pi1 (.neg negative) ρ σ := by
  exact h.trans (pi1_neg_iff_not_sigma1 negative ρ σ).symm

#print axioms eval_rename
#print axioms pi1_neg_iff_not_sigma1
#print axioms sigma1_neg_iff_not_pi1
#print axioms complementary_matrices_delta1
end MatematicaAbierta.Continuo.SintaxisAritmetica
