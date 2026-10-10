import MatematicaAbierta.Continuo.ReversionModular

/-!
FOR-11 / M03: closed interval bounds passed directly to a fast rational code.
No real supremum, infinite range set or completeness theorem is used here.
The finite-sum construction of EventualBands and its RCA₀ derivability are still open.
-/
namespace MatematicaAbierta.Continuo.BandasCodigo
open ReversionModular

def ApproximationBound (q a : ℕ → ℚ) : Prop :=
  ∀ k (ε : ℚ), 0 < ε → ∃ S, ∀ t, S ≤ t →
    |q t-a k| ≤ 1/(2:ℚ)^k + ε

def ScaledApproximation (q a : ℕ → ℚ) : Prop :=
  ∀ n (ε : ℚ), 0 < ε → ∃ S, ∀ t, S ≤ t →
    |4^(n+1)*q t-scaledSample a n| ≤ 1/64 + ε

theorem scale_error (n : ℕ) :
    (4:ℚ)^(n+1) * (1/(2:ℚ)^(readIndex n)) = 1/64 := by
  have he : (2:ℚ)^(readIndex n) = 64*(4:ℚ)^(n+1) := by
    unfold readIndex
    rw [show 2*n+8 = 2*(n+1)+6 by omega, pow_add, pow_mul]
    norm_num
    ring
  rw [he]
  have hp : (4:ℚ)^(n+1) ≠ 0 := by positivity
  field_simp

theorem scaled_of_approximation (q a : ℕ → ℚ) (ha : ApproximationBound q a) :
    ScaledApproximation q a := by
  intro n ε hε
  have hp : 0 < (4:ℚ)^(n+1) := by positivity
  obtain ⟨S,hs⟩ := ha (readIndex n) (ε/4^(n+1)) (div_pos hε hp)
  refine ⟨S,fun t ht => ?_⟩
  have h := mul_le_mul_of_nonneg_left (hs t ht) hp.le
  rw [mul_add, scale_error, mul_div_cancel₀ _ hp.ne'] at h
  simpa [scaledSample, ← mul_sub, abs_mul, abs_of_pos hp] using h

/-- A finite-stage envelope: the same integer prefix works after some stage. -/
def EventualBands (f : ℕ → ℕ) (q : ℕ → ℚ) : Prop :=
  ∀ n, ∃ m : ℤ, ∃ S : ℕ,
    ((∃ i, f i=n) → ∀ t, S ≤ t →
      (4*m+2:ℤ) ≤ (4:ℚ)^(n+1)*q t ∧
      (4:ℚ)^(n+1)*q t ≤ (4*m+2:ℤ)+(2/3:ℚ)) ∧
    ((¬ ∃ i, f i=n) → ∀ t, S ≤ t →
      (4*m:ℤ) ≤ (4:ℚ)^(n+1)*q t ∧
      (4:ℚ)^(n+1)*q t ≤ (4*m:ℤ)+(2/3:ℚ))

theorem closed_bounds_of_approximation (v : ℕ → ℚ) (z L U E : ℚ)
    (hb : ∃ S, ∀ t, S ≤ t → L ≤ v t ∧ v t ≤ U)
    (ha : ∀ ε : ℚ, 0 < ε → ∃ S, ∀ t, S ≤ t → |v t-z| ≤ E+ε) :
    L-E ≤ z ∧ z ≤ U+E := by
  obtain ⟨S,hS⟩ := hb
  constructor
  · by_contra hn
    have hg : 0 < (L-E-z)/2 := by linarith
    obtain ⟨T,hT⟩ := ha ((L-E-z)/2) hg
    have hlo := (hS (max S T) (le_max_left _ _)).1
    have herr := (abs_le.mp (hT (max S T) (le_max_right _ _))).2
    linarith
  · by_contra hn
    have hg : 0 < (z-U-E)/2 := by linarith
    obtain ⟨T,hT⟩ := ha ((z-U-E)/2) hg
    have hup := (hS (max S T) (le_max_left _ _)).2
    have herr := (abs_le.mp (hT (max S T) (le_max_right _ _))).1
    linarith

/-- This discharges the code-limit-to-bands bridge, conditional on a finite-stage envelope. -/
theorem rangeBands_of_eventual (f : ℕ → ℕ) (q a : ℕ → ℚ)
    (hb : EventualBands f q) (ha : ApproximationBound q a) : RangeBands f a := by
  have hscaled := scaled_of_approximation q a ha
  intro n
  obtain ⟨m,S,hy,hn⟩ := hb n
  refine ⟨m,?_,?_⟩
  · intro h
    exact closed_bounds_of_approximation
      (fun t => 4^(n+1)*q t) (scaledSample a n)
      (4*m+2:ℤ) ((4*m+2:ℤ)+(2/3:ℚ)) (1/64)
      ⟨S,hy h⟩ (hscaled n)
  · intro h
    exact closed_bounds_of_approximation
      (fun t => 4^(n+1)*q t) (scaledSample a n)
      (4*m:ℤ) ((4*m:ℤ)+(2/3:ℚ)) (1/64)
      ⟨S,hn h⟩ (hscaled n)

theorem decoded_range_from_eventual (f : ℕ → ℕ) (q a : ℕ → ℚ)
    (hb : EventualBands f q) (ha : ApproximationBound q a) (n : ℕ) :
    decoded a n ↔ ∃ i, f i=n :=
  decoded_iff_range f a (rangeBands_of_eventual f q a hb ha) n

#print axioms scale_error
#print axioms scaled_of_approximation
#print axioms rangeBands_of_eventual
#print axioms decoded_range_from_eventual
end MatematicaAbierta.Continuo.BandasCodigo
