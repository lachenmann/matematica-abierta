import MatematicaAbierta.Continuo.CRTFinitoUniformeRCA

/-! M12: structural, injective renaming of set names. Number terms are
unchanged. This is a transformation of ordinary proof trees, not a new rule
for set substitution, comprehension, CRT or code existence. -/
namespace MatematicaAbierta.Continuo.RenombradoConjuntosRCA
open CalculoRCA

def rename (ρ : ℕ → ℕ) : Formula → Formula
  | .bot => .bot
  | .eq t u => .eq t u
  | .le t u => .le t u
  | .lt t u => .lt t u
  | .member t g => .member t (ρ g)
  | .conj p q => .conj (rename ρ p) (rename ρ q)
  | .imp p q => .imp (rename ρ p) (rename ρ q)
  | .allN x p => .allN x (rename ρ p)
  | .exN x p => .exN x (rename ρ p)
  | .allB x t p => .allB x t (rename ρ p)
  | .exB x t p => .exB x t (rename ρ p)
  | .exS g p => .exS (ρ g) (rename ρ p)

@[simp] theorem numFree (ρ : ℕ → ℕ) (p : Formula) :
    (rename ρ p).numFree = p.numFree := by
  induction p <;> simp_all [rename, Formula.numFree]
@[simp] theorem safe (ρ : ℕ → ℕ) (p : Formula) (x : ℕ) (t : Term) :
    (rename ρ p).safe x t = p.safe x t := by
  induction p <;> simp_all [rename, Formula.safe]
@[simp] theorem subst (ρ : ℕ → ℕ) (p : Formula) (x : ℕ) (t : Term) :
    rename ρ (p.subst x t) = (rename ρ p).subst x t := by
  induction p <;> simp_all [rename, Formula.subst] <;> split <;> simp_all
@[simp] theorem bounded (ρ : ℕ → ℕ) (p : Formula) :
    (rename ρ p).bounded = p.bounded := by
  induction p <;> simp_all [rename, Formula.bounded]
@[simp] theorem freshNumMap (ρ : ℕ → ℕ) (Γ : List Formula) (x : ℕ) :
    freshNum x (Γ.map (rename ρ)) = freshNum x Γ := by
  induction Γ <;> simp_all [freshNum]

theorem containsInjective (ρ : ℕ → ℕ) (hi : Function.Injective ρ)
    (l : List ℕ) (g : ℕ) : (l.map ρ).contains (ρ g) = l.contains g := by
  induction l with
  | nil => rfl
  | cons a l ih =>
    simp only [List.map_cons, List.contains_cons, ih]
    have he : (ρ g == ρ a) = (g == a) := by
      apply Bool.eq_iff_iff.mpr
      simp only [beq_iff_eq]
      exact ⟨fun h => hi h, congrArg ρ⟩
    rw [he]

theorem setFree (ρ : ℕ → ℕ) (hi : Function.Injective ρ) (p : Formula) :
    (rename ρ p).setFree = p.setFree.map ρ := by
  induction p with
  | exS g p ih =>
    simp only [rename, Formula.setFree, ih, List.filter_map, Function.comp_def]
    congr 1
    apply congrArg (fun f => List.filter f p.setFree)
    funext a
    have he : (ρ a != ρ g) = (a != g) := by
      have e : (ρ a == ρ g) = (a == g) := by
        apply Bool.eq_iff_iff.mpr
        simp only [beq_iff_eq]
        exact ⟨fun h => hi h, congrArg ρ⟩
      exact congrArg Bool.not e
    exact he
  | _ => simp_all [rename, Formula.setFree]

theorem freshSetMap (ρ : ℕ → ℕ) (hi : Function.Injective ρ)
    (Γ : List Formula) (g : ℕ) :
    freshSet (ρ g) (Γ.map (rename ρ)) = freshSet g Γ := by
  induction Γ with
  | nil => rfl
  | cons p Γ ih =>
    simp only [freshSet, List.map_cons, List.all_cons] at ih ⊢
    rw [setFree ρ hi, containsInjective ρ hi, ih]

def sigma (ρ : ℕ → ℕ) {p : Formula} : Sigma1 p → Sigma1 (rename ρ p)
  | .bounded h => .bounded ((bounded ρ p).trans h)
  | .exists x h => .exists x (sigma ρ h)
