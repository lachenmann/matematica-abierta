import MatematicaAbierta.Continuo.CalculoOrdenRCA
import MatematicaAbierta.Continuo.TrazasInduccionRCA

/-! H04-04.f: polynomial pairing projection bounds and injectivity, as
INTERNAL proof programs. All square/separation facts below are derived;
the calculus has no pairing/square-growth/injectivity axiom. -/
namespace MatematicaAbierta.Continuo.EmparejamientoInternoRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA

def square (s : Term) : Term := .mul s s
def successorSquare (s : Term) :
    EqProof (square (.succ s)) (.add (.add (square s) s) (.succ s)) :=
  .trans (mulSuccessorLeft s (.succ s)) (.add (.mulSucc s s) (.refl _))

def squareMonotone {Γ : List Formula} {s t : Term} (h : Proof Γ (.le s t)) :
    Proof Γ (.le (square s) (square t)) :=
  .leTrans (.leMulRight s h) (leMulLeft t h)

def squareDominates {Γ : List Formula} (s : Term) : Proof Γ (.le s (square s)) := by
  apply Proof.orderCases (.lit 0) s
  · have h₁ : Proof (.lt (.lit 0) s :: Γ) (.le (.lit 1) s) :=
      .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (.ltSuccLe hyp)
    exact .leRewrite (ax (mulOneLeft s)) (eqRefl _) (.leMulRight s h₁)
  · have hsq : Proof (.eq (.lit 0) s :: Γ) (.eq (square s) (.lit 0)) :=
      .eqTrans (.eqMul (.eqSymm hyp) (.eqSymm hyp)) (ax (numeralMul 0 0))
    exact .leRewrite hyp (.eqSymm hsq) (leRefl (.lit 0))
  · exact .botE (.impE (.embed (.ltZeroFalse s)) hyp)

def firstProjection {Γ : List Formula} (k v : Term) : Proof Γ (.le k (pair k v)) :=
  leLeftAdd k (square (.add k v))
def secondProjection {Γ : List Formula} (k v : Term) : Proof Γ (.le v (pair k v)) :=
  .leTrans (.leTrans (leLeftAdd v k) (squareDominates (.add k v)))
    (leRightAdd (square (.add k v)) k)
def firstProjectionBound {Γ : List Formula} (k v : Term) : Proof Γ (.lt k (.succ (pair k v))) :=
  leThenSucc (firstProjection k v)
def secondProjectionBound {Γ : List Formula} (k v : Term) : Proof Γ (.lt v (.succ (pair k v))) :=
  leThenSucc (secondProjection k v)

def pairSeparated {Γ : List Formula} (k v l w : Term)
    (h : Proof Γ (.lt (.add k v) (.add l w))) : Proof Γ (.lt (pair k v) (pair l w)) := by
  let s := Term.add k v
  let t := Term.add l w
  have h₁ : Proof Γ (.le (pair k v) (.add (square s) s)) :=
    leAddLeft (square s) (leRightAdd k v)
  have hpos : Proof Γ (.lt (.lit 0) (.succ s)) := .leLtTrans (.zeroLe s) (ltSucc s)
  have h₂ : Proof Γ (.lt (.add (square s) s) (square (.succ s))) :=
    .ltRewrite (ax (.addZero _)) (ax (.symm (successorSquare s)))
      (ltAddLeft (.add (square s) s) hpos)
  have h₃ := squareMonotone (.ltSuccLe h)
  exact .ltLeTrans (.ltLeTrans (.leLtTrans h₁ h₂) h₃) (leRightAdd (square t) l)

def pairInjectiveOpen {Γ : List Formula} (k v l w : Term)
    (hp : Proof Γ (.eq (pair k v) (pair l w))) :
    Proof Γ (.conj (.eq k l) (.eq v w)) := by
  apply Proof.orderCases (.add k v) (.add l w)
  · exact .botE (.ltIrrefl (.ltRewrite (push hp) (eqRefl _) (pairSeparated k v l w hyp)))
  · have hsq : Proof (.eq (.add k v) (.add l w) :: Γ)
        (.eq (square (.add k v)) (square (.add l w))) := Proof.eqMul hyp hyp
    have hk : Proof (.eq (.add k v) (.add l w) :: Γ) (.eq k l) :=
      .addCancelLeft (square (.add l w))
        (.eqTrans (.eqSymm (.eqAdd hsq (eqRefl k))) (push hp))
    have hv : Proof (.eq (.add k v) (.add l w) :: Γ) (.eq v w) :=
      .addCancelLeft l (.eqTrans (.eqSymm (.eqAdd hk (eqRefl v))) hyp)
    exact .andI hk hv
  · exact .botE (.ltIrrefl (.ltRewrite (.eqSymm (push hp)) (eqRefl _) (pairSeparated l w k v hyp)))

def pairInjectiveFormula : Formula :=
  .allN 0 (.allN 1 (.allN 5 (.allN 6
    (.imp (.eq (pair (.var 0) (.var 1)) (pair (.var 5) (.var 6)))
      (.conj (.eq (.var 0) (.var 5)) (.eq (.var 1) (.var 6)))))))
def pairInjective : Proof [] pairInjectiveFormula :=
  .allI 0 rfl (.allI 1 rfl (.allI 5 rfl (.allI 6 rfl
    (.impI (pairInjectiveOpen (.var 0) (.var 1) (.var 5) (.var 6) hyp)))))
def projections : Proof []
    (.allN 0 (.allN 1 (.conj
      (.lt (.var 0) (.succ (pair (.var 0) (.var 1))))
      (.lt (.var 1) (.succ (pair (.var 0) (.var 1))))))) :=
  .allI 0 rfl (.allI 1 rfl (.andI (firstProjectionBound (.var 0) (.var 1))
    (secondProjectionBound (.var 0) (.var 1))))

#print axioms squareDominates
#print axioms projections
#print axioms pairInjective
#eval ("pair_injective", profile pairInjective)
#eval ("pair_projections", profile projections)
end MatematicaAbierta.Continuo.EmparejamientoInternoRCA
