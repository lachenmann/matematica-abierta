import MatematicaAbierta.Continuo.CalculoRCA

/-!
M06/H04-04.e–g. A conservative-intended ordered-arithmetic presentation
extension of the M05 deep calculus. The additional arithmetic basis is listed
as constructors: nonnegativity, discrete linear order, additive cancellation,
and monotonicity of multiplication. These are PA⁻ presentation axioms/rules,
NOT beta-code, pairing, recurrence or trace axioms. The metatheorem relating
this presentation to a canonical RCA₀ calculus remains unformalized.
Equality substitution is guarded; renamed existential elimination prevents
accidental capture when two beta readings share the bound-variable name 12.
-/
namespace MatematicaAbierta.Continuo.CalculoOrdenRCA
open CalculoRCA

inductive Proof : List Formula → Formula → Type where
  | embed {Γ : List Formula} {p : Formula} : Derives Γ p → Proof Γ p
  | hypothesis {Γ : List Formula} {p : Formula} : p ∈ Γ → Proof Γ p
  | weaken {Γ Δ : List Formula} {p : Formula} :
      (∀ q, q ∈ Γ → q ∈ Δ) → Proof Γ p → Proof Δ p
  | botE {Γ : List Formula} {p : Formula} : Proof Γ .bot → Proof Γ p
  | impI {Γ : List Formula} {p q : Formula} : Proof (p::Γ) q → Proof Γ (.imp p q)
  | impE {Γ : List Formula} {p q : Formula} : Proof Γ (.imp p q) → Proof Γ p → Proof Γ q
  | andI {Γ : List Formula} {p q : Formula} : Proof Γ p → Proof Γ q → Proof Γ (.conj p q)
  | andL {Γ : List Formula} {p q : Formula} : Proof Γ (.conj p q) → Proof Γ p
  | andR {Γ : List Formula} {p q : Formula} : Proof Γ (.conj p q) → Proof Γ q
  | allI {Γ : List Formula} {p : Formula} (x : ℕ) :
      freshNum x Γ = true → Proof Γ p → Proof Γ (.allN x p)
  | allE {Γ : List Formula} {p : Formula} (x : ℕ) (t : Term) :
      p.safe x t = true → Proof Γ (.allN x p) → Proof Γ (p.subst x t)
  | allBI {Γ : List Formula} {p : Formula} (x : ℕ) (bound : Term) :
      freshNum x Γ = true → bound.vars.contains x = false →
      Proof (.lt (.var x) bound :: Γ) p → Proof Γ (.allB x bound p)
  | allBE {Γ : List Formula} {p : Formula} (x : ℕ) (bound t : Term) :
      p.safe x t = true → Proof Γ (.allB x bound p) → Proof Γ (.lt t bound) → Proof Γ (p.subst x t)
  | exBI {Γ : List Formula} {p : Formula} (x : ℕ) (bound t : Term) :
      p.safe x t = true → Proof Γ (.lt t bound) → Proof Γ (p.subst x t) → Proof Γ (.exB x bound p)
  | exBE {Γ : List Formula} {p q : Formula} (x : ℕ) (bound : Term) :
      freshNum x Γ = true → q.numFree.contains x = false → bound.vars.contains x = false →
      Proof Γ (.exB x bound p) → Proof (p :: .lt (.var x) bound :: Γ) q → Proof Γ q
  | exBErename {Γ : List Formula} {p q : Formula} (x y : ℕ) (bound : Term) :
      freshNum y Γ = true → q.numFree.contains y = false → bound.vars.contains y = false →
      p.safe x (.var y) = true → Proof Γ (.exB x bound p) →
      Proof (p.subst x (.var y) :: .lt (.var y) bound :: Γ) q → Proof Γ q
  | eqSymm {Γ : List Formula} {t u : Term} : Proof Γ (.eq t u) → Proof Γ (.eq u t)
  | eqTrans {Γ : List Formula} {t u v : Term} : Proof Γ (.eq t u) → Proof Γ (.eq u v) → Proof Γ (.eq t v)
  | eqAdd {Γ : List Formula} {t u v w : Term} :
      Proof Γ (.eq t u) → Proof Γ (.eq v w) → Proof Γ (.eq (.add t v) (.add u w))
  | eqMul {Γ : List Formula} {t u v w : Term} :
      Proof Γ (.eq t u) → Proof Γ (.eq v w) → Proof Γ (.eq (.mul t v) (.mul u w))
  | eqSubst {Γ : List Formula} (p : Formula) (x : ℕ) (t u : Term) :
      p.safe x t = true → p.safe x u = true → Proof Γ (.eq t u) →
      Proof Γ (p.subst x t) → Proof Γ (p.subst x u)
  | leTrans {Γ : List Formula} {t u v : Term} : Proof Γ (.le t u) → Proof Γ (.le u v) → Proof Γ (.le t v)
  | leAdd {Γ : List Formula} {t u v w : Term} :
      Proof Γ (.le t u) → Proof Γ (.le v w) → Proof Γ (.le (.add t v) (.add u w))
  | leRewrite {Γ : List Formula} {t u t' u' : Term} :
      Proof Γ (.eq t t') → Proof Γ (.eq u u') → Proof Γ (.le t u) → Proof Γ (.le t' u')
  | ltRewrite {Γ : List Formula} {t u t' u' : Term} :
      Proof Γ (.eq t t') → Proof Γ (.eq u u') → Proof Γ (.lt t u) → Proof Γ (.lt t' u')
  | ltTrans {Γ : List Formula} {t u v : Term} : Proof Γ (.lt t u) → Proof Γ (.lt u v) → Proof Γ (.lt t v)
  | ltLe {Γ : List Formula} {t u : Term} : Proof Γ (.lt t u) → Proof Γ (.le t u)
  -- Explicit ordered PA⁻ basis; none is a code/recursion property.
  | zeroLe {Γ : List Formula} (t : Term) : Proof Γ (.le (.lit 0) t)
  | leAntisymm {Γ : List Formula} {t u : Term} : Proof Γ (.le t u) → Proof Γ (.le u t) → Proof Γ (.eq t u)
  | leMulRight {Γ : List Formula} {t u : Term} (v : Term) :
      Proof Γ (.le t u) → Proof Γ (.le (.mul t v) (.mul u v))
  | ltAddRight {Γ : List Formula} {t u : Term} (v : Term) :
      Proof Γ (.lt t u) → Proof Γ (.lt (.add t v) (.add u v))
  | leLtTrans {Γ : List Formula} {t u v : Term} : Proof Γ (.le t u) → Proof Γ (.lt u v) → Proof Γ (.lt t v)
  | ltLeTrans {Γ : List Formula} {t u v : Term} : Proof Γ (.lt t u) → Proof Γ (.le u v) → Proof Γ (.lt t v)
  | ltSuccLe {Γ : List Formula} {t u : Term} : Proof Γ (.lt t u) → Proof Γ (.le (.succ t) u)
  | succLeLt {Γ : List Formula} {t u : Term} : Proof Γ (.le (.succ t) u) → Proof Γ (.lt t u)
  | ltIrrefl {Γ : List Formula} {t : Term} : Proof Γ (.lt t t) → Proof Γ .bot
  | addCancelLeft {Γ : List Formula} {t u : Term} (v : Term) :
      Proof Γ (.eq (.add v t) (.add v u)) → Proof Γ (.eq t u)
  | orderCases {Γ : List Formula} {p : Formula} (t u : Term) :
      Proof (.lt t u :: Γ) p → Proof (.eq t u :: Γ) p → Proof (.lt u t :: Γ) p → Proof Γ p
  -- The SAME guarded RCA₀ IΣ₁ scheme, now accepting extended proof trees.
  | sigma1Induction {Γ : List Formula} {p : Formula} (x : ℕ) :
      Sigma1 p → freshNum x Γ = true →
      p.safe x (.lit 0) = true → p.safe x (.succ (.var x)) = true →
      Proof Γ (p.subst x (.lit 0)) →
      Proof Γ (.allN x (.imp p (p.subst x (.succ (.var x))))) → Proof Γ (.allN x p)

