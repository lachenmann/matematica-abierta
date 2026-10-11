import Mathlib.Data.List.Basic

/-!
FOR-11 / H04-04–06. Deep syntax and finite derivations for an RCA₀ fragment.
Number variables use names; capture/freshness side conditions are syntactic.
No rule embeds arbitrary Lean truth. The arithmetic presentation uses the
universal ordered-semiring laws of PA⁻, with successor/numeral abbreviations.
Only the actual IΣ₁ and Δ₁-comprehension schemes may introduce induction/sets.
The order basis is the nonnegative discrete PA⁻ presentation (including
successor positivity, zero least, and < implying ≤). No recurrence or invariant
is a theory axiom. Global soundness/presentation-equivalence is not proved here.
This is a fragment, not a completeness or equivalence proof for all RCA₀.
-/
namespace MatematicaAbierta.Continuo.CalculoRCA

inductive Term where
  | lit : ℕ → Term
  | var : ℕ → Term
  | succ : Term → Term
  | add : Term → Term → Term
  | mul : Term → Term → Term
  deriving DecidableEq, Repr

def Term.vars : Term → List ℕ
  | .lit _ => []
  | .var x => [x]
  | .succ t => t.vars
  | .add t u | .mul t u => t.vars ++ u.vars

def Term.subst (source : Term) (x : ℕ) (t : Term) : Term :=
  match source with
  | .lit n => .lit n
  | .var y => if y = x then t else .var y
  | .succ u => .succ (u.subst x t)
  | .add u v => .add (u.subst x t) (v.subst x t)
  | .mul u v => .mul (u.subst x t) (v.subst x t)

inductive Formula where
  | bot : Formula
  | eq : Term → Term → Formula
  | le : Term → Term → Formula
  | lt : Term → Term → Formula
  | member : Term → ℕ → Formula
  | conj : Formula → Formula → Formula
  | imp : Formula → Formula → Formula
  | allN : ℕ → Formula → Formula
  | exN : ℕ → Formula → Formula
  | allB : ℕ → Term → Formula → Formula
  | exB : ℕ → Term → Formula → Formula
  | exS : ℕ → Formula → Formula
  deriving DecidableEq, Repr

def iffF (p q : Formula) : Formula := .conj (.imp p q) (.imp q p)

def Formula.numFree : Formula → List ℕ
  | .bot => []
  | .eq t u | .le t u | .lt t u => t.vars ++ u.vars
  | .member t _ => t.vars
  | .conj p q | .imp p q => p.numFree ++ q.numFree
  | .allN x p | .exN x p => p.numFree.filter (· != x)
  | .allB x t p | .exB x t p => t.vars ++ p.numFree.filter (· != x)
  | .exS _ p => p.numFree

def Formula.setFree : Formula → List ℕ
  | .bot | .eq _ _ | .le _ _ | .lt _ _ => []
  | .member _ g => [g]
  | .conj p q | .imp p q => p.setFree ++ q.setFree
  | .allN _ p | .exN _ p | .allB _ _ p | .exB _ _ p => p.setFree
  | .exS g p => p.setFree.filter (· != g)

def Formula.subst (x : ℕ) (t : Term) : Formula → Formula
  | .bot => .bot
  | .eq u v => .eq (u.subst x t) (v.subst x t)
  | .le u v => .le (u.subst x t) (v.subst x t)
  | .lt u v => .lt (u.subst x t) (v.subst x t)
  | .member u g => .member (u.subst x t) g
  | .conj p q => .conj (p.subst x t) (q.subst x t)
  | .imp p q => .imp (p.subst x t) (q.subst x t)
  | .allN y p => .allN y (if y = x then p else p.subst x t)
  | .exN y p => .exN y (if y = x then p else p.subst x t)
  | .allB y u p => .allB y (u.subst x t) (if y = x then p else p.subst x t)
  | .exB y u p => .exB y (u.subst x t) (if y = x then p else p.subst x t)
  | .exS g p => .exS g (p.subst x t)

