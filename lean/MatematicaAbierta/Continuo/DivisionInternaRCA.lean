import MatematicaAbierta.Continuo.LecturasBetaRCA

/-! M07 / H04-04.c: Euclidean division as a finite INTERNAL proof tree.
No new calculus constructors, arithmetic axioms, total-function symbols or
ambient Nat division lemmas. The induction matrix is bounded. This does NOT
prove finite CRT or numeric beta-code extension. -/
namespace MatematicaAbierta.Continuo.DivisionInternaRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA

def addOne (t : Term) : EqProof (.add t (.lit 1)) (.succ t) :=
  .trans (.add (.refl _) (.literalSucc 0))
    (.trans (.addSucc _ _) (.succ (.addZero _)))

def succEq {Γ : List Formula} {t u : Term} (h : Proof Γ (.eq t u)) :
    Proof Γ (.eq (.succ t) (.succ u)) :=
  .eqTrans (ax (.symm (addOne t))) (.eqTrans (.eqAdd h (eqRefl _)) (ax (addOne u)))

def succLe {Γ : List Formula} {t u : Term} (h : Proof Γ (.le t u)) :
    Proof Γ (.le (.succ t) (.succ u)) :=
  .leRewrite (ax (addOne t)) (ax (addOne u)) (.leAdd h (leRefl _))

def succLt {Γ : List Formula} {t u : Term} (h : Proof Γ (.lt t u)) :
    Proof Γ (.lt (.succ t) (.succ u)) :=
  .ltRewrite (ax (addOne t)) (ax (addOne u)) (.ltAddRight (.lit 1) h)

/-- q,r < n+1, r<m, n=q*m+r. The names 14,15 are bound. -/
def division (n m : Term) : Formula :=
  .exB 14 (.succ n) (.exB 15 (.succ n)
    (.conj (.lt (.var 15) m) (.eq n (.add (.mul (.var 14) m) (.var 15)))))

def modulusHyp : Formula := .lt (.lit 0) (.var 9)
def divisionMatrix : Formula := division (.var 0) (.var 9)

def divisionBase : Proof [modulusHyp] (division (.lit 0) (.var 9)) := by
  apply Proof.exBI 14 (.succ (.lit 0)) (.lit 0) (by decide) (ltSucc _)
  apply Proof.exBI 15 (.succ (.lit 0)) (.lit 0) (by decide) (ltSucc _)
  apply Proof.andI hyp
  exact ax (.symm (.trans (.addZero _) (.trans (.mulComm _ _) (.mulZero _))))

def witnessContext : List Formula :=
  [.conj (.lt (.var 15) (.var 9))
     (.eq (.var 0) (.add (.mul (.var 14) (.var 9)) (.var 15))),
   .lt (.var 15) (.succ (.var 0)),
   .exB 15 (.succ (.var 0))
     (.conj (.lt (.var 15) (.var 9))
       (.eq (.var 0) (.add (.mul (.var 14) (.var 9)) (.var 15)))),
   .lt (.var 14) (.succ (.var 0)), divisionMatrix, modulusHyp]

def divisionIncrement : Proof witnessContext (division (.succ (.var 0)) (.var 9)) := by
  have hr : Proof witnessContext (.lt (.var 15) (.var 9)) := .andL hyp
  have he : Proof witnessContext
      (.eq (.var 0) (.add (.mul (.var 14) (.var 9)) (.var 15))) := .andR hyp
  have hqBound : Proof witnessContext (.lt (.var 14) (.succ (.var 0))) :=
    push (push (push hyp))
  have hrBound : Proof witnessContext (.lt (.var 15) (.succ (.var 0))) := push hyp
  have hm : Proof witnessContext modulusHyp := push (push (push (push (push hyp))))
  apply Proof.orderCases (.succ (.var 15)) (.var 9)
  · apply Proof.exBI 14 (.succ (.succ (.var 0))) (.var 14) (by decide)
      (.ltTrans (push hqBound) (ltSucc _))
    apply Proof.exBI 15 (.succ (.succ (.var 0))) (.succ (.var 15)) (by decide)
      (succLt (push hrBound))
    exact .andI hyp (.eqTrans (succEq (push he)) (ax (.symm (.addSucc _ _))))
  · apply Proof.exBI 14 (.succ (.succ (.var 0))) (.succ (.var 14)) (by decide)
      (succLt (push hqBound))
    apply Proof.exBI 15 (.succ (.succ (.var 0))) (.lit 0) (by decide)
      (.leLtTrans (.zeroLe _) (ltSucc _))
    apply Proof.andI (push hm)
    have h₁ : Proof (.eq (.succ (.var 15)) (.var 9) :: witnessContext)
        (.eq (.succ (.var 0)) (.add (.mul (.var 14) (.var 9)) (.succ (.var 15)))) :=
      .eqTrans (succEq (push he)) (ax (.symm (.addSucc _ _)))
    have h₂ := Proof.eqAdd (eqRefl (.mul (.var 14) (.var 9)))
      (hyp : Proof (.eq (.succ (.var 15)) (.var 9) :: witnessContext)
        (.eq (.succ (.var 15)) (.var 9)))
    exact .eqTrans (.eqTrans h₁ h₂)
      (ax (.symm (.trans (.addZero _) (mulSuccessorLeft _ _))))
  · exact .botE (.ltIrrefl (.ltLeTrans hyp (.ltSuccLe (push hr))))

def divisionStep : Proof [modulusHyp]
    (.allN 0 (.imp divisionMatrix (division (.succ (.var 0)) (.var 9)))) := by
  apply Proof.allI 0 (by decide)
  apply Proof.impI
  apply Proof.exBE 14 (.succ (.var 0)) (by decide) (by decide) (by decide) hyp
  apply Proof.exBE 15 (.succ (.var 0)) (by decide) (by decide) (by decide) hyp
  exact divisionIncrement

def divisionInduction : Proof [modulusHyp] (.allN 0 divisionMatrix) :=
  .sigma1Induction 0 (.bounded (by decide)) (by decide) (by decide) (by decide)
    divisionBase divisionStep

/-- Closed internal theorem: ∀m (0<m → ∀n ∃q<n+1 ∃r<n+1 (r<m ∧ n=q*m+r)). -/
def euclideanDivision : Proof []
    (.allN 9 (.imp modulusHyp (.allN 0 divisionMatrix))) :=
  .allI 9 rfl (.impI divisionInduction)

example : divisionMatrix.bounded = true := by decide
example : divisionMatrix.safe 0 (.succ (.var 0)) = true := by decide
example : freshNum 0 [modulusHyp] = true := by decide
example : (division (.succ (.var 0)) (.var 9)).numFree.contains 14 = false := by decide
example : (division (.succ (.var 0)) (.var 9)).numFree.contains 15 = false := by decide

#print axioms divisionIncrement
#print axioms divisionStep
#print axioms divisionInduction
#print axioms euclideanDivision
#eval ("division_increment", profile divisionIncrement)
#eval ("euclidean_division", profile euclideanDivision)
end MatematicaAbierta.Continuo.DivisionInternaRCA
