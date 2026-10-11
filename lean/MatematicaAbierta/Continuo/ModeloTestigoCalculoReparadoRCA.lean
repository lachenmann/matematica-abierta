import MatematicaAbierta.Continuo.CorreccionCalculoOrdenRCA

/-! A model witness for consistency. Adequacy itself is parametric in M16.
This does not identify the repaired calculus with canonical RCA₀. -/
namespace MatematicaAbierta.Continuo.ModeloTestigoCalculoReparadoRCA
open CalculoRCA InterpretacionParametricaRCA ContratosAdecuacionRCA CorreccionCalculoOrdenRCA
def naturalSignature : Signature ℕ (Set ℕ) :=
  ⟨id,Nat.succ,Nat.add,Nat.mul,(· ≤ ·),(· < ·),(· ∈ ·)⟩
theorem equational : EquationalContract naturalSignature := by
  exact {
    numeralSucc _ := rfl,
    addZero := Nat.add_zero,
    addSucc := Nat.add_succ,
    mulZero := Nat.mul_zero,
    mulSucc := Nat.mul_succ,
    addComm := Nat.add_comm,
    addAssoc := Nat.add_assoc,
    mulComm := Nat.mul_comm,
    mulAssoc := Nat.mul_assoc,
    distrib := Nat.mul_add }
theorem ordered : OrderedContract naturalSignature := by
  exact {
    leRefl := Nat.le_refl,
    leTrans _ _ _ := Nat.le_trans,
    leAdd _ _ _ _ := Nat.add_le_add,
    ltSucc := Nat.lt_succ_self,
    ltZeroFalse := Nat.not_lt_zero,
    ltTrans _ _ _ := Nat.lt_trans,
    ltLe _ _ := Nat.le_of_lt,
    zeroLe := Nat.zero_le,
    leAntisymm _ _ := Nat.le_antisymm,
    leMulRight _ _ _ := Nat.mul_le_mul_right _,
    ltAddRight _ _ c h := Nat.add_lt_add_right h c,
    leLtTrans _ _ _ := Nat.lt_of_le_of_lt,
    ltLeTrans _ _ _ := Nat.lt_of_lt_of_le,
    ltSuccLe _ _ := Nat.succ_le_of_lt,
    succLeLt _ _ := Nat.lt_of_succ_le,
    ltIrrefl := Nat.lt_irrefl,
    addCancelLeft _ _ _ := Nat.add_left_cancel,
    trichotomy := Nat.lt_trichotomy }
theorem induction : InductionContract naturalSignature := by
  intro p x ρ σ _ h0 hs n
  induction n with
  | zero => exact h0
  | succ n ih => exact hs n ih
theorem comprehension : ComprehensionContract naturalSignature := by
  intro p _ x _ ρ σ _ _ _ _ _
  exact ⟨{a | holds naturalSignature (Function.update ρ x a) σ p},fun _ => Iff.rfl⟩
theorem no_closed_bottom : ¬ Nonempty (CalculoOrdenRCA.Proof [] .bot) :=
  no_closed_bottom_relative naturalSignature equational ordered induction comprehension
    (fun _ => 0) (fun _ => ∅)
#print axioms equational
#print axioms ordered
#print axioms induction
#print axioms comprehension
#print axioms no_closed_bottom
end MatematicaAbierta.Continuo.ModeloTestigoCalculoReparadoRCA
