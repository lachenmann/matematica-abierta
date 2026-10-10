import MatematicaAbierta.TeoriaDeFunciones.NaturalidadSondas

/-!
# TF-CAT-016: instancia conjuntista sobre la categoría terminal

Cobertura estricta y parcial: para la categoría con un objeto y sólo su identidad,
un prehaz es un conjunto S, los representables son unitarios y su categoría de
elementos es discreta con objetos S. La descomposición de S como coproducto de
unitarios y su propiedad universal son instancias de TF-THM-00127; la separación
por las inclusiones es instancia de TF-THM-00131. También se comprueba la parte
finita del contraejemplo TF-CEX-00022. No se formalizan el teorema de densidad
para categorías generales, coextremos, categorías de elementos arbitrarias,
condiciones de tamaño o decidibilidad.
-/

namespace MatematicaAbierta.TeoriaDeFunciones

universe u v

/-- La suma de copias del conjunto unitario indexada por S se evalúa en S. -/
def density16Eval {S : Type u} : (Σ _ : S, PUnit) → S := fun p => p.1

/-- La inclusión del sumando unitario asociado a cada s. -/
def density16Incl {S : Type u} (s : S) : PUnit → S := fun _ => s

/-- TF-THM-00127, instancia terminal: la suma de representables unitarios es S. -/
def density16Equiv (S : Type u) : (Σ _ : S, PUnit) ≃ S where
  toFun := density16Eval
  invFun := fun s => ⟨s, PUnit.unit⟩
  left_inv := by
    intro p
    rcases p with ⟨s, z⟩
    cases z
    rfl
  right_inv := by
    intro s
    rfl

/-- TF-THM-00127, instancia terminal: la familia de unitarios es colimitante. -/
theorem density16_universal (S : Type u) (T : Type v)
    (cocone : (s : S) → PUnit → T) :
    ∃! f : S → T, ∀ s : S, (fun z : PUnit => f (density16Incl s z)) = cocone s := by
  refine ⟨fun s => cocone s PUnit.unit, ?_, ?_⟩
  · intro s
    funext z
    cases z
    rfl
  · intro f hf
    funext s
    have h := congrFun (hf s) PUnit.unit
    simpa [density16Incl] using h

/-- TF-THM-00131, instancia terminal: las sondas unitarias separan funciones. -/
theorem density16_detect {S : Type u} {T : Type v} (f g : S → T)
    (h : ∀ s : S,
      (fun z : PUnit => f (density16Incl s z)) =
      (fun z : PUnit => g (density16Incl s z))) : f = g := by
  funext s
  have hs := congrFun (h s) PUnit.unit
  simpa [density16Incl] using hs

/-- TF-CEX-00022, caso de dos elementos: Bool no es un representable unitario. -/
theorem density16_bool_not_unit : ¬ Nonempty (Bool ≃ PUnit) := by
  rintro ⟨e⟩
  have h : (true : Bool) = false :=
    e.injective (Subsingleton.elim (e true) (e false))
  cases h

end MatematicaAbierta.TeoriaDeFunciones
