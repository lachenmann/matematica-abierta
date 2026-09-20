import Mathlib

/-!
# TF-CAT-011: evaluación universal y diagonalización

La semántica formalizada aquí es la de familias de **funciones totales** entre tipos.
No se declara ningún intérprete de máquinas de Turing ni se identifica una
familia total con una familia de funciones parcialmente computables.

Correspondencia editorial:
* TF-THM-00088: `diagonal_ne_section` y `no_surjective_sections`.
* TF-THM-00089: `fixedPoint_of_surjective_sections`.
* TF-THM-00090: `cantor_predicate` (versión de predicados/subconjuntos).

Todas las pruebas sustanciales están desarrolladas aquí; Mathlib proporciona
los tipos de funciones, la noción `Function.Surjective` y la lógica de Lean.
-/

namespace MatematicaAbierta.TeoriaDeFunciones

universe u v

variable {A : Type u} {B : Type v}

/-- TF-THM-00088: la diagonal perturbada difiere de cada sección total. -/
theorem diagonal_ne_section (U : A → A → B) (s : B → B)
    (hs : ∀ b : B, s b ≠ b) (a : A) :
    (fun x : A => s (U x x)) ≠ U a := by
  intro h
  have hpoint : s (U a a) = U a a := congrFun h a
  exact hs (U a a) hpoint

/-- TF-THM-00089: una enumeración exhaustiva produce un punto fijo. -/
theorem fixedPoint_of_surjective_sections (U : A → A → B)
    (hU : Function.Surjective (fun a : A => U a)) (s : B → B) :
    ∃ b : B, s b = b := by
  obtain ⟨a, ha⟩ := hU (fun x : A => s (U x x))
  refine ⟨U a a, ?_⟩
  exact (congrFun ha a).symm

/-- TF-THM-00088: versión de imposibilidad de sobreyectividad. -/
theorem no_surjective_sections (U : A → A → B) (s : B → B)
    (hs : ∀ b : B, s b ≠ b) :
    ¬ Function.Surjective (fun a : A => U a) := by
  intro hU
  obtain ⟨b, hb⟩ := fixedPoint_of_surjective_sections U hU s
  exact hs b hb

/-- TF-THM-00090: Cantor para funciones con codominio de predicados. -/
theorem cantor_predicate (U : A → A → Prop) :
    ¬ Function.Surjective (fun a : A => U a) := by
  intro hU
  obtain ⟨a, ha⟩ := hU (fun x : A => ¬ U x x)
  have hdiag : U a a = (¬ U a a) := congrFun ha a
  have hn : ¬ U a a := by
    intro hp
    exact (Eq.mp hdiag hp) hp
  exact hn (Eq.mpr hdiag hn)

end MatematicaAbierta.TeoriaDeFunciones
