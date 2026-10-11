import MatematicaAbierta.Continuo.CalculoExistencialRCA

/-! M09 C07: actual Sigma1 induction with ordinary unbounded existential
introduction/elimination. Old modules and arithmetic calculus unchanged. -/
namespace MatematicaAbierta.Continuo.MultiploComunUniformeRCA
open CalculoRCA CalculoOrdenRCA DivisionInternaRCA DiferenciasInternasRCA AritmeticaModularInternaRCA
abbrev EProof := CalculoExistencialRCA.Proof

def cm (k m : Term) : Formula := .conj (.lt (.lit 0) m)
  (.allB 16 (.succ k) (.imp (.lt (.lit 0) (.var 16))
    (.exB 17 (.succ m) (.eq m (.mul (.var 16) (.var 17))))))
def K : Term := .var 3
def M : Term := .var 30
def nextM : Term := .mul M (.succ K)
def P : Formula := .exN 30 (cm K M)

def factorBound {Γ : List Formula} (m d q : Term)
    (hd : Proof Γ (.lt (.lit 0) d)) (he : Proof Γ (.eq m (.mul d q))) :
    Proof Γ (.lt q (.succ m)) :=
  quotientBound m q d (.lit 0) hd
    (.eqTrans he (ax (.trans (.mulComm _ _) (.symm (.addZero _)))))

def baseMatrix : Proof [] (cm (.lit 0) (.lit 1)) := by
  apply Proof.andI
  · exact .ltRewrite (eqRefl _) (ax (.symm (.literalSucc 0))) (ltSucc _)
  · apply Proof.allBI 16 (.succ (.lit 0)) rfl rfl
    apply Proof.impI
    have hOne : Proof [.lt (.lit 0) (.var 16), .lt (.var 16) (.succ (.lit 0))]
        (.le (.succ (.lit 0)) (.var 16)) := .ltSuccLe hyp
    exact .botE (.ltIrrefl (.ltLeTrans (push hyp) hOne))

def stepΓ : List Formula := [.lt (.lit 0) (.var 16), .lt (.var 16) (.succ (.succ K)), cm K M]
def stepResidue : Formula := .exB 17 (.succ nextM) (.eq nextM (.mul (.var 16) (.var 17)))

def stepCases : Proof stepΓ stepResidue := by
  apply Proof.orderCases (.var 16) (.succ K)
  · have old : Proof (.lt (.var 16) (.succ K)::stepΓ)
        (.exB 17 (.succ M) (.eq M (.mul (.var 16) (.var 17)))) :=
      .impE (.allBE 16 (.succ K) (.var 16) (by decide)
        (.andR (push (push (push hyp)))) hyp) (push hyp)
    apply Proof.exBErename 17 31 (.succ M) (by decide) (by decide) (by decide) (by decide) old
    have he : Proof (Formula.eq M (.mul (.var 16) (.var 31)) ::
        .lt (.var 31) (.succ M) :: .lt (.var 16) (.succ K) :: stepΓ)
        (.eq nextM (.mul (.var 16) (.mul (.var 31) (.succ K)))) :=
      .eqTrans (.eqMul hyp (eqRefl _)) (ax (.mulAssoc _ _ _))
    apply Proof.exBI 17 (.succ nextM) (.mul (.var 31) (.succ K)) (by decide)
      (factorBound nextM (.var 16) (.mul (.var 31) (.succ K)) (push (push (push hyp))) he)
    exact he
  · have he : Proof (.eq (.var 16) (.succ K)::stepΓ)
        (.eq nextM (.mul (.var 16) M)) :=
      .eqTrans (ax (.mulComm _ _)) (.eqMul (.eqSymm hyp) (eqRefl _))
    apply Proof.exBI 17 (.succ nextM) M (by decide) (factorBound nextM (.var 16) M (push hyp) he)
    exact he
  · exact .botE (.ltIrrefl (.ltLeTrans (push (push hyp)) (.ltSuccLe hyp)))

def stepMatrix : Proof [cm K M] (cm (.succ K) nextM) := by
  apply Proof.andI
  · exact positiveProduct M (.succ K) (.andL hyp) (.leLtTrans (.zeroLe _) (ltSucc _))
  · apply Proof.allBI 16 (.succ (.succ K)) (by decide) (by decide)
    apply Proof.impI
    exact stepCases

def base : EProof [] (P.subst 3 (.lit 0)) := by
  apply CalculoExistencialRCA.Proof.exNI 30 (.lit 1) (by decide)
  exact .embed baseMatrix

def inductionStep : EProof [] (.allN 3 (.imp P (P.subst 3 (.succ K)))) := by
  apply CalculoExistencialRCA.Proof.allI 3 rfl
  apply CalculoExistencialRCA.Proof.impI
  apply CalculoExistencialRCA.Proof.exNE 30 (by decide) (by decide) CalculoExistencialRCA.hyp
  apply CalculoExistencialRCA.Proof.exNI 30 nextM (by decide)
  exact .embed (.weaken (fun _ hm => by
    cases hm with
    | head => exact List.mem_cons_self
    | tail _ h => cases h) stepMatrix)

def commonMultipleClosed : EProof [] (.allN 3 ParametroParBetaRCA.commonMultipleExists) :=
  .sigma1Induction 3 ParametroParBetaRCA.commonMultipleSigma1 rfl (by decide) (by decide) base inductionStep

example : P = ParametroParBetaRCA.commonMultipleExists := rfl
example : (cm K M).bounded = true := by decide
example : P.safe 3 (.lit 0) = true := by decide
example : P.safe 3 (.succ K) = true := by decide
example : (cm (.succ K) M).safe 30 nextM = true := by decide
example : freshNum 30 [P] = true := by decide
example : (P.subst 3 (.succ K)).numFree.contains 30 = false := by decide
example : (Formula.allN 3 P).numFree = [] := by decide
example : (Formula.allN 3 P).setFree = [] := by decide
#print axioms factorBound
#print axioms baseMatrix
#print axioms stepMatrix
#print axioms commonMultipleClosed
#eval ("common_multiple_uniform", CalculoExistencialRCA.profile commonMultipleClosed)
end MatematicaAbierta.Continuo.MultiploComunUniformeRCA
