import MatematicaAbierta.Continuo.CRTDosModulosBetaRCA

/-! M08 C07 (pair case), C09: explicit NEW b'=delta*(L+1) and a code for
two arbitrary prescribed readings. No uniform finite-list coding premise.
The full finite common-multiple goal is classified only, NOT proved. -/
namespace MatematicaAbierta.Continuo.ParametroParBetaRCA
open CalculoRCA CalculoOrdenRCA DivisionInternaRCA LecturasBetaRCA TrazasInduccionRCA
open DiferenciasInternasRCA CoprimalidadPositivaRCA CRTDosModulosBetaRCA

def parameter (delta limit : Term) : Term := .mul delta (.succ limit)
def parameterLarge {Γ : List Formula} (delta limit : Term)
    (hdelta : Proof Γ (.lt (.lit 0) delta)) : Proof Γ (.lt limit (parameter delta limit)) :=
  .succLeLt (.leRewrite (ax (mulOneLeft (.succ limit))) (eqRefl _)
    (.leMulRight (.succ limit)
      (.leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (.ltSuccLe hdelta))))

def parameterReadingBound {Γ : List Formula} (i delta limit r : Term)
    (hdelta : Proof Γ (.lt (.lit 0) delta)) (hr : Proof Γ (.le r limit)) :
    Proof Γ (.lt r (modulus i (parameter delta limit))) := by
  have hi : Proof Γ (.lt (.lit 0) (.add i (.lit 1))) :=
    .ltRewrite (eqRefl _) (ax (.symm (addOne i))) (.leLtTrans (.zeroLe i) (ltSucc i))
  have hOne : Proof Γ (.le (.lit 1) (.add i (.lit 1))) :=
    .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (.ltSuccLe hi)
  have hscale : Proof Γ (.le (parameter delta limit)
      (.mul (.add i (.lit 1)) (parameter delta limit))) :=
    .leRewrite (ax (mulOneLeft _)) (eqRefl _) (.leMulRight (parameter delta limit) hOne)
  exact .ltTrans (.ltLeTrans (.leLtTrans hr (parameterLarge delta limit hdelta)) hscale)
    (oneAddPositive _)

def limit : Term := .add (.var 24) (.var 25)
def newB : Term := parameter (.var 2) limit
def newC : Term := .succ limit
def pairInput : Formula := .conj (.eq (.var 1) (.add (.var 0) (.var 2))) (.lt (.lit 0) (.var 2))
def instantiatedInput : Formula := (input.subst 3 newC).subst 4 newB
def pairResult : Formula := (result.subst 3 newC).subst 4 newB

def constructInput : Proof [pairInput] instantiatedInput :=
  .andI (.andL hyp) (.andI (eqRefl newB)
    (.andI (.andR hyp) (.andI (.leLtTrans (.zeroLe limit) (ltSucc limit))
      (.andI (parameterReadingBound (.var 0) (.var 2) limit (.var 24) (.andR hyp)
        (leRightAdd (.var 24) (.var 25)))
        (parameterReadingBound (.var 1) (.var 2) limit (.var 25) (.andR hyp)
          (leLeftAdd (.var 25) (.var 24)))))))

def pairOpen : Proof [pairInput] pairResult := by
  -- r,s first: substituting c'=r+s+1 or b' depending on r,s is capture-safe.
  have h0 := Proof.allE 24 (.var 24) (by decide) specialCRT
  have h1 := Proof.allE 25 (.var 25) (by decide) h0
  have h2 := Proof.allE 0 (.var 0) (by decide) h1
  have h3 := Proof.allE 1 (.var 1) (by decide) h2
  have h4 := Proof.allE 2 (.var 2) (by decide) h3
  have h5 := Proof.allE 3 newC (by decide) h4
  have h6 := Proof.allE 4 newB (by decide) h5
  exact .impE (SelectoresInternosRCA.closed h6) constructInput

def pairFormula : Formula := [24,25,0,1,2].foldr Formula.allN (.imp pairInput pairResult)
/-- Two arbitrary values r,s, gap delta>0: an explicit b' and a bounded a
satisfying beta(a,b',i,r) and beta(a,b',j,s). No inverse premise remains. -/
def pairCode : Proof [] pairFormula := by
  apply Proof.allI 24 rfl
  apply Proof.allI 25 rfl
  apply Proof.allI 0 rfl
  apply Proof.allI 1 rfl
  apply Proof.allI 2 rfl
  exact .impI pairOpen

def orderedResult : Formula := .exB 2 (.succ (.var 1)) pairResult
def orderedOpen : Proof [.lt (.var 0) (.var 1)] orderedResult := by
  have h0 := Proof.allE 20 (.var 0) (by decide) gapFromOrder
  have h1 := Proof.allE 21 (.var 1) (by decide) h0
  have hg : Proof [.lt (.var 0) (.var 1)]
      (.exB 2 (.succ (.var 1))
        (.conj (.eq (.var 1) (.add (.var 0) (.var 2))) (.lt (.lit 0) (.var 2)))) :=
    .impE (SelectoresInternosRCA.closed h1) hyp
  apply Proof.exBErename 2 26 (.succ (.var 1)) (by decide) (by decide) (by decide) (by decide) hg
  apply Proof.exBI 2 (.succ (.var 1)) (.var 26) (by decide) (push hyp)
  have p0 := Proof.allE 24 (.var 24) (by decide) pairCode
  have p1 := Proof.allE 25 (.var 25) (by decide) p0
  have p2 := Proof.allE 0 (.var 0) (by decide) p1
  have p3 := Proof.allE 1 (.var 1) (by decide) p2
  have p4 := Proof.allE 2 (.var 26) (by decide) p3
  exact .impE (SelectoresInternosRCA.closed p4) hyp
def pairCodeFromOrder : Proof []
    (.allN 24 (.allN 25 (.allN 0 (.allN 1 (.imp (.lt (.var 0) (.var 1)) orderedResult))))) :=
  .allI 24 rfl (.allI 25 rfl (.allI 0 rfl (.allI 1 rfl (.impI orderedOpen))))

/-- Uniform common-multiple induction target for all differences <=K.
There is deliberately NO Proof of this exN formula in M08. -/
def commonMultipleMatrix : Formula := .conj (.lt (.lit 0) (.var 30))
  (.allB 16 (.succ (.var 3))
    (.imp (.lt (.lit 0) (.var 16))
      (.exB 17 (.succ (.var 30)) (.eq (.var 30) (.mul (.var 16) (.var 17))))))
def commonMultipleExists : Formula := .exN 30 commonMultipleMatrix
def commonMultipleSigma1 : Sigma1 commonMultipleExists := .exists 30 (.bounded (by decide))

example : pairFormula.numFree = [] := by decide
example : pairFormula.setFree = [] := by decide
example : pairResult.bounded = true := by decide
example : result.safe 3 newC = true := by decide
example : result.safe 4 newB = true := by decide
example : commonMultipleMatrix.bounded = true := by decide
example : orderedResult.bounded = true := by decide
example : orderedResult.numFree.contains 26 = false := by decide
#print axioms parameterLarge
#print axioms parameterReadingBound
#print axioms pairCode
#print axioms pairCodeFromOrder
#print axioms commonMultipleSigma1
#eval ("two_readings_explicit_new_parameter", profile pairCode)
#eval ("two_readings_from_strict_order", profile pairCodeFromOrder)
end MatematicaAbierta.Continuo.ParametroParBetaRCA
