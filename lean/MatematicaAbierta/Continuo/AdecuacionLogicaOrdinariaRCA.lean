import MatematicaAbierta.Continuo.SustitucionSemanticaRCA
import MatematicaAbierta.Continuo.ContratoBitsAdmisiblesRCA

/-! M15: all ordinary M14 logical nodes are semantically checked.
Embedded M05--M13 derivations remain explicit finite leaf obligations.
The theorem below assumes no universal/global correctness of any calculus. -/
namespace MatematicaAbierta.Continuo.AdecuacionLogicaOrdinariaRCA
open CalculoRCA InterpretacionParametricaRCA SustitucionSemanticaRCA
abbrev Proof := LogicaClasicaOrdinariaRCA.Proof
universe u v
structure Sequent where
  assumptions : List Formula
  conclusion : Formula
  deriving DecidableEq, Repr

def leaves {Γ : List Formula} {p : Formula} : Proof Γ p → List Sequent
  | .embed _ => [⟨Γ,p⟩]
  | .hypothesis _ => []
  | .weaken _ h | .impI h | .andL h | .andR h | .allI _ _ h | .allE _ _ _ h | .exNI _ _ _ h | .exSI _ h => leaves h
  | .impE h k | .andI h k | .exNE _ _ _ h k | .exSE _ _ _ h k | .cases h k => leaves h ++ leaves k

theorem context_cons {A : Type u} {S : Type v} (m : Signature A S) (ρ : ℕ → A) (σ : ℕ → S)
    (p : Formula) (Γ : List Formula) : context m ρ σ (p::Γ) ↔ holds m ρ σ p ∧ context m ρ σ Γ := by
  constructor
  · intro h; exact ⟨h p List.mem_cons_self,fun q hq => h q (List.mem_cons_of_mem _ hq)⟩
  · rintro ⟨hp,hΓ⟩ q hq
    rcases List.mem_cons.mp hq with e | hm
    · subst q; exact hp
    · exact hΓ q hm

theorem logic_sound {A : Type u} {S : Type v} (m : Signature A S)
    {Γ : List Formula} {p : Formula} (h : Proof Γ p) :
    (∀ c ∈ leaves h, Valid m c.assumptions c.conclusion) → Valid m Γ p := by
  induction h with
  | embed h => intro hl; exact hl _ List.mem_cons_self
  | hypothesis hm => intro _ ρ σ hc; exact hc _ hm
  | weaken hw h ih => intro hl ρ σ hc; exact ih hl ρ σ (fun q hq => hc q (hw q hq))
  | impI h ih =>
    intro hl ρ σ hc hp
    exact ih hl ρ σ ((context_cons m ρ σ _ _).mpr ⟨hp,hc⟩)
  | impE h k ih ik =>
    intro hl ρ σ hc
    exact ih (fun c hm => hl c (List.mem_append_left _ hm)) ρ σ hc
      (ik (fun c hm => hl c (List.mem_append_right _ hm)) ρ σ hc)
  | andI h k ih ik =>
    intro hl ρ σ hc
    exact ⟨ih (fun c hm => hl c (List.mem_append_left _ hm)) ρ σ hc,
      ik (fun c hm => hl c (List.mem_append_right _ hm)) ρ σ hc⟩
  | andL h ih => intro hl ρ σ hc; exact (ih hl ρ σ hc).1
  | andR h ih => intro hl ρ σ hc; exact (ih hl ρ σ hc).2
  | allI x fresh h ih =>
    intro hl ρ σ hc a
    exact ih hl (Function.update ρ x a) σ ((context_number_fresh m _ ρ σ x a fresh).mpr hc)
  | allE x t safe h ih =>
    intro hl ρ σ hc
    exact (formula_substitution m _ x t ρ σ safe).mpr (ih hl ρ σ hc (term m ρ t))
  | exNI x t safe h ih =>
    intro hl ρ σ hc
    exact ⟨term m ρ t,(formula_substitution m _ x t ρ σ safe).mp (ih hl ρ σ hc)⟩
  | exNE x fresh free h k ih ik =>
    intro hl ρ σ hc
    obtain ⟨a,ha⟩ := ih (fun c hm => hl c (List.mem_append_left _ hm)) ρ σ hc
    have hk := ik (fun c hm => hl c (List.mem_append_right _ hm)) (Function.update ρ x a) σ
      ((context_cons m _ σ _ _).mpr ⟨ha,(context_number_fresh m _ ρ σ x a fresh).mpr hc⟩)
    exact (number_fresh m _ ρ σ x a free).mp hk
  | exSI g h ih =>
    intro hl ρ σ hc
    refine ⟨σ g,?_⟩
    simpa only [Function.update_eq_self] using ih hl ρ σ hc
  | exSE g fresh free h k ih ik =>
    intro hl ρ σ hc
    obtain ⟨X,hX⟩ := ih (fun c hm => hl c (List.mem_append_left _ hm)) ρ σ hc
    have hk := ik (fun c hm => hl c (List.mem_append_right _ hm)) ρ (Function.update σ g X)
      ((context_cons m ρ _ _ _).mpr ⟨hX,(context_set_fresh m _ ρ σ g X fresh).mpr hc⟩)
    exact (set_fresh m _ ρ σ g X free).mp hk
  | @cases Γ p q h k ih ik =>
    intro hl ρ σ hc
    classical
    by_cases hp : holds m ρ σ p
    · exact ih (fun c hm => hl c (List.mem_append_left _ hm)) ρ σ
        ((context_cons m ρ σ _ _).mpr ⟨hp,hc⟩)
    · exact ik (fun c hm => hl c (List.mem_append_right _ hm)) ρ σ
        ((context_cons m ρ σ _ _).mpr ⟨hp,hc⟩)

-- A complete logical tree, including cases, with zero theory leaves.
def classicalIdentity (p : Formula) : Proof [] (.imp p p) :=
  .impI (.cases LogicaClasicaOrdinariaRCA.hyp (LogicaClasicaOrdinariaRCA.push LogicaClasicaOrdinariaRCA.hyp))
theorem identity_valid {A : Type u} {S : Type v} (m : Signature A S) (p : Formula) :
    Valid m [] (.imp p p) := logic_sound m (classicalIdentity p) (by intro c hc; change c ∈ [] at hc; exact False.elim (List.not_mem_nil hc))
example : leaves (classicalIdentity (.member (.var 0) 2)) = [] := rfl
#print axioms identity_valid
#print axioms classicalIdentity
#eval ("M15_closed_logical_tree", LogicaClasicaOrdinariaRCA.profile (classicalIdentity (.member (.var 0) 2)))
#print axioms logic_sound
#eval ("M15_C13_logical_boundary_leaves", (leaves ContratoBitsAdmisiblesRCA.admissibleGraph).length)
#eval ("M15_C12_bridge_boundary_leaves", (leaves ContratoBitsAdmisiblesRCA.extensionFromBits).length)
#eval ("M15_C13_logical_profile", LogicaClasicaOrdinariaRCA.profile ContratoBitsAdmisiblesRCA.admissibleGraph)
#eval ("M15_C12_logical_profile", LogicaClasicaOrdinariaRCA.profile ContratoBitsAdmisiblesRCA.extensionFromBits)
end MatematicaAbierta.Continuo.AdecuacionLogicaOrdinariaRCA
