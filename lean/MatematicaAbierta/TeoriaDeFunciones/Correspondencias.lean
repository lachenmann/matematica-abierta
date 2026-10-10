import MatematicaAbierta.TeoriaDeFunciones.Reindexacion

/-!
# TF-CAT-013: correspondencias entre funciones, gráficas y exponenciales en Set

Alcance exacto:
* `TF-THM-00102`: sustitución y composición de gráficas como predicados
  en conjuntos interpretados por tipos Lean.
* `TF-THM-00103`: instancia en `Set` de la ley beta de currificación.
* `TF-THM-00104`: instancia en `Set` de la ley eta de currificación.

No se declaran formalizados el teorema categórico en una CCC arbitraria,
Yoneda (`TF-THM-00105`), los tipos dependientes del manuscrito ni el
contraejemplo computacional (`TF-THM-00108`).
-/

namespace MatematicaAbierta.TeoriaDeFunciones

universe u v w z
variable {A : Type u} {A' : Type v} {B : Type w} {C : Type z}

/-- Relación gráfica de una función en el modelo de conjuntos/tipos. -/
def graph13 (f : A → B) (a : A) (b : B) : Prop := b = f a

/-- TF-THM-00102, sustitución: la gráfica de una composición es la
    preimagen de la gráfica de la segunda función. -/
theorem graph13_precompose (f : A → B) (u : A' → A) (a : A') (b : B) :
    graph13 (fun x => f (u x)) a b ↔ graph13 f (u a) b := Iff.rfl

/-- TF-THM-00102, composición relacional de gráficas en Set. -/
theorem graph13_compose (f : A → B) (g : B → C) (a : A) (c : C) :
    (∃ b : B, graph13 f a b ∧ graph13 g b c) ↔
      graph13 (fun x => g (f x)) a c := by
  constructor
  · rintro ⟨b, hb, hc⟩
    dsimp [graph13] at hb hc ⊢
    calc
      c = g b := hc
      _ = g (f a) := congrArg g hb
  · intro h
    exact ⟨f a, rfl, h⟩

/-- TF-THM-00103: ley beta para la adjunción producto/exponencial en Set. -/
theorem set_beta_uncurry_curry (h : A × B → C) :
    (fun p : A × B => (fun x : A => fun y : B => h (x, y)) p.1 p.2) = h := by
  funext p
  rcases p with ⟨x, y⟩
  rfl

/-- TF-THM-00104: ley eta para la adjunción producto/exponencial en Set. -/
theorem set_eta_curry_uncurry (k : A → B → C) :
    (fun x : A => fun y : B => (fun p : A × B => k p.1 p.2) (x, y)) = k := by
  funext x y
  rfl

end MatematicaAbierta.TeoriaDeFunciones
