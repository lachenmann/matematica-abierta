import MatematicaAbierta.Continuo.ComputabilidadAproximante
import Mathlib.Analysis.Rat.NatSqrt.Real
import Mathlib.Computability.Primrec.List

/-!
# FDC-AUD-023 — O2, primera parte: nombre racional de raíz de dos

El racional finito se obtiene mediante raíz cuadrada natural. Se prueba
la corrección de su codificación numerador/denominador, computabilidad
primitiva recursiva y error estricto. El desplazamiento por `delta` y
su combinación de errores quedan para el siguiente tramo de O2.
-/

namespace Continuo.Indices

/-- Precisión entera positiva, con dos bits de margen. -/
def sqrtPrecision (n : ℕ) : ℕ := 2 ^ (n + 2)

/-- Nombre racional finito de la raíz de dos. -/
def sqrtTwoName (n : ℕ) : ℚ := Nat.ratSqrt 2 (sqrtPrecision n)

/-- Representación aritmética explícita del nombre racional. -/
def sqrtTwoPair (n : ℕ) : ℕ × ℕ :=
  (Nat.sqrt (2 * (sqrtPrecision n) ^ 2), sqrtPrecision n)

/-- Los pares de naturales representan exactamente los racionales elegidos. -/
theorem sqrtTwoPair_correct (n : ℕ) :
    pairValue (sqrtTwoPair n) = sqrtTwoName n := by
  simp [pairValue, sqrtTwoPair, sqrtTwoName, Nat.ratSqrt]

/-- La precisión es primitiva recursiva. -/
theorem primrec_sqrtPrecision : Primrec sqrtPrecision := by
  exact (Primrec₂.unpaired'.1 Nat.Primrec.pow).comp
    (Primrec.const 2) (Primrec.nat_add.comp Primrec.id (Primrec.const 2))

/-- Numerador y denominador se obtienen por un único algoritmo primitivo recursivo. -/
theorem primrec_sqrtTwoPair : Primrec sqrtTwoPair := by
  have hsq : Primrec (fun n : ℕ => (sqrtPrecision n) ^ 2) :=
    (Primrec₂.unpaired'.1 Nat.Primrec.pow).comp
      primrec_sqrtPrecision (Primrec.const 2)
  have hprod : Primrec (fun n : ℕ => 2 * (sqrtPrecision n) ^ 2) :=
    Primrec.nat_mul.comp (Primrec.const 2) hsq
  exact (Primrec.nat_sqrt.comp hprod).pair primrec_sqrtPrecision

/-- Cota estricta para un nombre racional de raíz de dos. -/
theorem sqrtTwoName_error (n : ℕ) :
    |(sqrtTwoName n : ℝ) - Real.sqrt 2| < 1 / (2 : ℝ) ^ (n + 2) := by
  have hp : 0 < sqrtPrecision n := by
    unfold sqrtPrecision
    positivity
  have hlow : (sqrtTwoName n : ℝ) ≤ Real.sqrt 2 := by
    simpa only [sqrtTwoName] using Nat.ratSqrt_le_realSqrt 2 hp
  have hhigh : Real.sqrt 2 < (sqrtTwoName n : ℝ) + 1 / (2 : ℝ) ^ (n + 2) := by
    simpa [sqrtTwoName, sqrtPrecision, Nat.cast_pow] using
      Nat.realSqrt_lt_ratSqrt_add_inv_prec 2 hp
  rw [abs_of_nonpos (sub_nonpos.mpr hlow)]
  linarith

/-- El mismo nombre con signo cambiado aproxima menos raíz de dos. -/
def negSqrtTwoName (n : ℕ) : ℚ := -sqrtTwoName n

theorem negSqrtTwoName_error (n : ℕ) :
    |(negSqrtTwoName n : ℝ) - (-Real.sqrt 2)| < 1 / (2 : ℝ) ^ (n + 2) := by
  simpa only [negSqrtTwoName, Rat.cast_neg, neg_sub, abs_neg] using
    sqrtTwoName_error n

end Continuo.Indices
