import MatematicaAbierta.Continuo.CoprimalidadPositivaRCA

/-! M08 C08/C09: TWO prescribed beta readings, with the inverse certificate
DERIVED and eliminated. No inverse/coprimality/CRT premise remains. Gap and
positive divisibility of b remain explicit. This is not finite-list coding. -/
namespace MatematicaAbierta.Continuo.CRTDosModulosBetaRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA TrazasInduccionRCA DivisionInternaRCA
open IdentidadModulosBetaRCA CRTConstructivoDosRCA

def input : Formula := .conj (.eq (.var 1) (.add (.var 0) (.var 2)))
  (.conj (.eq (.var 4) (.mul (.var 2) (.var 3)))
    (.conj (.lt (.lit 0) (.var 2)) (.conj (.lt (.lit 0) (.var 3))
      (.conj (.lt (.var 24) (modulus (.var 0) (.var 4)))
        (.lt (.var 25) (modulus (.var 1) (.var 4)))))))
def majorant : Term := .succ (.add qCandidate hbTerm)
def specialUpper (ell : Term) : Term := .add (.var 24)
  (.mul (.mul ell (.add (.var 24) (modulus (.var 1) (.var 4)))) (modulus (.var 0) (.var 4)))
def result : Formula := .exB 28 (.succ (specialUpper majorant))
  (.conj (beta (.var 28) (.var 4) (.var 0) (.var 24))
    (beta (.var 28) (.var 4) (.var 1) (.var 25)))

def inverseFromInput : Proof [input] conclusion := by
  have h0 := Proof.allE 0 (.var 0) (by decide) positiveInverse
  have h1 := Proof.allE 1 (.var 1) (by decide) h0
  have h2 := Proof.allE 2 (.var 2) (by decide) h1
  have h3 := Proof.allE 3 (.var 3) (by decide) h2
  have h4 := Proof.allE 4 (.var 4) (by decide) h3
  exact .impE (.impE (.impE (.impE (SelectoresInternosRCA.closed h4)
    (.andL (.andR (.andR (.andR hyp))))) (.andL (.andR (.andR hyp))))
    (.andL (.andR hyp))) (.andL hyp)

def inverseContext : List Formula :=
  [.conj (.lt (.lit 0) (.var 32))
     (.eq (.mul (.var 32) (modulus (.var 1) (.var 4)))
       (.add (.lit 1) (.mul (.var 33) (modulus (.var 0) (.var 4))))),
   .lt (.var 33) majorant,
   .exB 23 majorant
     (.conj (.lt (.lit 0) (.var 32))
       (.eq (.mul (.var 32) (modulus (.var 1) (.var 4)))
         (.add (.lit 1) (.mul (.var 23) (modulus (.var 0) (.var 4)))))),
   .lt (.var 32) (.succ qCandidate), input]

def crtFromInverse : Proof inverseContext
    (.exB 28 (.succ (specialUpper (.var 33)))
      (.conj (beta (.var 28) (.var 4) (.var 0) (.var 24))
        (beta (.var 28) (.var 4) (.var 1) (.var 25)))) := by
  have h0 := Proof.allE 20 (modulus (.var 0) (.var 4)) (by decide) crtTwo
  have h1 := Proof.allE 21 (modulus (.var 1) (.var 4)) (by decide) h0
  have h2 := Proof.allE 22 (.var 32) (by decide) h1
  have h3 := Proof.allE 23 (.var 33) (by decide) h2
  have h4 := Proof.allE 24 (.var 24) (by decide) h3
  have h5 := Proof.allE 25 (.var 25) (by decide) h4
  have hinput : Proof inverseContext input := push (push (push (push hyp)))
  have hrs := Proof.andR (.andR (.andR (.andR hinput)))
  exact .impE (.impE (.impE (.impE (.impE (.impE (SelectoresInternosRCA.closed h5)
    (modulusPositive (.var 0) (.var 4))) (modulusPositive (.var 1) (.var 4)))
    (.andL hyp)) (.andR hrs)) (.andL hrs)) (.andR hyp)

def eliminateCode : Proof inverseContext result := by
  have hupper : Proof inverseContext
      (.le (specialUpper (.var 33)) (specialUpper majorant)) :=
    leAddLeft (.var 24) (.leMulRight (modulus (.var 0) (.var 4))
      (.leMulRight (.add (.var 24) (modulus (.var 1) (.var 4))) (.ltLe (push hyp))))
  apply Proof.exBErename 28 34 (.succ (specialUpper (.var 33)))
    (by decide) (by decide) (by decide) (by decide) crtFromInverse
  apply Proof.exBI 28 (.succ (specialUpper majorant)) (.var 34) (by decide)
    (.ltLeTrans (push hyp) (succLe (push (push hupper))))
  exact hyp

def specialOpen : Proof [input] result := by
  apply Proof.exBErename 22 32 (.succ qCandidate) (by decide) (by decide) (by decide)
    (by decide) inverseFromInput
  apply Proof.exBErename 23 33 majorant (by decide) (by decide) (by decide) (by decide) hyp
  exact eliminateCode

/-- r,s are bound FIRST so substituting c,b depending on r,s cannot capture them. -/
def specialCRTFormula : Formula := [24,25,0,1,2,3,4].foldr Formula.allN (.imp input result)
def specialCRT : Proof [] specialCRTFormula := by
  apply Proof.allI 24 rfl
  apply Proof.allI 25 rfl
  apply Proof.allI 0 rfl
  apply Proof.allI 1 rfl
  apply Proof.allI 2 rfl
  apply Proof.allI 3 rfl
  apply Proof.allI 4 rfl
  exact .impI specialOpen

example : result.bounded = true := by decide
example : result.numFree.contains 32 = false := by decide
example : result.numFree.contains 33 = false := by decide
example : result.numFree.contains 34 = false := by decide
example : specialCRTFormula.numFree = [] := by decide
#print axioms crtFromInverse
#print axioms specialCRT
#eval ("crt_two_special_beta_no_inverse_premise", profile specialCRT)
end MatematicaAbierta.Continuo.CRTDosModulosBetaRCA
