import Mathlib

/-!
# Consecuencias elementales de los axiomas de cuerpo

Correspondencia editorial: MA-CON-0020, publicado en
`conceptos/axiomas-de-cuerpo-y-consecuencias-algebraicas-basicas.md`.

Los resultados multiplicativos se formulan para un cuerpo arbitrario `F`.
La cancelación aditiva se formula con la hipótesis más débil `[AddGroup G]`.
Las pruebas expresan pasos algebraicos explícitos y reutilizan las leyes
estructurales de Mathlib.
-/

namespace MatematicaAbierta

variable {F : Type*} [Field F]

/-- MA-CON-0020, §4.1: unicidad del neutro aditivo. -/
theorem neutro_aditivo_unico (e : F) (he : ∀ a : F, a + e = a) : e = 0 := by
  have h := he (0 : F)
  simpa only [zero_add] using h

/-- MA-CON-0020, §4.2: unicidad del neutro multiplicativo. -/
theorem neutro_multiplicativo_unico (e : F) (he : ∀ a : F, a * e = a) : e = 1 := by
  have h := he (1 : F)
  simpa only [one_mul] using h

/-- MA-CON-0020, §5.1: dos inversos aditivos de un mismo elemento coinciden. -/
theorem inverso_aditivo_unico (a b c : F)
    (hb : a + b = 0) (hc : a + c = 0) : b = c := by
  calc
    b = b + 0 := (add_zero b).symm
    _ = b + (a + c) := by rw [hc]
    _ = (b + a) + c := (add_assoc b a c).symm
    _ = (a + b) + c := by rw [add_comm b a]
    _ = 0 + c := by rw [hb]
    _ = c := zero_add c

/-- MA-CON-0020, §5.2: dos inversos multiplicativos del mismo elemento coinciden;
la demostración no utiliza cancelación multiplicativa ni necesita `a ≠ 0`. -/
theorem inverso_multiplicativo_unico (a b c : F)
    (hb : a * b = 1) (hc : a * c = 1) : b = c := by
  calc
    b = b * 1 := (mul_one b).symm
    _ = b * (a * c) := by rw [hc]
    _ = (b * a) * c := (mul_assoc b a c).symm
    _ = (a * b) * c := by rw [mul_comm b a]
    _ = 1 * c := by rw [hb]
    _ = c := one_mul c

/-- MA-CON-0020, §6: absorción del cero, deducida por distributividad y cancelación aditiva. -/
theorem cero_absorbe_producto (a : F) : (0 : F) * a = 0 := by
  have h : (0 : F) * a + 0 * a = 0 * a + 0 := by
    calc
      (0 : F) * a + 0 * a = (0 + 0) * a := (add_mul 0 0 a).symm
      _ = 0 * a := by rw [add_zero]
      _ = 0 * a + 0 := (add_zero _).symm
  exact add_left_cancel h

/-- MA-CON-0020, §10: cancelación multiplicativa (el factor debe ser no nulo). -/
theorem cancelacion_multiplicativa (a b c : F) (hc : c ≠ 0)
    (h : a * c = b * c) : a = b := by
  have hc_inv : c * c⁻¹ = 1 := mul_inv_cancel₀ hc
  calc
    a = a * 1 := (mul_one a).symm
    _ = a * (c * c⁻¹) := by rw [hc_inv]
    _ = (a * c) * c⁻¹ := (mul_assoc a c c⁻¹).symm
    _ = (b * c) * c⁻¹ := by rw [h]
    _ = b * (c * c⁻¹) := mul_assoc b c c⁻¹
    _ = b * 1 := by rw [hc_inv]
    _ = b := mul_one b

/-- MA-CON-0020, §11: propiedad del producto nulo, en ambos sentidos. -/
theorem producto_nulo_iff (a b : F) : a * b = 0 ↔ a = 0 ∨ b = 0 := by
  constructor
  · intro hab
    by_cases ha : a = 0
    · exact Or.inl ha
    · right
      have h : b * a = (0 : F) * a := by
        calc
          b * a = a * b := mul_comm b a
          _ = 0 := hab
          _ = (0 : F) * a := (cero_absorbe_producto a).symm
      exact cancelacion_multiplicativa b 0 a ha h
  · intro hab
    rcases hab with ha | hb
    · rw [ha, cero_absorbe_producto]
    · rw [hb, mul_zero]

variable {G : Type*} [AddGroup G]

/-- MA-CON-0020, §9: cancelación aditiva derecha, válida incluso en un grupo
aditivo no conmutativo; solo utiliza asociatividad, inverso y neutro. -/
theorem cancelacion_aditiva (a b c : G) (h : a + c = b + c) : a = b := by
  calc
    a = a + 0 := (add_zero a).symm
    _ = a + (c + -c) := by rw [add_neg_cancel]
    _ = (a + c) + -c := (add_assoc a c (-c)).symm
    _ = (b + c) + -c := congrArg (fun x : G => x + -c) h
    _ = b + (c + -c) := add_assoc b c (-c)
    _ = b + 0 := by rw [add_neg_cancel]
    _ = b := add_zero b

end MatematicaAbierta
