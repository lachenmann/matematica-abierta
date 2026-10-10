import MatematicaAbierta.Continuo.SemanticaComparadorCortes

/-!
# FDC-AUD-023 — O3: decididores efectivos de cortes

Este módulo cierra formalmente la obligación O3 para la familia de cortes
utilizada en la reducción del continuo.

La construcción establece:

* comparadores aritméticos especializados primitivamente recursivos;
* equivalencia exacta entre las etapas numéricas y las etapas semánticas;
* terminación para toda consulta racional codificada;
* búsqueda no acotada parcial-recursiva y total;
* extracción efectiva de índices `Nat.Partrec.Code`;
* un transformador primitivamente recursivo de índices para la familia
  desplazada;
* un índice fijo para el corte de `-√2`;
* corrección extensional exacta de las respuestas `true` y `false`;
* cobertura de todas las consultas racionales mediante `codedQuery`.

La búsqueda efectiva construida aquí no debe confundirse con el
`partial def buscarSinCota` histórico de `ProgramaTransparente`.
-/
namespace Continuo.Indices

open Denumerable

private theorem queryValue_eq (z : ℕ) :
    ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
        (queryDenominator z : ℚ) =
      codedQuery z := by
  rfl

private theorem intervalRadius_eq_inv_pow (n : ℕ) :
    (1 : ℚ) / ((2 ^ n : ℕ) : ℚ) = intervalRadius n := by
  simp [intervalRadius, Nat.cast_pow]

private theorem shiftedPair_value (c : Code) (n : ℕ) :
    (((shiftedPair c n).1 : ℚ) - (0 : ℚ)) /
        ((shiftedPair c n).2 : ℚ) =
      shiftedName c n := by
  simpa [pairValue] using shiftedPair_correct c n

private theorem shiftedPair_den_pos (c : Code) (n : ℕ) :
    0 < (shiftedPair c n).2 := by
  unfold shiftedPair addPair
  exact Nat.mul_pos
    (Nat.pos_of_ne_zero (sqrtTwoPair_den_ne_zero n))
    (Nat.pos_of_ne_zero (rationalPair_den_ne_zero c (n + 2)))

private theorem negativePair_value (n : ℕ) :
    ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
        ((sqrtTwoPair n).2 : ℚ) =
      negSqrtTwoName n := by
  have h :
      ((sqrtTwoPair n).1 : ℚ) /
          ((sqrtTwoPair n).2 : ℚ) =
        sqrtTwoName n := by
    simpa [pairValue] using sqrtTwoPair_correct n
  calc
    ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
        ((sqrtTwoPair n).2 : ℚ)
        =
        -(((sqrtTwoPair n).1 : ℚ) /
          ((sqrtTwoPair n).2 : ℚ)) := by ring
    _ = -sqrtTwoName n := by rw [h]
    _ = negSqrtTwoName n := by rfl

private theorem arithmeticStage_true_complete
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

private theorem arithmeticStage_false_complete
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

-- B2.1
example (c : Code) (z n : ℕ)
    (h :
      codedQuery z <
        shiftedName c n - intervalRadius n) :
    shiftedNumericStage ((c, z), n) = some true := by

  change
    arithmeticStage
      (queryPositive z)
      (queryNegative z)
      (queryDenominator z)
      (shiftedPair c n).1
      0
      (shiftedPair c n).2
      (2 ^ n) = some true

  have hraw :
      ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ) <
        (((shiftedPair c n).1 : ℚ) - (0 : ℚ)) /
            ((shiftedPair c n).2 : ℚ) -
          1 / ((2 ^ n : ℕ) : ℚ) := by
    calc
      ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ)
          = codedQuery z := queryValue_eq z
      _ < shiftedName c n - intervalRadius n := h
      _ =
          (((shiftedPair c n).1 : ℚ) - (0 : ℚ)) /
              ((shiftedPair c n).2 : ℚ) -
            1 / ((2 ^ n : ℕ) : ℚ) := by
          rw [shiftedPair_value c n,
              intervalRadius_eq_inv_pow n]

  exact arithmeticStage_true_complete
    _ _ _ _ _ _ _
    (queryDenominator_pos z)
    (shiftedPair_den_pos c n)
    (by positivity)
    hraw

-- B2.2
example (c : Code) (z n : ℕ)
    (h :
      shiftedName c n + intervalRadius n <
        codedQuery z) :
    shiftedNumericStage ((c, z), n) = some false := by

  change
    arithmeticStage
      (queryPositive z)
      (queryNegative z)
      (queryDenominator z)
      (shiftedPair c n).1
      0
      (shiftedPair c n).2
      (2 ^ n) = some false

  have hraw :
      (((shiftedPair c n).1 : ℚ) - (0 : ℚ)) /
          ((shiftedPair c n).2 : ℚ) +
        1 / ((2 ^ n : ℕ) : ℚ) <
      ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ) := by
    calc
      (((shiftedPair c n).1 : ℚ) - (0 : ℚ)) /
          ((shiftedPair c n).2 : ℚ) +
        1 / ((2 ^ n : ℕ) : ℚ)
          =
        shiftedName c n + intervalRadius n := by
          rw [shiftedPair_value c n,
              intervalRadius_eq_inv_pow n]
      _ < codedQuery z := h
      _ =
        ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ) := by
            symm
            exact queryValue_eq z

  exact arithmeticStage_false_complete
    _ _ _ _ _ _ _
    (queryDenominator_pos z)
    (shiftedPair_den_pos c n)
    (by positivity)
    hraw

