import MatematicaAbierta.Continuo.PrimitividadCertificadosSuma
import Mathlib.Algebra.Order.Archimedean.Basic

/-!
# FDC-AUD-025-M04c — Completitud de la etapa de certificados de suma

B4: para dos programas que deciden cortes principales reales, toda consulta
racional estrictamente separada de la frontera de la suma obtiene un
certificado interior o exterior en una etapa enumerada. La demostración
separa densidad racional, margen estricto, convergencia de `evaln` y
codificación de la cuaterna de parámetros.

No se asume la decidibilidad de la igualdad con la frontera.
-/

namespace Continuo.Indices

open Set
open scoped Pointwise

/-- Converso aritmético para desigualdades inferiores certificables. -/
private theorem arithmeticStage_true_complete_m04c
    (u v d plus minus s t : ℕ)
    (hd : 0 < d) (hs : 0 < s) (ht : 0 < t)
    (h :
      ((u : ℚ) - (v : ℚ)) / (d : ℚ) <
        ((plus : ℚ) - (minus : ℚ)) / (s : ℚ) -
          1 / (t : ℚ)) :
    arithmeticStage u v d plus minus s t = some true := by
  have hdq : (d : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hd)
  have hsq : (s : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hs)
  have htq : (t : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt ht)
  have hprod :
      0 < (d : ℚ) * (s : ℚ) * (t : ℚ) := by
    positivity
  have hscaled :
      ((((u : ℚ) - (v : ℚ)) / (d : ℚ)) -
        (((plus : ℚ) - (minus : ℚ)) / (s : ℚ) -
          1 / (t : ℚ))) *
        ((d : ℚ) * (s : ℚ) * (t : ℚ)) =
      ((u * s * t + minus * d * t + s * d : ℕ) : ℚ) -
        ((v * s * t + plus * d * t : ℕ) : ℚ) := by
    push_cast
    field_simp [hdq, hsq, htq]
    ring
  have hsub :
      (((u : ℚ) - (v : ℚ)) / (d : ℚ)) -
        (((plus : ℚ) - (minus : ℚ)) / (s : ℚ) -
          1 / (t : ℚ)) < 0 := by
    exact sub_neg.mpr h
  have hmul :
      ((((u : ℚ) - (v : ℚ)) / (d : ℚ)) -
        (((plus : ℚ) - (minus : ℚ)) / (s : ℚ) -
          1 / (t : ℚ))) *
        ((d : ℚ) * (s : ℚ) * (t : ℚ)) < 0 := by
    nlinarith
  rw [hscaled] at hmul
  have hcast :
      ((u * s * t + minus * d * t + s * d : ℕ) : ℚ) <
        ((v * s * t + plus * d * t : ℕ) : ℚ) := by
    exact sub_neg.mp hmul
  have hn :
      u * s * t + minus * d * t + s * d <
        v * s * t + plus * d * t := by
    exact_mod_cast hcast
  simp [arithmeticStage, hn]

/-- Converso aritmético para desigualdades exteriores certificables. -/
private theorem arithmeticStage_false_complete_m04c
    (u v d plus minus s t : ℕ)
    (hd : 0 < d) (hs : 0 < s) (ht : 0 < t)
    (h :
      ((plus : ℚ) - (minus : ℚ)) / (s : ℚ) +
          1 / (t : ℚ) <
        ((u : ℚ) - (v : ℚ)) / (d : ℚ)) :
    arithmeticStage u v d plus minus s t = some false := by
  have hdq : (d : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hd)
  have hsq : (s : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hs)
  have htq : (t : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt ht)
  have hprod :
      0 < (d : ℚ) * (s : ℚ) * (t : ℚ) := by
    positivity
  have hscaled :
      ((((plus : ℚ) - (minus : ℚ)) / (s : ℚ) +
          1 / (t : ℚ)) -
        (((u : ℚ) - (v : ℚ)) / (d : ℚ))) *
        ((d : ℚ) * (s : ℚ) * (t : ℚ)) =
      ((plus * d * t + v * s * t + s * d : ℕ) : ℚ) -
        ((u * s * t + minus * d * t : ℕ) : ℚ) := by
    push_cast
    field_simp [hdq, hsq, htq]
    ring
  have hsub :
      (((plus : ℚ) - (minus : ℚ)) / (s : ℚ) +
          1 / (t : ℚ)) -
        (((u : ℚ) - (v : ℚ)) / (d : ℚ)) < 0 := by
    exact sub_neg.mpr h
  have hmul :
      ((((plus : ℚ) - (minus : ℚ)) / (s : ℚ) +
          1 / (t : ℚ)) -
        (((u : ℚ) - (v : ℚ)) / (d : ℚ))) *
        ((d : ℚ) * (s : ℚ) * (t : ℚ)) < 0 := by
    nlinarith
  rw [hscaled] at hmul
  have hcast :
      ((plus * d * t + v * s * t + s * d : ℕ) : ℚ) <
        ((u * s * t + minus * d * t : ℕ) : ℚ) := by
    exact sub_neg.mp hmul
  have hn :
      plus * d * t + v * s * t + s * d <
        u * s * t + minus * d * t := by
    exact_mod_cast hcast
  have htqpos : 0 < (t : ℚ) := by
    exact_mod_cast ht
  have hradius : 0 < (1 : ℚ) / (t : ℚ) :=
    one_div_pos.mpr htqpos
  have hfirst :
      ¬ (u * s * t + minus * d * t + s * d <
          v * s * t + plus * d * t) := by
    intro hfirstNat
    have hout :
        arithmeticStage u v d plus minus s t = some true := by
      simp [arithmeticStage, hfirstNat]
    have hlow :=
      arithmeticStage_true_sound
        u v d plus minus s t hd hs ht hout
    linarith
  simp [arithmeticStage, hfirst, hn]

