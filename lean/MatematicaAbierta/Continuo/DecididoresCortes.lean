import MatematicaAbierta.Continuo.NombresRaiz
import Mathlib.NumberTheory.Real.Irrational

/-!
# FDC-AUD-023 — O3, primera parte: irracionalidad y certificados de intervalo

La irracionalidad de los extremos y la corrección de cada respuesta finita
se prueban sin decidir la detención. El siguiente tramo deberá probar que la
búsqueda termina y construir índices efectivos de decididores; este módulo
NO acredita todavía la obligación O3 completa.
-/

namespace Continuo.Indices

/-- El desplazamiento semántico es racional para cada programa, aunque no se
pueda obtener su valor exacto uniformemente a partir del código. -/
theorem shiftedReal_irrational (c : Code) : Irrational (shiftedReal c) := by
  simpa [shiftedReal, deltaReal] using
    (irrational_sqrt_two.add_ratCast (delta c))

/-- El segundo extremo de la reducción es irracional. -/
theorem negativeRoot_irrational : Irrational (-Real.sqrt 2) :=
  irrational_sqrt_two.neg

/-- Ninguna consulta racional coincide con el primer extremo. -/
theorem shiftedReal_ne_rat (c : Code) (q : ℚ) :
    shiftedReal c ≠ (q : ℝ) :=
  (shiftedReal_irrational c).ne_rat q

/-- Ninguna consulta racional coincide con el segundo extremo. -/
theorem negativeRoot_ne_rat (q : ℚ) :
    -Real.sqrt 2 ≠ (q : ℝ) :=
  negativeRoot_irrational.ne_rat q

/-- Radio racional estricto del algoritmo de intervalos. -/
def intervalRadius (n : ℕ) : ℚ := (1 / 2 : ℚ) ^ n

theorem intervalRadius_cast (n : ℕ) :
    (intervalRadius n : ℝ) = 1 / (2 : ℝ) ^ n := by
  simp [intervalRadius]

/-- Las aproximaciones desplazadas cumplen exactamente el contrato del radio. -/
theorem shiftedName_radius (c : Code) (n : ℕ) :
    |(shiftedName c n : ℝ) - shiftedReal c| < (intervalRadius n : ℝ) := by
  rw [intervalRadius_cast]
  exact shiftedName_error c n

/-- El nombre del extremo negativo conserva dos unidades de precisión. -/
theorem negativeName_radius (n : ℕ) :
    |(negSqrtTwoName n : ℝ) - (-Real.sqrt 2)| <
      (intervalRadius (n + 2) : ℝ) := by
  rw [intervalRadius_cast]
  exact negSqrtTwoName_error n

/-- Una etapa racional no consulta ni la igualdad real ni el problema de parada.
`true`: consulta debajo del intervalo; `false`: por encima; `none`: refinar. -/
def intervalStage (a q : ℚ) (n : ℕ) : Option Bool :=
  if q < a - intervalRadius n then some true
  else if a + intervalRadius n < q then some false
  else none

/-- Todo certificado afirmativo corresponde a una desigualdad real estricta. -/
theorem intervalStage_true (a q : ℚ) (n : ℕ) (x : ℝ)
    (hfast : |(a : ℝ) - x| < (intervalRadius n : ℝ))
    (hstage : intervalStage a q n = some true) : (q : ℝ) < x := by
  unfold intervalStage at hstage
  split_ifs at hstage with hleft hright
  · have hq : (q : ℝ) < (a : ℝ) - (intervalRadius n : ℝ) := by
      exact_mod_cast hleft
    have hx := (abs_lt.mp hfast).2
    linarith
  · cases hstage

/-- Todo certificado negativo corresponde a una desigualdad real estricta. -/
theorem intervalStage_false (a q : ℚ) (n : ℕ) (x : ℝ)
    (hfast : |(a : ℝ) - x| < (intervalRadius n : ℝ))
    (hstage : intervalStage a q n = some false) : x < (q : ℝ) := by
  unfold intervalStage at hstage
  split_ifs at hstage with hleft hright
  · cases hstage
  · have hq : (a : ℝ) + (intervalRadius n : ℝ) < (q : ℝ) := by
      exact_mod_cast hright
    have hx := (abs_lt.mp hfast).1
    linarith

/-- Etapa concreta para el corte de la raíz desplazada. -/
def shiftedCutStage (c : Code) (q : ℚ) (n : ℕ) : Option Bool :=
  intervalStage (shiftedName c n) q n

/-- Etapa concreta para el corte fijo de menos raíz de dos. -/
def negativeCutStage (q : ℚ) (n : ℕ) : Option Bool :=
  intervalStage (negSqrtTwoName n) q (n + 2)

/-- No hay falsos positivos en la familia desplazada. -/
theorem shiftedCutStage_true (c : Code) (q : ℚ) (n : ℕ)
    (h : shiftedCutStage c q n = some true) :
    (q : ℝ) < shiftedReal c :=
  intervalStage_true (shiftedName c n) q n (shiftedReal c)
    (shiftedName_radius c n) h

/-- No hay falsos negativos en la familia desplazada. -/
theorem shiftedCutStage_false (c : Code) (q : ℚ) (n : ℕ)
    (h : shiftedCutStage c q n = some false) :
    shiftedReal c < (q : ℝ) :=
  intervalStage_false (shiftedName c n) q n (shiftedReal c)
    (shiftedName_radius c n) h

/-- Corrección afirmativa del extremo fijo. -/
theorem negativeCutStage_true (q : ℚ) (n : ℕ)
    (h : negativeCutStage q n = some true) :
    (q : ℝ) < -Real.sqrt 2 :=
  intervalStage_true (negSqrtTwoName n) q (n + 2) (-Real.sqrt 2)
    (negativeName_radius n) h

/-- Corrección negativa del extremo fijo. -/
theorem negativeCutStage_false (q : ℚ) (n : ℕ)
    (h : negativeCutStage q n = some false) :
    -Real.sqrt 2 < (q : ℝ) :=
  intervalStage_false (negSqrtTwoName n) q (n + 2) (-Real.sqrt 2)
    (negativeName_radius n) h

end Continuo.Indices