-- B2.3
example (z n : ℕ)
    (h :
      codedQuery z <
        negSqrtTwoName n - intervalRadius (n + 2)) :
    negativeNumericStage (z, n) = some true := by

  change
    arithmeticStage
      (queryPositive z)
      (queryNegative z)
      (queryDenominator z)
      0
      (sqrtTwoPair n).1
      (sqrtTwoPair n).2
      (2 ^ (n + 2)) = some true

  have hraw :
      ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ) <
        ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
            ((sqrtTwoPair n).2 : ℚ) -
          1 / ((2 ^ (n + 2) : ℕ) : ℚ) := by
    calc
      ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ)
          = codedQuery z := queryValue_eq z
      _ < negSqrtTwoName n - intervalRadius (n + 2) := h
      _ =
        ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
            ((sqrtTwoPair n).2 : ℚ) -
          1 / ((2 ^ (n + 2) : ℕ) : ℚ) := by
            rw [negativePair_value n,
                intervalRadius_eq_inv_pow (n + 2)]

  exact arithmeticStage_true_complete
    _ _ _ _ _ _ _
    (queryDenominator_pos z)
    (Nat.pos_of_ne_zero (sqrtTwoPair_den_ne_zero n))
    (by positivity)
    hraw

-- B2.4
example (z n : ℕ)
    (h :
      negSqrtTwoName n + intervalRadius (n + 2) <
        codedQuery z) :
    negativeNumericStage (z, n) = some false := by

  change
    arithmeticStage
      (queryPositive z)
      (queryNegative z)
      (queryDenominator z)
      0
      (sqrtTwoPair n).1
      (sqrtTwoPair n).2
      (2 ^ (n + 2)) = some false

  have hraw :
      ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
          ((sqrtTwoPair n).2 : ℚ) +
        1 / ((2 ^ (n + 2) : ℕ) : ℚ) <
      ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ) := by
    calc
      ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
          ((sqrtTwoPair n).2 : ℚ) +
        1 / ((2 ^ (n + 2) : ℕ) : ℚ)
          =
        negSqrtTwoName n + intervalRadius (n + 2) := by
          rw [negativePair_value n,
              intervalRadius_eq_inv_pow (n + 2)]
      _ < codedQuery z := h
      _ =
        ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
          (queryDenominator z : ℚ) := by
            symm
            exact queryValue_eq z

  exact arithmeticStage_false_complete
    _ _ _ _ _ _ _
    (queryDenominator_pos z)
    (Nat.pos_of_ne_zero (sqrtTwoPair_den_ne_zero n))
    (by positivity)
    hraw


-- B3.1: la etapa numérica desplazada coincide exactamente
-- con la etapa semántica por intervalos sobre la consulta codificada.
private theorem shiftedNumericStage_eq_shiftedCutStage (c : Code) (z n : ℕ) :
    shiftedNumericStage ((c, z), n) =
      shiftedCutStage c (codedQuery z) n := by

  unfold shiftedCutStage intervalStage

  by_cases htrue :
      codedQuery z < shiftedName c n - intervalRadius n

  · rw [ite_eq_left htrue]
    unfold shiftedNumericStage

    have hraw :
        ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
            (queryDenominator z : ℚ) <
          (((shiftedPair c n).1 : ℚ) - (0 : ℚ)) /
              ((shiftedPair c n).2 : ℚ) -
            1 / ((2 ^ n : ℕ) : ℚ) := by
      calc
        ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
            (queryDenominator z : ℚ)
            = codedQuery z := queryValue_eq z
        _ < shiftedName c n - intervalRadius n := htrue
        _ =
            (((shiftedPair c n).1 : ℚ) - (0 : ℚ)) /
                ((shiftedPair c n).2 : ℚ) -
              1 / ((2 ^ n : ℕ) : ℚ) := by
            rw [shiftedPair_value c n,
                intervalRadius_eq_inv_pow n]

    exact arithmeticStage_true_complete
      _ _ _ _ _ _ _
      (queryDenominator_pos z)
      (shiftedPair_den_pos c n)
      (by positivity)
      hraw

  · rw [ite_eq_right htrue]

    by_cases hfalse :
        shiftedName c n + intervalRadius n < codedQuery z

    · rw [ite_eq_left hfalse]
      unfold shiftedNumericStage

      have hraw :
          (((shiftedPair c n).1 : ℚ) - (0 : ℚ)) /
              ((shiftedPair c n).2 : ℚ) +
            1 / ((2 ^ n : ℕ) : ℚ) <
          ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
              (queryDenominator z : ℚ) := by
        calc
          (((shiftedPair c n).1 : ℚ) - (0 : ℚ)) /
              ((shiftedPair c n).2 : ℚ) +
            1 / ((2 ^ n : ℕ) : ℚ)
              =
            shiftedName c n + intervalRadius n := by
              rw [shiftedPair_value c n,
                  intervalRadius_eq_inv_pow n]
          _ < codedQuery z := hfalse
          _ =
            ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
              (queryDenominator z : ℚ) := by
                symm
                exact queryValue_eq z

      exact arithmeticStage_false_complete
        _ _ _ _ _ _ _
        (queryDenominator_pos z)
        (shiftedPair_den_pos c n)
        (by positivity)
        hraw

    · rw [ite_eq_right hfalse]

      cases hnum :
          shiftedNumericStage ((c, z), n) with

      | none =>
          rfl

      | some b =>
          cases b with

          | false =>
              have hraw :=
                arithmeticStage_false_sound
                  (queryPositive z)
                  (queryNegative z)
                  (queryDenominator z)
                  (shiftedPair c n).1
                  0
                  (shiftedPair c n).2
                  (2 ^ n)
                  (queryDenominator_pos z)
                  (shiftedPair_den_pos c n)
                  (by positivity)
                  (by
                    simpa [shiftedNumericStage] using hnum)

              simp only [Nat.cast_zero] at hraw
              rw [queryValue_eq z,
                  shiftedPair_value c n,
                  intervalRadius_eq_inv_pow n] at hraw

              exact False.elim (hfalse hraw)

          | true =>
              have hraw :=
                arithmeticStage_true_sound
                  (queryPositive z)
                  (queryNegative z)
                  (queryDenominator z)
                  (shiftedPair c n).1
                  0
                  (shiftedPair c n).2
                  (2 ^ n)
                  (queryDenominator_pos z)
                  (shiftedPair_den_pos c n)
                  (by positivity)
                  (by
                    simpa [shiftedNumericStage] using hnum)

              simp only [Nat.cast_zero] at hraw
              rw [queryValue_eq z,
                  shiftedPair_value c n,
                  intervalRadius_eq_inv_pow n] at hraw

              exact False.elim (htrue hraw)