def ax {Γ : List Formula} {t u : Term} (h : EqProof t u) : Proof Γ (.eq t u) := .embed (.arithmetic h)
def eqRefl {Γ : List Formula} (t : Term) : Proof Γ (.eq t t) := ax (.refl t)
def leRefl {Γ : List Formula} (t : Term) : Proof Γ (.le t t) := .embed (.leRefl t)
def ltSucc {Γ : List Formula} (t : Term) : Proof Γ (.lt t (.succ t)) := .embed (.ltSucc t)
def hyp {Γ : List Formula} {p : Formula} : Proof (p::Γ) p := .hypothesis List.mem_cons_self
def push {Γ : List Formula} {p q : Formula} (h : Proof Γ p) : Proof (q::Γ) p :=
  .weaken (fun _ hm => List.mem_cons_of_mem _ hm) h
def addZeroLeft (t : Term) : EqProof (.add (.lit 0) t) t := .trans (.addComm _ _) (.addZero t)
def mulOneLeft (t : Term) : EqProof (.mul (.lit 1) t) t :=
  .trans (.mulComm _ _) (.trans (.mul (.refl _) (.literalSucc 0))
    (.trans (.mulSucc _ _) (.trans (.add (.mulZero _) (.refl _)) (addZeroLeft t))))
