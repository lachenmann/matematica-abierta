import MatematicaAbierta.Continuo.ParametroParBetaRCA

/-! M09: ordinary first-order existential rules over unchanged M05--M08.
No arithmetic, common-multiple, coding or CRT constructor is introduced.
Global adequacy of the old ordered presentation remains a separate obligation. -/
namespace MatematicaAbierta.Continuo.CalculoExistencialRCA
open CalculoRCA

inductive Proof : List Formula → Formula → Type where
  | embed {Γ : List Formula} {p : Formula} : CalculoOrdenRCA.Proof Γ p → Proof Γ p
  | hypothesis {Γ : List Formula} {p : Formula} : p ∈ Γ → Proof Γ p
  | weaken {Γ Δ : List Formula} {p : Formula} :
      (∀ q, q ∈ Γ → q ∈ Δ) → Proof Γ p → Proof Δ p
  | impI {Γ : List Formula} {p q : Formula} : Proof (p::Γ) q → Proof Γ (.imp p q)
  | impE {Γ : List Formula} {p q : Formula} : Proof Γ (.imp p q) → Proof Γ p → Proof Γ q
  | andI {Γ : List Formula} {p q : Formula} : Proof Γ p → Proof Γ q → Proof Γ (.conj p q)
  | andL {Γ : List Formula} {p q : Formula} : Proof Γ (.conj p q) → Proof Γ p
  | andR {Γ : List Formula} {p q : Formula} : Proof Γ (.conj p q) → Proof Γ q
  | allI {Γ : List Formula} {p : Formula} (x : ℕ) :
      freshNum x Γ = true → Proof Γ p → Proof Γ (.allN x p)
  | allE {Γ : List Formula} {p : Formula} (x : ℕ) (t : Term) :
      p.safe x t = true → Proof Γ (.allN x p) → Proof Γ (p.subst x t)
  | exNI {Γ : List Formula} {p : Formula} (x : ℕ) (t : Term) :
      p.safe x t = true → Proof Γ (p.subst x t) → Proof Γ (.exN x p)
  | exNE {Γ : List Formula} {p q : Formula} (x : ℕ) :
      freshNum x Γ = true → q.numFree.contains x = false →
      Proof Γ (.exN x p) → Proof (p::Γ) q → Proof Γ q
  | sigma1Induction {Γ : List Formula} {p : Formula} (x : ℕ) :
      Sigma1 p → freshNum x Γ = true →
      p.safe x (.lit 0) = true → p.safe x (.succ (.var x)) = true →
      Proof Γ (p.subst x (.lit 0)) →
      Proof Γ (.allN x (.imp p (p.subst x (.succ (.var x))))) → Proof Γ (.allN x p)

def hyp {Γ : List Formula} {p : Formula} : Proof (p::Γ) p := .hypothesis List.mem_cons_self
def push {Γ : List Formula} {p q : Formula} (h : Proof Γ p) : Proof (q::Γ) p :=
  .weaken (fun _ hm => List.mem_cons_of_mem _ hm) h
def closed {Γ : List Formula} {p : Formula} (h : Proof [] p) : Proof Γ p :=
  .weaken (fun _ hm => False.elim (List.not_mem_nil hm)) h

structure Profile where
  old : CalculoOrdenRCA.Profile := {}
  logicNodes : ℕ := 0
  exNI : ℕ := 0
  exNE : ℕ := 0
  sigma1 : ℕ := 0
  deriving Repr
def Profile.plus (a b : Profile) : Profile :=
  ⟨a.old.plus b.old,a.logicNodes+b.logicNodes,a.exNI+b.exNI,a.exNE+b.exNE,a.sigma1+b.sigma1⟩
def Profile.node (a : Profile) : Profile := {a with logicNodes:=a.logicNodes+1}
def profile {Γ : List Formula} {p : Formula} : Proof Γ p → Profile
  | .embed h => ⟨CalculoOrdenRCA.profile h,1,0,0,0⟩
  | .hypothesis _ => ⟨{},1,0,0,0⟩
  | .weaken _ h | .impI h | .andL h | .andR h | .allI _ _ h | .allE _ _ _ h => (profile h).node
  | .impE h k | .andI h k => ((profile h).plus (profile k)).node
  | .exNI _ _ _ h => let a:=(profile h).node; {a with exNI:=a.exNI+1}
  | .exNE _ _ _ h k => let a:=((profile h).plus (profile k)).node; {a with exNE:=a.exNE+1}
  | .sigma1Induction _ _ _ _ _ h k =>
      let a:=((profile h).plus (profile k)).node; {a with sigma1:=a.sigma1+1}

/-- Local logical adequacy interface. These laws are NOT Proof constructors,
nor mathematical hypotheses of commonMultipleClosed. An implementation of
full RCA0 semantics and global old-calculus adequacy remain separate. -/
structure QuantifierSemantics where
  holds : (ℕ → ℕ) → Formula → Prop
  evalTerm : (ℕ → ℕ) → Term → ℕ
  existsLaw : ∀ v x p, holds v (.exN x p) ↔ ∃ n, holds (Function.update v x n) p
  substitution : ∀ v p x t, p.safe x t = true →
    (holds v (p.subst x t) ↔ holds (Function.update v x (evalTerm v t)) p)
  irrelevant : ∀ v p x n, p.numFree.contains x = false →
    (holds (Function.update v x n) p ↔ holds v p)
  contextFresh : ∀ v Γ x n, freshNum x Γ = true →
    (∀ p ∈ Γ, holds v p) → ∀ p ∈ Γ, holds (Function.update v x n) p

theorem exNI_adequate (s : QuantifierSemantics) (v : ℕ → ℕ)
    (p : Formula) (x : ℕ) (t : Term) (guard : p.safe x t = true)
    (h : s.holds v (p.subst x t)) : s.holds v (.exN x p) :=
  (s.existsLaw v x p).mpr ⟨s.evalTerm v t,(s.substitution v p x t guard).mp h⟩

theorem exNE_adequate (s : QuantifierSemantics) (v : ℕ → ℕ)
    (Γ : List Formula) (p q : Formula) (x : ℕ)
    (fresh : freshNum x Γ = true) (free : q.numFree.contains x = false)
    (hΓ : ∀ r ∈ Γ, s.holds v r) (h : s.holds v (.exN x p))
    (branch : ∀ w, (∀ r ∈ p::Γ, s.holds w r) → s.holds w q) : s.holds v q := by
  obtain ⟨n,hn⟩ := (s.existsLaw v x p).mp h
  have hc := s.contextFresh v Γ x n fresh hΓ
  have hq := branch (Function.update v x n) (by
    intro r hr
    rcases List.mem_cons.mp hr with he | hm
    · subst r; exact hn
    · exact hc r hm)
  exact (s.irrelevant v q x n free).mp hq

-- Negative guard controls: capture or escaping eigenvariables are rejected.
example : (Formula.allN 16 (.eq (.var 30) (.var 16))).safe 30 (.var 16) = false := by decide
example : freshNum 30 [Formula.eq (.var 30) (.lit 0)] = false := by decide
example : (Formula.eq (.var 30) (.lit 0)).numFree.contains 30 = true := by decide
example : freshNum 30 [Formula.exN 30 (.eq (.var 30) (.lit 0))] = true := by decide
example : (Formula.exN 30 (.eq (.var 30) (.var 3))).numFree.contains 30 = false := by decide
example : (Formula.eq (.var 30) (.var 3)).safe 30 (.var 40) = true := by decide

#print axioms exNI_adequate
#print axioms exNE_adequate
end MatematicaAbierta.Continuo.CalculoExistencialRCA
