import MatematicaAbierta.Continuo.AuditoriaGuardaRenombradoRCA

/-! M15: sufficient guarded rule contracts and remaining theory obligations.
These structures are explicit contracts, NOT axioms and NOT inhabited here.
Semantic validity and independent derivation transport are distinct types. -/
namespace MatematicaAbierta.Continuo.ContratosAdecuacionRCA
open CalculoRCA InterpretacionParametricaRCA SustitucionSemanticaRCA AdecuacionLogicaOrdinariaRCA
universe u v w

theorem allBI_valid {A : Type u} {S : Type v} (m : Signature A S) (Γ : List Formula) (p : Formula)
    (x : ℕ) (b : Term) (fresh : freshNum x Γ = true) (free : b.vars.contains x = false)
    (h : Valid m (.lt (.var x) b::Γ) p) : Valid m Γ (.allB x b p) := by
  intro ρ σ hc a ha
  have hb : holds m (Function.update ρ x a) σ (.lt (.var x) b) := by
    simpa only [holds,term,Function.update_self,term_fresh m b ρ x a free] using ha
  exact h _ σ ((context_cons m _ σ _ _).mpr ⟨hb,(context_number_fresh m Γ ρ σ x a fresh).mpr hc⟩)
theorem allBE_valid {A : Type u} {S : Type v} (m : Signature A S) (Γ : List Formula) (p : Formula)
    (x : ℕ) (b t : Term) (safe : p.safe x t = true)
    (h : Valid m Γ (.allB x b p)) (hb : Valid m Γ (.lt t b)) : Valid m Γ (p.subst x t) := by
  intro ρ σ hc
  exact (formula_substitution m p x t ρ σ safe).mpr (h ρ σ hc _ (hb ρ σ hc))
theorem exBI_valid {A : Type u} {S : Type v} (m : Signature A S) (Γ : List Formula) (p : Formula)
    (x : ℕ) (b t : Term) (safe : p.safe x t = true)
    (hb : Valid m Γ (.lt t b)) (h : Valid m Γ (p.subst x t)) : Valid m Γ (.exB x b p) := by
  intro ρ σ hc
  exact ⟨term m ρ t,hb ρ σ hc,(formula_substitution m p x t ρ σ safe).mp (h ρ σ hc)⟩
theorem exBE_valid {A : Type u} {S : Type v} (m : Signature A S) (Γ : List Formula) (p q : Formula)
    (x : ℕ) (b : Term) (fresh : freshNum x Γ = true) (free : q.numFree.contains x = false)
    (boundFree : b.vars.contains x = false) (h : Valid m Γ (.exB x b p))
    (branch : Valid m (p::.lt (.var x) b::Γ) q) : Valid m Γ q := by
  intro ρ σ hc
  obtain ⟨a,ha,hp⟩ := h ρ σ hc
  have hb : holds m (Function.update ρ x a) σ (.lt (.var x) b) := by
    simpa only [holds,term,Function.update_self,term_fresh m b ρ x a boundFree] using ha
  have hq := branch _ σ ((context_cons m _ σ _ _).mpr ⟨hp,
    (context_cons m _ σ _ _).mpr ⟨hb,(context_number_fresh m Γ ρ σ x a fresh).mpr hc⟩⟩)
  exact (number_fresh m q ρ σ x a free).mp hq

-- This theorem needs the missing body guard; it does not alter M06.
theorem renamed_exBE_valid {A : Type u} {S : Type v} (m : Signature A S) (Γ : List Formula) (p q : Formula)
    (x y : ℕ) (b : Term) (hne : x≠y) (fresh : freshNum y Γ = true)
    (free : q.numFree.contains y = false) (boundFree : b.vars.contains y = false)
    (safe : p.safe x (.var y) = true) (bodyFresh : p.numFree.contains y = false)
    (h : Valid m Γ (.exB x b p)) (branch : Valid m (p.subst x (.var y)::.lt (.var y) b::Γ) q) : Valid m Γ q := by
  intro ρ σ hc
  obtain ⟨a,ha,hp⟩ := h ρ σ hc
  have hbody := (alpha_body m p x y ρ σ a hne safe bodyFresh).mpr hp
  have hb : holds m (Function.update ρ y a) σ (.lt (.var y) b) := by
    simpa only [holds,term,Function.update_self,term_fresh m b ρ y a boundFree] using ha
  have hq := branch _ σ ((context_cons m _ σ _ _).mpr ⟨hbody,
    (context_cons m _ σ _ _).mpr ⟨hb,(context_number_fresh m Γ ρ σ y a fresh).mpr hc⟩⟩)
  exact (number_fresh m q ρ σ y a free).mp hq