/-- La desigualdad racional estricta con margen fuerza una respuesta interior. -/
theorem sumStageComparison_true_complete (z i j t : ℕ) (ht : 0 < t)
    (h : codedQuery z <
        codedQuery i + codedQuery j - 1 / (t : ℚ)) :
    sumStageComparison z i j t = some true := by
  have hs : 0 < sumStageDenominator i j :=
    mul_pos (queryDenominator_pos i) (queryDenominator_pos j)
  have hraw :
      ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ) <
        ((sumStagePositive i j : ℚ) - (sumStageNegative i j : ℚ)) /
          (sumStageDenominator i j : ℚ) - 1 / (t : ℚ) := by
    change codedQuery z <
      ((sumStagePositive i j : ℚ) - (sumStageNegative i j : ℚ)) /
        (sumStageDenominator i j : ℚ) - 1 / (t : ℚ)
    rw [sumStage_rational_add]
    exact h
  exact arithmeticStage_true_complete_m04c _ _ _ _ _ _ _
    (queryDenominator_pos z) hs ht hraw

/-- La desigualdad racional estricta con margen fuerza una respuesta exterior. -/
theorem sumStageComparison_false_complete (z i j t : ℕ) (ht : 0 < t)
    (h : codedQuery i + codedQuery j + 1 / (t : ℚ) <
        codedQuery z) :
    sumStageComparison z i j t = some false := by
  have hs : 0 < sumStageDenominator i j :=
    mul_pos (queryDenominator_pos i) (queryDenominator_pos j)
  have hraw :
      ((sumStagePositive i j : ℚ) - (sumStageNegative i j : ℚ)) /
          (sumStageDenominator i j : ℚ) + 1 / (t : ℚ) <
        ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ) := by
    change
      ((sumStagePositive i j : ℚ) - (sumStageNegative i j : ℚ)) /
        (sumStageDenominator i j : ℚ) + 1 / (t : ℚ) <
          codedQuery z
    rw [sumStage_rational_add]
    exact h
  exact arithmeticStage_false_complete_m04c _ _ _ _ _ _ _
    (queryDenominator_pos z) hs ht hraw

/-- Dos racionales interiores dejan la consulta bajo su suma. -/
private theorem exists_interior_rational_witnesses (x y : ℝ) (z : ℕ)
    (h : (codedQuery z : ℝ) < x + y) :
    ∃ i j : ℕ,
      (codedQuery i : ℝ) < x ∧
      (codedQuery j : ℝ) < y ∧
      codedQuery z < codedQuery i + codedQuery j := by
  have haSpace : (codedQuery z : ℝ) - y < x := by linarith
  obtain ⟨a, haLower, haUpper⟩ := exists_rat_btwn haSpace
  have hbSpace : (codedQuery z : ℝ) - (a : ℝ) < y := by linarith
  obtain ⟨b, hbLower, hbUpper⟩ := exists_rat_btwn hbSpace
  obtain ⟨i, hi⟩ := codedQuery_surjective a
  obtain ⟨j, hj⟩ := codedQuery_surjective b
  have hsum : (codedQuery z : ℝ) < (a : ℝ) + (b : ℝ) := by linarith
  have hsumQ : codedQuery z < a + b := by exact_mod_cast hsum
  refine ⟨i, j, ?_, ?_, ?_⟩
  · simpa [hi] using haUpper
  · simpa [hj] using hbUpper
  · simpa [hi, hj] using hsumQ