def Formula.safe (x : ℕ) (t : Term) : Formula → Bool
  | .bot | .eq _ _ | .le _ _ | .lt _ _ | .member _ _ => true
  | .conj p q | .imp p q => p.safe x t && q.safe x t
  | .allN y p | .exN y p | .allB y _ p | .exB y _ p =>
      y == x || (!t.vars.contains y && p.safe x t)
  | .exS _ p => p.safe x t

def Formula.bounded : Formula → Bool
  | .bot | .eq _ _ | .le _ _ | .lt _ _ | .member _ _ => true
  | .conj p q | .imp p q => p.bounded && q.bounded
  | .allB _ _ p | .exB _ _ p => p.bounded
  | .allN _ _ | .exN _ _ | .exS _ _ => false

inductive Sigma1 : Formula → Type where
  | bounded {p : Formula} : p.bounded = true → Sigma1 p
  | exists {p : Formula} (x : ℕ) : Sigma1 p → Sigma1 (.exN x p)

inductive Pi1 : Formula → Type where
  | bounded {p : Formula} : p.bounded = true → Pi1 p
  | forall {p : Formula} (x : ℕ) : Pi1 p → Pi1 (.allN x p)

/-- Equational proof trees. Literal expansion is syntax of numerals; ground
addition/multiplication below are DERIVED, not assumed as theorem axioms. -/
inductive EqProof : Term → Term → Type where
  | refl (t : Term) : EqProof t t
  | symm {t u : Term} : EqProof t u → EqProof u t
  | trans {t u v : Term} : EqProof t u → EqProof u v → EqProof t v
  | succ {t u : Term} : EqProof t u → EqProof (.succ t) (.succ u)
  | add {t u v w : Term} : EqProof t u → EqProof v w → EqProof (.add t v) (.add u w)
  | mul {t u v w : Term} : EqProof t u → EqProof v w → EqProof (.mul t v) (.mul u w)
  | literalSucc (n : ℕ) : EqProof (.lit (n+1)) (.succ (.lit n))
  | addZero (t : Term) : EqProof (.add t (.lit 0)) t
  | addSucc (t u : Term) : EqProof (.add t (.succ u)) (.succ (.add t u))
  | mulZero (t : Term) : EqProof (.mul t (.lit 0)) (.lit 0)
  | mulSucc (t u : Term) : EqProof (.mul t (.succ u)) (.add (.mul t u) t)
  | addComm (t u : Term) : EqProof (.add t u) (.add u t)
  | addAssoc (t u v : Term) : EqProof (.add (.add t u) v) (.add t (.add u v))
  | mulComm (t u : Term) : EqProof (.mul t u) (.mul u t)
  | mulAssoc (t u v : Term) : EqProof (.mul (.mul t u) v) (.mul t (.mul u v))
  | distrib (t u v : Term) : EqProof (.mul t (.add u v)) (.add (.mul t u) (.mul t v))

def numeralAdd (m : ℕ) : (n : ℕ) → EqProof (.add (.lit m) (.lit n)) (.lit (m+n))
  | 0 => .addZero _
  | n+1 => .trans (.add (.refl _) (.literalSucc n))
      (.trans (.addSucc _ _) (.trans (.succ (numeralAdd m n)) (.symm (.literalSucc (m+n)))))

def numeralMul (m : ℕ) : (n : ℕ) → EqProof (.mul (.lit m) (.lit n)) (.lit (m*n))
  | 0 => .mulZero _
  | n+1 => .trans (.mul (.refl _) (.literalSucc n))
      (.trans (.mulSucc _ _) (.trans (.add (numeralMul m n) (.refl _)) (numeralAdd (m*n) m)))

def coefficientProduct (a b : ℕ) (t : Term) :
    EqProof (.mul (.lit a) (.mul (.lit b) t)) (.mul (.lit (a*b)) t) :=
  .trans (.symm (.mulAssoc _ _ _)) (.mul (numeralMul a b) (.refl t))

def freshNum (x : ℕ) (Γ : List Formula) : Bool :=
  Γ.all fun p => !p.numFree.contains x

def freshSet (g : ℕ) (Γ : List Formula) : Bool :=
  Γ.all fun p => !p.setFree.contains g