-- B3.2: la etapa numérica del corte fijo negativo coincide
-- exactamente con la etapa semántica correspondiente.
private theorem negativeNumericStage_eq_negativeCutStage (z n : ℕ) :
    negativeNumericStage (z, n) =
      negativeCutStage (codedQuery z) n := by

  unfold negativeCutStage intervalStage

  by_cases htrue :
      codedQuery z <
        negSqrtTwoName n - intervalRadius (n + 2)

  · rw [ite_eq_left htrue]
    unfold negativeNumericStage

    have hraw :
        ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
            (queryDenominator z : ℚ) <
          ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
              ((sqrtTwoPair n).2 : ℚ) -
            1 / ((2 ^ (n + 2) : ℕ) : ℚ) := by
      calc
        ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
            (queryDenominator z : ℚ)
            = codedQuery z := queryValue_eq z
        _ <
            negSqrtTwoName n -
              intervalRadius (n + 2) := htrue
        _ =
            ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
                ((sqrtTwoPair n).2 : ℚ) -
              1 / ((2 ^ (n + 2) : ℕ) : ℚ) := by
            rw [negativePair_value n,
                intervalRadius_eq_inv_pow (n + 2)]

    exact arithmeticStage_true_complete
      _ _ _ _ _ _ _
      (queryDenominator_pos z)
      (Nat.pos_of_ne_zero (sqrtTwoPair_den_ne_zero n))
      (by positivity)
      hraw

  · rw [ite_eq_right htrue]

    by_cases hfalse :
        negSqrtTwoName n + intervalRadius (n + 2) <
          codedQuery z

    · rw [ite_eq_left hfalse]
      unfold negativeNumericStage

      have hraw :
          ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
              ((sqrtTwoPair n).2 : ℚ) +
            1 / ((2 ^ (n + 2) : ℕ) : ℚ) <
          ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
              (queryDenominator z : ℚ) := by
        calc
          ((0 : ℚ) - ((sqrtTwoPair n).1 : ℚ)) /
              ((sqrtTwoPair n).2 : ℚ) +
            1 / ((2 ^ (n + 2) : ℕ) : ℚ)
              =
            negSqrtTwoName n +
              intervalRadius (n + 2) := by
              rw [negativePair_value n,
                  intervalRadius_eq_inv_pow (n + 2)]
          _ < codedQuery z := hfalse
          _ =
            ((queryPositive z : ℚ) - (queryNegative z : ℚ)) /
              (queryDenominator z : ℚ) := by
                symm
                exact queryValue_eq z

      exact arithmeticStage_false_complete
        _ _ _ _ _ _ _
        (queryDenominator_pos z)
        (Nat.pos_of_ne_zero (sqrtTwoPair_den_ne_zero n))
        (by positivity)
        hraw

    · rw [ite_eq_right hfalse]

      cases hnum :
          negativeNumericStage (z, n) with

      | none =>
          rfl

      | some b =>
          cases b with

          | false =>
              have hraw :=
                arithmeticStage_false_sound
                  (queryPositive z)
                  (queryNegative z)
                  (queryDenominator z)
                  0
                  (sqrtTwoPair n).1
                  (sqrtTwoPair n).2
                  (2 ^ (n + 2))
                  (queryDenominator_pos z)
                  (Nat.pos_of_ne_zero
                    (sqrtTwoPair_den_ne_zero n))
                  (by positivity)
                  (by
                    simpa [negativeNumericStage] using hnum)

              simp only [Nat.cast_zero] at hraw
              rw [queryValue_eq z,
                  negativePair_value n,
                  intervalRadius_eq_inv_pow (n + 2)] at hraw

              exact False.elim (hfalse hraw)

          | true =>
              have hraw :=
                arithmeticStage_true_sound
                  (queryPositive z)
                  (queryNegative z)
                  (queryDenominator z)
                  0
                  (sqrtTwoPair n).1
                  (sqrtTwoPair n).2
                  (2 ^ (n + 2))
                  (queryDenominator_pos z)
                  (Nat.pos_of_ne_zero
                    (sqrtTwoPair_den_ne_zero n))
                  (by positivity)
                  (by
                    simpa [negativeNumericStage] using hnum)

              simp only [Nat.cast_zero] at hraw
              rw [queryValue_eq z,
                  negativePair_value n,
                  intervalRadius_eq_inv_pow (n + 2)] at hraw

              exact False.elim (htrue hraw)