/-- Dos racionales exteriores dejan la consulta sobre su suma. -/
private theorem exists_exterior_rational_witnesses (x y : ℝ) (z : ℕ)
    (h : x + y < (codedQuery z : ℝ)) :
    ∃ i j : ℕ,
      x < (codedQuery i : ℝ) ∧
      y < (codedQuery j : ℝ) ∧
      codedQuery i + codedQuery j < codedQuery z := by
  have haSpace : x < (codedQuery z : ℝ) - y := by linarith
  obtain ⟨a, haLower, haUpper⟩ := exists_rat_btwn haSpace
  have hbSpace : y < (codedQuery z : ℝ) - (a : ℝ) := by linarith
  obtain ⟨b, hbLower, hbUpper⟩ := exists_rat_btwn hbSpace
  obtain ⟨i, hi⟩ := codedQuery_surjective a
  obtain ⟨j, hj⟩ := codedQuery_surjective b
  have hsum : (a : ℝ) + (b : ℝ) < (codedQuery z : ℝ) := by linarith
  have hsumQ : a + b < codedQuery z := by exact_mod_cast hsum
  refine ⟨i, j, ?_, ?_, ?_⟩
  · simpa [hi] using haLower
  · simpa [hj] using hbLower
  · simpa [hi, hj] using hsumQ

/-- La semántica total de un decididor produce eventualmente una observación
finita de `true` por `evaln`. -/
private theorem evaln_cut_true_eventually (e : Code) (x : ℝ)
    (hdec : DecidesCut e (lowerCut x)) (i : ℕ)
    (hi : (codedQuery i : ℝ) < x) :
    ∃ fuel : ℕ,
      Encodable.encode true ∈ Nat.Partrec.Code.evaln fuel e i := by
  obtain ⟨b, hb, hiff⟩ := hdec i
  have htrue : b = true :=
    hiff.mpr ((lowerCut_mem_iff _ x).mpr hi)
  subst b
  exact (Nat.Partrec.Code.evaln_complete).mp hb

/-- La exterioridad estricta produce eventualmente una observación
finita de `false` por `evaln`. -/
private theorem evaln_cut_false_eventually (e : Code) (x : ℝ)
    (hdec : DecidesCut e (lowerCut x)) (i : ℕ)
    (hi : x < (codedQuery i : ℝ)) :
    ∃ fuel : ℕ,
      Encodable.encode false ∈ Nat.Partrec.Code.evaln fuel e i := by
  obtain ⟨b, hb, hiff⟩ := hdec i
  have hfalse : b = false := by
    cases b with
    | false => rfl
    | true =>
        exfalso
        have hmem : codedQuery i ∈ lowerCut x := hiff.mp rfl
        have hlow : (codedQuery i : ℝ) < x :=
          (lowerCut_mem_iff _ x).mp hmem
        exact (lt_asymm hlow hi)
  subst b
  exact (Nat.Partrec.Code.evaln_complete).mp hb

/-- La existencia de un certificado exterior basta para que la etapa lo
emita: las condiciones interior y exterior son incompatibles. -/
theorem sumCertificateStage_false_iff
    (w : ((Code × Code) × ℕ) × ℕ) :
    sumCertificateStage w = some false ↔ sumStageExterior w := by
  constructor
  · exact sumCertificateStage_false_sound w
  · intro he
    have hni : ¬ sumStageInterior w := by
      intro hi
      have hcontr : sumStageComparison w.1.2
          (sumStageLeft w.2) (sumStageRight w.2)
          (sumStageMargin w.2) = some true := hi.2.2
      rw [he.2.2] at hcontr
      cases hcontr
    simp [sumCertificateStage, hni, he]