/-- A fragment of actual inference rules. Hypotheses are context entries,
not theory axioms. Induction/comprehension have syntactic complexity guards. -/
inductive Derives : List Formula → Formula → Type where
  | hypothesis {Γ : List Formula} {p : Formula} : p ∈ Γ → Derives Γ p
  | botE {Γ : List Formula} {p : Formula} : Derives Γ .bot → Derives Γ p
  | weaken {Γ Δ : List Formula} {p : Formula} :
      (∀ q, q ∈ Γ → q ∈ Δ) → Derives Γ p → Derives Δ p
  | impI {Γ : List Formula} {p q : Formula} : Derives (p::Γ) q → Derives Γ (.imp p q)
  | impE {Γ : List Formula} {p q : Formula} : Derives Γ (.imp p q) → Derives Γ p → Derives Γ q
  | andI {Γ : List Formula} {p q : Formula} : Derives Γ p → Derives Γ q → Derives Γ (.conj p q)
  | andL {Γ : List Formula} {p q : Formula} : Derives Γ (.conj p q) → Derives Γ p
  | andR {Γ : List Formula} {p q : Formula} : Derives Γ (.conj p q) → Derives Γ q
  | allI {Γ : List Formula} {p : Formula} (x : ℕ) :
      freshNum x Γ = true → Derives Γ p → Derives Γ (.allN x p)
  | allE {Γ : List Formula} {p : Formula} (x : ℕ) (t : Term) :
      p.safe x t = true → Derives Γ (.allN x p) → Derives Γ (p.subst x t)
  | exNI {Γ : List Formula} {p : Formula} (x : ℕ) (t : Term) :
      p.safe x t = true → Derives Γ (p.subst x t) → Derives Γ (.exN x p)
  | allBI {Γ : List Formula} {p : Formula} (x : ℕ) (bound : Term) :
      freshNum x Γ = true → bound.vars.contains x = false →
      Derives (.lt (.var x) bound :: Γ) p → Derives Γ (.allB x bound p)
  | allBE {Γ : List Formula} {p : Formula} (x : ℕ) (bound t : Term) :
      p.safe x t = true → Derives Γ (.allB x bound p) →
      Derives Γ (.lt t bound) → Derives Γ (p.subst x t)
  | exBE {Γ : List Formula} {p q : Formula} (x : ℕ) (bound : Term) :
      freshNum x Γ = true → q.numFree.contains x = false →
      bound.vars.contains x = false → Derives Γ (.exB x bound p) →
      Derives (p :: .lt (.var x) bound :: Γ) q → Derives Γ q
  | exBI {Γ : List Formula} {p : Formula} (x : ℕ) (bound t : Term) :
      p.safe x t = true → Derives Γ (.lt t bound) →
      Derives Γ (p.subst x t) → Derives Γ (.exB x bound p)
  | arithmetic {Γ : List Formula} {t u : Term} : EqProof t u → Derives Γ (.eq t u)
  | eqSymm {Γ : List Formula} {t u : Term} : Derives Γ (.eq t u) → Derives Γ (.eq u t)
  | eqAdd {Γ : List Formula} {t u v w : Term} :
      Derives Γ (.eq t u) → Derives Γ (.eq v w) → Derives Γ (.eq (.add t v) (.add u w))
  | eqMul {Γ : List Formula} {t u v w : Term} :
      Derives Γ (.eq t u) → Derives Γ (.eq v w) → Derives Γ (.eq (.mul t v) (.mul u w))
  | leRefl {Γ : List Formula} (t : Term) : Derives Γ (.le t t)
  | leTrans {Γ : List Formula} {t u v : Term} :
      Derives Γ (.le t u) → Derives Γ (.le u v) → Derives Γ (.le t v)
  | leAdd {Γ : List Formula} {t u v w : Term} :
      Derives Γ (.le t u) → Derives Γ (.le v w) → Derives Γ (.le (.add t v) (.add u w))
  | leRewrite {Γ : List Formula} {t u t' u' : Term} :
      Derives Γ (.eq t t') → Derives Γ (.eq u u') →
      Derives Γ (.le t u) → Derives Γ (.le t' u')
  | ltSucc {Γ : List Formula} (t : Term) : Derives Γ (.lt t (.succ t))
  | ltZeroFalse {Γ : List Formula} (t : Term) : Derives Γ (.imp (.lt t (.lit 0)) .bot)
  | ltTrans {Γ : List Formula} {t u v : Term} :
      Derives Γ (.lt t u) → Derives Γ (.lt u v) → Derives Γ (.lt t v)
  | ltLe {Γ : List Formula} {t u : Term} : Derives Γ (.lt t u) → Derives Γ (.le t u)
  | ltRewrite {Γ : List Formula} {t u t' u' : Term} :
      Derives Γ (.eq t t') → Derives Γ (.eq u u') →
      Derives Γ (.lt t u) → Derives Γ (.lt t' u')
  | sigma1Induction {Γ : List Formula} {p : Formula} (x : ℕ) :
      Sigma1 p → freshNum x Γ = true →
      p.safe x (.lit 0) = true → p.safe x (.succ (.var x)) = true →
      Derives Γ (p.subst x (.lit 0)) →
      Derives Γ (.allN x (.imp p (p.subst x (.succ (.var x))))) →
      Derives Γ (.allN x p)
  | delta1Comprehension {Γ : List Formula} {p q : Formula} (x g : ℕ) :
      Sigma1 p → Pi1 q → freshSet g Γ = true →
      p.setFree.contains g = false → q.setFree.contains g = false →
      Derives Γ (.allN x (iffF p q)) →
      Derives Γ (.exS g (.allN x (iffF (.member (.var x) g) p)))

