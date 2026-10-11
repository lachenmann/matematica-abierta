import MatematicaAbierta.Continuo.CertificadosOrdenFinito
import Mathlib.Tactic

/-!
FOR-11 / M04: finite rational construction and bounds. Every ambient result
below discharges the explicit finite-sums obligation, not the full reversal.
Lean's Nat induction/Finset infrastructure is NOT claimed as an RCA₀ derivation.
The polynomial successor step is separately witnessed by a finite certificate.
-/
namespace MatematicaAbierta.Continuo.SumasRacionalesFinitas

open scoped BigOperators
open CertificadosOrdenFinito

/-- Horner numerator; the denominator is 4^k and never zero. -/
def numerator (digits : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | k + 1 => 4 * numerator digits k + 2 * digits k

def rationalDigits (digits : ℕ → ℕ) (k : ℕ) : ℚ :=
  (numerator digits k : ℚ) / (4 : ℚ) ^ k

theorem rationalDigits_succ (digits : ℕ → ℕ) (k : ℕ) :
    rationalDigits digits (k + 1) = rationalDigits digits k +
      2 * (digits k : ℚ) / (4 : ℚ) ^ (k + 1) := by
  have hp : (4 : ℚ) ^ k ≠ 0 := by positivity
  simp only [rationalDigits, numerator, Nat.cast_add, Nat.cast_mul, Nat.cast_ofNat,
    pow_succ]
  field_simp

theorem rationalDigits_sum (digits : ℕ → ℕ) (k : ℕ) :
    rationalDigits digits k = ∑ j ∈ Finset.range k,
      2 * (digits j : ℚ) / (4 : ℚ) ^ (j + 1) := by
  induction k with
  | zero => simp [rationalDigits, numerator]
  | succ k ih => rw [rationalDigits_succ, Finset.sum_range_succ, ih]

theorem numerator_bound (digits : ℕ → ℕ) (h : ∀ j, digits j ≤ 1) (k : ℕ) :
    3 * numerator digits k + 2 ≤ 2 * 4 ^ k := by
  induction k with
  | zero => simp [numerator]
  | succ k ih =>
      simpa only [numerator, pow_succ, Nat.mul_comm (4 ^ k) 4] using
        successor_bound (numerator digits k) (4 ^ k) (digits k) ih (h k)

theorem rationalDigits_bounds (digits : ℕ → ℕ) (h : ∀ j, digits j ≤ 1) (k : ℕ) :
    0 ≤ rationalDigits digits k ∧ rationalDigits digits k < 2 / 3 := by
  have hp : (0 : ℚ) < 4 ^ k := by positivity
  have hn : (3 : ℚ) * numerator digits k + 2 ≤ 2 * 4 ^ k :=
    by exact_mod_cast numerator_bound digits h k
  constructor
  · unfold rationalDigits
    positivity
  · unfold rationalDigits
    apply (div_lt_iff₀ hp).2
    linarith

def weight (j : ℕ) : ℚ := 2 / (4 : ℚ) ^ (j + 1)
def sumStage (f : ℕ → ℕ) (s : ℕ) : ℚ := ∑ i ∈ Finset.range s, weight (f i)
def geometric (k : ℕ) : ℚ := ∑ j ∈ Finset.range k, weight j

theorem weight_pos (j : ℕ) : 0 < weight j := by unfold weight; positivity

theorem partial_zero (f : ℕ → ℕ) : sumStage f 0 = 0 := by simp [sumStage]

theorem partial_succ (f : ℕ → ℕ) (s : ℕ) :
    sumStage f (s + 1) = sumStage f s + weight (f s) := by
  exact Finset.sum_range_succ _ s

theorem partial_nonneg (f : ℕ → ℕ) (s : ℕ) : 0 ≤ sumStage f s := by
  exact Finset.sum_nonneg fun j _ => le_of_lt (weight_pos (f j))

theorem partial_monotone (f : ℕ → ℕ) : Monotone (sumStage f) := by
  apply monotone_nat_of_le_succ
  intro s
  rw [partial_succ]
  exact le_add_of_nonneg_right (le_of_lt (weight_pos (f s)))

theorem geometric_identity (k : ℕ) :
    3 * geometric k + 2 / (4 : ℚ) ^ k = 2 := by
  induction k with
  | zero => norm_num [geometric]
  | succ k ih =>
      have hp : (4 : ℚ) ^ k ≠ 0 := by positivity
      simp only [geometric, Finset.sum_range_succ, weight] at *
      rw [pow_succ]
      field_simp at *
      nlinarith

theorem geometric_lt (k : ℕ) : geometric k < 2 / 3 := by
  have hi := geometric_identity k
  have hp : (0 : ℚ) < 2 / (4 : ℚ) ^ k := by positivity
  linarith

/-- Finite image only: no infinite range set is formed. -/
theorem partial_image (f : ℕ → ℕ) (hf : Function.Injective f) (s : ℕ) :
    sumStage f s = ∑ j ∈ (Finset.range s).image f, weight j := by
  exact (Finset.sum_image hf.injOn).symm

/-- A concrete finite cutoff, computed from the initial segment. -/
def cutoff (f : ℕ → ℕ) (s : ℕ) : ℕ := ((Finset.range s).image f).sup id + 1

theorem partial_le_geometric (f : ℕ → ℕ) (hf : Function.Injective f) (s : ℕ) :
    sumStage f s ≤ geometric (cutoff f s) := by
  rw [partial_image f hf]
  apply Finset.sum_le_sum_of_subset_of_nonneg
  · intro j hj
    apply Finset.mem_range.mpr
    exact Nat.lt_succ_of_le (Finset.le_sup (f := id) hj)
  · intro j _ _
    exact le_of_lt (weight_pos j)

theorem partial_bounds (f : ℕ → ℕ) (hf : Function.Injective f) (s : ℕ) :
    0 ≤ sumStage f s ∧ sumStage f s < 2 / 3 :=
  ⟨partial_nonneg f s, lt_of_le_of_lt (partial_le_geometric f hf s)
    (geometric_lt (cutoff f s))⟩

/-- Decidable membership in a finite image, not in the infinite range. -/
def finiteDigit (f : ℕ → ℕ) (s j : ℕ) : ℕ :=
  if j ∈ (Finset.range s).image f then 1 else 0

theorem finiteDigit_bound (f : ℕ → ℕ) (s j : ℕ) : finiteDigit f s j ≤ 1 := by
  unfold finiteDigit
  split <;> omega

theorem partial_rationalDigits (f : ℕ → ℕ) (hf : Function.Injective f) (s : ℕ) :
    sumStage f s = rationalDigits (finiteDigit f s) (cutoff f s) := by
  rw [partial_image f hf, rationalDigits_sum]
  have hs : (Finset.range s).image f ⊆ Finset.range (cutoff f s) := by
    intro j hj
    exact Finset.mem_range.mpr (Nat.lt_succ_of_le (Finset.le_sup (f := id) hj))
  calc
    (∑ j ∈ (Finset.range s).image f, weight j) =
        ∑ j ∈ (Finset.range s).image f,
          2 * (finiteDigit f s j : ℚ) / (4 : ℚ) ^ (j + 1) := by
      apply Finset.sum_congr rfl
      intro j hj
      simp [finiteDigit, hj, weight]
    _ = ∑ j ∈ Finset.range (cutoff f s),
        2 * (finiteDigit f s j : ℚ) / (4 : ℚ) ^ (j + 1) := by
      apply Finset.sum_subset hs
      intro j _ hj
      simp [finiteDigit, hj]

#print axioms numerator_bound
#print axioms rationalDigits_bounds
#print axioms geometric_identity
#print axioms partial_bounds
#print axioms partial_rationalDigits

end MatematicaAbierta.Continuo.SumasRacionalesFinitas
