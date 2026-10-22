import MatematicaAbierta.Continuo.DatosRecodificacionBetaRCA

/-! M12: ordinary existential set introduction/elimination over unchanged
M05--M11. No rule grants sets, codes, recurrence or arithmetic truths.
Existence is obtained only by embedded Delta1 comprehension. Local set-rule
adequacy is relative to the explicit interpretation laws below; canonical
RCA0 adequacy of the entire numerical presentation remains C14. -/
namespace MatematicaAbierta.Continuo.CalculoConjuntosRCA
open CalculoRCA

inductive Proof : List Formula → Formula → Type where
  | embed {Γ : List Formula} {p : Formula} : CalculoExistencialRCA.Proof Γ p → Proof Γ p
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
  | exSI {Γ : List Formula} {p : Formula} (g : ℕ) : Proof Γ p → Proof Γ (.exS g p)
  | exSE {Γ : List Formula} {p q : Formula} (g : ℕ) :
      freshSet g Γ = true → q.setFree.contains g = false →
      Proof Γ (.exS g p) → Proof (p::Γ) q → Proof Γ q

def hyp {Γ : List Formula} {p : Formula} : Proof (p::Γ) p := .hypothesis List.mem_cons_self
def push {Γ : List Formula} {p q : Formula} (h : Proof Γ p) : Proof (q::Γ) p :=
  .weaken (fun _ hm => List.mem_cons_of_mem _ hm) h
def closed {Γ : List Formula} {p : Formula} (h : Proof [] p) : Proof Γ p :=
  .weaken (fun _ hm => False.elim (List.not_mem_nil hm)) h

def old {Γ : List Formula} {p : Formula} (h : CalculoOrdenRCA.Proof Γ p) : Proof Γ p :=
  .embed (.embed h)

structure Profile where
  previous : CalculoExistencialRCA.Profile := {}
  logicNodes : ℕ := 0
  exSI : ℕ := 0
  exSE : ℕ := 0
  exNI : ℕ := 0
  exNE : ℕ := 0
  deriving Repr
def Profile.plus (a b : Profile) : Profile :=
  ⟨a.previous.plus b.previous,a.logicNodes+b.logicNodes,
    a.exSI+b.exSI,a.exSE+b.exSE,a.exNI+b.exNI,a.exNE+b.exNE⟩
def Profile.node (a : Profile) : Profile := {a with logicNodes:=a.logicNodes+1}
def profile {Γ : List Formula} {p : Formula} : Proof Γ p → Profile
  | .embed h => ⟨CalculoExistencialRCA.profile h,1,0,0,0,0⟩
  | .hypothesis _ => ⟨{},1,0,0,0,0⟩
  | .weaken _ h | .impI h | .andL h | .andR h | .allI _ _ h | .allE _ _ _ h => (profile h).node
  | .impE h k | .andI h k => ((profile h).plus (profile k)).node
  | .exSI _ h => let a:=(profile h).node; {a with exSI:=a.exSI+1}
  | .exSE _ _ _ h k => let a:=((profile h).plus (profile k)).node; {a with exSE:=a.exSE+1}
  | .exNI _ _ _ h => let a:=(profile h).node; {a with exNI:=a.exNI+1}
  | .exNE _ _ _ h k => let a:=((profile h).plus (profile k)).node; {a with exNE:=a.exNE+1}

structure SetQuantifierSemantics where
  holds : (ℕ → Set ℕ) → Formula → Prop
  existsLaw : ∀ s g p, holds s (.exS g p) ↔ ∃ A, holds (Function.update s g A) p
  sameUpdate : ∀ s p g, holds (Function.update s g (s g)) p ↔ holds s p
  irrelevant : ∀ s p g A, p.setFree.contains g = false →
    (holds (Function.update s g A) p ↔ holds s p)
  contextFresh : ∀ s Γ g A, freshSet g Γ = true →
    (∀ p ∈ Γ, holds s p) → ∀ p ∈ Γ, holds (Function.update s g A) p

theorem exSI_adequate (m : SetQuantifierSemantics) (s : ℕ → Set ℕ)
    (p : Formula) (g : ℕ) (h : m.holds s p) : m.holds s (.exS g p) :=
  (m.existsLaw s g p).mpr ⟨s g,(m.sameUpdate s p g).mpr h⟩
theorem exSE_adequate (m : SetQuantifierSemantics) (s : ℕ → Set ℕ)
    (Γ : List Formula) (p q : Formula) (g : ℕ)
    (fresh : freshSet g Γ = true) (free : q.setFree.contains g = false)
    (hΓ : ∀ r ∈ Γ, m.holds s r) (h : m.holds s (.exS g p))
    (branch : ∀ t, (∀ r ∈ p::Γ, m.holds t r) → m.holds t q) : m.holds s q := by
  obtain ⟨A,hA⟩ := (m.existsLaw s g p).mp h
  have hc := m.contextFresh s Γ g A fresh hΓ
  have hq := branch (Function.update s g A) (by
    intro r hr
    rcases List.mem_cons.mp hr with he | hm
    · subst r; exact hA
    · exact hc r hm)
  exact (m.irrelevant s q g A free).mp hq

example : freshSet 3 [Formula.member (.lit 0) 3] = false := rfl
example : (Formula.member (.lit 0) 3).setFree.contains 3 = true := rfl
example : freshSet 3 [Formula.exS 3 (.member (.lit 0) 3)] = true := rfl
example : freshSet 4 [Formula.member (.lit 0) 2,Formula.member (.lit 0) 3] = true := rfl
#print axioms exSI_adequate
#print axioms exSE_adequate
end MatematicaAbierta.Continuo.CalculoConjuntosRCA