def addLeft {Γ : List Formula} {t u : Term} (r : Term)
    (h : Derives Γ (.le t u)) : Derives Γ (.le (.add r t) (.add r u)) :=
  .leAdd (.leRefl r) h

def mulSuccLeft (n : ℕ) (t : Term) :
    EqProof (.mul (.lit (n+1)) t) (.add (.mul (.lit n) t) t) :=
  .trans (.mulComm _ _) (.trans (.mul (.refl _) (.literalSucc n))
    (.trans (.mulSucc _ _) (.add (.mulComm _ _) (.refl _))))

/-- Multiplication by a numeral is obtained by finite recursion on proof trees,
using addition monotonicity. It is NOT a new multiplication-order axiom. -/
def scale {Γ : List Formula} {t u : Term} (h : Derives Γ (.le t u)) :
    (n : ℕ) → Derives Γ (.le (.mul (.lit n) t) (.mul (.lit n) u))
  | 0 => .leRewrite
      (.arithmetic (.symm (.trans (.mulComm _ _) (.mulZero _))))
      (.arithmetic (.symm (.trans (.mulComm _ _) (.mulZero _)))) (.leRefl (.lit 0))
  | n+1 => .leRewrite (.arithmetic (.symm (mulSuccLeft n t)))
      (.arithmetic (.symm (mulSuccLeft n u))) (.leAdd (scale h n) h)

def invariant (u d : Term) : Formula :=
  .le (.add (.mul (.lit 3) u) (.lit 2)) (.mul (.lit 2) d)

def successorLeftEq (u b : Term) :
    EqProof (.add (.mul (.lit 3) (.add (.mul (.lit 4) u) (.mul (.lit 2) b))) (.lit 2))
      (.add (.mul (.lit 12) u) (.add (.mul (.lit 6) b) (.lit 2))) :=
  .trans (.add (.trans (.distrib _ _ _)
    (.add (coefficientProduct 3 4 u) (coefficientProduct 3 2 b))) (.refl _))
    (.addAssoc _ _ _)

def scaledInvariantEq (u : Term) :
    EqProof (.mul (.lit 4) (.add (.mul (.lit 3) u) (.lit 2)))
      (.add (.mul (.lit 12) u) (.lit 8)) :=
  .trans (.distrib _ _ _) (.add (coefficientProduct 4 3 u) (numeralMul 4 2))

