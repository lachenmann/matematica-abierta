import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic

/-!
FOR-01 / FDC-T001a. All sums and separators are rational and finite.
Index `i : Nat` represents the essay's positive position `i+1`.
No real completion, limit, computability, or choice of program is asserted.
-/
namespace MatematicaAbierta.Continuo.InyeccionBinaria

abbrev Bits := ℕ → Bool

def weight (n : ℕ) : ℚ := (1 / 4 : ℚ) ^ n

def partialSum (b : Bits) : ℕ → ℚ
  | 0 => 0
  | n + 1 => partialSum b n + if b n then 2 * weight (n + 1) else 0

def binaryCut (b : Bits) : Set ℚ := {q | ∃ n, q < partialSum b n}

def IsLowerCut (A : Set ℚ) : Prop :=
  A.Nonempty ∧ (∃ q, q ∉ A) ∧
  (∀ p ∈ A, ∀ q < p, q ∈ A) ∧ (∀ p ∈ A, ∃ r ∈ A, p < r)

lemma weight_pos (n : ℕ) : 0 < weight n := by
  unfold weight
  positivity

lemma weight_succ (n : ℕ) : weight (n + 1) = weight n / 4 := by
  unfold weight
  rw [pow_succ]
  ring

lemma partialSum_step_bounds (b : Bits) (n : ℕ) :
    0 ≤ partialSum b (n + 1) - partialSum b n ∧
    partialSum b (n + 1) - partialSum b n ≤ 2 * weight (n + 1) := by
  have hp := weight_pos (n + 1)
  cases h : b n <;> simp [partialSum, h] <;> linarith

lemma partialSum_mono (b : Bits) : Monotone (partialSum b) := by
  apply monotone_nat_of_le_succ
  intro n
  have h := (partialSum_step_bounds b n).1
  linarith

lemma partialSum_nonneg (b : Bits) (n : ℕ) : 0 ≤ partialSum b n := by
  have h := partialSum_mono b (Nat.zero_le n)
  simpa [partialSum] using h

lemma tail_bound (b : Bits) (k n : ℕ) (hkn : k ≤ n) :
    partialSum b n ≤ partialSum b k + (2 / 3 : ℚ) * (weight k - weight n) := by
  induction n, hkn using Nat.le_induction with
  | base => simp
  | succ n hkn ih =>
    have hs := (partialSum_step_bounds b n).2
    rw [weight_succ] at hs ⊢
    linarith

lemma partialSum_lt_two_thirds (b : Bits) (n : ℕ) :
    partialSum b n < (2 / 3 : ℚ) := by
  have h := tail_bound b 0 n (Nat.zero_le n)
  have hp := weight_pos n
  simp [partialSum, weight] at h
  linarith

 theorem binaryCut_isLowerCut (b : Bits) : IsLowerCut (binaryCut b) := by
  constructor
  · exact ⟨-1, 0, by norm_num [partialSum]⟩
  constructor
  · refine ⟨2 / 3, ?_⟩
    rintro ⟨n, hn⟩
    have h := partialSum_lt_two_thirds b n
    linarith
  constructor
  · rintro p ⟨n, hp⟩ q hq
    exact ⟨n, lt_trans hq hp⟩
  · rintro p ⟨n, hp⟩
    refine ⟨(p + partialSum b n) / 2, ⟨n, ?_⟩, ?_⟩ <;> linarith

lemma prefix_eq (b c : Bits) (k : ℕ) (h : ∀ i < k, b i = c i) :
    partialSum b k = partialSum c k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    have he := h k (Nat.lt_succ_self k)
    have hi := ih (fun i hi => h i (Nat.lt_trans hi (Nat.lt_succ_self k)))
    simp only [partialSum, hi, he]

lemma zero_bit_excludes_separator (b : Bits) (k : ℕ) (hb : b k = false) :
    partialSum b k + weight (k + 1) ∉ binaryCut b := by
  rintro ⟨n, hn⟩
  have hp := weight_pos (k + 1)
  by_cases hnk : n ≤ k
  · have hle := partialSum_mono b hnk
    linarith
  · have hkn : k + 1 ≤ n := by omega
    have ht := tail_bound b (k + 1) n hkn
    have hw := weight_pos n
    simp only [partialSum, hb, Bool.false_eq_true, ↓reduceIte, add_zero] at ht
    linarith

lemma one_bit_includes_separator (b : Bits) (k : ℕ) (hb : b k = true) :
    partialSum b k + weight (k + 1) ∈ binaryCut b := by
  refine ⟨k + 1, ?_⟩
  have hp := weight_pos (k + 1)
  simp only [partialSum, hb, ↓reduceIte]
  linarith

 theorem binaryCut_injective : Function.Injective binaryCut := by
  intro b c heq
  by_contra hbc
  have hex : ∃ k, b k ≠ c k := by
    by_contra hn
    push_neg at hn
    exact hbc (funext hn)
  let k := Nat.find hex
  have hk : b k ≠ c k := Nat.find_spec hex
  have hpre : ∀ i < k, b i = c i := by
    intro i hi
    exact not_not.mp (Nat.find_min hex hi)
  have hp := prefix_eq b c k hpre
  cases hb : b k <;> cases hc : c k
  · exact hk (hb.trans hc.symm)
  · have hn := zero_bit_excludes_separator b k hb
    have hy := one_bit_includes_separator c k hc
    rw [← hp, ← heq] at hy
    exact hn hy
  · have hn := zero_bit_excludes_separator c k hc
    have hy := one_bit_includes_separator b k hb
    rw [hp, heq] at hy
    exact hn hy
  · exact hk (hb.trans hc.symm)

/-- An actual injection into the subtype of proper, rounded rational lower cuts. -/
def toLowerCut (b : Bits) : {A : Set ℚ // IsLowerCut A} :=
  ⟨binaryCut b, binaryCut_isLowerCut b⟩

 theorem toLowerCut_injective : Function.Injective toLowerCut := by
  intro b c h
  exact binaryCut_injective (congrArg Subtype.val h)

#print axioms binaryCut_isLowerCut
#print axioms binaryCut_injective
#print axioms toLowerCut_injective
end MatematicaAbierta.Continuo.InyeccionBinaria
