import Mathlib.Data.Rat.Floor
import Mathlib.Tactic

/-!
FOR-11 / CIERRE-M02: arithmetic and graph-reading obligations of RM005.1/2 and P005b.
These are ambient Lean theorems, NOT a derivation of RCA₀ or ACA₀.
Band hypotheses are explicit obligations; no global range set is assumed as input.
-/
namespace MatematicaAbierta.Continuo.ReversionModular

/-- Euclidean floor and remainder, also correct for negative approximations. -/
def residue (z : ℚ) : ℤ := (⌊z + 1 / 8⌋ : ℤ) % 4

def readIndex (n : ℕ) : ℕ := 2 * n + 8

def scaledSample (a : ℕ → ℚ) (n : ℕ) : ℚ := 4 ^ (n + 1) * a (readIndex n)

def decoded (a : ℕ → ℚ) (n : ℕ) : Prop := residue (scaledSample a n) = 2

instance decodedDecidable (a : ℕ → ℚ) (n : ℕ) : Decidable (decoded a n) :=
  inferInstanceAs (Decidable (residue (scaledSample a n) = 2))

/-- The explicit margins 7/64 and 155/192, with no floor ambiguity. -/
theorem band_margins (m : ℤ) (d : ℤ) (z : ℚ)
    (hl : (4 * m + d : ℤ) - (1 / 64 : ℚ) ≤ z)
    (hu : z ≤ (4 * m + d : ℤ) + (2 / 3 : ℚ) + 1 / 64) :
    (4 * m + d : ℤ) < z + (1 / 8 : ℚ) ∧
    z + (1 / 8 : ℚ) < (4 * m + d : ℤ) + 1 := by
  constructor <;> linarith

 theorem floor_of_band (m d : ℤ) (z : ℚ)
    (hl : (4 * m + d : ℤ) - (1 / 64 : ℚ) ≤ z)
    (hu : z ≤ (4 * m + d : ℤ) + (2 / 3 : ℚ) + 1 / 64) :
    (⌊z + 1 / 8⌋ : ℤ) = 4 * m + d := by
  have h := band_margins m d z hl hu
  exact Int.floor_eq_iff.mpr ⟨le_of_lt h.1, h.2⟩

 theorem residue_of_band (m d : ℤ) (z : ℚ)
    (hl : (4 * m + d : ℤ) - (1 / 64 : ℚ) ≤ z)
    (hu : z ≤ (4 * m + d : ℤ) + (2 / 3 : ℚ) + 1 / 64) :
    residue z = d % 4 := by
  unfold residue
  rw [floor_of_band m d z hl hu]
  omega

 theorem zero_band (m : ℤ) (z : ℚ)
    (hl : (4 * m : ℤ) - (1 / 64 : ℚ) ≤ z)
    (hu : z ≤ (4 * m : ℤ) + (2 / 3 : ℚ) + 1 / 64) : residue z = 0 := by
  have h := residue_of_band m 0 z (by simpa using hl) (by simpa using hu)
  simpa using h

 theorem one_band (m : ℤ) (z : ℚ)
    (hl : (4 * m + 2 : ℤ) - (1 / 64 : ℚ) ≤ z)
    (hu : z ≤ (4 * m + 2 : ℤ) + (2 / 3 : ℚ) + 1 / 64) : residue z = 2 := by
  simpa using residue_of_band m 2 z hl hu

/-- No preceding bits are needed: the integer prefix disappears modulo four. -/
theorem residue_bit (m : ℤ) (b : Bool) (z : ℚ)
    (hl : (4 * m + (if b then 2 else 0) : ℤ) - (1 / 64 : ℚ) ≤ z)
    (hu : z ≤ (4 * m + (if b then 2 else 0) : ℤ) + (2 / 3 : ℚ) + 1 / 64) :
    residue z = 2 ↔ b = true := by
  cases b with
  | false => simp only [Bool.false_eq_true, ↓reduceIte, add_zero] at hl hu
             rw [zero_band m z hl hu]
             simp
  | true => simp only [↓reduceIte] at hl hu
            rw [one_band m z hl hu]
            simp

/-- A proof boundary: the band construction is a hypothesis, not an axiom. -/
def RangeBands (f : ℕ → ℕ) (a : ℕ → ℚ) : Prop :=
  ∀ n, ∃ m : ℤ,
    ((∃ i, f i = n) →
      (4 * m + 2 : ℤ) - (1 / 64 : ℚ) ≤ scaledSample a n ∧
      scaledSample a n ≤ (4 * m + 2 : ℤ) + (2 / 3 : ℚ) + 1 / 64) ∧
    ((¬ ∃ i, f i = n) →
      (4 * m : ℤ) - (1 / 64 : ℚ) ≤ scaledSample a n ∧
      scaledSample a n ≤ (4 * m : ℤ) + (2 / 3 : ℚ) + 1 / 64)

 theorem decoded_iff_range (f : ℕ → ℕ) (a : ℕ → ℚ) (hb : RangeBands f a) (n : ℕ) :
    decoded a n ↔ ∃ i, f i = n := by
  obtain ⟨m, hy, hn⟩ := hb n
  by_cases h : ∃ i, f i = n
  · have hr := one_band m (scaledSample a n) (hy h).1 (hy h).2
    simp [decoded, hr, h]
  · have hr := zero_band m (scaledSample a n) (hn h).1 (hn h).2
    simp [decoded, hr, h]