-- O3-C1.1: toda consulta codificada al corte desplazado
-- obtiene una respuesta numérica en alguna etapa finita.
private theorem shiftedNumericStage_exists_encoded (c : Code) (z : ℕ) :
    ∃ n : ℕ, ∃ b : Bool,
      shiftedNumericStage ((c, z), n) = some b := by

  obtain ⟨n, b, h⟩ :=
    shiftedCutStage_exists c (codedQuery z)

  refine ⟨n, b, ?_⟩

  rw [shiftedNumericStage_eq_shiftedCutStage]
  exact h


-- O3-C1.2: toda consulta codificada al corte fijo negativo
-- obtiene una respuesta numérica en alguna etapa finita.
private theorem negativeNumericStage_exists_encoded (z : ℕ) :
    ∃ n : ℕ, ∃ b : Bool,
      negativeNumericStage (z, n) = some b := by

  obtain ⟨n, b, h⟩ :=
    negativeCutStage_exists (codedQuery z)

  refine ⟨n, b, ?_⟩

  rw [negativeNumericStage_eq_negativeCutStage]
  exact h


-- O3-C2.A: primitividad recursiva de las dos etapas especializadas.
-- Se repiten aquí como lemas locales porque los ensayos anteriores
-- permanecen deliberadamente fuera de la biblioteca publicada.

