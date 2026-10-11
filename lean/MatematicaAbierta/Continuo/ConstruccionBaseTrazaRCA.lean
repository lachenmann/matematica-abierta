import MatematicaAbierta.Continuo.TrazasInduccionRCA

/-!
H04-04: an actual closed base-case code-existence derivation, K=0.
Witnesses are T=2, (a_U,b_U)=(0,0), (a_D,b_D)=(1,1).
The uniform β-code extension step is NOT a theory axiom and remains open.
-/
namespace MatematicaAbierta.Continuo.ConstruccionBaseTrazaRCA
open CalculoRCA TrazasInduccionRCA

def zeroProduct (t : Term) : EqProof (.mul (.lit 0) t) (.lit 0) :=
  .trans (.mulComm _ _) (.mulZero _)

def betaZeroDenominator :
    EqProof (.add (.lit 1) (.mul (.add (.lit 0) (.lit 1)) (.lit 0))) (.lit 1) :=
  .trans (.add (.refl _) (.trans (.mul (numeralAdd 0 1) (.refl _)) (numeralMul 1 0)))
    (numeralAdd 1 0)

def betaOneDenominator :
    EqProof (.add (.lit 1) (.mul (.add (.lit 0) (.lit 1)) (.lit 1))) (.lit 2) :=
  .trans (.add (.refl _) (.trans (.mul (numeralAdd 0 1) (.refl _)) (numeralMul 1 1)))
    (numeralAdd 1 1)

def zeroLtOne {Γ : List Formula} : Derives Γ (.lt (.lit 0) (.lit 1)) :=
  .ltRewrite (.arithmetic (.refl _)) (.arithmetic (.symm (.literalSucc 0))) (.ltSucc (.lit 0))

def oneLtTwo {Γ : List Formula} : Derives Γ (.lt (.lit 1) (.lit 2)) :=
  .ltRewrite (.arithmetic (.refl _)) (.arithmetic (.symm (.literalSucc 1))) (.ltSucc (.lit 1))

def betaNumeratorZero {Γ : List Formula} :
    Derives Γ (beta (.lit 0) (.lit 0) (.lit 0) (.lit 0)) := by
  apply Derives.andI
  · exact .ltRewrite (.arithmetic (.refl _))
      (.arithmetic (.symm betaZeroDenominator)) zeroLtOne
  · apply Derives.exBI 12 (.succ (.lit 0)) (.lit 0) (by decide) (.ltSucc (.lit 0))
    exact .arithmetic (.symm (.trans
      (.add (zeroProduct _) (.refl _)) (numeralAdd 0 0)))

def betaDenominatorOne {Γ : List Formula} :
    Derives Γ (beta (.lit 1) (.lit 1) (.lit 0) (.lit 1)) := by
  apply Derives.andI
  · exact .ltRewrite (.arithmetic (.refl _))
      (.arithmetic (.symm betaOneDenominator)) oneLtTwo
  · apply Derives.exBI 12 (.succ (.lit 1)) (.lit 0) (by decide)
      (Derives.ltTrans zeroLtOne (.ltSucc (.lit 1)))
    exact .arithmetic (.symm (.trans
      (.add (zeroProduct _) (.refl _)) (numeralAdd 0 1)))

def baseTraceFormula : Formula :=
  let p := finiteTraceMatrix.subst 3 (.lit 0)
  let p := p.subst 4 (.lit 2)
  let p := p.subst 8 (.lit 0)
  let p := p.subst 9 (.lit 0)
  let p := p.subst 10 (.lit 1)
  p.subst 11 (.lit 1)

/-- The REAL Σ₁ formula for the still pending uniform code-existence induction.
The code fields are quantified, with the bit graph as the only set parameter. -/
def uniformCodeFormula : Formula :=
  .exN 4 (.exN 8 (.exN 9 (.exN 10 (.exN 11 finiteTraceMatrix))))

def uniformCodeSigma1 : Sigma1 uniformCodeFormula :=
  .exists 4 (.exists 8 (.exists 9 (.exists 10 (.exists 11 (.bounded rfl)))))

def baseTrace : Derives [] baseTraceFormula := by
  apply Derives.andI oneLtTwo
  apply Derives.andI betaNumeratorZero
  apply Derives.andI betaDenominatorOne
  apply Derives.allBI 0 (.lit 0) rfl rfl
  exact .botE (.impE (.ltZeroFalse (.var 0)) hyp0)

def codeExistenceBase : Derives []
    (.exN 4 (.exN 8 (.exN 9 (.exN 10 (.exN 11 (finiteTraceMatrix.subst 3 (.lit 0))))))) := by
  apply Derives.exNI 4 (.lit 2) (by decide)
  apply Derives.exNI 8 (.lit 0) (by decide)
  apply Derives.exNI 9 (.lit 0) (by decide)
  apply Derives.exNI 10 (.lit 1) (by decide)
  apply Derives.exNI 11 (.lit 1) (by decide)
  exact baseTrace

#print axioms betaNumeratorZero
#print axioms betaDenominatorOne
#print axioms baseTrace
#print axioms codeExistenceBase
#print axioms uniformCodeSigma1

#eval ("code_existence_base", ruleProfile codeExistenceBase)

end MatematicaAbierta.Continuo.ConstruccionBaseTrazaRCA
