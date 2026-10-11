import MatematicaAbierta.Continuo.AritmeticaModularInternaRCA

/-! M07 / H04-04.c/d: numeric preservation with the SAME b, conditional on
explicit bounded divisibility certificates. This is a CRT sub-obligation,
not CRT existence and not the extension with a new prescribed reading. -/
namespace MatematicaAbierta.Continuo.PreservacionModularBetaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA LecturasBetaRCA
open AritmeticaModularInternaRCA

def liftedA : Term := .add (.var 8) (.mul (.var 30) (.var 31))
def oldReading (k v : Term) : Formula := beta (.var 8) (.var 9) k v
def newReading (k v : Term) : Formula := beta liftedA (.var 9) k v
def factorCertificate (k : Term) : Formula :=
  .exB 23 (.succ (.var 30))
    (.eq (.var 30) (.mul (.var 23) (modulus k (.var 9))))

def pointContext : List Formula := [factorCertificate (.var 0), oldReading (.var 0) (.var 1)]
def quotientContext : List Formula :=
  [.eq (.var 8) (.add (.mul (.var 14) (modulus (.var 0) (.var 9))) (.var 1)),
   .lt (.var 14) (.succ (.var 8)),
   .eq (.var 30) (.mul (.var 15) (modulus (.var 0) (.var 9))),
   .lt (.var 15) (.succ (.var 30))] ++ pointContext

def liftedWitness : Proof quotientContext (newReading (.var 0) (.var 1)) := by
  have hβ : Proof quotientContext (oldReading (.var 0) (.var 1)) :=
    push (push (push (push (push hyp))))
  have he : Proof quotientContext
      (.eq liftedA (.add (.mul (.add (.var 14) (.mul (.var 15) (.var 31)))
        (modulus (.var 0) (.var 9))) (.var 1))) :=
    liftEquality (.var 8) (.var 14) (modulus (.var 0) (.var 9)) (.var 1)
      (.var 30) (.var 15) (.var 31) hyp (push (push hyp))
  apply Proof.andI (.andL hβ)
  apply Proof.exBI 12 (.succ liftedA) (.add (.var 14) (.mul (.var 15) (.var 31)))
    (by decide) (quotientBound liftedA _ (modulus (.var 0) (.var 9)) (.var 1)
      (modulusPositive (.var 0) (.var 9)) he)
  exact he

def pointOpen : Proof pointContext (newReading (.var 0) (.var 1)) := by
  apply Proof.exBErename 23 15 (.succ (.var 30)) (by decide) (by decide) (by decide)
    (by decide) hyp
  have hβ : Proof
      [.eq (.var 30) (.mul (.var 15) (modulus (.var 0) (.var 9))),
       .lt (.var 15) (.succ (.var 30)), factorCertificate (.var 0), oldReading (.var 0) (.var 1)]
      (oldReading (.var 0) (.var 1)) := push (push (push hyp))
  apply Proof.exBErename 12 14 (.succ (.var 8)) (by decide) (by decide) (by decide)
    (by decide) (.andR hβ)
  exact liftedWitness

def pointFormula : Formula := .imp (oldReading (.var 0) (.var 1))
  (.imp (factorCertificate (.var 0)) (newReading (.var 0) (.var 1)))
def liftBetaClosed : Proof []
    (.allN 8 (.allN 9 (.allN 0 (.allN 1 (.allN 30 (.allN 31 pointFormula)))))) :=
  .allI 8 rfl (.allI 9 rfl (.allI 0 rfl (.allI 1 rfl (.allI 30 rfl (.allI 31 rfl
    (.impI (.impI pointOpen)))))))

def atFreshReading : Proof []
    (.imp (oldReading (.var 20) (.var 21))
      (.imp (factorCertificate (.var 20)) (newReading (.var 20) (.var 21)))) := by
  have h₁ := Proof.allE 8 (.var 8) (by decide) liftBetaClosed
  have h₂ := Proof.allE 9 (.var 9) (by decide) h₁
  have h₃ := Proof.allE 0 (.var 20) (by decide) h₂
  have h₄ := Proof.allE 1 (.var 21) (by decide) h₃
  have h₅ := Proof.allE 30 (.var 30) (by decide) h₄
  exact Proof.allE 31 (.var 31) (by decide) h₅

def allFactors : Formula := .allB 20 (.succ (.var 3)) (factorCertificate (.var 20))
def segmentPreserved : Formula := .allB 20 (.succ (.var 3)) (.allB 21 (.var 4)
  (.imp (oldReading (.var 20) (.var 21)) (newReading (.var 20) (.var 21))))

def preservesSegment : Proof [] (.imp allFactors segmentPreserved) := by
  apply Proof.impI
  apply Proof.allBI 20 (.succ (.var 3)) (by decide) (by decide)
  apply Proof.allBI 21 (.var 4) (by decide) (by decide)
  have hfac : Proof
      [.lt (.var 21) (.var 4), .lt (.var 20) (.succ (.var 3)), allFactors]
      (factorCertificate (.var 20)) :=
    .allBE 20 (.succ (.var 3)) (.var 20) (by decide) (push (push hyp)) (push hyp)
  apply Proof.impI
  exact .impE (.impE (SelectoresInternosRCA.closed atFreshReading) hyp) (push hfac)

def preservesSegmentClosed : Proof []
    (.allN 8 (.allN 9 (.allN 3 (.allN 4 (.allN 30 (.allN 31
      (.imp allFactors segmentPreserved))))))) :=
  .allI 8 rfl (.allI 9 rfl (.allI 3 rfl (.allI 4 rfl (.allI 30 rfl (.allI 31 rfl
    preservesSegment))))))

example : allFactors.bounded = true := by decide
example : segmentPreserved.bounded = true := by decide
example : segmentPreserved.safe 8 (.var 22) = true := by decide
example : (newReading (.var 0) (.var 1)).numFree.contains 14 = false := by decide
example : (newReading (.var 0) (.var 1)).numFree.contains 15 = false := by decide

#print axioms liftedWitness
#print axioms liftBetaClosed
#print axioms preservesSegmentClosed
#eval ("beta_modular_lift", profile liftBetaClosed)
#eval ("beta_segment_preserved_given_factors", profile preservesSegmentClosed)
end MatematicaAbierta.Continuo.PreservacionModularBetaRCA
