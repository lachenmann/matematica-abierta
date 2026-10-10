import MatematicaAbierta.Continuo.IndicesCortes

/-!
# FDC-AUD-023 — O3: semántica del comparador aritmético

El comparador con numeradores naturales con signo separado y denominadores
positivos solo produce certificados verdaderos: `true` demuestra que el
racional está bajo el intervalo y `false`, que está sobre él.
No se afirma aquí la primitividad recursiva de las especializaciones ni la
extracción de códigos de programas.
-/

namespace Continuo.Indices

/-- El certificado positivo implica exactamente la desigualdad inferior. -/
theorem arithmeticStage_true_sound (u v d plus minus s t : ℕ)
    (hd : 0 < d) (hs : 0 < s) (ht : 0 < t)
    (h : arithmeticStage u v d plus minus s t = some true) :
    ((u : ℚ) - (v : ℚ)) / (d : ℚ) <
      ((plus : ℚ) - (minus : ℚ)) / (s : ℚ) - 1 / (t : ℚ) := by
  have hn : u * s * t + minus * d * t + s * d <
      v * s * t + plus * d * t := by
    unfold arithmeticStage at h
    split_ifs at h with hleft hright
    · exact hleft
    · cases h
  have hdq : (d : ℚ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hd)
  have hsq : (s : ℚ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hs)
  have htq : (t : ℚ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt ht)
  have hprod : 0 < (d : ℚ) * (s : ℚ) * (t : ℚ) := by positivity
  have hscaled :
      ((((u : ℚ) - (v : ℚ)) / (d : ℚ)) -
         (((plus : ℚ) - (minus : ℚ)) / (s : ℚ) - 1 / (t : ℚ))) *
        ((d : ℚ) * (s : ℚ) * (t : ℚ)) =
      ((u * s * t + minus * d * t + s * d : ℕ) : ℚ) -
        ((v * s * t + plus * d * t : ℕ) : ℚ) := by
    push_cast
    field_simp [hdq, hsq, htq]
    ring
  have hmul :
      ((((u : ℚ) - (v : ℚ)) / (d : ℚ)) -
         (((plus : ℚ) - (minus : ℚ)) / (s : ℚ) - 1 / (t : ℚ))) *
        ((d : ℚ) * (s : ℚ) * (t : ℚ)) < 0 := by
    rw [hscaled]
    exact sub_neg.mpr (by exact_mod_cast hn)
  have hsub :
      ((((u : ℚ) - (v : ℚ)) / (d : ℚ)) -
         (((plus : ℚ) - (minus : ℚ)) / (s : ℚ) - 1 / (t : ℚ))) < 0 := by
    rw [← mul_lt_mul_iff_of_pos_right hprod]
    simpa using hmul
  exact sub_neg.mp hsub

/-- El certificado negativo implica exactamente la desigualdad superior. -/
theorem arithmeticStage_false_sound (u v d plus minus s t : ℕ)
    (hd : 0 < d) (hs : 0 < s) (ht : 0 < t)
    (h : arithmeticStage u v d plus minus s t = some false) :
    ((plus : ℚ) - (minus : ℚ)) / (s : ℚ) + 1 / (t : ℚ) <
      ((u : ℚ) - (v : ℚ)) / (d : ℚ) := by
  have hn : plus * d * t + v * s * t + s * d <
      u * s * t + minus * d * t := by
    unfold arithmeticStage at h
    split_ifs at h with hleft hright
    · cases h
    · exact hright
  have hdq : (d : ℚ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hd)
  have hsq : (s : ℚ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hs)
  have htq : (t : ℚ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt ht)
  have hprod : 0 < (d : ℚ) * (s : ℚ) * (t : ℚ) := by positivity
  have hscaled :
      ((((plus : ℚ) - (minus : ℚ)) / (s : ℚ) + 1 / (t : ℚ)) -
         (((u : ℚ) - (v : ℚ)) / (d : ℚ))) *
        ((d : ℚ) * (s : ℚ) * (t : ℚ)) =
      ((plus * d * t + v * s * t + s * d : ℕ) : ℚ) -
        ((u * s * t + minus * d * t : ℕ) : ℚ) := by
    push_cast
    field_simp [hdq, hsq, htq]
    ring
  have hmul :
      ((((plus : ℚ) - (minus : ℚ)) / (s : ℚ) + 1 / (t : ℚ)) -
         (((u : ℚ) - (v : ℚ)) / (d : ℚ))) *
        ((d : ℚ) * (s : ℚ) * (t : ℚ)) < 0 := by
    rw [hscaled]
    exact sub_neg.mpr (by exact_mod_cast hn)
  have hsub :
      ((((plus : ℚ) - (minus : ℚ)) / (s : ℚ) + 1 / (t : ℚ)) -
         (((u : ℚ) - (v : ℚ)) / (d : ℚ))) < 0 := by
    rw [← mul_lt_mul_iff_of_pos_right hprod]
    simpa using hmul
  exact sub_neg.mp hsub

end Continuo.Indices
