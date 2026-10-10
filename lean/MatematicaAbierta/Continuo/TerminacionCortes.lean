import MatematicaAbierta.Continuo.DecididoresCortes
import Mathlib.Algebra.Order.Archimedean.Basic

/-!
# FDC-AUD-023 — O3: terminación de la búsqueda de intervalos

Cada consulta racional es distinta del extremo irracional. El radio geométrico
puede hacerse menor que la mitad de la separación, lo que obliga a que alguna
etapa emita un certificado. Esta capa es una prueba de terminación semántica;
la extracción de índices de programas se formaliza por separado.
-/

namespace Continuo.Indices

/-- Los radios geométricos se hacen arbitrariamente pequeños aun si se
incrementa el exponente en una cantidad fija. -/
theorem intervalRadius_small (k : ℕ) {ε : ℝ} (hε : 0 < ε) :
    ∃ n : ℕ, (intervalRadius (n + k) : ℝ) < ε := by
  obtain ⟨n, hn⟩ := exists_pow_lt_of_lt_one hε
    (show (1 / 2 : ℝ) < 1 by norm_num)
  refine ⟨n, ?_⟩
  have hle : (1 / 2 : ℝ) ^ (n + k) ≤ (1 / 2 : ℝ) ^ n :=
    pow_le_pow_of_le_one (by norm_num) (by norm_num) (Nat.le_add_right n k)
  have hr : (intervalRadius (n + k) : ℝ) ≤ (1 / 2 : ℝ) ^ n := by
    simpa [intervalRadius_cast, one_div_pow] using hle
  exact lt_of_le_of_lt hr hn

/-- Una sucesión de aproximaciones estrictas y un extremo distinto de la
consulta producen, en una etapa finita, una respuesta cierta o falsa. -/
theorem intervalStage_eventually (a : ℕ → ℚ) (x : ℝ) (q : ℚ) (k : ℕ)
    (hfast : ∀ n, |(a n : ℝ) - x| < (intervalRadius (n + k) : ℝ))
    (hne : x ≠ (q : ℝ)) :
    ∃ n : ℕ, ∃ b : Bool, intervalStage (a n) q (n + k) = some b := by
  rcases lt_trichotomy (q : ℝ) x with hbelow | heq | habove
  · obtain ⟨n, hr⟩ := intervalRadius_small k
      (show (0 : ℝ) < (x - (q : ℝ)) / 2 by linarith)
    have hqreal : (q : ℝ) < (a n : ℝ) - (intervalRadius (n + k) : ℝ) := by
      have ha := (abs_lt.mp (hfast n)).1
      linarith
    have hq : q < a n - intervalRadius (n + k) := by
      exact_mod_cast hqreal
    exact ⟨n, true, by simp [intervalStage, hq]⟩
  · exact (hne heq.symm).elim
  · obtain ⟨n, hr⟩ := intervalRadius_small k
      (show (0 : ℝ) < ((q : ℝ) - x) / 2 by linarith)
    have hqreal : (a n : ℝ) + (intervalRadius (n + k) : ℝ) < (q : ℝ) := by
      have ha := (abs_lt.mp (hfast n)).2
      linarith
    have hq : a n + intervalRadius (n + k) < q := by
      exact_mod_cast hqreal
    have hrpos : 0 ≤ intervalRadius (n + k) := by
      unfold intervalRadius
      positivity
    have hfirst : ¬ q < a n - intervalRadius (n + k) := by
      linarith
    exact ⟨n, false, by simp [intervalStage, hfirst, hq]⟩

/-- Para cada programa y cada racional, aparece un certificado del corte
`L_(√2+δ_c)` en una etapa finita. -/
theorem shiftedCutStage_exists (c : Code) (q : ℚ) :
    ∃ n : ℕ, ∃ b : Bool, shiftedCutStage c q n = some b := by
  have hfast : ∀ n, |(shiftedName c n : ℝ) - shiftedReal c| <
      (intervalRadius (n + 0) : ℝ) := by
    intro n
    simpa using shiftedName_radius c n
  simpa [shiftedCutStage] using
    intervalStage_eventually (shiftedName c) (shiftedReal c) q 0
      hfast (shiftedReal_ne_rat c q)

/-- Para cada racional también aparece un certificado del corte fijo
`L_(-√2)`, incluido cuando la consulta se aproxima arbitrariamente a la raíz. -/
theorem negativeCutStage_exists (q : ℚ) :
    ∃ n : ℕ, ∃ b : Bool, negativeCutStage q n = some b := by
  simpa [negativeCutStage] using
    intervalStage_eventually negSqrtTwoName (-Real.sqrt 2) q 2
      negativeName_radius (negativeRoot_ne_rat q)

end Continuo.Indices
