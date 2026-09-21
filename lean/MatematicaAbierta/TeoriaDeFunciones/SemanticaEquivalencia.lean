import MatematicaAbierta.TeoriaDeFunciones.Correspondencias

/-!
# TF-CAT-014: semántica de nombres, observadores y cambios de coordenadas

Cobertura estricta:
* TF-THM-00111: sólo identidad de denotaciones bajo traductores TOTALES
  suministrados; no se formaliza su computabilidad ni dominios parciales.
* TF-THM-00113: criterio suficiente para un observador inyectivo en Set.
* TF-THM-00114: transporte e inversa de funciones mediante `Equiv` de tipos,
  y compatibilidad de los transportes con composición (modelo Set).

Ninguna de estas pruebas demuestra equivalencia de categorías arbitrarias,
Kleisli, computabilidad de traducciones ni indecidibilidad del cociente.
-/

namespace MatematicaAbierta.TeoriaDeFunciones

universe u v w x y z

/-- TF-THM-00111 (instancia semántica): composición correcta de nombres.
    No afirma que las funciones provistas sean computables. -/
theorem names14_transport
    {X : Type u} {Y : Type v}
    (δX δX' : Nat → X) (δY δY' : Nat → Y)
    (TX TY F : Nat → Nat) (f : X → Y)
    (hX : ∀ n, δX (TX n) = δX' n)
    (hY : ∀ n, δY' (TY n) = δY n)
    (hF : ∀ n, δY (F n) = f (δX n)) (n : Nat) :
    δY' (TY (F (TX n))) = f (δX' n) := by
  calc
    δY' (TY (F (TX n))) = δY (F (TX n)) := hY _
    _ = f (δX (TX n)) := hF _
    _ = f (δX' n) := congrArg f (hX n)

/-- TF-THM-00113 (instancia): un observador inyectivo separa dos funciones. -/
theorem observer14_injective
    {A : Type u} {B : Type v} {C : Type w}
    (t : B → C) (ht : Function.Injective t) (f g : A → B)
    (h : t ∘ f = t ∘ g) : f = g := by
  funext a
  exact ht (congrFun h a)

/-- Transporte de una flecha por equivalencias de tipos. -/
def transport14 {A : Type u} {A' : Type v} {B : Type w} {B' : Type x}
    (eA : A ≃ A') (eB : B ≃ B') (f : A → B) : A' → B' :=
  fun a' => eB (f (eA.symm a'))

/-- TF-THM-00114 (Set): el transporte inverso recupera la función. -/
theorem transport14_inverse
    {A : Type u} {A' : Type v} {B : Type w} {B' : Type x}
    (eA : A ≃ A') (eB : B ≃ B') (f : A → B) :
    transport14 eA.symm eB.symm (transport14 eA eB f) = f := by
  funext a
  simp [transport14]

/-- TF-THM-00114 (Set): compatibilidad de los cambios con composición. -/
theorem transport14_comp
    {A : Type u} {A' : Type v} {B : Type w} {B' : Type x}
    {C : Type y} {C' : Type z}
    (eA : A ≃ A') (eB : B ≃ B') (eC : C ≃ C')
    (f : A → B) (g : B → C) :
    transport14 eA eC (g ∘ f) =
      (transport14 eB eC g) ∘ (transport14 eA eB f) := by
  funext a'
  simp [transport14]

end MatematicaAbierta.TeoriaDeFunciones
