import MatematicaAbierta.Continuo.AritmeticaModularInternaRCA

/-! M07 / H04-04.c/d. Exact numeric extension GOAL, not an axiom/theorem.
The only proof terms here discharge the bound obligation. H04-03 bit graph
admissibility remains an explicit antecedent. No CRT/code existence rule. -/
namespace MatematicaAbierta.Continuo.ContratoExtensionBetaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA

def nextU (u bit : Term) : Term := .add (.mul (.lit 4) u) (.mul (.lit 2) bit)
def nextD (d : Term) : Term := .mul (.lit 4) d
def boundCandidate (t : Term) : Term := .succ (.add (.mul (.lit 4) t) (.lit 2))

def oldBoundBelow {Γ : List Formula} (t : Term) : Proof Γ (.lt t (boundCandidate t)) := by
  have hOneFour : Proof Γ (.le (.lit 1) (.lit 4)) :=
    .leRewrite (eqRefl _) (ax (numeralAdd 1 3)) (leRightAdd (.lit 1) (.lit 3))
  have hFour : Proof Γ (.le t (.mul (.lit 4) t)) :=
    .leRewrite (ax (mulOneLeft t)) (eqRefl _) (.leMulRight t hOneFour)
  exact leThenSucc (.leTrans hFour (leRightAdd (.mul (.lit 4) t) (.lit 2)))

def nextUBound {Γ : List Formula} (u bit t : Term)
    (hu : Proof Γ (.lt u t)) (hb : Proof Γ (.le bit (.lit 1))) :
    Proof Γ (.lt (nextU u bit) (boundCandidate t)) := by
  have hbit : Proof Γ (.le (.mul (.lit 2) bit) (.lit 2)) :=
    .leRewrite (eqRefl _) (ax (numeralMul 2 1)) (leMulLeft (.lit 2) hb)
  exact leThenSucc (.leAdd (leMulLeft (.lit 4) (.ltLe hu)) hbit)

def nextDBound {Γ : List Formula} (d t : Term) (hd : Proof Γ (.lt d t)) :
    Proof Γ (.lt (nextD d) (boundCandidate t)) :=
  leThenSucc (.leTrans (leMulLeft (.lit 4) (.ltLe hd))
    (leRightAdd (.mul (.lit 4) t) (.lit 2)))

def boundsContext : List Formula :=
  [.le (.var 7) (.lit 1), .lt (.var 2) (.var 4), .lt (.var 1) (.var 4)]
def boundsConclusion : Formula := .conj (.lt (.var 4) (boundCandidate (.var 4)))
  (.conj (.lt (nextU (.var 1) (.var 7)) (boundCandidate (.var 4)))
    (.lt (nextD (.var 2)) (boundCandidate (.var 4))))
def boundsOpen : Proof boundsContext boundsConclusion :=
  .andI (oldBoundBelow _) (.andI (nextUBound _ _ _ (push (push hyp)) hyp)
    (nextDBound _ _ (push hyp)))
def boundsClosed : Proof []
    (.allN 1 (.allN 2 (.allN 4 (.allN 7
      (.imp (.lt (.var 1) (.var 4)) (.imp (.lt (.var 2) (.var 4))
        (.imp (.le (.var 7) (.lit 1)) boundsConclusion))))))) :=
  .allI 1 rfl (.allI 2 rfl (.allI 4 rfl (.allI 7 rfl (.impI (.impI (.impI boundsOpen))))))

/-- H04-03 dependency: B is set 2, with an admissible bit at K. Its totality,
uniqueness and construction are NOT discharged by this formula. -/
def admissibleBit : Formula := .conj (gb (.var 3) (.var 7)) (.le (.var 7) (.lit 1))
def extensionInput : Formula := .conj finiteTraceMatrix
  (.conj (.lt (.var 1) (.var 4)) (.conj (.lt (.var 2) (.var 4))
    (.conj (beta (.var 8) (.var 9) (.var 3) (.var 1))
      (.conj (beta (.var 10) (.var 11) (.var 3) (.var 2)) admissibleBit))))

def preserves (oldA oldB newA newB : Term) : Formula :=
  .allB 20 (.succ (.var 3)) (.allB 21 (.var 4)
    (.imp (beta oldA oldB (.var 20) (.var 21))
      (beta newA newB (.var 20) (.var 21))))

def extendedTrace : Formula :=
  let p := finiteTraceMatrix.subst 3 (.succ (.var 3))
  let p := p.subst 4 (.var 24)
  let p := p.subst 8 (.var 22)
  let p := p.subst 9 (.var 23)
  let p := p.subst 10 (.var 25)
  p.subst 11 (.var 26)
def extensionBody : Formula := .conj (.lt (.var 4) (.var 24))
  (.conj (preserves (.var 8) (.var 9) (.var 22) (.var 23))
    (.conj (preserves (.var 10) (.var 11) (.var 25) (.var 26))
      (.conj (beta (.var 22) (.var 23) (.succ (.var 3)) (nextU (.var 1) (.var 7)))
        (.conj (beta (.var 25) (.var 26) (.succ (.var 3)) (nextD (.var 2))) extendedTrace))))
def extensionExists : Formula := .exN 24 (.exN 22 (.exN 23 (.exN 25 (.exN 26 extensionBody))))
/-- This is only the exact goal. There is intentionally NO Proof of it. -/
def numericExtensionContract : Formula :=
  [3,4,8,9,10,11,1,2,7].foldr Formula.allN (.imp extensionInput extensionExists)
def extensionExistsSigma1 : Sigma1 extensionExists :=
  .exists 24 (.exists 22 (.exists 23 (.exists 25 (.exists 26 (.bounded (by decide))))))

example : extensionInput.bounded = true := by decide
example : extensionBody.bounded = true := by decide
example : numericExtensionContract.numFree = [] := by decide
example : numericExtensionContract.setFree = [2,2,2] := by decide
example : finiteTraceMatrix.safe 3 (.succ (.var 3)) = true := by decide
example : finiteTraceMatrix.safe 4 (.var 24) = true := by decide
example : finiteTraceMatrix.safe 8 (.var 22) = true := by decide
example : finiteTraceMatrix.safe 9 (.var 23) = true := by decide
example : finiteTraceMatrix.safe 10 (.var 25) = true := by decide
example : finiteTraceMatrix.safe 11 (.var 26) = true := by decide
example : extensionBody.numFree.contains 12 = false := by decide
example : extensionBody.numFree.contains 20 = false := by decide
example : extensionBody.numFree.contains 21 = false := by decide

#print axioms oldBoundBelow
#print axioms nextUBound
#print axioms nextDBound
#print axioms boundsClosed
#print axioms extensionExistsSigma1
#eval ("extension_bound", profile boundsClosed)
end MatematicaAbierta.Continuo.ContratoExtensionBetaRCA
