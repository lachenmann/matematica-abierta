import MatematicaAbierta.Continuo.ContratosAdecuacionRCA

/-! M16 relative soundness by induction on every base and ordered constructor.
Primitive model laws are explicit premises. No canonical RCA₀ equivalence is claimed. -/
namespace MatematicaAbierta.Continuo.CorreccionCalculoOrdenRCA
open CalculoRCA InterpretacionParametricaRCA SustitucionSemanticaRCA
open AdecuacionLogicaOrdinariaRCA ContratosAdecuacionRCA
universe u v

theorem raw_sound {A : Type u} {S : Type v} (m : Signature A S)
    (eqs : EquationalContract m) (ord : OrderedContract m)
    (ind : InductionContract m) (comp : ComprehensionContract m)
    {Γ : List Formula} {p : Formula} (h : Derives Γ p) : Valid m Γ p := by
  induction h with
  | hypothesis hm => intro ρ σ hc; exact hc _ hm
  | botE h ih => intro ρ σ hc; exact False.elim (ih ρ σ hc)
  | weaken hw h ih => intro ρ σ hc; exact ih ρ σ (fun q hq => hc q (hw q hq))
  | impI h ih => intro ρ σ hc hp; exact ih ρ σ ((context_cons m ρ σ _ _).mpr ⟨hp,hc⟩)
  | impE h k ih ik => intro ρ σ hc; exact ih ρ σ hc (ik ρ σ hc)
  | andI h k ih ik => intro ρ σ hc; exact ⟨ih ρ σ hc,ik ρ σ hc⟩
  | andL h ih => intro ρ σ hc; exact (ih ρ σ hc).1
  | andR h ih => intro ρ σ hc; exact (ih ρ σ hc).2
  | allI x fresh h ih =>
    intro ρ σ hc a
    exact ih (Function.update ρ x a) σ ((context_number_fresh m _ ρ σ x a fresh).mpr hc)
  | allE x t safe h ih =>
    intro ρ σ hc
    exact (formula_substitution m _ x t ρ σ safe).mpr (ih ρ σ hc (term m ρ t))
  | allBI x b fresh free h ih => exact allBI_valid m _ _ x b fresh free ih
  | allBE x b t safe h k ih ik => exact allBE_valid m _ _ x b t safe ih ik
  | exBE x b fresh free boundFree h k ih ik => exact exBE_valid m _ _ _ x b fresh free boundFree ih ik
  | exBI x b t safe h k ih ik => exact exBI_valid m _ _ x b t safe ih ik
  | eqSymm h ih => intro ρ σ hc; exact (ih ρ σ hc).symm
  | eqAdd h k ih ik => intro ρ σ hc; exact congrArg₂ m.add (ih ρ σ hc) (ik ρ σ hc)
  | eqMul h k ih ik => intro ρ σ hc; exact congrArg₂ m.mul (ih ρ σ hc) (ik ρ σ hc)
  | leTrans h k ih ik => intro ρ σ hc; exact ord.leTrans _ _ _ (ih ρ σ hc) (ik ρ σ hc)
  | leAdd h k ih ik => intro ρ σ hc; exact ord.leAdd _ _ _ _ (ih ρ σ hc) (ik ρ σ hc)
  | leRewrite h k l ih ik il =>
    intro ρ σ hc
    have he := ih ρ σ hc
    have hf := ik ρ σ hc
    dsimp only [holds] at he hf
    simpa only [holds, he, hf] using il ρ σ hc
  | ltRewrite h k l ih ik il =>
    intro ρ σ hc
    have he := ih ρ σ hc
    have hf := ik ρ σ hc
    dsimp only [holds] at he hf
    simpa only [holds, he, hf] using il ρ σ hc
  | ltTrans h k ih ik => intro ρ σ hc; exact ord.ltTrans _ _ _ (ih ρ σ hc) (ik ρ σ hc)
  | ltLe h ih => intro ρ σ hc; exact ord.ltLe _ _ (ih ρ σ hc)
  | sigma1Induction x cls _ safeZero safeSucc h k ih ik =>
    exact induction_valid m ind _ _ x cls safeZero safeSucc ih ik
  | exNI x t safe h ih =>
    intro ρ σ hc
    exact ⟨term m ρ t,(formula_substitution m _ x t ρ σ safe).mp (ih ρ σ hc)⟩
  | arithmetic h => intro ρ σ _; exact equation_sound m eqs h ρ
  | leRefl t => intro ρ σ _; exact ord.leRefl (term m ρ t)
  | ltSucc t => intro ρ σ _; exact ord.ltSucc (term m ρ t)
  | ltZeroFalse t => intro ρ σ _ ht; exact ord.ltZeroFalse _ ht
  | delta1Comprehension x g sp pq _ pf qf h ih =>
    exact comprehension_valid m comp _ _ _ x g sp pq pf qf ih

