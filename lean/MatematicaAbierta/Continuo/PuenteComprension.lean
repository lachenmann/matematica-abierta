import MatematicaAbierta.Continuo.CodificacionResiduo
import MatematicaAbierta.Continuo.BandasCodigo

/-!
M03: concrete bounded matrices and a conditional standard-model comprehension bridge.
Delta1Schema is an explicit hypothesis on a family of subsets of the STANDARD naturals.
It is not an implementation of the RCA₀ proof calculus, nor an ACA₀ theorem.
-/
namespace MatematicaAbierta.Continuo.PuenteComprension
open SintaxisAritmetica CodificacionResiduo ReversionModular

/-- Polynomial pairing: injective, but intentionally not asserted surjective. -/
def pair (x y : ℕ) : ℕ := (x+y)*(x+y)+x

theorem pair_left_le (x y : ℕ) : x ≤ pair x y := by unfold pair; omega

theorem pair_right_le (x y : ℕ) : y ≤ pair x y := by
  unfold pair
  nlinarith [Nat.le_mul_self y]

theorem pair_injective {x y u v : ℕ} (h : pair x y = pair u v) : x=u ∧ y=v := by
  have he : x+y=u+v := by
    unfold pair at h
    by_contra hn
    rcases lt_or_gt_of_ne hn with hl | hl <;> nlinarith
  unfold pair at h
  constructor <;> nlinarith

def code (p m d : ℕ) : ℕ := pair p (pair m d)

theorem code_bounds (p m d : ℕ) : p ≤ code p m d ∧ m ≤ code p m d ∧ d ≤ code p m d := by
  exact ⟨pair_left_le _ _, le_trans (pair_left_le m d) (pair_right_le _ _),
    le_trans (pair_right_le m d) (pair_right_le _ _)⟩

theorem code_injective {p m d p' m' d' : ℕ} (h : code p m d = code p' m' d') :
    p=p' ∧ m=m' ∧ d=d' := by
  obtain ⟨hp, hmd⟩ := pair_injective h
  obtain ⟨hm, hd⟩ := pair_injective hmd
  exact ⟨hp, hm, hd⟩

def pairTerm {n : ℕ} (x y : Term n) : Term n :=
  .add (.mul (.add x y) (.add x y)) x
def codeTerm {n : ℕ} (p m d : Term n) : Term n := pairTerm p (pairTerm m d)

def codePredicate (u : ℕ) : Prop :=
  ∃ p m d, u=code p m d ∧ ResidueTwo p m d

def codeMatrix {n s : ℕ} (u : Term n) : BoundedFormula n s :=
  .existsLt (.succ u)
    (.existsLt (.succ (u.rename Fin.succ))
      (.existsLt (.succ (u.rename (Fin.succ ∘ Fin.succ)))
        (.conj
          (.equal (u.rename (Fin.succ ∘ Fin.succ ∘ Fin.succ))
            (codeTerm (.var (Fin.succ (Fin.succ 0))) (.var (Fin.succ 0)) (.var 0)))
          (residueMatrix (.var (Fin.succ (Fin.succ 0))) (.var (Fin.succ 0)) (.var 0)))))

theorem codeMatrix_correct {n s : ℕ} (u : Term n)
    (ρ : Fin n → ℕ) (σ : Fin s → Set ℕ) :
    (codeMatrix u).eval ρ σ ↔ codePredicate (u.eval ρ) := by
  simp only [codeMatrix, BoundedFormula.eval, Term.eval, eval_rename,
    Function.comp_def, extend, Fin.cases_zero, Fin.cases_succ,
    codeTerm, pairTerm]
  change (∃ p, p < u.eval ρ + 1 ∧ ∃ m, m < u.eval ρ + 1 ∧
    ∃ d, d < u.eval ρ + 1 ∧ u.eval ρ = code p m d ∧
      (residueMatrix (.var (Fin.succ (Fin.succ 0))) (.var (Fin.succ 0)) (.var 0)).eval
        (extend d (extend m (extend p ρ))) σ) ↔ _
  simp only [residueMatrix_correct, Term.eval, extend_zero, extend_succ]
  simp only [← residueTwo_iff_residue]
  constructor
  · rintro ⟨p, _, m, _, d, _, he, hr⟩
    exact ⟨p,m,d,he,hr⟩
  · rintro ⟨p,m,d,he,hr⟩
    have hb := code_bounds p m d
    exact ⟨p, by omega, m, by omega, d, by omega, he, hr⟩

theorem codePredicate_correct (p m d : ℕ) :
    codePredicate (code p m d) ↔ residue (rational p m d) = 2 := by
  rw [← residueTwo_iff_residue]
  constructor
  · rintro ⟨p',m',d',he,hr⟩
    obtain ⟨rfl,rfl,rfl⟩ := code_injective he
    exact hr
  · intro hr
    exact ⟨p,m,d,rfl,hr⟩

