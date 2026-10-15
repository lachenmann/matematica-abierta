import MatematicaAbierta.Continuo.DiferenciasInternasRCA

/-! M08 C08/C09: an internally derived POSITIVE inverse certificate.
Gap j=i+delta and b=delta*c, delta,c>0, remain explicit antecedents.
No Bezout/CRT/coprimality axiom, subtraction or beta-code existence. -/
namespace MatematicaAbierta.Continuo.IdentidadModulosBetaRCA
open CalculoRCA CalculoOrdenRCA LecturasBetaRCA DivisionInternaRCA
open DiferenciasInternasRCA AritmeticaModularInternaRCA

def squareRegroup (h b : Term) : EqProof
    (.mul (.mul (.mul h h) b) b) (.mul (.mul h b) (.mul h b)) :=
  .trans (.mul (.mulAssoc _ _ _) (.refl _))
    (.trans (.mulAssoc _ _ _)
      (.symm (.trans (.mulAssoc _ _ _)
        (.mul (.refl _) (.trans (.symm (.mulAssoc _ _ _))
          (.mul (.mulComm _ _) (.refl _)))))))

def squarePacket (z : Term) : EqProof
    (.mul (.add (.lit 1) z) (.add (.lit 1) z))
    (.add (.lit 1) (.mul z (.add (.lit 1) (.add (.lit 1) z)))) := by
  have left : EqProof
      (.mul (.add (.lit 1) z) (.add (.lit 1) z))
      (.add (.lit 1) (.add z (.add z (.mul z z)))) :=
    .trans (.distrib _ _ _)
      (.trans (.add (.trans (.mulComm _ _) (mulOneLeft _))
        (.trans (mulRightDistrib _ _ _) (.add (mulOneLeft _) (.refl _))))
        (.addAssoc _ _ _))
  have right : EqProof
      (.add (.lit 1) (.mul z (.add (.lit 1) (.add (.lit 1) z))))
      (.add (.lit 1) (.add z (.add z (.mul z z)))) :=
    .add (.refl _) (.trans (.distrib _ _ _)
      (.add (.trans (.mulComm _ _) (mulOneLeft _))
        (.trans (.distrib _ _ _) (.add (.trans (.mulComm _ _) (mulOneLeft _)) (.refl _)))))
  exact .trans left (.symm right)

def inverseEquality {Γ : List Formula} (i j delta c b z : Term)
    (hj : Proof Γ (.eq j (.add i delta)))
    (hb : Proof Γ (.eq b (.mul delta c)))
    (hz : Proof Γ (.eq (.mul (.add i (.lit 1)) b) (.add (.lit 1) z))) :
    Proof Γ (.eq
      (.mul (.mul (.mul (.add i (.lit 1)) (.add i (.lit 1))) c) (modulus j b))
      (.add (.lit 1)
        (.mul (.add (.mul (.mul (.add i (.lit 1)) (.add i (.lit 1))) c) z) (modulus i b)))) := by
  let h := Term.add i (.lit 1)
  let q := Term.mul (.mul h h) c
  let mi := modulus i b
  let mj := modulus j b
  have hindex : Proof Γ (.eq (.add j (.lit 1)) (.add h delta)) :=
    .eqTrans (.eqAdd hj (eqRefl _)) (ax (shuffle i delta (.lit 1)))
  have hmod : Proof Γ (.eq mj (.add mi (.mul delta b))) :=
    .eqTrans (.eqAdd (eqRefl _) (.eqMul hindex (eqRefl _)))
      (ax (.trans (.add (.refl _) (mulRightDistrib h delta b)) (.symm (.addAssoc _ _ _))))
  have hcd : Proof Γ (.eq (.mul c delta) b) :=
    .eqTrans (ax (.mulComm _ _)) (.eqSymm hb)
  have hprod : Proof Γ (.eq (.mul q (.mul delta b)) (.mul (.mul h b) (.mul h b))) :=
    .eqTrans (ax (.trans (.mulAssoc _ _ _) (.mul (.refl _) (.symm (.mulAssoc _ _ _)))))
      (.eqTrans (.eqMul (eqRefl (.mul h h)) (.eqMul hcd (eqRefl b)))
        (ax (.trans (.symm (.mulAssoc _ _ _)) (squareRegroup h b))))
  have hmi : Proof Γ (.eq mi (.add (.lit 1) (.add (.lit 1) z))) :=
    .eqAdd (eqRefl _) hz
  have hsquare : Proof Γ
      (.eq (.mul (.mul h b) (.mul h b)) (.add (.lit 1) (.mul z mi))) :=
    .eqTrans (.eqMul hz hz) (.eqTrans (ax (squarePacket z))
      (.eqAdd (eqRefl _) (.eqMul (eqRefl z) (.eqSymm hmi))))
  have hsum : EqProof
      (.add (.mul q mi) (.add (.lit 1) (.mul z mi)))
      (.add (.lit 1) (.mul (.add q z) mi)) :=
    .trans (.symm (.addAssoc _ _ _))
      (.trans (.add (.addComm _ _) (.refl _))
        (.trans (.addAssoc _ _ _) (.add (.refl _) (.symm (mulRightDistrib q z mi)))))
  exact .eqTrans (.eqMul (eqRefl q) hmod)
    (.eqTrans (ax (.distrib q mi (.mul delta b)))
      (.eqTrans (.eqAdd (eqRefl _) (.eqTrans hprod hsquare)) (ax hsum)))

