import Mathlib
import MatematicaAbierta.CauchySchwarz

/-!
# Cauchy–Schwarz para sumas finitas: prueba y caso de igualdad

Correspondencia editorial: MA-ART-0004, `teoria/resultados/_cauchy-1.qmd`, §3,
y `teoria/resultados/_cauchy-2.qmd`, §§5 y 8.
La prueba usa una identidad cuadrática propia, la positividad de una suma de
cuadrados y una separación explícita del caso de vector nulo; no invoca
el teorema general de Cauchy–Schwarz de Mathlib.
-/

namespace MatematicaAbierta

/-- Identidad del cuadrado completado: `Q * (P * Q - R²)` es una suma
 de cuadrados, con `P = ∑ aᵢ²`, `Q = ∑ bᵢ²`, `R = ∑ aᵢbᵢ`. -/
theorem identidad_cuadratica_cauchy_finita {ι : Type*} (s : Finset ι)
    (a b : ι → ℝ) :
    (∑ i ∈ s, ((∑ j ∈ s, b j ^ 2) * a i -
      (∑ j ∈ s, a j * b j) * b i) ^ 2) =
      (∑ i ∈ s, b i ^ 2) *
        ((∑ i ∈ s, a i ^ 2) * (∑ i ∈ s, b i ^ 2) -
          (∑ i ∈ s, a i * b i) ^ 2) := by
  let P : ℝ := ∑ i ∈ s, a i ^ 2
  let Q : ℝ := ∑ i ∈ s, b i ^ 2
  let R : ℝ := ∑ i ∈ s, a i * b i
  change (∑ i ∈ s, (Q * a i - R * b i) ^ 2) = Q * (P * Q - R ^ 2)
  calc
    (∑ i ∈ s, (Q * a i - R * b i) ^ 2) =
        ∑ i ∈ s, (Q ^ 2 * a i ^ 2 - (2 * Q * R) * (a i * b i) +
          R ^ 2 * b i ^ 2) := by
      apply Finset.sum_congr rfl
      intro i hi
      ring
    _ = Q ^ 2 * P - (2 * Q * R) * R + R ^ 2 * Q := by
      simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib,
        ← Finset.mul_sum]
      ring
    _ = Q * (P * Q - R ^ 2) := by ring

/-- MA-ART-0004, §3: Cauchy–Schwarz para un conjunto finito cualquiera,
 incluidos el conjunto vacío y los vectores nulos. -/
theorem cauchy_schwarz_finito {ι : Type*} (s : Finset ι)
    (a b : ι → ℝ) :
    (∑ i ∈ s, a i * b i) ^ 2 ≤
      (∑ i ∈ s, a i ^ 2) * (∑ i ∈ s, b i ^ 2) := by
  let P : ℝ := ∑ i ∈ s, a i ^ 2
  let Q : ℝ := ∑ i ∈ s, b i ^ 2
  let R : ℝ := ∑ i ∈ s, a i * b i
  change R ^ 2 ≤ P * Q
  have hQ : 0 ≤ Q := Finset.sum_nonneg (fun i hi => sq_nonneg (b i))
  rcases eq_or_lt_of_le hQ with hQzero | hQpos
  · have hb : ∀ i ∈ s, b i = 0 :=
      (Finset.sum_sq_eq_zero_iff s b).mp hQzero.symm
    have hRzero : R = 0 := by
      dsimp [R]
      apply Finset.sum_eq_zero
      intro i hi
      simp [hb i hi]
    rw [hRzero, ← hQzero]
    norm_num
  · have hsum : 0 ≤ ∑ i ∈ s, (Q * a i - R * b i) ^ 2 :=
      Finset.sum_nonneg (fun i hi => sq_nonneg _)
    have hid := identidad_cuadratica_cauchy_finita s a b
    change (∑ i ∈ s, (Q * a i - R * b i) ^ 2) =
      Q * (P * Q - R ^ 2) at hid
    by_contra h
    have hneg : P * Q - R ^ 2 < 0 := sub_neg.mpr (lt_of_not_ge h)
    have hprod : Q * (P * Q - R ^ 2) < 0 :=
      mul_neg_of_pos_of_neg hQpos hneg
    linarith

/-- MA-ART-0004, §8: igualdad si `b` es nulo o si `a` es múltiplo de `b`.
 Esta disyunción cubre sin división el caso en que uno o ambos vectores son cero. -/