def mulSuccessorLeft (t u : Term) : EqProof (.mul (.succ t) u) (.add (.mul t u) u) :=
  .trans (.mulComm _ _) (.trans (.mulSucc _ _) (.add (.mulComm _ _) (.refl _)))
def leAddLeft {Γ : List Formula} {t u : Term} (v : Term) (h : Proof Γ (.le t u)) :
    Proof Γ (.le (.add v t) (.add v u)) := .leAdd (leRefl v) h
def ltAddLeft {Γ : List Formula} {t u : Term} (v : Term) (h : Proof Γ (.lt t u)) :
    Proof Γ (.lt (.add v t) (.add v u)) :=
  .ltRewrite (ax (.addComm _ _)) (ax (.addComm _ _)) (.ltAddRight v h)
def leRightAdd {Γ : List Formula} (t u : Term) : Proof Γ (.le t (.add t u)) :=
  .leRewrite (ax (.addZero _)) (eqRefl _) (.leAdd (leRefl t) (.zeroLe u))
def leLeftAdd {Γ : List Formula} (t u : Term) : Proof Γ (.le t (.add u t)) :=
  .leRewrite (eqRefl _) (ax (.addComm _ _)) (leRightAdd t u)
def leMulLeft {Γ : List Formula} {t u : Term} (v : Term) (h : Proof Γ (.le t u)) :
    Proof Γ (.le (.mul v t) (.mul v u)) :=
  .leRewrite (ax (.mulComm _ _)) (ax (.mulComm _ _)) (.leMulRight v h)
def leSucc {Γ : List Formula} (t : Term) : Proof Γ (.le t (.succ t)) := .ltLe (ltSucc t)
def leThenSucc {Γ : List Formula} {t u : Term} (h : Proof Γ (.le t u)) :
    Proof Γ (.lt t (.succ u)) := .leLtTrans h (ltSucc u)

structure Profile where
  nodes : ℕ := 0
  orderCases : ℕ := 0
  arithmeticBasis : ℕ := 0
  sigma1 : ℕ := 0
  delta1 : ℕ := 0
  deriving Repr
def Profile.plus (a b : Profile) : Profile :=
  ⟨a.nodes+b.nodes,a.orderCases+b.orderCases,a.arithmeticBasis+b.arithmeticBasis,a.sigma1+b.sigma1,a.delta1+b.delta1⟩
def Profile.node (a : Profile) : Profile := {a with nodes:=a.nodes+1}
def profile {Γ : List Formula} {p : Formula} : Proof Γ p → Profile
  | .embed h => let a:=ruleProfile h; ⟨a.nodes,0,0,a.sigma1Instances,a.delta1Instances⟩
  | .hypothesis _ => ⟨1,0,0,0,0⟩
  | .weaken _ h | .botE h | .impI h | .andL h | .andR h | .eqSymm h | .ltLe h => (profile h).node
  | .impE h k | .andI h k | .eqTrans h k | .eqAdd h k | .eqMul h k | .leTrans h k | .leAdd h k | .ltTrans h k =>
      ((profile h).plus (profile k)).node
  | .allI _ _ h | .allE _ _ _ h | .allBI _ _ _ _ h => (profile h).node
  | .allBE _ _ _ _ h k | .exBI _ _ _ _ h k | .exBE _ _ _ _ _ h k | .exBErename _ _ _ _ _ _ _ h k =>
      ((profile h).plus (profile k)).node
  | .eqSubst _ _ _ _ _ _ h k => ((profile h).plus (profile k)).node
  | .leRewrite h k l | .ltRewrite h k l => (((profile h).plus (profile k)).plus (profile l)).node
  | .zeroLe _ => ⟨1,0,1,0,0⟩
  | .leAntisymm h k | .leLtTrans h k | .ltLeTrans h k =>
      let a:=((profile h).plus (profile k)).node; {a with arithmeticBasis:=a.arithmeticBasis+1}
  | .leMulRight _ h | .ltAddRight _ h | .ltSuccLe h | .succLeLt h | .ltIrrefl h | .addCancelLeft _ h =>
      let a:=(profile h).node; {a with arithmeticBasis:=a.arithmeticBasis+1}
  | .orderCases _ _ h k l =>
      let a:=(((profile h).plus (profile k)).plus (profile l)).node; {a with orderCases:=a.orderCases+1}
  | .sigma1Induction _ _ _ _ _ h k =>
      let a:=((profile h).plus (profile k)).node; {a with sigma1:=a.sigma1+1}

#print axioms mulSuccessorLeft
#print axioms leThenSucc
end MatematicaAbierta.Continuo.CalculoOrdenRCA
