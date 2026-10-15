import MatematicaAbierta.Continuo.LogicaClasicaOrdinariaRCA

/-! M15/C14 first stage. Two arbitrary domains, including Henkin set domains.
No standard-model restriction; no arithmetic, induction or comprehension
soundness is assumed. The operations below are an uninterpreted signature. -/
namespace MatematicaAbierta.Continuo.InterpretacionParametricaRCA
open CalculoRCA
universe u v
structure Signature (A : Type u) (S : Type v) where
  numeral : ℕ → A
  succ : A → A
  add : A → A → A
  mul : A → A → A
  le : A → A → Prop
  lt : A → A → Prop
  member : A → S → Prop

def term {A : Type u} {S : Type v} (m : Signature A S) (ρ : ℕ → A) : Term → A
  | .lit n => m.numeral n
  | .var x => ρ x
  | .succ t => m.succ (term m ρ t)
  | .add t r => m.add (term m ρ t) (term m ρ r)
  | .mul t r => m.mul (term m ρ t) (term m ρ r)

def holds {A : Type u} {S : Type v} (m : Signature A S) (ρ : ℕ → A) (σ : ℕ → S) : Formula → Prop
  | .bot => False
  | .eq t r => term m ρ t = term m ρ r
  | .le t r => m.le (term m ρ t) (term m ρ r)
  | .lt t r => m.lt (term m ρ t) (term m ρ r)
  | .member t g => m.member (term m ρ t) (σ g)
  | .conj p q => holds m ρ σ p ∧ holds m ρ σ q
  | .imp p q => holds m ρ σ p → holds m ρ σ q
  | .allN x p => ∀ a : A, holds m (Function.update ρ x a) σ p
  | .exN x p => ∃ a : A, holds m (Function.update ρ x a) σ p
  | .allB x b p => ∀ a : A, m.lt a (term m ρ b) → holds m (Function.update ρ x a) σ p
  | .exB x b p => ∃ a : A, m.lt a (term m ρ b) ∧ holds m (Function.update ρ x a) σ p
  | .exS g p => ∃ X : S, holds m ρ (Function.update σ g X) p

def context {A : Type u} {S : Type v} (m : Signature A S) (ρ : ℕ → A) (σ : ℕ → S) (Γ : List Formula) : Prop :=
  ∀ p ∈ Γ, holds m ρ σ p

def Valid {A : Type u} {S : Type v} (m : Signature A S) (Γ : List Formula) (p : Formula) : Prop :=
  ∀ ρ σ, context m ρ σ Γ → holds m ρ σ p

-- Pure environment algebra, independent of arithmetic interpretation.
theorem update_shadow {D : Type u} (ρ : ℕ → D) (x : ℕ) (a b : D) :
    Function.update (Function.update ρ x a) x b = Function.update ρ x b := by
  funext y; by_cases h : y=x <;> simp [h]
theorem update_commute {D : Type u} (ρ : ℕ → D) (x y : ℕ) (a b : D) (h : x≠y) :
    Function.update (Function.update ρ x a) y b = Function.update (Function.update ρ y b) x a := by
  funext z; by_cases hx : z=x <;> by_cases hy : z=y <;> simp_all

theorem term_coincidence {A : Type u} {S : Type v} (m : Signature A S) (t : Term) (ρ τ : ℕ → A)
    (h : ∀ x ∈ t.vars, ρ x = τ x) : term m ρ t = term m τ t := by
  induction t with
  | lit n => rfl
  | var x => exact h x (by simp [Term.vars])
  | succ t ih => exact congrArg m.succ (ih (by simpa [Term.vars] using h))
  | add t r it ir =>
    exact congrArg₂ m.add (it (fun x hx => h x (by simp [Term.vars,hx])))
      (ir (fun x hx => h x (by simp [Term.vars,hx])))
  | mul t r it ir =>
    exact congrArg₂ m.mul (it (fun x hx => h x (by simp [Term.vars,hx])))
      (ir (fun x hx => h x (by simp [Term.vars,hx])))

theorem term_fresh {A : Type u} {S : Type v} (m : Signature A S) (t : Term) (ρ : ℕ → A) (x : ℕ) (a : A)
    (h : t.vars.contains x = false) : term m (Function.update ρ x a) t = term m ρ t := by
  apply term_coincidence
  intro y hy
  have hx : x ∉ t.vars := by simpa using h
  have hne : y≠x := by intro he; subst y; exact hx hy
  simp [hne]

theorem term_substitution {A : Type u} {S : Type v} (m : Signature A S) (t r : Term) (x : ℕ) (ρ : ℕ → A) :
    term m ρ (t.subst x r) = term m (Function.update ρ x (term m ρ r)) t := by
  induction t with
  | lit n => rfl
  | var y => by_cases h : y=x <;> simp [Term.subst,term,h]
  | succ t ih => simpa [Term.subst,term] using congrArg m.succ ih
  | add t s it is => simpa [Term.subst,term] using congrArg₂ m.add it is
  | mul t s it is => simpa [Term.subst,term] using congrArg₂ m.mul it is

#print axioms update_shadow
#print axioms update_commute
#print axioms term_coincidence
#print axioms term_fresh
#print axioms term_substitution
end MatematicaAbierta.Continuo.InterpretacionParametricaRCA