structure EquationalContract {A : Type u} {S : Type v} (m : Signature A S) : Prop where
  numeralSucc : ∀ n, m.numeral (n+1) = m.succ (m.numeral n)
  addZero : ∀ a, m.add a (m.numeral 0) = a
  addSucc : ∀ a b, m.add a (m.succ b) = m.succ (m.add a b)
  mulZero : ∀ a, m.mul a (m.numeral 0) = m.numeral 0
  mulSucc : ∀ a b, m.mul a (m.succ b) = m.add (m.mul a b) a
  addComm : ∀ a b, m.add a b = m.add b a
  addAssoc : ∀ a b c, m.add (m.add a b) c = m.add a (m.add b c)
  mulComm : ∀ a b, m.mul a b = m.mul b a
  mulAssoc : ∀ a b c, m.mul (m.mul a b) c = m.mul a (m.mul b c)
  distrib : ∀ a b c, m.mul a (m.add b c) = m.add (m.mul a b) (m.mul a c)

theorem equation_sound {A : Type u} {S : Type v} (m : Signature A S) (laws : EquationalContract m)
    {t r : Term} (h : EqProof t r) (ρ : ℕ → A) : term m ρ t = term m ρ r := by
  induction h with
  | refl _ => rfl
  | symm _ ih => exact ih.symm
  | trans _ _ ih ik => exact ih.trans ik
  | succ _ ih => exact congrArg m.succ ih
  | add _ _ ih ik => exact congrArg₂ m.add ih ik
  | mul _ _ ih ik => exact congrArg₂ m.mul ih ik
  | literalSucc n => exact laws.numeralSucc n
  | addZero t => exact laws.addZero _
  | addSucc t r => exact laws.addSucc _ _
  | mulZero t => exact laws.mulZero _
  | mulSucc t r => exact laws.mulSucc _ _
  | addComm t r => exact laws.addComm _ _
  | addAssoc t r s => exact laws.addAssoc _ _ _
  | mulComm t r => exact laws.mulComm _ _
  | mulAssoc t r s => exact laws.mulAssoc _ _ _
  | distrib t r s => exact laws.distrib _ _ _

structure OrderedContract {A : Type u} {S : Type v} (m : Signature A S) : Prop where
  leRefl : ∀ a, m.le a a
  leTrans : ∀ a b c, m.le a b → m.le b c → m.le a c
  leAdd : ∀ a b c d, m.le a b → m.le c d → m.le (m.add a c) (m.add b d)
  ltSucc : ∀ a, m.lt a (m.succ a)
  ltZeroFalse : ∀ a, ¬ m.lt a (m.numeral 0)
  ltTrans : ∀ a b c, m.lt a b → m.lt b c → m.lt a c
  ltLe : ∀ a b, m.lt a b → m.le a b
  zeroLe : ∀ a, m.le (m.numeral 0) a
  leAntisymm : ∀ a b, m.le a b → m.le b a → a=b
  leMulRight : ∀ a b c, m.le a b → m.le (m.mul a c) (m.mul b c)
  ltAddRight : ∀ a b c, m.lt a b → m.lt (m.add a c) (m.add b c)
  leLtTrans : ∀ a b c, m.le a b → m.lt b c → m.lt a c
  ltLeTrans : ∀ a b c, m.lt a b → m.le b c → m.lt a c
  ltSuccLe : ∀ a b, m.lt a b → m.le (m.succ a) b
  succLeLt : ∀ a b, m.le (m.succ a) b → m.lt a b
  ltIrrefl : ∀ a, ¬ m.lt a a
  addCancelLeft : ∀ a b c, m.add a b = m.add a c → b=c
  trichotomy : ∀ a b, m.lt a b ∨ a=b ∨ m.lt b a

