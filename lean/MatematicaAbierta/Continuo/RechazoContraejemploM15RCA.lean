import MatematicaAbierta.Continuo.CorreccionCalculoOrdenRCA

namespace MatematicaAbierta.Continuo.RechazoContraejemploM15RCA
open CalculoRCA CalculoOrdenRCA GraficaBitsAcotadosRCA
def different : Formula := .imp (.eq (.var 170) (.var 171)) .bot
def existsDifferent : Formula := .exB 170 (.lit 2) different

-- Legitimate arithmetic/logical proof of: there is a bit unequal to y.
def existsDifferentProof : Proof [] existsDifferent := by
  apply Proof.orderCases (.lit 0) (.var 171)
  · apply Proof.exBI 170 (.lit 2) (.lit 0) (by decide) zeroBelowTwo
    apply Proof.impI
    have hl : Proof [Formula.eq (.lit 0) (.var 171),Formula.lt (.lit 0) (.var 171)]
        (.lt (.lit 0) (.var 171)) := push hyp
    exact .ltIrrefl (.ltRewrite hyp (eqRefl _) hl)
  · apply Proof.exBI 170 (.lit 2) (.lit 1) (by decide) oneBelowTwo
    apply Proof.impI
    have hz : Proof [Formula.eq (.lit 1) (.var 171),Formula.eq (.lit 0) (.var 171)]
        (.eq (.lit 0) (.var 171)) := push hyp
    exact .impE zeroNotOne (.eqTrans hz (.eqSymm hyp))
  · exact .botE (.impE (.embed (.ltZeroFalse (.var 171))) hyp)

-- All guards actually present in M06 accept the invalid renaming 170 -> 171.
example : freshNum 171 ([] : List Formula) = true := rfl
example : Formula.bot.numFree.contains 171 = false := rfl
example : (Term.lit 2).vars.contains 171 = false := rfl
example : different.safe 170 (.var 171) = true := rfl
-- The missing guard fails, and substitution changes x != y into y != y.
example : different.numFree.contains 171 = true := rfl
example : different.subst 170 (.var 171) = .imp (.eq (.var 171) (.var 171)) .bot := rfl

def renamedBranch : Proof
    [different.subst 170 (.var 171),Formula.lt (.var 171) (.lit 2)] .bot :=
  .impE hyp (eqRefl (.var 171))


-- Both the old signature and the missing freshness certificate are rejected.
example : True := by
  fail_if_success exact (Proof.exBErename 170 171 (.lit 2) rfl rfl rfl rfl existsDifferentProof renamedBranch : Proof [] .bot)
  trivial
example : True := by
  fail_if_success exact (Proof.exBErename 170 171 (.lit 2) rfl rfl rfl rfl (by decide) (by decide) existsDifferentProof renamedBranch : Proof [] .bot)
  trivial
example : True := by
  fail_if_success have bad : (170 : ℕ) ≠ 170 := by decide
  trivial
#print axioms existsDifferentProof
#print axioms renamedBranch
#eval ("M16_legitimate_premise", profile existsDifferentProof)
end MatematicaAbierta.Continuo.RechazoContraejemploM15RCA