/-- Variables are [u,n]; the sole set parameter is the graph of scaled samples. -/
def positiveMatrix : BoundedFormula 2 1 :=
  .conj (.member (pairTerm (.var (Fin.succ 0)) (.var 0)) 0) (codeMatrix (.var 0))
def negativeMatrix : BoundedFormula 2 1 :=
  .conj (.member (pairTerm (.var (Fin.succ 0)) (.var 0)) 0) (.neg (codeMatrix (.var 0)))

def assignment (n : ℕ) : Fin 1 → ℕ := fun _ => n
def parameters (G : Set ℕ) : Fin 1 → Set ℕ := fun _ => G
def graph (G : Set ℕ) (n u : ℕ) : Prop := pair n u ∈ G
def positive (G : Set ℕ) (n : ℕ) : Prop := ∃ u, graph G n u ∧ codePredicate u
def negative (G : Set ℕ) (n : ℕ) : Prop := ∃ u, graph G n u ∧ ¬ codePredicate u

theorem positiveMatrix_correct (G : Set ℕ) (n : ℕ) :
    sigma1 positiveMatrix (assignment n) (parameters G) ↔ positive G n := by
  simp only [sigma1, positiveMatrix, BoundedFormula.eval, codeMatrix_correct,
    pairTerm, Term.eval, extend, Fin.cases_zero, Fin.cases_succ,
    assignment, parameters, positive, graph, pair]

theorem negativeMatrix_correct (G : Set ℕ) (n : ℕ) :
    sigma1 negativeMatrix (assignment n) (parameters G) ↔ negative G n := by
  simp only [sigma1, negativeMatrix, BoundedFormula.eval, codeMatrix_correct,
    pairTerm, Term.eval, extend, Fin.cases_zero, Fin.cases_succ,
    assignment, parameters, negative, graph, pair]

structure NaturalGraph (G : Set ℕ) : Prop where
  total : ∀ n, ∃ u, graph G n u
  unique : ∀ n u v, graph G n u → graph G n v → u=v

theorem presentations_complement (G : Set ℕ) (hg : NaturalGraph G) (n : ℕ) :
    positive G n ↔ ¬ negative G n := by
  classical
  constructor
  · rintro ⟨u,hgu,hru⟩ ⟨v,hgv,hrv⟩
    have he := hg.unique n u v hgu hgv
    exact hrv (he ▸ hru)
  · intro hn
    obtain ⟨u,hu⟩ := hg.total n
    by_cases hr : codePredicate u
    · exact ⟨u,hu,hr⟩
    · exact False.elim (hn ⟨u,hu,hr⟩)

theorem presentations_delta1 (G : Set ℕ) (hg : NaturalGraph G) (n : ℕ) :
    sigma1 positiveMatrix (assignment n) (parameters G) ↔
      pi1 (.neg negativeMatrix) (assignment n) (parameters G) := by
  apply complementary_matrices_delta1
  rw [positiveMatrix_correct, negativeMatrix_correct]
  exact presentations_complement G hg n

/-- An explicit model-theoretic assumption; not an ambient set comprehension shortcut. -/
def Delta1Schema (M : Set (Set ℕ)) : Prop :=
  ∀ s (φ ψ : BoundedFormula 2 s) (σ : Fin s → Set ℕ),
    (∀ i, σ i ∈ M) →
    (∀ n, sigma1 φ (assignment n) σ ↔ pi1 ψ (assignment n) σ) →
    ∃ X ∈ M, ∀ n, n ∈ X ↔ sigma1 φ (assignment n) σ

theorem decoded_set_in_family (M : Set (Set ℕ)) (hc : Delta1Schema M)
    (G : Set ℕ) (hG : G ∈ M) (hg : NaturalGraph G) :
    ∃ X ∈ M, ∀ n, n ∈ X ↔ positive G n := by
  obtain ⟨X,hX,hdef⟩ := hc 1 positiveMatrix (.neg negativeMatrix) (parameters G)
    (fun _ => hG) (presentations_delta1 G hg)
  exact ⟨X,hX,fun n => (hdef n).trans (positiveMatrix_correct G n)⟩

/-- Valid scaled-sample graph. Internal construction and admissibility in RCA₀ remain open. -/
structure CodedScaledSamples (G : Set ℕ) (a : ℕ → ℚ) : Prop where
  naturalGraph : NaturalGraph G
  represents : ∀ n, ∃ p m d,
    graph G n (code p m d) ∧ rational p m d = scaledSample a n

/-- Computable rational fields give a concrete code; no choice of representation is used. -/
def encodeRat (z : ℚ) : ℕ := code z.num.toNat (-z.num).toNat (z.den-1)