theorem cauchy_schwarz_finito_igualdad {ι : Type*} (s : Finset ι)
    (a b : ι → ℝ) :
    ((∑ i ∈ s, a i * b i) ^ 2 =
      (∑ i ∈ s, a i ^ 2) * (∑ i ∈ s, b i ^ 2)) ↔
      (∀ i ∈ s, b i = 0) ∨
        ∃ c : ℝ, ∀ i ∈ s, a i = c * b i := by
  let P : ℝ := ∑ i ∈ s, a i ^ 2
  let Q : ℝ := ∑ i ∈ s, b i ^ 2
  let R : ℝ := ∑ i ∈ s, a i * b i
  change (R ^ 2 = P * Q) ↔
    (∀ i ∈ s, b i = 0) ∨ ∃ c : ℝ, ∀ i ∈ s, a i = c * b i
  have hQ : 0 ≤ Q := Finset.sum_nonneg (fun i hi => sq_nonneg (b i))
  constructor
  · intro heq
    rcases eq_or_lt_of_le hQ with hQzero | hQpos
    · left
      exact (Finset.sum_sq_eq_zero_iff s b).mp hQzero.symm
    · right
      refine ⟨R / Q, ?_⟩
      have hid := identidad_cuadratica_cauchy_finita s a b
      change (∑ i ∈ s, (Q * a i - R * b i) ^ 2) =
        Q * (P * Q - R ^ 2) at hid
      have hzero : (∑ i ∈ s, (Q * a i - R * b i) ^ 2) = 0 := by
        rw [hid, ← heq]
        ring
      have hcoords :=
        (Finset.sum_sq_eq_zero_iff s (fun i => Q * a i - R * b i)).mp hzero
      intro i hi
      have hcoord := hcoords i hi
      calc
        a i = (R * b i) / Q := by
          apply (eq_div_iff (ne_of_gt hQpos)).2
          nlinarith [hcoord]
        _ = (R / Q) * b i := by ring
  · rintro (hb | ⟨c, hc⟩)
    · have hQzero : Q = 0 := by
        dsimp [Q]
        apply Finset.sum_eq_zero
        intro i hi
        simp [hb i hi]
      have hRzero : R = 0 := by
        dsimp [R]
        apply Finset.sum_eq_zero
        intro i hi
        simp [hb i hi]
      rw [hQzero, hRzero]
      ring
    · have hR : R = c * Q := by
        dsimp [R, Q]
        calc
          (∑ i ∈ s, a i * b i) = ∑ i ∈ s, c * b i ^ 2 := by
            apply Finset.sum_congr rfl
            intro i hi
            rw [hc i hi]
            ring
          _ = c * (∑ i ∈ s, b i ^ 2) := by rw [Finset.mul_sum]
      have hP : P = c ^ 2 * Q := by
        dsimp [P, Q]
        calc
          (∑ i ∈ s, a i ^ 2) = ∑ i ∈ s, c ^ 2 * b i ^ 2 := by
            apply Finset.sum_congr rfl
            intro i hi
            rw [hc i hi]
            ring
          _ = c ^ 2 * (∑ i ∈ s, b i ^ 2) := by rw [Finset.mul_sum]
      rw [hR, hP]
      ring

/-- La versión con índices `Fin n` corresponde literalmente a `n` sumandos. -/
theorem cauchy_schwarz_n_terminos (n : ℕ) (a b : Fin n → ℝ) :
    (∑ i : Fin n, a i * b i) ^ 2 ≤
      (∑ i : Fin n, a i ^ 2) * (∑ i : Fin n, b i ^ 2) := by
  simpa using cauchy_schwarz_finito (Finset.univ : Finset (Fin n)) a b

/-- Igualdad para `n` términos, incluidos los casos de vector nulo. -/
theorem cauchy_schwarz_n_terminos_igualdad (n : ℕ) (a b : Fin n → ℝ) :
    ((∑ i : Fin n, a i * b i) ^ 2 =
      (∑ i : Fin n, a i ^ 2) * (∑ i : Fin n, b i ^ 2)) ↔
      (∀ i : Fin n, b i = 0) ∨
        ∃ c : ℝ, ∀ i : Fin n, a i = c * b i := by
  simpa using cauchy_schwarz_finito_igualdad
    (Finset.univ : Finset (Fin n)) a b

end MatematicaAbierta
