import MatematicaAbierta.Continuo.InterpretacionParametricaRCA

/-! M15: coincidence on free variables, freshness, guarded substitution.
Works in arbitrary signatures and both domains; no model axioms are needed. -/
namespace MatematicaAbierta.Continuo.SustitucionSemanticaRCA
open CalculoRCA InterpretacionParametricaRCA
universe u v

def Agree {D : Type u} (xs : List ℕ) (ρ τ : ℕ → D) : Prop := ∀ x ∈ xs, ρ x = τ x
theorem agree_left {D : Type u} {xs ys : List ℕ} {ρ τ : ℕ → D}
    (h : Agree (xs++ys) ρ τ) : Agree xs ρ τ := fun x hx => h x (List.mem_append_left _ hx)
theorem agree_right {D : Type u} {xs ys : List ℕ} {ρ τ : ℕ → D}
    (h : Agree (xs++ys) ρ τ) : Agree ys ρ τ := fun x hx => h x (List.mem_append_right _ hx)
theorem agree_update {D : Type u} (xs : List ℕ) (x : ℕ) (ρ τ : ℕ → D) (a : D)
    (h : Agree (xs.filter (· != x)) ρ τ) : Agree xs (Function.update ρ x a) (Function.update τ x a) := by
  intro y hy
  by_cases he : y=x
  · simp [he]
  · simpa [he] using h y (by simp [hy,he])

theorem formula_coincidence {A : Type u} {S : Type v} (m : Signature A S) (p : Formula)
    (ρ τ : ℕ → A) (σ π : ℕ → S)
    (hn : Agree p.numFree ρ τ) (hs : Agree p.setFree σ π) : holds m ρ σ p ↔ holds m τ π p := by
  induction p generalizing ρ τ σ π with
  | bot => rfl
  | eq t r | le t r | lt t r =>
    have ht := term_coincidence m t ρ τ (agree_left hn)
    have hr := term_coincidence m r ρ τ (agree_right hn)
    simp only [holds,ht,hr]
  | member t g =>
    have ht := term_coincidence m t ρ τ hn
    have hg : σ g = π g := hs g (by simp [Formula.setFree])
    simp only [holds,ht,hg]
  | conj p q ip iq =>
    exact and_congr (ip _ _ _ _ (agree_left hn) (agree_left hs))
      (iq _ _ _ _ (agree_right hn) (agree_right hs))
  | imp p q ip iq =>
    exact imp_congr (ip _ _ _ _ (agree_left hn) (agree_left hs))
      (iq _ _ _ _ (agree_right hn) (agree_right hs))
  | allN x p ih =>
    exact forall_congr' fun a => ih _ _ _ _ (agree_update _ x ρ τ a hn) hs
  | exN x p ih =>
    exact exists_congr fun a => ih _ _ _ _ (agree_update _ x ρ τ a hn) hs
  | allB x b p ih =>
    have hb := term_coincidence m b ρ τ (agree_left hn)
    change (∀ a, m.lt a (term m ρ b) → _) ↔ (∀ a, m.lt a (term m τ b) → _)
    rw [hb]
    exact forall_congr' fun a => imp_congr Iff.rfl (ih _ _ _ _ (agree_update _ x ρ τ a (agree_right hn)) hs)
  | exB x b p ih =>
    have hb := term_coincidence m b ρ τ (agree_left hn)
    change (∃ a, m.lt a (term m ρ b) ∧ _) ↔ (∃ a, m.lt a (term m τ b) ∧ _)
    rw [hb]
    exact exists_congr fun a => and_congr Iff.rfl (ih _ _ _ _ (agree_update _ x ρ τ a (agree_right hn)) hs)
  | exS g p ih =>
    exact exists_congr fun X => ih _ _ _ _ hn (agree_update _ g σ π X hs)

theorem number_fresh {A : Type u} {S : Type v} (m : Signature A S) (p : Formula)
    (ρ : ℕ → A) (σ : ℕ → S) (x : ℕ) (a : A) (h : p.numFree.contains x = false) :
    holds m (Function.update ρ x a) σ p ↔ holds m ρ σ p := by
  apply formula_coincidence
  · intro y hy
    have hx : x ∉ p.numFree := by simpa using h
    have he : y≠x := by intro e; subst y; exact hx hy
    simp [he]
  · exact fun _ _ => rfl