def pi (ρ : ℕ → ℕ) {p : Formula} : Pi1 p → Pi1 (rename ρ p)
  | .bounded h => .bounded ((bounded ρ p).trans h)
  | .forall x h => .forall x (pi ρ h)

def raw (ρ : ℕ → ℕ) (hi : Function.Injective ρ)
    {Γ : List Formula} {p : Formula} : Derives Γ p →
    Derives (Γ.map (rename ρ)) (rename ρ p)
  | .hypothesis hm => by
    simpa only [rename, subst, List.map_cons] using Derives.hypothesis (List.mem_map_of_mem hm)
  | .botE h => by
    simpa only [rename, subst, List.map_cons] using Derives.botE (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .weaken hw h => by
    simpa only [rename, subst, List.map_cons] using Derives.weaken (fun f hf => by
      obtain ⟨q,hq,rfl⟩ := List.mem_map.mp hf
      exact List.mem_map_of_mem (hw q hq)) (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .impI h => by
    simpa only [rename, subst, List.map_cons] using Derives.impI (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .impE h k => by
    simpa only [rename, subst, List.map_cons] using Derives.impE (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .andI h k => by
    simpa only [rename, subst, List.map_cons] using Derives.andI (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .andL h => by
    simpa only [rename, subst, List.map_cons] using Derives.andL (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .andR h => by
    simpa only [rename, subst, List.map_cons] using Derives.andR (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .allI x f h => by
    simpa only [rename, subst, List.map_cons] using Derives.allI x (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .allE x t f h => by
    simpa only [rename, subst, List.map_cons] using Derives.allE x t (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .exNI x t f h => by
    simpa only [rename, subst, List.map_cons] using Derives.exNI x t (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .allBI x b f g h => by
    simpa only [rename, subst, List.map_cons] using Derives.allBI x b (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .allBE x b t f h k => by
    simpa only [rename, subst, List.map_cons] using Derives.allBE x b t (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .exBE x b f g l h k => by
    simpa only [rename, subst, List.map_cons] using Derives.exBE x b (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) l (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .exBI x b t f h k => by
    simpa only [rename, subst, List.map_cons] using Derives.exBI x b t (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .arithmetic e => by
    simpa only [rename, subst, List.map_cons] using Derives.arithmetic e
  | .eqSymm h => by
    simpa only [rename, subst, List.map_cons] using Derives.eqSymm (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .eqAdd h k => by
    simpa only [rename, subst, List.map_cons] using Derives.eqAdd (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .eqMul h k => by
    simpa only [rename, subst, List.map_cons] using Derives.eqMul (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .leRefl t => by
    simpa only [rename, subst, List.map_cons] using Derives.leRefl t
  | .leTrans h k => by
    simpa only [rename, subst, List.map_cons] using Derives.leTrans (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .leAdd h k => by
    simpa only [rename, subst, List.map_cons] using Derives.leAdd (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .leRewrite h k l => by
    simpa only [rename, subst, List.map_cons] using Derives.leRewrite (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k) (by simpa only [rename, subst, List.map_cons] using raw ρ hi l)
  | .ltSucc t => by
    simpa only [rename, subst, List.map_cons] using Derives.ltSucc t
  | .ltZeroFalse t => by
    simpa only [rename, subst, List.map_cons] using Derives.ltZeroFalse t
  | .ltTrans h k => by
    simpa only [rename, subst, List.map_cons] using Derives.ltTrans (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | .ltLe h => by
    simpa only [rename, subst, List.map_cons] using Derives.ltLe (by simpa only [rename, subst, List.map_cons] using raw ρ hi h)
  | .ltRewrite h k l => by
    simpa only [rename, subst, List.map_cons] using Derives.ltRewrite (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k) (by simpa only [rename, subst, List.map_cons] using raw ρ hi l)
  | .sigma1Induction x ss f g l h k => by
    simpa only [rename, subst, List.map_cons] using Derives.sigma1Induction x (sigma ρ ss) (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) (by simpa only [freshNumMap, numFree, safe] using l) (by simpa only [rename, subst, List.map_cons] using raw ρ hi h) (by simpa only [rename, subst, List.map_cons] using raw ρ hi k)
  | @Derives.delta1Comprehension _ dp dq x g ss pp f hpg hqg h => by
    have fg := (freshSetMap ρ hi Γ g).trans f
    have pg : (rename ρ dp).setFree.contains (ρ g) = false := by
      rw [setFree ρ hi, containsInjective ρ hi]; exact hpg
    have qg : (rename ρ dq).setFree.contains (ρ g) = false := by
      rw [setFree ρ hi, containsInjective ρ hi]; exact hqg
    have ih := raw ρ hi h
    simp only [rename, iffF] at ih ⊢
    exact .delta1Comprehension x (ρ g) (sigma ρ ss) (pi ρ pp) fg pg qg ih

def ordered (ρ : ℕ → ℕ) (hi : Function.Injective ρ)
    {Γ : List Formula} {p : Formula} : CalculoOrdenRCA.Proof Γ p →
    CalculoOrdenRCA.Proof (Γ.map (rename ρ)) (rename ρ p)
  | .embed h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.embed (raw ρ hi h)
  | .hypothesis hm => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.hypothesis (List.mem_map_of_mem hm)
  | .weaken hw h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.weaken (fun f hf => by
      obtain ⟨q,hq,rfl⟩ := List.mem_map.mp hf
      exact List.mem_map_of_mem (hw q hq)) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .botE h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.botE (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .impI h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.impI (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .impE h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.impE (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .andI h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.andI (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .andL h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.andL (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .andR h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.andR (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .allI x f h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.allI x (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .allE x t f h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.allE x t (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .allBI x b f g h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.allBI x b (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .allBE x b t f h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.allBE x b t (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .exBI x b t f h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.exBI x b t (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .exBE x b f g l h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.exBE x b (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) l (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | @CalculoOrdenRCA.Proof.exBErename _ bp _ x y b f g l z h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.exBErename (p := rename ρ bp) x y b (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) l (by simpa only [freshNumMap, numFree, safe] using z) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .eqSymm h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.eqSymm (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .eqTrans h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.eqTrans (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .eqAdd h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.eqAdd (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .eqMul h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.eqMul (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .eqSubst p x t u f g h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.eqSubst (rename ρ p) x t u (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .leTrans h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.leTrans (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .leAdd h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.leAdd (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .leRewrite h k l => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.leRewrite (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi l)
  | .ltRewrite h k l => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.ltRewrite (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi l)
  | .ltTrans h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.ltTrans (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .ltLe h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.ltLe (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .zeroLe t => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.zeroLe t
  | .leAntisymm h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.leAntisymm (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .leMulRight t h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.leMulRight t (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .ltAddRight t h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.ltAddRight t (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .leLtTrans h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.leLtTrans (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .ltLeTrans h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.ltLeTrans (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)
  | .ltSuccLe h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.ltSuccLe (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .succLeLt h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.succLeLt (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .ltIrrefl h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.ltIrrefl (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .addCancelLeft t h => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.addCancelLeft t (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h)
  | .orderCases t u h k l => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.orderCases t u (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi l)
  | .sigma1Induction x ss f g l h k => by
    simpa only [rename, subst, List.map_cons] using CalculoOrdenRCA.Proof.sigma1Induction x (sigma ρ ss) (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) (by simpa only [freshNumMap, numFree, safe] using l) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi h) (by simpa only [rename, subst, List.map_cons] using ordered ρ hi k)

def logical (ρ : ℕ → ℕ) (hi : Function.Injective ρ)
    {Γ : List Formula} {p : Formula} : CalculoExistencialRCA.Proof Γ p →
    CalculoExistencialRCA.Proof (Γ.map (rename ρ)) (rename ρ p)
  | .embed h => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.embed (ordered ρ hi h)
  | .hypothesis hm => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.hypothesis (List.mem_map_of_mem hm)
  | .weaken hw h => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.weaken (fun f hf => by
      obtain ⟨q,hq,rfl⟩ := List.mem_map.mp hf
      exact List.mem_map_of_mem (hw q hq)) (by simpa only [rename, subst, List.map_cons] using logical ρ hi h)
  | .impI h => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.impI (by simpa only [rename, subst, List.map_cons] using logical ρ hi h)
  | .impE h k => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.impE (by simpa only [rename, subst, List.map_cons] using logical ρ hi h) (by simpa only [rename, subst, List.map_cons] using logical ρ hi k)
  | .andI h k => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.andI (by simpa only [rename, subst, List.map_cons] using logical ρ hi h) (by simpa only [rename, subst, List.map_cons] using logical ρ hi k)
  | .andL h => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.andL (by simpa only [rename, subst, List.map_cons] using logical ρ hi h)
  | .andR h => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.andR (by simpa only [rename, subst, List.map_cons] using logical ρ hi h)
  | .allI x f h => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.allI x (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using logical ρ hi h)
  | .allE x t f h => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.allE x t (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using logical ρ hi h)
  | .exNI x t f h => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.exNI x t (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [rename, subst, List.map_cons] using logical ρ hi h)
  | .exNE x f g h k => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.exNE x (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) (by simpa only [rename, subst, List.map_cons] using logical ρ hi h) (by simpa only [rename, subst, List.map_cons] using logical ρ hi k)
  | .sigma1Induction x ss f g l h k => by
    simpa only [rename, subst, List.map_cons] using CalculoExistencialRCA.Proof.sigma1Induction x (sigma ρ ss) (by simpa only [freshNumMap, numFree, safe] using f) (by simpa only [freshNumMap, numFree, safe] using g) (by simpa only [freshNumMap, numFree, safe] using l) (by simpa only [rename, subst, List.map_cons] using logical ρ hi h) (by simpa only [rename, subst, List.map_cons] using logical ρ hi k)

def swap (a b x : ℕ) : ℕ := if x = a then b else if x = b then a else x

theorem swap_twice (a b x : ℕ) : swap a b (swap a b x) = x := by
  by_cases ha : x = a
  · subst x; by_cases hab : a = b <;> simp [swap, hab]
  · by_cases hb : x = b
    · subst x; simp [swap, ha]
    · simp [swap, ha, hb]
theorem swap_injective (a b : ℕ) : Function.Injective (swap a b) := by
  intro x y h
  have e := congrArg (swap a b) h
  exact (swap_twice a b x).symm.trans (e.trans (swap_twice a b y))

def crtU : CalculoExistencialRCA.Proof []
    (rename (swap 2 3) InvarianteCRTParcialRCA.fixedBCRTGoal) :=
  logical (swap 2 3) (swap_injective 2 3) CRTFinitoUniformeRCA.fixedBCRT

def crtD : CalculoExistencialRCA.Proof []
    (rename (swap 2 4) InvarianteCRTParcialRCA.fixedBCRTGoal) :=
  logical (swap 2 4) (swap_injective 2 4) CRTFinitoUniformeRCA.fixedBCRT

example : (rename (swap 2 3) InvarianteCRTParcialRCA.fixedBCRTGoal).setFree.all (· == 3) = true := by decide
example : (rename (swap 2 4) InvarianteCRTParcialRCA.fixedBCRTGoal).setFree.all (· == 4) = true := by decide
example : (rename (swap 2 3) InvarianteCRTParcialRCA.fixedBCRTGoal).setFree.contains 2 = false := by decide
example : (rename (swap 2 4) InvarianteCRTParcialRCA.fixedBCRTGoal).setFree.contains 2 = false := by decide
example : rename (swap 2 3) (.exS 3 (.member (.lit 0) 2)) =
    .exS 2 (.member (.lit 0) 3) := rfl
-- Renaming the binder too avoids capture, unlike naïve replacement 2 -> 3.
example : swap 2 3 3 = 2 := rfl
example : (rename (swap 2 3) (.allN 16 (.member (.var 30) 2))).safe 30 (.var 16) = false := rfl
#print axioms raw
#print axioms ordered
#print axioms logical
#print axioms crtU
#print axioms crtD
#eval ("crt_renamed_U", CalculoExistencialRCA.profile crtU)
#eval ("crt_renamed_D", CalculoExistencialRCA.profile crtD)
end MatematicaAbierta.Continuo.RenombradoConjuntosRCA
