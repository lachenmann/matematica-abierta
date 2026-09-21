import MatematicaAbierta.Continuo.SimulacionAcotada

/-!
# FDC-AUD-023 — Primera etapa de éxito y estimación diádica

Extensión de la simulación finita: carácter mínimo de `firstHit`,
valor semántico no computable `delta` y aproximación racional ejecutable.
`evaln` mide una cota de evaluación, NO pasos literales de máquina.
No se formaliza aquí la computabilidad uniforme a nivel de índices ni T002b/T002f.
-/

namespace Continuo.Indices

/-- No hay primer éxito hasta `N` exactamente si todas las etapas anteriores fallan. -/
theorem firstHit_none_iff (c : Code) (N : ℕ) :
    firstHit c N = none ↔ ∀ k < N, run c k = none := by
  induction N with
  | zero => simp [firstHit]
  | succ N ih =>
    constructor
    · intro h k hk
      have hp : firstHit c N = none := by
        cases hp : firstHit c N with
        | none => rfl
        | some t => simp [firstHit, hp] at h
      have hr : run c N = none := by
        cases hr : run c N with
        | none => rfl
        | some x => simp [firstHit, hp, hr] at h
      rcases Nat.lt_succ_iff_lt_or_eq.mp hk with hlt | heq
      · exact (ih.mp hp) k hlt
      · subst k
        exact hr
    · intro h
      have hp : firstHit c N = none :=
        ih.mpr (fun k hk => h k (Nat.lt_succ_of_lt hk))
      have hr : run c N = none := h N (Nat.lt_succ_self N)
      simp [firstHit, hp, hr]

/-- La primera respuesta aparece inmediatamente después de su etapa mínima. -/
theorem firstHit_at_minimum (c : Code) (t : ℕ)
    (ht : run c t ≠ none) (hmin : ∀ k < t, run c k = none) :
    firstHit c (t + 1) = some t := by
  have hp : firstHit c t = none := (firstHit_none_iff c t).mpr hmin
  cases hr : run c t with
  | none => exact (ht hr).elim
  | some x => simp [firstHit, hp, hr]

/-- Una primera respuesta nunca cambia al aumentar la cota. -/
theorem firstHit_stable {c : Code} {N t : ℕ}
    (h : firstHit c N = some t) :
    ∀ d : ℕ, firstHit c (N + d) = some t := by
  intro d
  induction d with
  | zero => exact h
  | succ d ih => simpa [Nat.add_succ, firstHit, ih]

/-- Caracterización exacta de la primera etapa observada. -/
theorem firstHit_iff_minimal (c : Code) (N t : ℕ) :
    firstHit c N = some t ↔
      t < N ∧ run c t ≠ none ∧ ∀ k < t, run c k = none := by
  constructor
  · intro h
    induction N generalizing t with
    | zero => simp [firstHit] at h
    | succ N ih =>
      cases hp : firstHit c N with
      | some j =>
        have hj : j = t := by simpa [firstHit, hp] using h
        subst t
        obtain ⟨hlt, hrun, hmin⟩ := ih j hp
        exact ⟨Nat.lt_succ_of_lt hlt, hrun, hmin⟩
      | none =>
        cases hr : run c N with
        | none => simp [firstHit, hp, hr] at h
        | some x =>
          have ht : N = t := by simpa [firstHit, hp, hr] using h
          subst t
          exact ⟨Nat.lt_succ_self N, by simp [hr], (firstHit_none_iff c N).mp hp⟩
  · rintro ⟨hlt, hrun, hmin⟩
    have h0 := firstHit_at_minimum c t hrun hmin
    have heq : t + 1 + (N - (t + 1)) = N := by omega
    rw [← heq]
    exact firstHit_stable h0 _

/-- El valor semántico es racional; su definición puede consultar clásicamente la parada. -/
noncomputable def delta (c : Code) : ℚ := by
  classical
  exact if h : ∃ t, run c t ≠ none then dyadic (Nat.find h) else 0