theorem primrec_shiftedNumericStage :
    Primrec shiftedNumericStage := by
  change Primrec (fun w : (Code × ℕ) × ℕ =>
    arithmeticStage
      (queryPositive w.1.2)
      (queryNegative w.1.2)
      (queryDenominator w.1.2)
      (shiftedPair w.1.1 w.2).1
      0
      (shiftedPair w.1.1 w.2).2
      (2 ^ w.2))

  have hquery :
      Primrec (fun w : (Code × ℕ) × ℕ => w.1.2) :=
    Primrec.snd.comp Primrec.fst

  have hpair :
      Primrec (fun w : (Code × ℕ) × ℕ =>
        shiftedPair w.1.1 w.2) :=
    primrec_shiftedPair.comp
      (Primrec.fst.comp Primrec.fst) Primrec.snd

  exact primrec_arithmeticStage
    (u := fun w : (Code × ℕ) × ℕ =>
      queryPositive w.1.2)
    (v := fun w : (Code × ℕ) × ℕ =>
      queryNegative w.1.2)
    (d := fun w : (Code × ℕ) × ℕ =>
      queryDenominator w.1.2)
    (plus := fun w : (Code × ℕ) × ℕ =>
      (shiftedPair w.1.1 w.2).1)
    (minus := fun _ : (Code × ℕ) × ℕ => (0 : ℕ))
    (s := fun w : (Code × ℕ) × ℕ =>
      (shiftedPair w.1.1 w.2).2)
    (t := fun w : (Code × ℕ) × ℕ =>
      2 ^ w.2)
    (primrec_queryPositive.comp hquery)
    (primrec_queryNegative.comp hquery)
    (primrec_queryDenominator.comp hquery)
    (Primrec.fst.comp hpair)
    (Primrec.const 0)
    (Primrec.snd.comp hpair)
    ((Primrec₂.unpaired'.1 Nat.Primrec.pow).comp
      (Primrec.const 2) Primrec.snd)


theorem primrec_negativeNumericStage :
    Primrec negativeNumericStage := by
  change Primrec (fun w : ℕ × ℕ =>
    arithmeticStage
      (queryPositive w.1)
      (queryNegative w.1)
      (queryDenominator w.1)
      0
      (sqrtTwoPair w.2).1
      (sqrtTwoPair w.2).2
      (2 ^ (w.2 + 2)))

  have hpair :
      Primrec (fun w : ℕ × ℕ =>
        sqrtTwoPair w.2) :=
    primrec_sqrtTwoPair.comp Primrec.snd

  exact primrec_arithmeticStage
    (u := fun w : ℕ × ℕ =>
      queryPositive w.1)
    (v := fun w : ℕ × ℕ =>
      queryNegative w.1)
    (d := fun w : ℕ × ℕ =>
      queryDenominator w.1)
    (plus := fun _ : ℕ × ℕ => (0 : ℕ))
    (minus := fun w : ℕ × ℕ =>
      (sqrtTwoPair w.2).1)
    (s := fun w : ℕ × ℕ =>
      (sqrtTwoPair w.2).2)
    (t := fun w : ℕ × ℕ =>
      2 ^ (w.2 + 2))
    (primrec_queryPositive.comp Primrec.fst)
    (primrec_queryNegative.comp Primrec.fst)
    (primrec_queryDenominator.comp Primrec.fst)
    (Primrec.const 0)
    (Primrec.fst.comp hpair)
    (Primrec.snd.comp hpair)
    ((Primrec₂.unpaired'.1 Nat.Primrec.pow).comp
      (Primrec.const 2)
      (Primrec.nat_add.comp Primrec.snd
        (Primrec.const 2)))


-- O3-C2.B: búsquedas no acotadas efectivas.
-- Nat.rfindOpt devuelve la respuesta de la primera etapa que produce some b.

def shiftedNumericSearch (p : Code × ℕ) : Part Bool :=
  Nat.rfindOpt (fun n =>
    shiftedNumericStage (p, n))

def negativeNumericSearch (z : ℕ) : Part Bool :=
  Nat.rfindOpt (fun n =>
    negativeNumericStage (z, n))


-- O3-C2.1: la búsqueda desplazada es parcial-recursiva.
example : Partrec shiftedNumericSearch := by
  unfold shiftedNumericSearch
  exact Partrec.rfindOpt
    (primrec_shiftedNumericStage.to_comp.to₂)


-- O3-C2.2: la búsqueda negativa es parcial-recursiva.
example : Partrec negativeNumericSearch := by
  unfold negativeNumericSearch
  exact Partrec.rfindOpt
    (primrec_negativeNumericStage.to_comp.to₂)


-- O3-C2.3: la búsqueda desplazada está definida para toda entrada.
example (c : Code) (z : ℕ) :
    (shiftedNumericSearch (c, z)).Dom := by
  unfold shiftedNumericSearch
  apply Nat.rfindOpt_dom.mpr

  obtain ⟨n, b, h⟩ :=
    shiftedNumericStage_exists_encoded c z

  refine ⟨n, b, ?_⟩
  simpa only [Option.mem_def] using h


-- O3-C2.4: la búsqueda negativa está definida para toda entrada.
example (z : ℕ) :
    (negativeNumericSearch z).Dom := by
  unfold negativeNumericSearch
  apply Nat.rfindOpt_dom.mpr

  obtain ⟨n, b, h⟩ :=
    negativeNumericStage_exists_encoded z

  refine ⟨n, b, ?_⟩
  simpa only [Option.mem_def] using h


-- O3-C3.A: versiones reutilizables de las pruebas de parcial-recursividad.

theorem partrec_shiftedNumericSearch :
    Partrec shiftedNumericSearch := by
  unfold shiftedNumericSearch
  exact Partrec.rfindOpt
    (primrec_shiftedNumericStage.to_comp.to₂)

theorem partrec_negativeNumericSearch :
    Partrec negativeNumericSearch := by
  unfold negativeNumericSearch
  exact Partrec.rfindOpt
    (primrec_negativeNumericStage.to_comp.to₂)


-- O3-C3.B: empaquetado natural de las búsquedas.
-- La salida Bool se codifica con Encodable.encode para poder utilizar
-- directamente Nat.Partrec.Code.exists_code.

private def shiftedSearchNatural (w : ℕ) : Part ℕ :=
  (shiftedNumericSearch
    (ofNat Code w.unpair.1, w.unpair.2)).map Encodable.encode

private def negativeSearchNatural (z : ℕ) : Part ℕ :=
  (negativeNumericSearch z).map Encodable.encode


private theorem partrec_shiftedSearchNatural :
    Partrec shiftedSearchNatural := by

  change Partrec (fun w : ℕ =>
    (shiftedNumericSearch
      (ofNat Code w.unpair.1, w.unpair.2)).map Encodable.encode)

  have hin :
      Computable (fun w : ℕ =>
        (ofNat Code w.unpair.1, w.unpair.2)) :=
    ((Computable.ofNat Code).comp
        (Computable.fst.comp Computable.unpair)).pair
      (Computable.snd.comp Computable.unpair)

  have hs :
      Partrec (fun w : ℕ =>
        shiftedNumericSearch
          (ofNat Code w.unpair.1, w.unpair.2)) :=
    partrec_shiftedNumericSearch.comp hin

  have henc :
      Computable₂
        (fun (_ : ℕ) (b : Bool) =>
          Encodable.encode b) := by
    exact (Computable.encode.comp Computable.snd).to₂

  exact hs.map henc

private theorem partrec_negativeSearchNatural :
    Partrec negativeSearchNatural := by

  change Partrec (fun z : ℕ =>
    (negativeNumericSearch z).map Encodable.encode)

  have henc :
      Computable₂
        (fun (_ : ℕ) (b : Bool) =>
          Encodable.encode b) := by
    exact (Computable.encode.comp Computable.snd).to₂

  exact partrec_negativeNumericSearch.map henc

-- O3-C3.C: extracción de códigos universales.

private theorem exists_shiftedSearchNatural_code :
    ∃ u : Code, ∀ w : ℕ,
      Nat.Partrec.Code.eval u w =
        shiftedSearchNatural w := by

  have hn :
      Nat.Partrec shiftedSearchNatural :=
    Partrec.nat_iff.mp partrec_shiftedSearchNatural

  obtain ⟨u, hu⟩ :=
    (Nat.Partrec.Code.exists_code).mp hn

  refine ⟨u, ?_⟩
  intro w
  exact congrFun hu w


private theorem exists_negativeSearchNatural_code :
    ∃ v : Code, ∀ z : ℕ,
      Nat.Partrec.Code.eval v z =
        negativeSearchNatural z := by

  have hn :
      Nat.Partrec negativeSearchNatural :=
    Partrec.nat_iff.mp partrec_negativeSearchNatural

  obtain ⟨v, hv⟩ :=
    (Nat.Partrec.Code.exists_code).mp hn

  refine ⟨v, ?_⟩
  intro z
  exact congrFun hv z


-- O3-C3.1:
-- existe un transformador PR que, dado c, produce el código
-- de la búsqueda efectiva del corte desplazado.

example :
    ∃ index : Code → Code,
      Primrec index ∧
      ∀ c z,
        Nat.Partrec.Code.eval (index c) z =
          (shiftedNumericSearch (c, z)).map Encodable.encode := by

  obtain ⟨u, hu⟩ :=
    exists_shiftedSearchNatural_code

  refine
    ⟨fun c =>
        Nat.Partrec.Code.curry u (Encodable.encode c),
      ?_, ?_⟩

  · exact Nat.Partrec.Code.primrec₂_curry.comp
      (Primrec.const u) Primrec.encode

  · intro c z
    rw [Nat.Partrec.Code.eval_curry]
    rw [hu]

    simp [shiftedSearchNatural]


-- O3-C3.2:
-- existe un código fijo para la búsqueda efectiva del corte -√2.

example :
    ∃ negativeIndex : Code,
      ∀ z,
        Nat.Partrec.Code.eval negativeIndex z =
          (negativeNumericSearch z).map Encodable.encode := by

  obtain ⟨v, hv⟩ :=
    exists_negativeSearchNatural_code

  refine ⟨v, ?_⟩
  intro z

  simpa [negativeSearchNatural] using hv z


-- O3-D1.A: totalidad reutilizable de las búsquedas.

theorem shiftedNumericSearch_dom
    (c : Code) (z : ℕ) :
    (shiftedNumericSearch (c, z)).Dom := by
  unfold shiftedNumericSearch
  apply Nat.rfindOpt_dom.mpr

  obtain ⟨n, b, h⟩ :=
    shiftedNumericStage_exists_encoded c z

  refine ⟨n, b, ?_⟩
  simpa only [Option.mem_def] using h


theorem negativeNumericSearch_dom
    (z : ℕ) :
    (negativeNumericSearch z).Dom := by
  unfold negativeNumericSearch
  apply Nat.rfindOpt_dom.mpr

  obtain ⟨n, b, h⟩ :=
    negativeNumericStage_exists_encoded z

  refine ⟨n, b, ?_⟩
  simpa only [Option.mem_def] using h


-- O3-D1.B: soundness de la búsqueda completa.

private theorem shiftedNumericSearch_true_sound
    (c : Code) (z : ℕ)
    (h : true ∈ shiftedNumericSearch (c, z)) :
    (codedQuery z : ℝ) < shiftedReal c := by

  unfold shiftedNumericSearch at h

  obtain ⟨n, hn⟩ :=
    Nat.rfindOpt_spec h

  have hs :
      shiftedNumericStage ((c, z), n) = some true := by
    simpa only [Option.mem_def] using hn

  rw [shiftedNumericStage_eq_shiftedCutStage] at hs

  exact shiftedCutStage_true c (codedQuery z) n hs


private theorem shiftedNumericSearch_false_sound
    (c : Code) (z : ℕ)
    (h : false ∈ shiftedNumericSearch (c, z)) :
    shiftedReal c < (codedQuery z : ℝ) := by

  unfold shiftedNumericSearch at h

  obtain ⟨n, hn⟩ :=
    Nat.rfindOpt_spec h

  have hs :
      shiftedNumericStage ((c, z), n) = some false := by
    simpa only [Option.mem_def] using hn

  rw [shiftedNumericStage_eq_shiftedCutStage] at hs

  exact shiftedCutStage_false c (codedQuery z) n hs


private theorem negativeNumericSearch_true_sound
    (z : ℕ)
    (h : true ∈ negativeNumericSearch z) :
    (codedQuery z : ℝ) < -Real.sqrt 2 := by

  unfold negativeNumericSearch at h

  obtain ⟨n, hn⟩ :=
    Nat.rfindOpt_spec h

  have hs :
      negativeNumericStage (z, n) = some true := by
    simpa only [Option.mem_def] using hn

  rw [negativeNumericStage_eq_negativeCutStage] at hs

  exact negativeCutStage_true (codedQuery z) n hs


private theorem negativeNumericSearch_false_sound
    (z : ℕ)
    (h : false ∈ negativeNumericSearch z) :
    -Real.sqrt 2 < (codedQuery z : ℝ) := by

  unfold negativeNumericSearch at h

  obtain ⟨n, hn⟩ :=
    Nat.rfindOpt_spec h

  have hs :
      negativeNumericStage (z, n) = some false := by
    simpa only [Option.mem_def] using hn

  rw [negativeNumericStage_eq_negativeCutStage] at hs

  exact negativeCutStage_false (codedQuery z) n hs


-- O3-D1.1: caracterización exacta de la respuesta true desplazada.

theorem shiftedNumericSearch_true_iff
    (c : Code) (z : ℕ) :
    true ∈ shiftedNumericSearch (c, z) ↔
      (codedQuery z : ℝ) < shiftedReal c := by
  constructor

  · exact shiftedNumericSearch_true_sound c z

  · intro hq

    obtain ⟨b, hb⟩ :=
      Part.dom_iff_mem.mp
        (shiftedNumericSearch_dom c z)

    cases b with
    | false =>
        have hbad :=
          shiftedNumericSearch_false_sound c z hb
        exfalso
        exact lt_asymm hq hbad
    | true =>
        exact hb


-- O3-D1.2: caracterización exacta de la respuesta false desplazada.

theorem shiftedNumericSearch_false_iff
    (c : Code) (z : ℕ) :
    false ∈ shiftedNumericSearch (c, z) ↔
      shiftedReal c < (codedQuery z : ℝ) := by
  constructor

  · exact shiftedNumericSearch_false_sound c z

  · intro hq

    obtain ⟨b, hb⟩ :=
      Part.dom_iff_mem.mp
        (shiftedNumericSearch_dom c z)

    cases b with
    | false =>
        exact hb
    | true =>
        have hbad :=
          shiftedNumericSearch_true_sound c z hb
        exfalso
        exact lt_asymm hbad hq


-- O3-D1.3: caracterización exacta de la respuesta true fija.

theorem negativeNumericSearch_true_iff
    (z : ℕ) :
    true ∈ negativeNumericSearch z ↔
      (codedQuery z : ℝ) < -Real.sqrt 2 := by
  constructor

  · exact negativeNumericSearch_true_sound z

  · intro hq

    obtain ⟨b, hb⟩ :=
      Part.dom_iff_mem.mp
        (negativeNumericSearch_dom z)

    cases b with
    | false =>
        have hbad :=
          negativeNumericSearch_false_sound z hb
        exfalso
        exact lt_asymm hq hbad
    | true =>
        exact hb


-- O3-D1.4: caracterización exacta de la respuesta false fija.

theorem negativeNumericSearch_false_iff
    (z : ℕ) :
    false ∈ negativeNumericSearch z ↔
      -Real.sqrt 2 < (codedQuery z : ℝ) := by
  constructor

  · exact negativeNumericSearch_false_sound z

  · intro hq

    obtain ⟨b, hb⟩ :=
      Part.dom_iff_mem.mp
        (negativeNumericSearch_dom z)

    cases b with
    | false =>
        exact hb
    | true =>
        have hbad :=
          negativeNumericSearch_true_sound z hb
        exfalso
        exact lt_asymm hbad hq


-- O3-D2.A: pertenencia de los booleanos codificados a un Part.map.

private theorem encode_true_mem_map_iff (o : Part Bool) :
    Encodable.encode true ∈ o.map Encodable.encode ↔
      true ∈ o := by
  constructor
  · intro h
    obtain ⟨b, hb, he⟩ :=
      (Part.mem_map_iff Encodable.encode).mp h
    have hbt : b = true :=
      Encodable.encode_injective he
    simpa [hbt] using hb
  · intro h
    exact
      (Part.mem_map_iff Encodable.encode).mpr
        ⟨true, h, rfl⟩


private theorem encode_false_mem_map_iff (o : Part Bool) :
    Encodable.encode false ∈ o.map Encodable.encode ↔
      false ∈ o := by
  constructor
  · intro h
    obtain ⟨b, hb, he⟩ :=
      (Part.mem_map_iff Encodable.encode).mp h
    have hbf : b = false :=
      Encodable.encode_injective he
    simpa [hbf] using hb
  · intro h
    exact
      (Part.mem_map_iff Encodable.encode).mpr
        ⟨false, h, rfl⟩


-- O3-D2.1
-- El transformador PR de índices produce programas cuya salida codificada
-- decide exactamente el corte desplazado sobre cada consulta natural.

theorem exists_uniform_shifted_cut_decider_codes :
    ∃ index : Code → Code,
      Primrec index ∧
      ∀ c z,
        (Encodable.encode true ∈
            Nat.Partrec.Code.eval (index c) z ↔
          (codedQuery z : ℝ) < shiftedReal c) ∧
        (Encodable.encode false ∈
            Nat.Partrec.Code.eval (index c) z ↔
          shiftedReal c < (codedQuery z : ℝ)) := by

  obtain ⟨u, hu⟩ :=
    exists_shiftedSearchNatural_code

  refine
    ⟨fun c =>
        Nat.Partrec.Code.curry u (Encodable.encode c),
      ?_, ?_⟩

  · exact Nat.Partrec.Code.primrec₂_curry.comp
      (Primrec.const u) Primrec.encode

  · intro c z

    have heval :
        Nat.Partrec.Code.eval
            (Nat.Partrec.Code.curry u (Encodable.encode c)) z =
          (shiftedNumericSearch (c, z)).map
            Encodable.encode := by
      rw [Nat.Partrec.Code.eval_curry]
      rw [hu]
      simp [shiftedSearchNatural]

    constructor

    · calc
        Encodable.encode true ∈
            Nat.Partrec.Code.eval
              (Nat.Partrec.Code.curry u (Encodable.encode c)) z
            ↔
          Encodable.encode true ∈
            (shiftedNumericSearch (c, z)).map
              Encodable.encode := by rw [heval]
        _ ↔ true ∈ shiftedNumericSearch (c, z) :=
          encode_true_mem_map_iff _
        _ ↔
          (codedQuery z : ℝ) < shiftedReal c :=
          shiftedNumericSearch_true_iff c z

    · calc
        Encodable.encode false ∈
            Nat.Partrec.Code.eval
              (Nat.Partrec.Code.curry u (Encodable.encode c)) z
            ↔
          Encodable.encode false ∈
            (shiftedNumericSearch (c, z)).map
              Encodable.encode := by rw [heval]
        _ ↔ false ∈ shiftedNumericSearch (c, z) :=
          encode_false_mem_map_iff _
        _ ↔
          shiftedReal c < (codedQuery z : ℝ) :=
          shiftedNumericSearch_false_iff c z


-- O3-D2.2
-- El índice fijo produce un programa cuya salida codificada
-- decide exactamente el corte de -√2.

theorem exists_negative_cut_decider_code :
    ∃ negativeIndex : Code,
      ∀ z,
        (Encodable.encode true ∈
            Nat.Partrec.Code.eval negativeIndex z ↔
          (codedQuery z : ℝ) < -Real.sqrt 2) ∧
        (Encodable.encode false ∈
            Nat.Partrec.Code.eval negativeIndex z ↔
          -Real.sqrt 2 < (codedQuery z : ℝ)) := by

  obtain ⟨v, hv⟩ :=
    exists_negativeSearchNatural_code

  refine ⟨v, ?_⟩
  intro z

  have heval :
      Nat.Partrec.Code.eval v z =
        (negativeNumericSearch z).map
          Encodable.encode := by
    simpa [negativeSearchNatural] using hv z

  constructor

  · calc
      Encodable.encode true ∈
          Nat.Partrec.Code.eval v z
          ↔
        Encodable.encode true ∈
          (negativeNumericSearch z).map
            Encodable.encode := by rw [heval]
      _ ↔ true ∈ negativeNumericSearch z :=
        encode_true_mem_map_iff _
      _ ↔
        (codedQuery z : ℝ) < -Real.sqrt 2 :=
        negativeNumericSearch_true_iff z

  · calc
      Encodable.encode false ∈
          Nat.Partrec.Code.eval v z
          ↔
        Encodable.encode false ∈
          (negativeNumericSearch z).map
            Encodable.encode := by rw [heval]
      _ ↔ false ∈ negativeNumericSearch z :=
        encode_false_mem_map_iff _
      _ ↔
        -Real.sqrt 2 < (codedQuery z : ℝ) :=
        negativeNumericSearch_false_iff z


-- O3-E.A
-- Empaquetado efectivo de una consulta racional.
-- El triple (u,v,d) representa (u-v)/(d+1).

def queryCode (p : (ℕ × ℕ) × ℕ) : ℕ :=
  Nat.pair (Nat.pair p.1.1 p.1.2) p.2


theorem primrec_queryCode :
    Primrec queryCode := by
  exact
    (Primrec₂.natPair.comp
      (Primrec₂.natPair.comp
        (Primrec.fst.comp Primrec.fst)
        (Primrec.snd.comp Primrec.fst))
      Primrec.snd).of_eq
        (fun p => rfl)


-- O3-E.B
-- Recuperación exacta de las tres componentes.

theorem queryPositive_queryCode (u v d : ℕ) :
    queryPositive (queryCode ((u, v), d)) = u := by
  simp [queryPositive, queryCode]


theorem queryNegative_queryCode (u v d : ℕ) :
    queryNegative (queryCode ((u, v), d)) = v := by
  simp [queryNegative, queryCode]


theorem queryDenominator_queryCode (u v d : ℕ) :
    queryDenominator (queryCode ((u, v), d)) = d + 1 := by
  simp [queryDenominator, queryCode]


-- O3-E.C
-- Semántica exacta de la codificación.

theorem codedQuery_queryCode (u v d : ℕ) :
    codedQuery (queryCode ((u, v), d)) =
      ((u : ℚ) - (v : ℚ)) / ((d + 1 : ℕ) : ℚ) := by
  simp [codedQuery, queryCode]


-- O3-E.1
-- Todo racional posee una consulta natural de nuestra numeración.

theorem codedQuery_surjective :
    Function.Surjective codedQuery := by
  intro q

  have hden : 0 < q.den :=
    Rat.den_pos q

  cases hD : q.den with

  | zero =>
      simp [hD] at hden

  | succ d =>

      cases hN : q.num with

      | ofNat n =>
          refine
            ⟨queryCode ((n, 0), d), ?_⟩

          rw [codedQuery_queryCode]
          rw [← Rat.num_div_den q]

          simp [hN, hD]

      | negSucc n =>
          refine
            ⟨queryCode ((0, n + 1), d), ?_⟩

          rw [codedQuery_queryCode]
          rw [← Rat.num_div_den q]

          simp [hN, hD]


-- O3-E.2
-- Forma explícita derivada de la sobreyectividad:
-- para cada racional existen u,v,d naturales cuyo código representa q.

example (q : ℚ) :
    ∃ u v d : ℕ,
      codedQuery (queryCode ((u, v), d)) = q := by

  obtain ⟨z, hz⟩ :=
    codedQuery_surjective q

  refine
    ⟨queryPositive z,
     queryNegative z,
     queryDenominator z - 1,
     ?_⟩

  rw [codedQuery_queryCode]
  rw [← hz]

  have hd :
      queryDenominator z - 1 + 1 =
        queryDenominator z := by
    have hp := queryDenominator_pos z
    omega

  rw [hd]

  change
    ((queryPositive z : ℚ) -
        (queryNegative z : ℚ)) /
        (queryDenominator z : ℚ) =
      codedQuery z

  rfl
end Continuo.Indices
