import MatematicaAbierta.Continuo.DivisionInternaRCA
import MatematicaAbierta.Continuo.TotalidadTrazaRCA
import MatematicaAbierta.Continuo.ExtensionGraficaRCA

/-! M07: a remainder exists for ANY given numeric beta code. This statement
does NOT assert that a code exists for a prescribed list of readings.
The seven M06 modules are reused transitively, without editing their sources. -/
namespace MatematicaAbierta.Continuo.DivisionBetaRCA
open CalculoRCA CalculoOrdenRCA TrazasInduccionRCA LecturasBetaRCA DivisionInternaRCA

def betaTotalFormula : Formula :=
  .exB 1 (.succ (.var 8)) (beta (.var 8) (.var 9) (.var 0) (.var 1))

def betaDivision : Proof [] (division (.var 8) (modulus (.var 0) (.var 9))) := by
  -- Instantiate the dividend BEFORE the modulus: otherwise k=0 is captured
  -- by the original allN 0 binder. The syntactic safe guard rejects that order.
  have atA : Proof [modulusHyp] (division (.var 8) (.var 9)) :=
    .allE 0 (.var 8) (by decide) divisionInduction
  have atAClosed : Proof []
      (.allN 9 (.imp modulusHyp (division (.var 8) (.var 9)))) :=
    .allI 9 rfl (.impI atA)
  have h₁ := Proof.allE 9 (modulus (.var 0) (.var 9)) (by decide) atAClosed
  exact Proof.impE h₁ (modulusPositive (.var 0) (.var 9))

def betaTotalOpen : Proof [] betaTotalFormula := by
  apply Proof.exBE 14 (.succ (.var 8)) (by decide) (by decide) (by decide) betaDivision
  apply Proof.exBE 15 (.succ (.var 8)) (by decide) (by decide) (by decide) hyp
  apply Proof.exBI 1 (.succ (.var 8)) (.var 15) (by decide) (push hyp)
  apply Proof.andI (.andL hyp)
  apply Proof.exBI 12 (.succ (.var 8)) (.var 14) (by decide) (push (push (push hyp)))
  exact .andR hyp

/-- ∀a,b,k ∃v<a+1 beta(a,b,k,v), with division derived internally. -/
def betaTotal : Proof [] (.allN 8 (.allN 9 (.allN 0 betaTotalFormula))) :=
  .allI 8 rfl (.allI 9 rfl (.allI 0 rfl betaTotalOpen))

example : betaTotalFormula.bounded = true := by decide
example : betaTotalFormula.numFree.contains 14 = false := by decide
example : betaTotalFormula.numFree.contains 15 = false := by decide
example : betaTotalFormula.safe 8 (.var 22) = true := by decide
-- Regression control: the tempting reversed instantiation IS unsafe.
example : (Formula.imp modulusHyp (.allN 0 divisionMatrix)).safe 9
    (modulus (.var 0) (.var 9)) = false := by decide

#print axioms betaDivision
#print axioms betaTotalOpen
#print axioms betaTotal
#eval ("beta_total_given_code", profile betaTotal)
end MatematicaAbierta.Continuo.DivisionBetaRCA