/-- Reading a function through its graph: totality and uniqueness are separate. -/
structure TotalUniqueGraph (G : ℕ → ℚ → Prop) : Prop where
  total : ∀ k, ∃ u, G k u
  unique : ∀ k u v, G k u → G k v → u = v

def positiveRead (G : ℕ → ℚ → Prop) (R : ℕ → ℚ → Prop) (n : ℕ) : Prop :=
  ∃ u, G (readIndex n) u ∧ R n u

def negativeRead (G : ℕ → ℚ → Prop) (R : ℕ → ℚ → Prop) (n : ℕ) : Prop :=
  ∃ u, G (readIndex n) u ∧ ¬ R n u

 theorem reads_incompatible (G R : ℕ → ℚ → Prop) (hg : TotalUniqueGraph G) (n : ℕ) :
    ¬ (positiveRead G R n ∧ negativeRead G R n) := by
  rintro ⟨⟨u, hgu, hru⟩, ⟨v, hgv, hrv⟩⟩
  have huv := hg.unique (readIndex n) u v hgu hgv
  exact hrv (huv ▸ hru)

 theorem reads_exhaustive (G R : ℕ → ℚ → Prop) (hg : TotalUniqueGraph G) (n : ℕ) :
    positiveRead G R n ∨ negativeRead G R n := by
  obtain ⟨u, hu⟩ := hg.total (readIndex n)
  by_cases hr : R n u
  · exact Or.inl ⟨u, hu, hr⟩
  · exact Or.inr ⟨u, hu, hr⟩

 theorem positiveRead_iff_not_negativeRead (G R : ℕ → ℚ → Prop)
    (hg : TotalUniqueGraph G) (n : ℕ) :
    positiveRead G R n ↔ ¬ negativeRead G R n := by
  constructor
  · intro hp hn
    exact reads_incompatible G R hg n ⟨hp, hn⟩
  · intro hn
    rcases reads_exhaustive G R hg n with hp | hneg
    · exact hp
    · exact False.elim (hn hneg)

 theorem graph_of_function_total_unique (a : ℕ → ℚ) :
    TotalUniqueGraph (fun k u => u = a k) := by
  constructor
  · intro k
    exact ⟨a k, rfl⟩
  · intro k u v hu hv
    exact hu.trans hv.symm

 theorem positiveRead_function (a : ℕ → ℚ) (n : ℕ) :
    positiveRead (fun k u => u = a k)
      (fun j u => residue (4 ^ (j + 1) * u) = 2) n ↔ decoded a n := by
  simp [positiveRead, decoded, scaledSample]

 theorem negativeRead_function (a : ℕ → ℚ) (n : ℕ) :
    negativeRead (fun k u => u = a k)
      (fun j u => residue (4 ^ (j + 1) * u) = 2) n ↔ ¬ decoded a n := by
  simp [negativeRead, decoded, scaledSample]

/-- Output correctness if the missing band obligation is subsequently proved. -/
theorem positiveRead_iff_range (f : ℕ → ℕ) (a : ℕ → ℚ)
    (hb : RangeBands f a) (n : ℕ) :
    positiveRead (fun k u => u = a k)
      (fun j u => residue (4 ^ (j + 1) * u) = 2) n ↔ ∃ i, f i = n := by
  exact (positiveRead_function a n).trans (decoded_iff_range f a hb n)

/-- Bounded natural monotonicity stabilizes, in ambient classical Lean. -/
theorem bounded_monotone_stabilizes (c : ℕ → ℕ) (M : ℕ)
    (hc : Monotone c) (hb : ∀ s, c s ≤ M) :
    ∃ S, ∀ t, S ≤ t → c t = c S := by
  have he : ∃ s, ∀ t, c t ≤ c s := by
    by_contra hn
    push Not at hn
    have hp : ∀ k, ∃ s, k ≤ c s := by
      intro k
      induction k with
      | zero => exact ⟨0, Nat.zero_le _⟩
      | succ k ih =>
        obtain ⟨s, hs⟩ := ih
        obtain ⟨t, ht⟩ := hn s
        exact ⟨t, by omega⟩
    obtain ⟨s, hs⟩ := hp (M + 1)
    have hbs := hb s
    omega
  obtain ⟨S, hs⟩ := he
  exact ⟨S, fun t ht => Nat.le_antisymm (hs t) (hc ht)⟩

#print axioms residue_of_band
#print axioms decoded_iff_range
#print axioms positiveRead_iff_not_negativeRead
#print axioms positiveRead_iff_range
#print axioms bounded_monotone_stabilizes
end MatematicaAbierta.Continuo.ReversionModular