theorem ordered_sound {A : Type u} {S : Type v} (m : Signature A S)
    (eqs : EquationalContract m) (ord : OrderedContract m)
    (ind : InductionContract m) (comp : ComprehensionContract m)
    {Γ : List Formula} {p : Formula} (h : CalculoOrdenRCA.Proof Γ p) : Valid m Γ p := by
  induction h with
  | hypothesis hm => intro ρ σ hc; exact hc _ hm
  | botE h ih => intro ρ σ hc; exact False.elim (ih ρ σ hc)
  | weaken hw h ih => intro ρ σ hc; exact ih ρ σ (fun q hq => hc q (hw q hq))
  | impI h ih => intro ρ σ hc hp; exact ih ρ σ ((context_cons m ρ σ _ _).mpr ⟨hp,hc⟩)
  | impE h k ih ik => intro ρ σ hc; exact ih ρ σ hc (ik ρ σ hc)
  | andI h k ih ik => intro ρ σ hc; exact ⟨ih ρ σ hc,ik ρ σ hc⟩
  | andL h ih => intro ρ σ hc; exact (ih ρ σ hc).1
  | andR h ih => intro ρ σ hc; exact (ih ρ σ hc).2
  | allI x fresh h ih =>
    intro ρ σ hc a
    exact ih (Function.update ρ x a) σ ((context_number_fresh m _ ρ σ x a fresh).mpr hc)
  | allE x t safe h ih =>
    intro ρ σ hc
    exact (formula_substitution m _ x t ρ σ safe).mpr (ih ρ σ hc (term m ρ t))
  | allBI x b fresh free h ih => exact allBI_valid m _ _ x b fresh free ih
  | allBE x b t safe h k ih ik => exact allBE_valid m _ _ x b t safe ih ik
  | exBE x b fresh free boundFree h k ih ik => exact exBE_valid m _ _ _ x b fresh free boundFree ih ik
  | exBI x b t safe h k ih ik => exact exBI_valid m _ _ x b t safe ih ik
  | eqSymm h ih => intro ρ σ hc; exact (ih ρ σ hc).symm
  | eqAdd h k ih ik => intro ρ σ hc; exact congrArg₂ m.add (ih ρ σ hc) (ik ρ σ hc)
  | eqMul h k ih ik => intro ρ σ hc; exact congrArg₂ m.mul (ih ρ σ hc) (ik ρ σ hc)
  | leTrans h k ih ik => intro ρ σ hc; exact ord.leTrans _ _ _ (ih ρ σ hc) (ik ρ σ hc)
  | leAdd h k ih ik => intro ρ σ hc; exact ord.leAdd _ _ _ _ (ih ρ σ hc) (ik ρ σ hc)
  | leRewrite h k l ih ik il =>
    intro ρ σ hc
    have he := ih ρ σ hc
    have hf := ik ρ σ hc
    dsimp only [holds] at he hf
    simpa only [holds, he, hf] using il ρ σ hc
  | ltRewrite h k l ih ik il =>
    intro ρ σ hc
    have he := ih ρ σ hc
    have hf := ik ρ σ hc
    dsimp only [holds] at he hf
    simpa only [holds, he, hf] using il ρ σ hc
  | ltTrans h k ih ik => intro ρ σ hc; exact ord.ltTrans _ _ _ (ih ρ σ hc) (ik ρ σ hc)
  | ltLe h ih => intro ρ σ hc; exact ord.ltLe _ _ (ih ρ σ hc)
  | sigma1Induction x cls _ safeZero safeSucc h k ih ik =>
    exact induction_valid m ind _ _ x cls safeZero safeSucc ih ik
  | embed h => exact raw_sound m eqs ord ind comp h
  | exBErename x y b fresh free boundFree safe ne bodyFresh h k ih ik =>
    exact renamed_exBE_valid m _ _ _ x y b ne fresh free boundFree safe bodyFresh ih ik
  | eqTrans h k ih ik => intro ρ σ hc; exact (ih ρ σ hc).trans (ik ρ σ hc)
  | eqSubst p x t r st sr h k ih ik =>
    intro ρ σ hc
    have hp := (formula_substitution m p x t ρ σ st).mp (ik ρ σ hc)
    have he : term m ρ t = term m ρ r := ih ρ σ hc
    rw [he] at hp
    exact (formula_substitution m p x r ρ σ sr).mpr hp
  | zeroLe t => intro ρ σ _; exact ord.zeroLe (term m ρ t)
  | leAntisymm h k ih ik => intro ρ σ hc; exact ord.leAntisymm _ _ (ih ρ σ hc) (ik ρ σ hc)
  | leMulRight t h ih => intro ρ σ hc; exact ord.leMulRight _ _ (term m ρ t) (ih ρ σ hc)
  | ltAddRight t h ih => intro ρ σ hc; exact ord.ltAddRight _ _ (term m ρ t) (ih ρ σ hc)
  | leLtTrans h k ih ik => intro ρ σ hc; exact ord.leLtTrans _ _ _ (ih ρ σ hc) (ik ρ σ hc)
  | ltLeTrans h k ih ik => intro ρ σ hc; exact ord.ltLeTrans _ _ _ (ih ρ σ hc) (ik ρ σ hc)
  | ltSuccLe h ih => intro ρ σ hc; exact ord.ltSuccLe _ _ (ih ρ σ hc)
  | succLeLt h ih => intro ρ σ hc; exact ord.succLeLt _ _ (ih ρ σ hc)
  | ltIrrefl h ih => intro ρ σ hc; exact ord.ltIrrefl _ (ih ρ σ hc)
  | addCancelLeft t h ih => intro ρ σ hc; exact ord.addCancelLeft (term m ρ t) _ _ (ih ρ σ hc)
  | orderCases t r h k l ih ik il =>
    intro ρ σ hc
    rcases ord.trichotomy (term m ρ t) (term m ρ r) with hl | he | hr
    · exact ih ρ σ ((context_cons m ρ σ _ _).mpr ⟨hl,hc⟩)
    · exact ik ρ σ ((context_cons m ρ σ _ _).mpr ⟨he,hc⟩)
    · exact il ρ σ ((context_cons m ρ σ _ _).mpr ⟨hr,hc⟩)

theorem no_closed_bottom_relative {A : Type u} {S : Type v} (m : Signature A S)
    (eqs : EquationalContract m) (ord : OrderedContract m)
    (ind : InductionContract m) (comp : ComprehensionContract m)
    (ρ : ℕ → A) (σ : ℕ → S) : ¬ Nonempty (CalculoOrdenRCA.Proof [] .bot) := by
  rintro ⟨h⟩
  exact ordered_sound m eqs ord ind comp h ρ σ (by intro p hp; exact False.elim (List.not_mem_nil hp))

#print axioms raw_sound
#print axioms ordered_sound
#print axioms no_closed_bottom_relative
end MatematicaAbierta.Continuo.CorreccionCalculoOrdenRCA
