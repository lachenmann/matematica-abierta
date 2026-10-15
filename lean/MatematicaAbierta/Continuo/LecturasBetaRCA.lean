import MatematicaAbierta.Continuo.CalculoOrdenRCA
import MatematicaAbierta.Continuo.ConstruccionBaseTrazaRCA

/-! H04-04.e: INTERNAL remainder uniqueness and modulus positivity.
No uniqueness constructor/axiom is admitted. Quotients are eliminated with
fresh names 14 and 15; their original beta binder is 12. -/
namespace MatematicaAbierta.Continuo.LecturasBetaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA

def modulus (k b : Term) : Term := .add (.lit 1) (.mul (.add k (.lit 1)) b)

def modulusPositive {Γ : List Formula} (k b : Term) : Proof Γ (.lt (.lit 0) (modulus k b)) := by
  let z := Term.mul (.add k (.lit 1)) b
  have hz : Proof Γ (.lt z (.add (.lit 1) z)) :=
    .ltRewrite (ax (addZeroLeft z)) (eqRefl _) (.ltAddRight z (.embed ConstruccionBaseTrazaRCA.zeroLtOne))
  exact .leLtTrans (.zeroLe z) hz

def quotientStrict {Γ : List Formula} (q r m v w : Term)
    (hqr : Proof Γ (.lt q r)) (hv : Proof Γ (.lt v m)) :
    Proof Γ (.lt (.add (.mul q m) v) (.add (.mul r m) w)) := by
  have h₁ : Proof Γ (.lt (.add (.mul q m) v) (.add (.mul q m) m)) :=
    ltAddLeft (.mul q m) hv
  have h₂ : Proof Γ (.le (.add (.mul q m) m) (.mul r m)) :=
    .leRewrite (ax (mulSuccessorLeft q m)) (eqRefl _) (.leMulRight m (.ltSuccLe hqr))
  exact .ltLeTrans (.ltLeTrans h₁ h₂) (leRightAdd (.mul r m) w)

def remainderUnique {Γ : List Formula} (q r m v w : Term)
    (he : Proof Γ (.eq (.add (.mul q m) v) (.add (.mul r m) w)))
    (hv : Proof Γ (.lt v m)) (hw : Proof Γ (.lt w m)) : Proof Γ (.eq v w) := by
  apply Proof.orderCases q r
  · exact .botE (.ltIrrefl (.ltRewrite (push he) (eqRefl _)
      (quotientStrict q r m v w hyp (push hv))))
  · have ht : Proof (.eq q r :: Γ)
        (.eq (.add (.mul q m) v) (.add (.mul r m) v)) :=
      Proof.eqAdd (Proof.eqMul hyp (eqRefl m)) (eqRefl v)
    exact .addCancelLeft (.mul r m) (.eqTrans (.eqSymm ht) (push he))
  · exact .botE (.ltIrrefl (.ltRewrite (.eqSymm (push he)) (eqRefl _)
      (quotientStrict r q m w v hyp (push hw))))

def betaU : Formula := beta (.var 8) (.var 9) (.var 0) (.var 1)
def betaV : Formula := beta (.var 8) (.var 9) (.var 0) (.var 2)
def betaContext : List Formula := [betaV,betaU]
def betaWitnessContext : List Formula :=
  [.eq (.var 8) (.add (.mul (.var 15) (modulus (.var 0) (.var 9))) (.var 2)),
   .lt (.var 15) (.succ (.var 8)),
   .eq (.var 8) (.add (.mul (.var 14) (modulus (.var 0) (.var 9))) (.var 1)),
   .lt (.var 14) (.succ (.var 8))] ++ betaContext

def betaWitnessUnique : Proof betaWitnessContext (.eq (.var 1) (.var 2)) := by
  have h₁ : Proof betaWitnessContext
      (.eq (.var 8) (.add (.mul (.var 14) (modulus (.var 0) (.var 9))) (.var 1))) := push (push hyp)
  have h₂ : Proof betaWitnessContext
      (.eq (.var 8) (.add (.mul (.var 15) (modulus (.var 0) (.var 9))) (.var 2))) := hyp
  have hu : Proof betaWitnessContext betaU := push (push (push (push (push hyp))))
  have hv : Proof betaWitnessContext betaV := push (push (push (push hyp)))
  exact remainderUnique (.var 14) (.var 15) (modulus (.var 0) (.var 9)) (.var 1) (.var 2)
    (.eqTrans (.eqSymm h₁) h₂) (.andL hu) (.andL hv)

def betaUniqueOpen : Proof betaContext (.eq (.var 1) (.var 2)) := by
  have hu : Proof betaContext betaU := push hyp
  apply Proof.exBErename 12 14 (.succ (.var 8)) (by decide) (by decide) rfl (by decide) (.andR hu)
  have hv : Proof
      [.eq (.var 8) (.add (.mul (.var 14) (modulus (.var 0) (.var 9))) (.var 1)),
       .lt (.var 14) (.succ (.var 8)), betaV, betaU] betaV := push (push hyp)
  apply Proof.exBErename 12 15 (.succ (.var 8)) (by decide) (by decide) rfl (by decide) (.andR hv)
  exact betaWitnessUnique

def betaUniqueFormula : Formula :=
  .allN 8 (.allN 9 (.allN 0 (.allN 1 (.allN 2
    (.imp betaU (.imp betaV (.eq (.var 1) (.var 2))))))))
def betaUnique : Proof [] betaUniqueFormula :=
  .allI 8 rfl (.allI 9 rfl (.allI 0 rfl (.allI 1 rfl (.allI 2 rfl
    (.impI (.impI betaUniqueOpen))))))
def modulusPositiveClosed : Proof []
    (.allN 0 (.allN 9 (.lt (.lit 0) (modulus (.var 0) (.var 9))))) :=
  .allI 0 rfl (.allI 9 rfl (modulusPositive (.var 0) (.var 9)))

#print axioms modulusPositiveClosed
#print axioms remainderUnique
#print axioms betaUnique
#eval ("beta_unique", profile betaUnique)
end MatematicaAbierta.Continuo.LecturasBetaRCA