theorem set_fresh {A : Type u} {S : Type v} (m : Signature A S) (p : Formula)
    (ρ : ℕ → A) (σ : ℕ → S) (g : ℕ) (X : S) (h : p.setFree.contains g = false) :
    holds m ρ (Function.update σ g X) p ↔ holds m ρ σ p := by
  apply formula_coincidence
  · exact fun _ _ => rfl
  · intro y hy
    have hx : g ∉ p.setFree := by simpa using h
    have he : y≠g := by intro e; subst y; exact hx hy
    simp [he]

theorem context_number_fresh {A : Type u} {S : Type v} (m : Signature A S) (Γ : List Formula)
    (ρ : ℕ → A) (σ : ℕ → S) (x : ℕ) (a : A) (h : freshNum x Γ = true) :
    context m (Function.update ρ x a) σ Γ ↔ context m ρ σ Γ := by
  have hf : ∀ p ∈ Γ, p.numFree.contains x = false := by simpa [freshNum] using h
  constructor <;> intro hc p hp
  · exact (number_fresh m p ρ σ x a (hf p hp)).mp (hc p hp)
  · exact (number_fresh m p ρ σ x a (hf p hp)).mpr (hc p hp)
theorem context_set_fresh {A : Type u} {S : Type v} (m : Signature A S) (Γ : List Formula)
    (ρ : ℕ → A) (σ : ℕ → S) (g : ℕ) (X : S) (h : freshSet g Γ = true) :
    context m ρ (Function.update σ g X) Γ ↔ context m ρ σ Γ := by
  have hf : ∀ p ∈ Γ, p.setFree.contains g = false := by simpa [freshSet] using h
  constructor <;> intro hc p hp
  · exact (set_fresh m p ρ σ g X (hf p hp)).mp (hc p hp)
  · exact (set_fresh m p ρ σ g X (hf p hp)).mpr (hc p hp)

theorem formula_substitution {A : Type u} {S : Type v} (m : Signature A S) (p : Formula)
    (x : ℕ) (r : Term) (ρ : ℕ → A) (σ : ℕ → S) (h : p.safe x r = true) :
    holds m ρ σ (p.subst x r) ↔ holds m (Function.update ρ x (term m ρ r)) σ p := by
  induction p generalizing ρ σ with
  | bot => rfl
  | eq t b | le t b | lt t b => simp only [Formula.subst,holds,term_substitution]
  | member t g => simp only [Formula.subst,holds,term_substitution]
  | conj p q ip iq =>
    have hg : p.safe x r = true ∧ q.safe x r = true := by simpa [Formula.safe] using h
    exact and_congr (ip ρ σ hg.1) (iq ρ σ hg.2)
  | imp p q ip iq =>
    have hg : p.safe x r = true ∧ q.safe x r = true := by simpa [Formula.safe] using h
    exact imp_congr (ip ρ σ hg.1) (iq ρ σ hg.2)
  | allN y p ih =>
    by_cases hy : y=x
    · subst y; simp only [Formula.subst,ite_true,holds,update_shadow]
    · have hg : r.vars.contains y = false ∧ p.safe x r = true := by simpa [Formula.safe,hy] using h
      simp only [Formula.subst,ite_eq_right hy,holds]
      apply forall_congr'; intro a
      have hi := ih (Function.update ρ y a) σ hg.2
      rw [term_fresh m r ρ y a hg.1, ← update_commute ρ x y (term m ρ r) a (Ne.symm hy)] at hi
      exact hi
  | exN y p ih =>
    by_cases hy : y=x
    · subst y; simp only [Formula.subst,ite_true,holds,update_shadow]
    · have hg : r.vars.contains y = false ∧ p.safe x r = true := by simpa [Formula.safe,hy] using h
      simp only [Formula.subst,ite_eq_right hy,holds]
      apply exists_congr; intro a
      have hi := ih (Function.update ρ y a) σ hg.2
      rw [term_fresh m r ρ y a hg.1, ← update_commute ρ x y (term m ρ r) a (Ne.symm hy)] at hi
      exact hi
  | allB y b p ih =>
    by_cases hy : y=x
    · subst y; simp only [Formula.subst,ite_true,holds,term_substitution,update_shadow]
    · have hg : r.vars.contains y = false ∧ p.safe x r = true := by simpa [Formula.safe,hy] using h
      simp only [Formula.subst,ite_eq_right hy,holds,term_substitution]
      apply forall_congr'; intro a
      apply imp_congr Iff.rfl
      have hi := ih (Function.update ρ y a) σ hg.2
      rw [term_fresh m r ρ y a hg.1, ← update_commute ρ x y (term m ρ r) a (Ne.symm hy)] at hi
      exact hi
  | exB y b p ih =>
    by_cases hy : y=x
    · subst y; simp only [Formula.subst,ite_true,holds,term_substitution,update_shadow]
    · have hg : r.vars.contains y = false ∧ p.safe x r = true := by simpa [Formula.safe,hy] using h
      simp only [Formula.subst,ite_eq_right hy,holds,term_substitution]
      apply exists_congr; intro a
      apply and_congr Iff.rfl
      have hi := ih (Function.update ρ y a) σ hg.2
      rw [term_fresh m r ρ y a hg.1, ← update_commute ρ x y (term m ρ r) a (Ne.symm hy)] at hi
      exact hi
  | exS g p ih =>
    exact exists_congr fun X => ih ρ (Function.update σ g X) h