theorem encodeRat_correct (z : ℚ) :
    rational z.num.toNat (-z.num).toNat (z.den-1) = z := by
  have hi : (z.num.toNat : ℤ) - ((-z.num).toNat : ℤ) = z.num := by omega
  have hq : (z.num.toNat : ℚ) - ((-z.num).toNat : ℚ) = (z.num : ℚ) := by
    exact_mod_cast hi
  have hd : z.den-1+1 = z.den := by have hp := z.den_pos; omega
  unfold rational
  have hdq : ((z.den-1 : ℕ) : ℚ)+1 = (z.den : ℚ) := by exact_mod_cast hd
  rw [hq, hdq, z.num_div_den]

/-- Ambient set construction only: membership in the permitted family M is not inferred. -/
def canonicalGraph (a : ℕ → ℚ) : Set ℕ :=
  {x | ∃ n, x = pair n (encodeRat (scaledSample a n))}

theorem canonicalGraph_read (a : ℕ → ℚ) (n u : ℕ) :
    graph (canonicalGraph a) n u ↔ u = encodeRat (scaledSample a n) := by
  constructor
  · rintro ⟨j,hj⟩
    obtain ⟨rfl,hu⟩ := pair_injective hj
    exact hu
  · intro hu
    exact ⟨n, by rw [hu]⟩

theorem canonicalGraph_valid (a : ℕ → ℚ) : CodedScaledSamples (canonicalGraph a) a := by
  constructor
  · constructor
    · intro n
      exact ⟨encodeRat (scaledSample a n), (canonicalGraph_read a n _).mpr rfl⟩
    · intro n u v hu hv
      exact ((canonicalGraph_read a n u).mp hu).trans ((canonicalGraph_read a n v).mp hv).symm
  · intro n
    let z := scaledSample a n
    exact ⟨z.num.toNat, (-z.num).toNat, z.den-1,
      (canonicalGraph_read a n _).mpr rfl, encodeRat_correct z⟩

theorem coded_positive_iff_decoded (G : Set ℕ) (a : ℕ → ℚ)
    (hg : CodedScaledSamples G a) (n : ℕ) :
    positive G n ↔ decoded a n := by
  obtain ⟨p,m,d,hcode,he⟩ := hg.represents n
  constructor
  · rintro ⟨u,hu,hr⟩
    have hu' := hg.naturalGraph.unique n u (code p m d) hu hcode
    rw [hu', codePredicate_correct, he] at hr
    exact hr
  · intro hr
    refine ⟨code p m d,hcode,?_⟩
    rw [codePredicate_correct, he]
    exact hr

/-- Conditional range existence in a standard-natural family satisfying this schema.
NOT a formal derivation RCA₀ + MON-rat ⇒ ACA₀. Every input hypothesis stays visible. -/
theorem range_in_family_from_bands (M : Set (Set ℕ)) (hc : Delta1Schema M)
    (G : Set ℕ) (hG : G ∈ M) (f : ℕ → ℕ) (a : ℕ → ℚ)
    (hg : CodedScaledSamples G a) (hb : RangeBands f a) :
    ∃ X ∈ M, ∀ n, n ∈ X ↔ ∃ i, f i=n := by
  obtain ⟨X,hX,hdef⟩ := decoded_set_in_family M hc G hG hg.naturalGraph
  exact ⟨X,hX,fun n => (hdef n).trans
    ((coded_positive_iff_decoded G a hg n).trans (decoded_iff_range f a hb n))⟩

/-- Combined conditional pipeline. MON-rat itself and the finite envelope are not derived here. -/
theorem range_in_family_from_limit (M : Set (Set ℕ)) (hc : Delta1Schema M)
    (G : Set ℕ) (hG : G ∈ M) (f : ℕ → ℕ) (q a : ℕ → ℚ)
    (hg : CodedScaledSamples G a) (hb : BandasCodigo.EventualBands f q)
    (ha : BandasCodigo.ApproximationBound q a) :
    ∃ X ∈ M, ∀ n, n ∈ X ↔ ∃ i, f i=n :=
  range_in_family_from_bands M hc G hG f a hg
    (BandasCodigo.rangeBands_of_eventual f q a hb ha)

/-- Concrete ambient graph, with the crucial family-membership obligation retained. -/
theorem range_from_canonical_graph (M : Set (Set ℕ)) (hc : Delta1Schema M)
    (f : ℕ → ℕ) (q a : ℕ → ℚ) (hG : canonicalGraph a ∈ M)
    (hb : BandasCodigo.EventualBands f q) (ha : BandasCodigo.ApproximationBound q a) :
    ∃ X ∈ M, ∀ n, n ∈ X ↔ ∃ i, f i=n :=
  range_in_family_from_limit M hc (canonicalGraph a) hG f q a
    (canonicalGraph_valid a) hb ha

#print axioms pair_injective
#print axioms codeMatrix_correct
#print axioms presentations_delta1
#print axioms decoded_set_in_family
#print axioms range_in_family_from_bands
#print axioms range_in_family_from_limit
#print axioms encodeRat_correct
#print axioms canonicalGraph_valid
#print axioms range_from_canonical_graph
end MatematicaAbierta.Continuo.PuenteComprension
