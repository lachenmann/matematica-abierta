import MatematicaAbierta.Continuo.MultiploComunUniformeRCA

/-! M09 C07: scaled uniform multiple and explicit certificates for positive
index differences. No finite CRT iteration is claimed. -/
namespace MatematicaAbierta.Continuo.ParametroUniformeBetaRCA
open CalculoRCA CalculoOrdenRCA DivisionInternaRCA DiferenciasInternasRCA MultiploComunUniformeRCA
abbrev EProof := CalculoExistencialRCA.Proof

def L : Term := .var 4
def scaled : Term := .mul M (.succ L)
def largeMatrix (k l b : Term) : Formula := .conj (.lt l b) (cm k b)
def largeExists : Formula := .exN 40 (largeMatrix K L (.var 40))

def scaledMatrix : Proof [cm K M] (cm K scaled) := by
  apply Proof.andI
  · exact positiveProduct M (.succ L) (.andL hyp) (.leLtTrans (.zeroLe _) (ltSucc _))
  · apply Proof.allBI 16 (.succ K) (by decide) (by decide)
    apply Proof.impI
    have ho : Proof [.lt (.lit 0) (.var 16),.lt (.var 16) (.succ K),cm K M]
        (.exB 17 (.succ M) (.eq M (.mul (.var 16) (.var 17)))) :=
      .impE (.allBE 16 (.succ K) (.var 16) (by decide)
        (.andR (push (push hyp))) (push hyp)) hyp
    apply Proof.exBErename 17 31 (.succ M) (by decide) (by decide) (by decide) (by decide) ho
    have he : Proof [Formula.eq M (.mul (.var 16) (.var 31)),
        .lt (.var 31) (.succ M), .lt (.lit 0) (.var 16), .lt (.var 16) (.succ K),cm K M]
        (.eq scaled (.mul (.var 16) (.mul (.var 31) (.succ L)))) :=
      .eqTrans (.eqMul hyp (eqRefl _)) (ax (.mulAssoc _ _ _))
    exact .exBI 17 (.succ scaled) (.mul (.var 31) (.succ L)) (by decide)
      (factorBound scaled (.var 16) (.mul (.var 31) (.succ L)) (push (push hyp)) he) he

def largeWitness : Proof [cm K M] (largeMatrix K L scaled) :=
  .andI (ParametroParBetaRCA.parameterLarge M L (.andL hyp)) scaledMatrix

/-- ∀K,L ∃b (L<b ∧ 0<b ∧ every positive d≤K has a bounded quotient b=dq). -/
def uniformParameter : EProof [] (.allN 3 (.allN 4 largeExists)) := by
  apply CalculoExistencialRCA.Proof.allI 3 rfl
  apply CalculoExistencialRCA.Proof.allI 4 rfl
  apply CalculoExistencialRCA.Proof.exNE 30 (by decide) (by decide)
    (CalculoExistencialRCA.Proof.allE 3 K (by decide) commonMultipleClosed)
  apply CalculoExistencialRCA.Proof.exNI 40 scaled (by decide)
  exact .embed largeWitness

def B : Term := .var 40
def pairΓ : List Formula := [.le (.var 21) K,.lt (.var 20) (.var 21),cm K B]
def differenceCertificate : Formula := .exB 2 (.succ K)
  (.conj (.eq (.var 21) (.add (.var 20) (.var 2)))
    (.conj (.lt (.lit 0) (.var 2))
      (.exB 17 (.succ B) (.eq B (.mul (.var 2) (.var 17))))))

def differenceOpen : Proof pairΓ differenceCertificate := by
  have hg : Proof pairΓ (.exB 2 (.succ (.var 21))
      (.conj (.eq (.var 21) (.add (.var 20) (.var 2))) (.lt (.lit 0) (.var 2)))) :=
    .impE (SelectoresInternosRCA.closed (.allE 21 (.var 21) (by decide)
      (.allE 20 (.var 20) (by decide) gapFromOrder))) (push hyp)
  apply Proof.exBErename 2 26 (.succ (.var 21)) (by decide) (by decide) (by decide) (by decide) hg
  have hd : Proof [Formula.conj (.eq (.var 21) (.add (.var 20) (.var 26))) (.lt (.lit 0) (.var 26)),
      .lt (.var 26) (.succ (.var 21)),.le (.var 21) K,.lt (.var 20) (.var 21),cm K B]
      (.lt (.var 26) (.succ K)) :=
    leThenSucc (.leTrans
      (.leRewrite (eqRefl _) (.eqSymm (.andL hyp)) (leLeftAdd (.var 26) (.var 20)))
      (push (push hyp)))
  apply Proof.exBI 2 (.succ K) (.var 26) (by decide) hd
  apply Proof.andI (.andL hyp)
  apply Proof.andI (.andR hyp)
  exact .impE (.allBE 16 (.succ K) (.var 26) (by decide)
    (.andR (push (push (push (push hyp))))) hd) (.andR hyp)

def differencesClosed : Proof [] ([3,40,20,21].foldr Formula.allN
    (.imp (cm K B) (.imp (.lt (.var 20) (.var 21)) (.imp (.le (.var 21) K) differenceCertificate)))) :=
  .allI 3 rfl (.allI 40 rfl (.allI 20 rfl (.allI 21 rfl
    (.impI (.impI (.impI differenceOpen))))))

example : freshNum 30 [] = true := rfl
example : largeExists.numFree.contains 30 = false := by decide
example : (largeMatrix K L B).safe 40 scaled = true := by decide
example : (cm K B).bounded = true := by decide
example : differenceCertificate.bounded = true := by decide
example : differenceCertificate.numFree.contains 26 = false := by decide
example : (Formula.allN 3 (.allN 4 largeExists)).numFree = [] := by decide
#print axioms scaledMatrix
#print axioms uniformParameter
#print axioms differencesClosed
#eval ("uniform_large_parameter", CalculoExistencialRCA.profile uniformParameter)
#eval ("all_positive_index_differences", CalculoOrdenRCA.profile differencesClosed)
end MatematicaAbierta.Continuo.ParametroUniformeBetaRCA