theorem guarded_number_rename {A : Type u} {S : Type v} (m : Signature A S) (p : Formula)
    (x y : ℕ) (ρ : ℕ → A) (σ : ℕ → S) (h : p.safe x (.var y) = true) :
    holds m ρ σ (p.subst x (.var y)) ↔ holds m (Function.update ρ x (ρ y)) σ p :=
  formula_substitution m p x (.var y) ρ σ h

theorem rename_update {D : Type u} (σ : ℕ → D) (f : ℕ → ℕ) (hi : Function.Injective f) (g : ℕ) (X : D) :
    (Function.update σ (f g) X) ∘ f = Function.update (σ ∘ f) g X := by
  funext y
  by_cases hy : y=g
  · simp [Function.comp_def,hy]
  · have hf : f y ≠ f g := fun e => hy (hi e)
    simp [Function.comp_def,hy,hf]

theorem set_renaming {A : Type u} {S : Type v} (m : Signature A S) (p : Formula)
    (f : ℕ → ℕ) (hi : Function.Injective f) (ρ : ℕ → A) (σ : ℕ → S) :
    holds m ρ σ (RenombradoConjuntosRCA.rename f p) ↔ holds m ρ (σ ∘ f) p := by
  induction p generalizing ρ σ with
  | exS g p ih =>
    simp only [RenombradoConjuntosRCA.rename,holds]
    apply exists_congr; intro X
    have h := ih ρ (Function.update σ (f g) X)
    rw [rename_update σ f hi g X] at h
    exact h
  | _ => simp_all [RenombradoConjuntosRCA.rename,holds,Function.comp_def]

theorem alpha_body {A : Type u} {S : Type v} (m : Signature A S) (p : Formula)
    (x y : ℕ) (ρ : ℕ → A) (σ : ℕ → S) (a : A) (hne : x≠y)
    (safe : p.safe x (.var y) = true) (fresh : p.numFree.contains y = false) :
    holds m (Function.update ρ y a) σ (p.subst x (.var y)) ↔ holds m (Function.update ρ x a) σ p := by
  have h := formula_substitution m p x (.var y) (Function.update ρ y a) σ safe
  simp only [term,Function.update_self] at h
  rw [← update_commute ρ x y a a hne] at h
  exact h.trans (number_fresh m p (Function.update ρ x a) σ y a fresh)
theorem alpha_exists {A : Type u} {S : Type v} (m : Signature A S) (p : Formula)
    (x y : ℕ) (ρ : ℕ → A) (σ : ℕ → S) (hne : x≠y)
    (safe : p.safe x (.var y) = true) (fresh : p.numFree.contains y = false) :
    holds m ρ σ (.exN y (p.subst x (.var y))) ↔ holds m ρ σ (.exN x p) :=
  exists_congr fun a => alpha_body m p x y ρ σ a hne safe fresh

#print axioms set_renaming
#print axioms alpha_body
#print axioms alpha_exists

example : (Formula.allN 2 (.eq (.var 1) (.var 2))).safe 1 (.var 2) = false := rfl
example : (Formula.allN 2 (.eq (.var 1) (.var 2))).safe 1 (.var 3) = true := rfl
example : (Formula.allB 1 (.var 1) (.eq (.var 1) (.lit 0))).numFree = [1] := rfl
example : (Formula.exS 2 (.member (.var 2) 2)).numFree = [2] := rfl
example : (Formula.exS 2 (.member (.var 2) 2)).setFree = [] := rfl
#print axioms formula_substitution
#print axioms guarded_number_rename

#print axioms formula_coincidence
#print axioms number_fresh
#print axioms set_fresh
#print axioms context_number_fresh
#print axioms context_set_fresh
end MatematicaAbierta.Continuo.SustitucionSemanticaRCA
