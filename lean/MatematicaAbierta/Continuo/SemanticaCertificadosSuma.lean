import MatematicaAbierta.Continuo.CertificadosSumaEfectivos

/-!
# FDC-AUD-025-M04b — Corrección semántica de los certificados de suma

Una etapa puede emitir un certificado de interior o exterior estricto.
En ambos casos las respuestas finitas se contrastan con los decididores
prometidos y la desigualdad racional se interpreta en la semántica clásica.

Se preservan las hipótesis exactas de DecidesCut y lowerCut. La prueba
NO establece aún la primitividad recursiva de la etapa completa, ni su
completitud por enumeración, ni la proposición uniforme P025a.
-/

namespace Continuo.Indices

open Set
open scoped Pointwise

/-- La fracción con numeradores separados y producto de denominadores
representa la suma exacta de las dos consultas racionales codificadas. -/
theorem sumStage_rational_add (i j : ℕ) :
    (((sumStagePositive i j : ℕ) : ℚ) -
          ((sumStageNegative i j : ℕ) : ℚ)) /
        ((sumStageDenominator i j : ℕ) : ℚ) =
      codedQuery i + codedQuery j := by
  have hi : (queryDenominator i : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt (queryDenominator_pos i))
  have hj : (queryDenominator j : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt (queryDenominator_pos j))
  have hqi : codedQuery i =
      ((queryPositive i : ℚ) - (queryNegative i : ℚ)) /
        (queryDenominator i : ℚ) := rfl
  have hqj : codedQuery j =
      ((queryPositive j : ℚ) - (queryNegative j : ℚ)) /
        (queryDenominator j : ℚ) := rfl
  rw [hqi, hqj]
  simp only [sumStagePositive, sumStageNegative, sumStageDenominator,
    Nat.cast_add, Nat.cast_mul]
  field_simp [hi, hj]
  ring

/-- El certificado interior establece una separación racional estricta. -/
theorem sumStageComparison_true_sound (z i j t : ℕ) (ht : 0 < t)
    (h : sumStageComparison z i j t = some true) :
    codedQuery z < codedQuery i + codedQuery j := by
  have hs : 0 < sumStageDenominator i j :=
    mul_pos (queryDenominator_pos i) (queryDenominator_pos j)
  have hraw := arithmeticStage_true_sound
    (queryPositive z) (queryNegative z)
    (queryDenominator z) (sumStagePositive i j)
    (sumStageNegative i j) (sumStageDenominator i j) t
    (queryDenominator_pos z) hs ht
    (by simpa only [sumStageComparison] using h)
  have hq : codedQuery z <
      codedQuery i + codedQuery j - 1 / (t : ℚ) := by
    rw [sumStage_rational_add] at hraw
    exact hraw
  have hr : 0 ≤ (1 : ℚ) / (t : ℚ) := by positivity
  exact lt_of_lt_of_le hq (sub_le_self _ hr)

/-- El certificado exterior establece separación estricta en sentido contrario. -/
theorem sumStageComparison_false_sound (z i j t : ℕ) (ht : 0 < t)
    (h : sumStageComparison z i j t = some false) :
    codedQuery i + codedQuery j < codedQuery z := by
  have hs : 0 < sumStageDenominator i j :=
    mul_pos (queryDenominator_pos i) (queryDenominator_pos j)
  have hraw := arithmeticStage_false_sound
    (queryPositive z) (queryNegative z)
    (queryDenominator z) (sumStagePositive i j)
    (sumStageNegative i j) (sumStageDenominator i j) t
    (queryDenominator_pos z) hs ht
    (by simpa only [sumStageComparison] using h)
  have hq : codedQuery i + codedQuery j + 1 / (t : ℚ) <
      codedQuery z := by
    rw [sumStage_rational_add] at hraw
    exact hraw
  have hr : 0 ≤ (1 : ℚ) / (t : ℚ) := by positivity
  exact lt_of_le_of_lt (le_add_of_nonneg_right hr) hq

/-- Una salida positiva de la etapa certifica pertenencia al corte suma. -/
theorem sumCertificateStage_true_correct
    (w : ((Code × Code) × ℕ) × ℕ) (x y : ℝ)
    (hA : DecidesCut w.1.1.1 (lowerCut x))
    (hB : DecidesCut w.1.1.2 (lowerCut y))
    (h : sumCertificateStage w = some true) :
    codedQuery w.1.2 ∈ lowerCut x + lowerCut y := by
  have hi : sumStageInterior w :=
    (sumCertificateStage_true_iff w).mp h
  obtain ⟨ha, hb⟩ :=
    sumStageInterior_correct_inputs w (lowerCut x) (lowerCut y) hA hB hi
  have ha' : (codedQuery (sumStageLeft w.2) : ℝ) < x :=
    (lowerCut_mem_iff _ x).mp ha
  have hb' : (codedQuery (sumStageRight w.2) : ℝ) < y :=
    (lowerCut_mem_iff _ y).mp hb
  have hq : codedQuery w.1.2 <
      codedQuery (sumStageLeft w.2) +
        codedQuery (sumStageRight w.2) :=
    sumStageComparison_true_sound _ _ _ _
      (by simp [sumStageMargin]) hi.2.2
  have hc : (codedQuery w.1.2 : ℝ) <
      (codedQuery (sumStageLeft w.2) : ℝ) +
        (codedQuery (sumStageRight w.2) : ℝ) := by
    exact_mod_cast hq
  rw [lowerCut_add]
  exact (lowerCut_mem_iff _ (x + y)).mpr
    (lt_trans hc (add_lt_add ha' hb'))

/-- Una salida negativa certifica exterioridad estricta; no confunde
frontera con no pertenencia general. -/
theorem sumCertificateStage_false_correct
    (w : ((Code × Code) × ℕ) × ℕ) (x y : ℝ)
    (hA : DecidesCut w.1.1.1 (lowerCut x))
    (hB : DecidesCut w.1.1.2 (lowerCut y))
    (h : sumCertificateStage w = some false) :
    (x + y) < (codedQuery w.1.2 : ℝ) := by
  have he : sumStageExterior w :=
    sumCertificateStage_false_sound w h
  obtain ⟨ha, hb⟩ :=
    sumStageExterior_correct_inputs w (lowerCut x) (lowerCut y) hA hB he
  have ha' : x ≤ (codedQuery (sumStageLeft w.2) : ℝ) := by
    exact le_of_not_gt (fun hh => ha ((lowerCut_mem_iff _ x).mpr hh))
  have hb' : y ≤ (codedQuery (sumStageRight w.2) : ℝ) := by
    exact le_of_not_gt (fun hh => hb ((lowerCut_mem_iff _ y).mpr hh))
  have hq : codedQuery (sumStageLeft w.2) +
      codedQuery (sumStageRight w.2) < codedQuery w.1.2 :=
    sumStageComparison_false_sound _ _ _ _
      (by simp [sumStageMargin]) he.2.2
  have hc :
      (codedQuery (sumStageLeft w.2) : ℝ) +
        (codedQuery (sumStageRight w.2) : ℝ) <
          (codedQuery w.1.2 : ℝ) := by
    exact_mod_cast hq
  exact lt_of_le_of_lt (add_le_add ha' hb') hc

end Continuo.Indices
