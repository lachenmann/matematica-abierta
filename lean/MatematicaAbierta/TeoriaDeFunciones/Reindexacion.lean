import MatematicaAbierta.TeoriaDeFunciones.Diagonalizacion

/-!
# TF-CAT-012: reindexación de familias de funciones y extensionalidad

Correspondencia exacta:
* TF-THM-00098: `reindexed_diagonal_ne_section` y
  `reindexed_no_surjective_sections`.
* TF-DEF-00051: `extensional_sections_iff` comprueba la equivalencia
  entre igualdad funcional e igualdad puntual de secciones.

No se declara formalizado el teorema de recursión de Kleene, la sintaxis
completa del cálculo simplemente tipado ni el cociente extensional
`TF-THM-00099`. No se añaden axiomas ni marcadores de prueba incompleta.
-/

namespace MatematicaAbierta.TeoriaDeFunciones

universe u v w
variable {P : Type u} {A : Type v} {B : Type w}

/-- TF-THM-00098: la diagonal reindexada difiere de cada sección cuando
    la aplicación de argumentos a índices es sobreyectiva. -/
theorem reindexed_diagonal_ne_section (U : P → A → B) (q : A → P)
    (hq : Function.Surjective q) (s : B → B)
    (hs : ∀ b : B, s b ≠ b) (p : P) :
    (fun a : A => s (U (q a) a)) ≠ U p := by
  intro h
  obtain ⟨a, ha⟩ := hq p
  have hpoint : s (U p a) = U p a := by
    simpa only [ha] using congrFun h a
  exact hs (U p a) hpoint

/-- TF-THM-00098: no hay representación exhaustiva de todas las funciones
    mediante las secciones de una familia reindexada sobreyectivamente. -/
theorem reindexed_no_surjective_sections (U : P → A → B) (q : A → P)
    (hq : Function.Surjective q) (s : B → B)
    (hs : ∀ b : B, s b ≠ b) :
    ¬ Function.Surjective (fun p : P => U p) := by
  intro hU
  obtain ⟨p, hp⟩ := hU (fun a : A => s (U (q a) a))
  exact reindexed_diagonal_ne_section U q hq s hs p hp.symm

/-- TF-DEF-00051: criterio extensional de equivalencia semántica de índices.
    No se afirma decidibilidad de ninguno de los dos lados. -/
theorem extensional_sections_iff (U : P → A → B) (p r : P) :
    (∀ a : A, U p a = U r a) ↔ U p = U r := by
  constructor
  · intro h
    funext a
    exact h a
  · intro h a
    exact congrFun h a

end MatematicaAbierta.TeoriaDeFunciones
