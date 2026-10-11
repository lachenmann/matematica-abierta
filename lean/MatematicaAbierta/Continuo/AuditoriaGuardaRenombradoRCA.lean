import MatematicaAbierta.Continuo.AdecuacionLogicaOrdinariaRCA

/-! M15: a concrete rejected constructor instance. This is an audit witness,
not a rule used to justify any new mathematical result. M05--M14 unchanged.
exBErename lacks freshness of the target variable for the existential body. -/
namespace MatematicaAbierta.Continuo.AuditoriaGuardaRenombradoRCA
open CalculoRCA CalculoOrdenRCA InterpretacionParametricaRCA
open GraficaBitsAcotadosRCA

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

/-- Audit-only effective contradiction tree admitted by the frozen syntax. -/
def rejectedClosedTree : Proof [] .bot :=
  .exBErename 170 171 (.lit 2) rfl rfl rfl rfl existsDifferentProof renamedBranch

-- A concrete signature gives a countermodel, not a standard-model-only
-- adequacy argument. The other M15 theorems quantify arbitrary signatures.
def naturalSignature : Signature ℕ (Set ℕ) :=
  ⟨id,Nat.succ,Nat.add,Nat.mul,(· ≤ ·),(· < ·),(· ∈ ·)⟩
def zeroEnvironment : ℕ → ℕ := fun _ => 0
def emptyEnvironment : ℕ → Set ℕ := fun _ => ∅

theorem bottom_invalid : ¬ Valid naturalSignature [] .bot := by
  intro h
  exact h zeroEnvironment emptyEnvironment (by intro p hp; exact False.elim (List.not_mem_nil hp))
theorem no_global_order_soundness :
    ¬ (∀ (Γ : List Formula) (p : Formula), Proof Γ p → Valid naturalSignature Γ p) := by
  intro h
  exact bottom_invalid (h [] .bot rejectedClosedTree)

#print axioms existsDifferentProof
#print axioms renamedBranch
#print axioms rejectedClosedTree
#print axioms bottom_invalid
#print axioms no_global_order_soundness
#eval ("M15_rejected_closed_tree", profile rejectedClosedTree)
end MatematicaAbierta.Continuo.AuditoriaGuardaRenombradoRCA