-- Model axiom SCHEMES, not soundness axioms for proof trees.
def InductionContract {A : Type u} {S : Type v} (m : Signature A S) : Prop :=
  ∀ (p : Formula) (x : ℕ) (ρ : ℕ → A) (σ : ℕ → S), Nonempty (Sigma1 p) →
    holds m (Function.update ρ x (m.numeral 0)) σ p →
    (∀ a, holds m (Function.update ρ x a) σ p → holds m (Function.update ρ x (m.succ a)) σ p) →
    ∀ a, holds m (Function.update ρ x a) σ p

def ComprehensionContract {A : Type u} {S : Type v} (m : Signature A S) : Prop :=
  ∀ (p q : Formula) (x g : ℕ) (ρ : ℕ → A) (σ : ℕ → S),
    Nonempty (Sigma1 p) → Nonempty (Pi1 q) →
    p.setFree.contains g = false → q.setFree.contains g = false →
    (∀ a, holds m (Function.update ρ x a) σ p ↔ holds m (Function.update ρ x a) σ q) →
    ∃ X : S, ∀ a, m.member a X ↔ holds m (Function.update ρ x a) σ p

theorem induction_valid {A : Type u} {S : Type v} (m : Signature A S) (law : InductionContract m)
    (Γ : List Formula) (p : Formula) (x : ℕ) (cls : Sigma1 p)
    (safeZero : p.safe x (.lit 0) = true) (safeSucc : p.safe x (.succ (.var x)) = true)
    (base : Valid m Γ (p.subst x (.lit 0)))
    (step : Valid m Γ (.allN x (.imp p (p.subst x (.succ (.var x)))))) : Valid m Γ (.allN x p) := by
  intro ρ σ hc
  apply law p x ρ σ ⟨cls⟩
  · exact (formula_substitution m p x (.lit 0) ρ σ safeZero).mp (base ρ σ hc)
  · intro a ha
    have hs := step ρ σ hc a ha
    have ht := (formula_substitution m p x (.succ (.var x)) (Function.update ρ x a) σ safeSucc).mp hs
    simpa only [term,Function.update_self,update_shadow] using ht

theorem comprehension_valid {A : Type u} {S : Type v} (m : Signature A S) (law : ComprehensionContract m)
    (Γ : List Formula) (p q : Formula) (x g : ℕ) (sp : Sigma1 p) (pq : Pi1 q)
    (pFree : p.setFree.contains g = false) (qFree : q.setFree.contains g = false)
    (equiv : Valid m Γ (.allN x (iffF p q))) :
    Valid m Γ (.exS g (.allN x (iffF (.member (.var x) g) p))) := by
  intro ρ σ hc
  have he : ∀ a, holds m (Function.update ρ x a) σ p ↔ holds m (Function.update ρ x a) σ q := by
    intro a
    exact ⟨(equiv ρ σ hc a).1,(equiv ρ σ hc a).2⟩
  obtain ⟨X,hX⟩ := law p q x g ρ σ ⟨sp⟩ ⟨pq⟩ pFree qFree he
  refine ⟨X,?_⟩
  intro a
  have hp := set_fresh m p (Function.update ρ x a) σ g X pFree
  have ha := (hX a).trans hp.symm
  simpa only [holds,iffF,term,Function.update_self] using And.intro ha.mp ha.mpr

#print axioms induction_valid
#print axioms comprehension_valid

structure SetDomainContract {A : Type u} {S : Type v} (m : Signature A S) : Prop where
  nonempty : Nonempty S
  extensional : ∀ X Y, (∀ a, m.member a X ↔ m.member a Y) → X=Y

-- Independent proof objects are abstract here. No target is instantiated,
-- no translation/soundness axiom is provided, and no preservation is claimed.
structure IndependentPresentation where
  formula : Type w
  derivation : List formula → formula → Type w
  encode : Formula → formula

def PreservationContract (target : IndependentPresentation) : Prop :=
  ∀ (Γ : List Formula) (p : Formula), LogicaClasicaOrdinariaRCA.Proof Γ p →
    Nonempty (target.derivation (Γ.map target.encode) (target.encode p))

example : AuditoriaGuardaRenombradoRCA.different.numFree.contains 171 = true := rfl
example : (Formula.allN 171 AuditoriaGuardaRenombradoRCA.different).numFree.contains 171 = false := rfl
#print axioms allBI_valid
#print axioms allBE_valid
#print axioms exBI_valid
#print axioms exBE_valid
#print axioms renamed_exBE_valid
#print axioms equation_sound
end MatematicaAbierta.Continuo.ContratosAdecuacionRCA
