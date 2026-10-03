import Mathlib

/-!
# MCL-M00-L01 — ¿Qué significa demostrar?

Primera lección ejecutable de *Aprender matemáticas con Lean*.

La finalidad de este módulo no es introducir una colección de tácticas aisladas,
sino mostrar tres ideas matemáticas elementales:

1. cada objeto es igual a sí mismo;
2. una hipótesis que coincide con la conclusión puede utilizarse directamente;
3. la igualdad es simétrica y transitiva.

Las herramientas `rfl` y `exact` aparecen porque estas ideas las necesitan.
-/

namespace MatematicaAbierta.AprenderMatematicasConLean.M00

/-- MCL-M00-L01-R001: cada objeto es igual a sí mismo. -/
theorem igualdad_reflexiva {α : Type*} (a : α) : a = a := by
  rfl

/-- MCL-M00-L01-R002: si una proposición se tiene como hipótesis, puede concluirse. -/
theorem usar_hipotesis (P : Prop) (h : P) : P := by
  exact h

/-- MCL-M00-L01-R003: la igualdad puede leerse en el sentido inverso. -/
theorem igualdad_simetrica {α : Type*} {a b : α} (h : a = b) : b = a := by
  exact h.symm

/-- MCL-M00-L01-R004: dos igualdades compatibles pueden encadenarse. -/
theorem igualdad_transitiva {α : Type*} {a b c : α}
    (hab : a = b) (hbc : b = c) : a = c := by
  exact hab.trans hbc

/-- MCL-M00-L01-E001: primer ejercicio mínimo de lectura de una meta reflexiva. -/
example (n : ℕ) : n = n := by
  rfl

end MatematicaAbierta.AprenderMatematicasConLean.M00