/-- The actual M04 successor proof reconstructed in raw arithmetic syntax. -/
def successorDerivation {Γ : List Formula} (u d b : Term)
    (hi : Derives Γ (invariant u d)) (hb : Derives Γ (.le b (.lit 1))) :
    Derives Γ (invariant (.add (.mul (.lit 4) u) (.mul (.lit 2) b)) (.mul (.lit 4) d)) := by
  have h₁ : Derives Γ (.le (.add (.mul (.lit 12) u) (.lit 8)) (.mul (.lit 8) d)) :=
    .leRewrite (.arithmetic (scaledInvariantEq u))
      (.arithmetic (coefficientProduct 4 2 d)) (scale hi 4)
  have h₂ : Derives Γ (.le (.add (.mul (.lit 6) b) (.lit 2)) (.lit 8)) :=
    .leRewrite (.arithmetic (.addComm _ _))
      (.arithmetic (.trans (.add (.refl _) (numeralMul 6 1)) (numeralAdd 2 6)))
      (addLeft (.lit 2) (scale hb 6))
  exact .leRewrite (.arithmetic (.symm (successorLeftEq u b)))
    (.arithmetic (.symm (coefficientProduct 2 4 d)))
    (.leTrans (addLeft (.mul (.lit 12) u) h₂) h₁)

def baseDerivation {Γ : List Formula} : Derives Γ (invariant (.lit 0) (.lit 1)) :=
  .leRewrite
    (.arithmetic (.symm (.trans (.add (numeralMul 3 0) (.refl _)) (numeralAdd 0 2))))
    (.arithmetic (.symm (numeralMul 2 1))) (.leRefl (.lit 2))

structure RuleProfile where
  nodes : ℕ := 0
  hypothesisLeaves : ℕ := 0
  arithmeticPackets : ℕ := 0
  sigma1Instances : ℕ := 0
  delta1Instances : ℕ := 0
  deriving Repr

def RuleProfile.combine (p q : RuleProfile) : RuleProfile :=
  ⟨p.nodes+q.nodes, p.hypothesisLeaves+q.hypothesisLeaves,
    p.arithmeticPackets+q.arithmeticPackets, p.sigma1Instances+q.sigma1Instances,
    p.delta1Instances+q.delta1Instances⟩

def RuleProfile.node (p : RuleProfile) : RuleProfile := {p with nodes := p.nodes+1}

/-- Reproducible traversal of ACTUAL proof objects: records theory-schema
uses rather than mistaking a Lean axiom inventory for an RCA₀ axiom inventory. -/
def ruleProfile {Γ : List Formula} {p : Formula} : Derives Γ p → RuleProfile
  | .hypothesis _ => ⟨1,1,0,0,0⟩
  | .botE h | .weaken _ h | .impI h | .andL h | .andR h | .ltLe h => (ruleProfile h).node
  | .impE h k | .andI h k => ((ruleProfile h).combine (ruleProfile k)).node
  | .allI _ _ h | .allE _ _ _ h | .exNI _ _ _ h | .allBI _ _ _ _ h => (ruleProfile h).node
  | .allBE _ _ _ _ h k | .exBE _ _ _ _ _ h k | .exBI _ _ _ _ h k =>
      ((ruleProfile h).combine (ruleProfile k)).node
  | .arithmetic _ => ⟨1,0,1,0,0⟩
  | .eqSymm h => (ruleProfile h).node
  | .eqAdd h k | .eqMul h k | .leTrans h k | .leAdd h k | .ltTrans h k =>
      ((ruleProfile h).combine (ruleProfile k)).node
  | .leRefl _ | .ltSucc _ | .ltZeroFalse _ => ⟨1,0,0,0,0⟩
  | .leRewrite h k l | .ltRewrite h k l =>
      (((ruleProfile h).combine (ruleProfile k)).combine (ruleProfile l)).node
  | .sigma1Induction _ _ _ _ _ h k =>
      let p := ((ruleProfile h).combine (ruleProfile k)).node
      {p with sigma1Instances := p.sigma1Instances+1}
  | .delta1Comprehension _ _ _ _ _ _ _ h =>
      let p := (ruleProfile h).node
      {p with delta1Instances := p.delta1Instances+1}

#print axioms numeralAdd
#print axioms numeralMul
#print axioms scale
#print axioms successorDerivation
#print axioms baseDerivation

end MatematicaAbierta.Continuo.CalculoRCA