def h : Term := .add (.var 0) (.lit 1)
def qCandidate : Term := .mul (.mul h h) (.var 3)
def hbTerm : Term := .mul h (.var 4)
def identityContext : List Formula :=
  [.eq (.var 1) (.add (.var 0) (.var 2)), .eq (.var 4) (.mul (.var 2) (.var 3)),
   .lt (.lit 0) (.var 2), .lt (.lit 0) (.var 3)]
def conclusion : Formula := .exB 22 (.succ qCandidate)
  (.exB 23 (.succ (.add qCandidate hbTerm))
    (.conj (.lt (.lit 0) (.var 22))
      (.eq (.mul (.var 22) (modulus (.var 1) (.var 4)))
        (.add (.lit 1) (.mul (.var 23) (modulus (.var 0) (.var 4)))))))

def hPositive {Γ : List Formula} : Proof Γ (.lt (.lit 0) h) :=
  .ltRewrite (eqRefl _) (ax (.symm (addOne _))) (.leLtTrans (.zeroLe _) (ltSucc _))
def hbPositive : Proof identityContext (.lt (.lit 0) hbTerm) :=
  positiveProduct h (.var 4) hPositive
    (.ltRewrite (eqRefl _) (.eqSymm (push hyp))
      (positiveProduct (.var 2) (.var 3) (push (push hyp)) (push (push (push hyp)))))
def qPositive : Proof identityContext (.lt (.lit 0) qCandidate) :=
  positiveProduct (.mul h h) (.var 3) (positiveProduct h h hPositive hPositive)
    (push (push (push hyp)))

def predecessorExists : Proof identityContext
    (.exB 2 (.succ hbTerm) (.eq hbTerm (.add (.lit 1) (.var 2)))) := by
  have hd : Proof identityContext (differences hbTerm) :=
    SelectoresInternosRCA.closed (.allE 0 hbTerm (by decide) boundedDifference)
  have hone : Proof identityContext (.le (.lit 1) hbTerm) :=
    .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (.ltSuccLe hbPositive)
  exact .impE (.allBE 1 (.succ hbTerm) (.lit 1) (by decide) hd (leThenSucc hone)) hone

def identityOpen : Proof identityContext conclusion := by
  apply Proof.exBErename 2 24 (.succ hbTerm) (by decide) (by decide) (by decide)
    (by decide) predecessorExists
  have hz : Proof
      (.eq hbTerm (.add (.lit 1) (.var 24)) :: .lt (.var 24) (.succ hbTerm) :: identityContext)
      (.le (.var 24) hbTerm) :=
    .leRewrite (eqRefl _) (.eqSymm hyp) (leLeftAdd (.var 24) (.lit 1))
  apply Proof.exBI 22 (.succ qCandidate) qCandidate (by decide) (ltSucc _)
  apply Proof.exBI 23 (.succ (.add qCandidate hbTerm)) (.add qCandidate (.var 24))
    (by decide) (leThenSucc (leAddLeft qCandidate hz))
  apply Proof.andI (push (push qPositive))
  exact inverseEquality (.var 0) (.var 1) (.var 2) (.var 3) (.var 4) (.var 24)
    (push (push hyp)) (push (push (push hyp))) hyp

def positiveInverse : Proof []
    (.allN 0 (.allN 1 (.allN 2 (.allN 3 (.allN 4
      (.imp (.lt (.lit 0) (.var 3)) (.imp (.lt (.lit 0) (.var 2))
        (.imp (.eq (.var 4) (.mul (.var 2) (.var 3)))
          (.imp (.eq (.var 1) (.add (.var 0) (.var 2))) conclusion))))))))) :=
  .allI 0 rfl (.allI 1 rfl (.allI 2 rfl (.allI 3 rfl (.allI 4 rfl
    (.impI (.impI (.impI (.impI identityOpen))))))))

example : conclusion.bounded = true := by decide
example : conclusion.numFree.contains 24 = false := by decide
example : (differences (.var 0)).safe 0 hbTerm = true := by decide
#print axioms inverseEquality
#print axioms positiveInverse
#eval ("positive_inverse_special_moduli", profile positiveInverse)
end MatematicaAbierta.Continuo.IdentidadModulosBetaRCA
