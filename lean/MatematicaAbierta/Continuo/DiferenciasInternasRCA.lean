import MatematicaAbierta.Continuo.ContratoExtensionBetaRCA
import MatematicaAbierta.Continuo.PreservacionModularBetaRCA

/-! M08 C07-C09. Bounded additive differences and positive predecessors,
derived using the unchanged M06 Proof calculus. No subtraction function,
predecessor rule or existence axiom is added. -/
namespace MatematicaAbierta.Continuo.DiferenciasInternasRCA
open CalculoRCA CalculoOrdenRCA DivisionInternaRCA

def differences (n : Term) : Formula := .allB 1 (.succ n)
  (.imp (.le (.var 1) n) (.exB 2 (.succ n) (.eq n (.add (.var 1) (.var 2)))))
def matrix : Formula := differences (.var 0)

def differenceBase : Proof [] (differences (.lit 0)) := by
  apply Proof.allBI 1 (.succ (.lit 0)) rfl rfl
  apply Proof.impI
  apply Proof.exBI 2 (.succ (.lit 0)) (.lit 0) (by decide) (ltSucc _)
  exact .eqTrans (.eqSymm (.leAntisymm hyp (.zeroLe _))) (ax (.symm (.addZero _)))

def stepContext : List Formula :=
  [.le (.var 1) (.succ (.var 0)), .lt (.var 1) (.succ (.succ (.var 0))), matrix]
def stepConclusion : Formula := .exB 2 (.succ (.succ (.var 0)))
  (.eq (.succ (.var 0)) (.add (.var 1) (.var 2)))

def differenceCases : Proof stepContext stepConclusion := by
  apply Proof.orderCases (.var 1) (.var 0)
  · have old : Proof (.lt (.var 1) (.var 0) :: stepContext)
        (.exB 2 (.succ (.var 0)) (.eq (.var 0) (.add (.var 1) (.var 2)))) :=
      .impE (.allBE 1 (.succ (.var 0)) (.var 1) (by decide)
        (push (push (push hyp))) (.ltTrans hyp (ltSucc _))) (.ltLe hyp)
    apply Proof.exBE 2 (.succ (.var 0)) (by decide) (by decide) (by decide) old
    apply Proof.exBI 2 (.succ (.succ (.var 0))) (.succ (.var 2)) (by decide)
      (succLt (push hyp))
    exact .eqTrans (succEq hyp) (ax (.symm (.addSucc _ _)))
  · apply Proof.exBI 2 (.succ (.succ (.var 0))) (.lit 1) (by decide)
    · have hz : Proof (.eq (.var 1) (.var 0) :: stepContext)
          (.le (.lit 1) (.succ (.var 0))) :=
        .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (succLe (.zeroLe _))
      exact leThenSucc hz
    · exact .eqTrans (.eqSymm (succEq hyp)) (ax (.symm (addOne _)))
  · have he : Proof (.lt (.var 0) (.var 1) :: stepContext)
        (.eq (.var 1) (.succ (.var 0))) :=
      .leAntisymm (push hyp) (.ltSuccLe hyp)
    apply Proof.exBI 2 (.succ (.succ (.var 0))) (.lit 0) (by decide)
      (.leLtTrans (.zeroLe _) (ltSucc _))
    exact .eqTrans (.eqSymm he) (ax (.symm (.addZero _)))

def differenceStep : Proof [] (.allN 0 (.imp matrix (differences (.succ (.var 0))))) := by
  apply Proof.allI 0 rfl
  apply Proof.impI
  apply Proof.allBI 1 (.succ (.succ (.var 0))) (by decide) (by decide)
  apply Proof.impI
  exact differenceCases

/-- ∀n ∀s<n+1 (s≤n → ∃d<n+1 n=s+d), actually derived by bounded induction. -/
def boundedDifference : Proof [] (.allN 0 matrix) :=
  .sigma1Induction 0 (.bounded (by decide)) rfl (by decide) (by decide)
    differenceBase differenceStep

def positiveProduct {Γ : List Formula} (t u : Term)
    (ht : Proof Γ (.lt (.lit 0) t)) (hu : Proof Γ (.lt (.lit 0) u)) :
    Proof Γ (.lt (.lit 0) (.mul t u)) := by
  have hOne : Proof Γ (.le (.lit 1) t) :=
    .leRewrite (ax (.symm (.literalSucc 0))) (eqRefl _) (.ltSuccLe ht)
  exact .ltLeTrans hu (.leRewrite (ax (mulOneLeft u)) (eqRefl _) (.leMulRight u hOne))

def positiveComplement {Γ : List Formula} (s d n : Term)
    (hs : Proof Γ (.lt s n)) (he : Proof Γ (.eq n (.add s d))) :
    Proof Γ (.lt (.lit 0) d) := by
  apply Proof.orderCases (.lit 0) d
  · exact hyp
  · have hn : Proof (.eq (.lit 0) d :: Γ) (.eq n s) :=
      .eqTrans (push he) (.eqTrans (.eqAdd (eqRefl s) (.eqSymm hyp)) (ax (.addZero _)))
    exact .botE (.ltIrrefl (.ltRewrite (eqRefl _) hn (push hs)))
  · exact .botE (.ltIrrefl (.ltLeTrans hyp (.zeroLe _)))

def gapFormula : Formula := .exB 2 (.succ (.var 21))
  (.conj (.eq (.var 21) (.add (.var 20) (.var 2))) (.lt (.lit 0) (.var 2)))
def gapOpen : Proof [.lt (.var 20) (.var 21)] gapFormula := by
  have hd : Proof [.lt (.var 20) (.var 21)]
      (.exB 2 (.succ (.var 21)) (.eq (.var 21) (.add (.var 20) (.var 2)))) :=
    .impE (.allBE 1 (.succ (.var 21)) (.var 20) (by decide)
      (SelectoresInternosRCA.closed (.allE 0 (.var 21) (by decide) boundedDifference))
      (leThenSucc (.ltLe hyp))) (.ltLe hyp)
  apply Proof.exBErename 2 26 (.succ (.var 21)) (by decide) (by decide) (by decide) (by decide) hd
  apply Proof.exBI 2 (.succ (.var 21)) (.var 26) (by decide) (push hyp)
  exact .andI hyp (positiveComplement (.var 20) (.var 26) (.var 21) (push (push hyp)) hyp)
def gapFromOrder : Proof []
    (.allN 20 (.allN 21 (.imp (.lt (.var 20) (.var 21)) gapFormula))) :=
  .allI 20 rfl (.allI 21 rfl (.impI gapOpen))

example : matrix.bounded = true := by decide
example : matrix.safe 0 (.succ (.var 0)) = true := by decide
example : stepConclusion.numFree.contains 2 = false := by decide
example : gapFormula.numFree.contains 26 = false := by decide
#print axioms boundedDifference
#print axioms positiveProduct
#print axioms positiveComplement
#print axioms gapFromOrder
#eval ("bounded_difference", profile boundedDifference)
#eval ("positive_gap_from_order", profile gapFromOrder)
end MatematicaAbierta.Continuo.DiferenciasInternasRCA