/-- El mismo valor en el modelo real externo de Mathlib. -/
noncomputable def deltaReal (c : Code) : ℝ := (delta c : ℝ)

private theorem dyadic_pos (N : ℕ) : 0 < dyadic N := by
  unfold dyadic
  positivity

private theorem dyadic_antitone {N t : ℕ} (h : N ≤ t) : dyadic t ≤ dyadic N := by
  unfold dyadic
  apply one_div_le_one_div_of_le (by positivity)
  exact pow_le_pow_right₀ (by norm_num : (1 : ℚ) ≤ 2) (by omega)

/-- La detención en la entrada fija equivale a la existencia de etapa exitosa. -/
theorem halts_iff_exists_hit (c : Code) :
    (∃ x : ℕ, x ∈ Nat.Partrec.Code.eval c fixedInput) ↔
      ∃ t : ℕ, run c t ≠ none := by
  rw [halts_iff_exists_run]
  constructor
  · rintro ⟨t, x, hx⟩
    refine ⟨t, ?_⟩
    cases hr : run c t with
    | none => simp [hr] at hx
    | some y => simp
  · rintro ⟨t, ht⟩
    cases hr : run c t with
    | none => exact (ht hr).elim
    | some x => exact ⟨t, x, by simp [hr]⟩

/-- Positividad del valor racional exactamente para los programas que paran. -/
theorem delta_pos_iff_halts (c : Code) :
    0 < delta c ↔ ∃ x : ℕ, x ∈ Nat.Partrec.Code.eval c fixedInput := by
  classical
  rw [halts_iff_exists_hit]
  by_cases hh : ∃ t : ℕ, run c t ≠ none
  · simp [delta, hh, dyadic_pos]
  · simp [delta, hh]

/-- La búsqueda finita produce un nombre racional con cota diádica del valor semántico. -/
theorem approximant_error (c : Code) (N : ℕ) :
    |approximant c N - delta c| ≤ dyadic N := by
  classical
  by_cases hh : ∃ t : ℕ, run c t ≠ none
  · let t := Nat.find hh
    have hrun : run c t ≠ none := Nat.find_spec hh
    have hmin : ∀ k < t, run c k = none := by
      intro k hk
      by_contra hne
      exact (Nat.find_min hh hk) hne
    by_cases hlt : t < N
    · have hfirst : firstHit c N = some t :=
        (firstHit_iff_minimal c N t).mpr ⟨hlt, hrun, hmin⟩
      have heq : approximant c N = delta c := by
        simp [approximant, hfirst, delta, hh, t]
      rw [heq, sub_self, abs_zero]
      exact (dyadic_pos N).le
    · have hnone : firstHit c N = none :=
        (firstHit_none_iff c N).mpr (by
          intro k hk
          exact hmin k (lt_of_lt_of_le hk (Nat.le_of_not_gt hlt)))
      have hzero : approximant c N = 0 := by simp [approximant, hnone]
      have hdelta : delta c = dyadic t := by simp [delta, hh, t]
      rw [hzero, hdelta]
      have hnonneg : 0 ≤ dyadic t := (dyadic_pos t).le
      simpa [abs_neg, abs_of_nonneg hnonneg] using
        (dyadic_antitone (Nat.le_of_not_gt hlt))
  · have hnone : firstHit c N = none :=
      (firstHit_none_iff c N).mpr (by
        intro k hk
        by_contra hne
        exact hh ⟨k, hne⟩)
    have hzero : approximant c N = 0 := by simp [approximant, hnone]
    simp [hzero, delta, hh, (dyadic_pos N).le]

/-- La misma cota transferida a los reales externos de Mathlib. -/
theorem approximant_error_real (c : Code) (N : ℕ) :
    |(approximant c N : ℝ) - deltaReal c| ≤ (dyadic N : ℝ) := by
  change |(approximant c N : ℝ) - (delta c : ℝ)| ≤ (dyadic N : ℝ)
  exact_mod_cast approximant_error c N

end Continuo.Indices
