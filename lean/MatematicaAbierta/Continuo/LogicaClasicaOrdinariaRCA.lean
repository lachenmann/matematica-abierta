import MatematicaAbierta.Continuo.GraficaBitsAcotadosRCA

/-! M14: explicit ordinary classical case rule, not a set/code existence rule.
Previous M05--M13 sources are unchanged. Global presentation adequacy is C14.
The only new logical principle is cases on p versus p -> bottom. -/
namespace MatematicaAbierta.Continuo.LogicaClasicaOrdinariaRCA
open CalculoRCA
inductive Proof : List Formula → Formula → Type where
  | embed {Γ : List Formula} {p : Formula} : CalculoConjuntosRCA.Proof Γ p → Proof Γ p
  | hypothesis {Γ : List Formula} {p : Formula} : p ∈ Γ → Proof Γ p
  | weaken {Γ Δ : List Formula} {p : Formula} : (∀ q, q ∈ Γ → q ∈ Δ) → Proof Γ p → Proof Δ p
  | impI {Γ : List Formula} {p q : Formula} : Proof (p::Γ) q → Proof Γ (.imp p q)
  | impE {Γ : List Formula} {p q : Formula} : Proof Γ (.imp p q) → Proof Γ p → Proof Γ q
  | andI {Γ : List Formula} {p q : Formula} : Proof Γ p → Proof Γ q → Proof Γ (.conj p q)
  | andL {Γ : List Formula} {p q : Formula} : Proof Γ (.conj p q) → Proof Γ p
  | andR {Γ : List Formula} {p q : Formula} : Proof Γ (.conj p q) → Proof Γ q
  | allI {Γ : List Formula} {p : Formula} (x : ℕ) : freshNum x Γ = true → Proof Γ p → Proof Γ (.allN x p)
  | allE {Γ : List Formula} {p : Formula} (x : ℕ) (t : Term) : p.safe x t = true → Proof Γ (.allN x p) → Proof Γ (p.subst x t)
  | exNI {Γ : List Formula} {p : Formula} (x : ℕ) (t : Term) : p.safe x t = true → Proof Γ (p.subst x t) → Proof Γ (.exN x p)
  | exNE {Γ : List Formula} {p q : Formula} (x : ℕ) : freshNum x Γ = true → q.numFree.contains x = false → Proof Γ (.exN x p) → Proof (p::Γ) q → Proof Γ q
  | exSI {Γ : List Formula} {p : Formula} (g : ℕ) : Proof Γ p → Proof Γ (.exS g p)
  | exSE {Γ : List Formula} {p q : Formula} (g : ℕ) : freshSet g Γ = true → q.setFree.contains g = false → Proof Γ (.exS g p) → Proof (p::Γ) q → Proof Γ q
  | cases {Γ : List Formula} {p q : Formula} : Proof (p::Γ) q → Proof (.imp p .bot::Γ) q → Proof Γ q

def hyp {Γ : List Formula} {p : Formula} : Proof (p::Γ) p := .hypothesis List.mem_cons_self
def push {Γ : List Formula} {p q : Formula} (h : Proof Γ p) : Proof (q::Γ) p := .weaken (fun _ hm => List.mem_cons_of_mem _ hm) h
def closed {Γ : List Formula} {p : Formula} (h : Proof [] p) : Proof Γ p := .weaken (fun _ hm => False.elim (List.not_mem_nil hm)) h
def old {Γ : List Formula} {p : Formula} (h : CalculoOrdenRCA.Proof Γ p) : Proof Γ p := .embed (CalculoConjuntosRCA.old h)
structure Profile where
  previous : CalculoConjuntosRCA.Profile := {}
  logicNodes : ℕ := 0
  classicalCases : ℕ := 0
  deriving Repr
def Profile.plus (a b : Profile) : Profile := ⟨a.previous.plus b.previous,a.logicNodes+b.logicNodes,a.classicalCases+b.classicalCases⟩
def Profile.node (a : Profile) : Profile := {a with logicNodes:=a.logicNodes+1}
def profile {Γ : List Formula} {p : Formula} : Proof Γ p → Profile
  | .embed h => ⟨CalculoConjuntosRCA.profile h,1,0⟩
  | .hypothesis _ => ⟨{},1,0⟩
  | .weaken _ h | .impI h | .andL h | .andR h | .allI _ _ h | .allE _ _ _ h | .exNI _ _ _ h | .exSI _ h => (profile h).node
  | .impE h k | .andI h k | .exNE _ _ _ h k | .exSE _ _ _ h k => ((profile h).plus (profile k)).node
  | .cases h k => let a:=((profile h).plus (profile k)).node; {a with classicalCases:=a.classicalCases+1}

-- Relative local adequacy of the new rule. No global RCA0 metatheorem.
theorem cases_adequate (p q : Prop) (yes : p → q) (no : (p → False) → q) : q := by
  classical
  exact (Classical.em p).elim yes no
#print axioms cases_adequate
end MatematicaAbierta.Continuo.LogicaClasicaOrdinariaRCA
