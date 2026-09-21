import MatematicaAbierta.TeoriaDeFunciones.SemanticaEquivalencia

/-!
# TF-CAT-015: naturalidad, Yoneda en Set y productos

Cobertura estricta: instancia Set de TF-THM-00120 mediante recuperación,
plenitud y fidelidad de transformaciones naturales de representables;
instancia Set de TF-THM-00123 para naturalidad y recuperación de productos.
No formaliza el lema de Yoneda para categorías arbitrarias, tamaño de
categorías de funtores ni decidibilidad o computabilidad.
-/

namespace MatematicaAbierta.TeoriaDeFunciones

universe u

/-- Acción sobre flechas de la representación contravariante en Set. -/
def yoneda15Map {A B : Type u} (f : A → B)
    (X : Type u) (g : X → A) : X → B := f ∘ g

/-- TF-THM-00120 (Set): la acción representable es natural. -/
theorem yoneda15_map_natural {A B X Y : Type u}
    (f : A → B) (g : X → A) (u : Y → X) :
    yoneda15Map f Y (g ∘ u) = (yoneda15Map f X g) ∘ u := by
  funext y
  rfl

/-- TF-THM-00120 (Set): recuperar una familia natural por su identidad. -/
theorem yoneda15_recover {A B : Type u}
    (α : (X : Type u) → (X → A) → (X → B))
    (hnat : ∀ (X Y : Type u) (u : Y → X) (g : X → A),
      α Y (g ∘ u) = (α X g) ∘ u)
    (X : Type u) (g : X → A) :
    α X g = (α A id) ∘ g := by
  have h := hnat A X g (id : A → A)
  simpa only [id_comp] using h

/-- TF-THM-00120 (Set): plenitud y unicidad del mapa recuperado. -/
theorem yoneda15_full {A B : Type u}
    (α : (X : Type u) → (X → A) → (X → B))
    (hnat : ∀ (X Y : Type u) (u : Y → X) (g : X → A),
      α Y (g ∘ u) = (α X g) ∘ u) :
    ∃! f : A → B, ∀ (X : Type u) (g : X → A),
      α X g = yoneda15Map f X g := by
  refine ⟨α A id, ?_, ?_⟩
  · intro X g
    exact yoneda15_recover α hnat X g
  · intro f hf
    have h := hf A (id : A → A)
    simpa [yoneda15Map] using h.symm

/-- TF-THM-00120 (Set): fidelidad de la representación. -/
theorem yoneda15_faithful {A B : Type u} (f g : A → B)
    (h : ∀ (X : Type u) (k : X → A),
      yoneda15Map f X k = yoneda15Map g X k) : f = g := by
  have hi := h A (id : A → A)
  simpa [yoneda15Map] using hi

/-- TF-THM-00123 (Set): familia natural asociada a h : A → B. -/
def product15 {A B : Type u} (h : A → B)
    (X : Type u) (p : X × A) : X × B := (p.1, h p.2)

/-- TF-THM-00123 (Set): la familia construida conmuta con parámetros. -/
theorem product15_natural {A B X Y : Type u}
    (h : A → B) (u : X → Y) (p : X × A) :
    product15 h Y (u p.1, p.2) =
      (u (product15 h X p).1, (product15 h X p).2) := by
  rfl

/-- TF-THM-00123 (Set): todo producto natural se recupera en PUnit. -/
theorem product15_recover {A B : Type u}
    (α : (X : Type u) → X × A → X × B)
    (hnat : ∀ (X Y : Type u) (u : X → Y) (p : X × A),
      α Y (u p.1, p.2) = (u (α X p).1, (α X p).2))
    (X : Type u) (p : X × A) :
    α X p = (p.1, (α PUnit.{u} (PUnit.unit, p.2)).2) := by
  rcases p with ⟨x, a⟩
  let c : PUnit.{u} → X := fun _ => x
  have h := hnat PUnit.{u} X c (PUnit.unit, a)
  simpa [c] using h

end MatematicaAbierta.TeoriaDeFunciones