/-- B4: toda consulta racional estrictamente distinta de la frontera
de una suma de cortes con decididores correctos obtiene un certificado
finito, ya sea interior o exterior. -/
theorem sumCertificateStage_eventually (eA eB : Code) (x y : ℝ)
    (hA : DecidesCut eA (lowerCut x))
    (hB : DecidesCut eB (lowerCut y))
    (z : ℕ) (hne : x + y ≠ (codedQuery z : ℝ)) :
    ∃ n : ℕ, ∃ b : Bool,
      sumCertificateStage (((eA, eB), z), n) = some b := by
  rcases lt_trichotomy (codedQuery z : ℝ) (x + y) with hlt | heq | hgt
  · obtain ⟨i, j, hi, hj, hsum⟩ :=
      exists_interior_rational_witnesses x y z hlt
    obtain ⟨t, ht⟩ := exists_nat_one_div_lt
      (show (0 : ℚ) <
        codedQuery i + codedQuery j - codedQuery z by linarith)
    have hmargin :
        codedQuery z <
          codedQuery i + codedQuery j - 1 / (((t + 1 : ℕ) : ℚ)) := by
      have ht' : 1 / (((t + 1 : ℕ) : ℚ)) <
          codedQuery i + codedQuery j - codedQuery z := by
        simpa only [Nat.cast_add, Nat.cast_one] using ht
      have ht' : 1 / (((t + 1 : ℕ) : ℚ)) <
          codedQuery z - (codedQuery i + codedQuery j) := by
        simpa only [Nat.cast_add, Nat.cast_one] using ht
      linarith
    have hcomparison :
        sumStageComparison z i j (t + 1) = some true :=
      sumStageComparison_true_complete z i j (t + 1)
        (by omega) hmargin
    obtain ⟨kA, hkA⟩ := evaln_cut_true_eventually eA x hA i hi
    obtain ⟨kB, hkB⟩ := evaln_cut_true_eventually eB y hB j hj
    let k := max kA kB
    have hfuelA :
        Nat.Partrec.Code.evaln (k + 1) eA i =
          some (Encodable.encode true) := by
      have hm := Nat.Partrec.Code.evaln_mono
        (show kA ≤ k + 1 by dsimp [k]; omega) hkA
      simpa only [Option.mem_def] using hm
    have hfuelB :
        Nat.Partrec.Code.evaln (k + 1) eB j =
          some (Encodable.encode true) := by
      have hm := Nat.Partrec.Code.evaln_mono
        (show kB ≤ k + 1 by dsimp [k]; omega) hkB
      simpa only [Option.mem_def] using hm
    let n := Nat.pair i (Nat.pair j (Nat.pair t k))
    have hp := sumStageParameters_surjective i j t k
    have hparams :
        sumStageLeft n = i ∧
        sumStageRight n = j ∧
        sumStageMargin n = t + 1 ∧
        sumStageFuel n = k + 1 := by
      simpa only [n] using hp
    rcases hparams with ⟨hli, hlj, hlm, hlf⟩
    refine ⟨n, true, ?_⟩
    apply (sumCertificateStage_true_iff _).mpr
    change
      Nat.Partrec.Code.evaln (sumStageFuel n) eA (sumStageLeft n) =
          some (Encodable.encode true) ∧
      Nat.Partrec.Code.evaln (sumStageFuel n) eB (sumStageRight n) =
          some (Encodable.encode true) ∧
      sumStageComparison z (sumStageLeft n) (sumStageRight n)
        (sumStageMargin n) = some true
    rw [hli, hlj, hlm, hlf]
    exact ⟨hfuelA, hfuelB, hcomparison⟩
  · exact (hne heq.symm).elim
  · obtain ⟨i, j, hi, hj, hsum⟩ :=
      exists_exterior_rational_witnesses x y z hgt
    obtain ⟨t, ht⟩ := exists_nat_one_div_lt
      (show (0 : ℚ) <
        codedQuery z - (codedQuery i + codedQuery j) by linarith)
    have hmargin :
        codedQuery i + codedQuery j + 1 / (((t + 1 : ℕ) : ℚ)) <
          codedQuery z := by
      linarith
    have hcomparison :
        sumStageComparison z i j (t + 1) = some false :=
      sumStageComparison_false_complete z i j (t + 1)
        (by omega) hmargin
    obtain ⟨kA, hkA⟩ := evaln_cut_false_eventually eA x hA i hi
    obtain ⟨kB, hkB⟩ := evaln_cut_false_eventually eB y hB j hj
    let k := max kA kB
    have hfuelA :
        Nat.Partrec.Code.evaln (k + 1) eA i =
          some (Encodable.encode false) := by
      have hm := Nat.Partrec.Code.evaln_mono
        (show kA ≤ k + 1 by dsimp [k]; omega) hkA
      simpa only [Option.mem_def] using hm
    have hfuelB :
        Nat.Partrec.Code.evaln (k + 1) eB j =
          some (Encodable.encode false) := by
      have hm := Nat.Partrec.Code.evaln_mono
        (show kB ≤ k + 1 by dsimp [k]; omega) hkB
      simpa only [Option.mem_def] using hm
    let n := Nat.pair i (Nat.pair j (Nat.pair t k))
    have hp := sumStageParameters_surjective i j t k
    have hparams :
        sumStageLeft n = i ∧
        sumStageRight n = j ∧
        sumStageMargin n = t + 1 ∧
        sumStageFuel n = k + 1 := by
      simpa only [n] using hp
    rcases hparams with ⟨hli, hlj, hlm, hlf⟩
    refine ⟨n, false, ?_⟩
    apply (sumCertificateStage_false_iff _).mpr
    change
      Nat.Partrec.Code.evaln (sumStageFuel n) eA (sumStageLeft n) =
          some (Encodable.encode false) ∧
      Nat.Partrec.Code.evaln (sumStageFuel n) eB (sumStageRight n) =
          some (Encodable.encode false) ∧
      sumStageComparison z (sumStageLeft n) (sumStageRight n)
        (sumStageMargin n) = some false
    rw [hli, hlj, hlm, hlf]
    exact ⟨hfuelA, hfuelB, hcomparison⟩

end Continuo.Indices
