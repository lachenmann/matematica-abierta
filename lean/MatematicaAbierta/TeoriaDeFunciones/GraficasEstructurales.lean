import Mathlib.CategoryTheory.Subobject.Basic
import Mathlib.CategoryTheory.Limits.Shapes.BinaryProducts.BinaryProducts

/-!
# TF-THM-00005: caracterización estructural de las gráficas

Marco: categoría arbitraria con un producto binario elegido para A y B.
Los subobjetos se comparan como clases de monomorfismos, no por igualdad
literal de sus flechas representantes. No se supone regularidad ni elección
en la teoría objeto. `inv`/`Subobject` pueden utilizar elección metateórica
para escoger representantes: la demostración categórica no postula AC.
-/

namespace MatematicaAbierta.TeoriaDeFunciones

open CategoryTheory CategoryTheory.Limits

-- La instancia local de invertibilidad es una prueba (Prop); `letI` es necesario
-- para que Lean pueda elaborar `inv` y `asIso`, incluso dentro de una prueba.
set_option linter.style.haveILetI false

universe v u
variable {C : Type u} [Category.{v} C]
variable {A B R : C} [HasBinaryProduct A B]

/-- Flecha gráfica `⟨𝟙 A, f⟩ : A ⟶ A ⨯ B`. -/
noncomputable def graphStructural (f : A ⟶ B) : A ⟶ A ⨯ B :=
  prod.lift (𝟙 A) f

instance graphStructural_mono (f : A ⟶ B) : Mono (graphStructural f) := by
  unfold graphStructural
  infer_instance

@[simp]
theorem graphStructural_fst (f : A ⟶ B) :
    graphStructural f ≫ prod.fst = 𝟙 A := prod.lift_fst _ _

@[simp]
theorem graphStructural_snd (f : A ⟶ B) :
    graphStructural f ≫ prod.snd = f := prod.lift_snd _ _

/-- La igualdad de subobjetos gráficos proporciona un isomorfismo de
representantes sobre el producto. -/
private theorem graphStructural_rep_witness (m : R ⟶ A ⨯ B) [Mono m]
    (f : A ⟶ B) (h : Subobject.mk m = Subobject.mk (graphStructural f)) :
    (Subobject.isoOfMkEqMk m (graphStructural f) h).hom ≫ graphStructural f = m := by
  change Subobject.ofMkLEMk m (graphStructural f) h.le ≫ graphStructural f = m
  exact Subobject.ofMkLEMk_comp h.le

/-- TF-THM-00005: un mono representa la gráfica de una flecha exactamente
cuando su primera proyección es un isomorfismo. -/
theorem tf_thm_00005 (m : R ⟶ A ⨯ B) [Mono m] :
    (∃ f : A ⟶ B, Subobject.mk m = Subobject.mk (graphStructural f)) ↔
      IsIso (m ≫ prod.fst) := by
  constructor
  · rintro ⟨f, h⟩
    let i : R ≅ A := Subobject.isoOfMkEqMk m (graphStructural f) h
    have wi : i.hom ≫ graphStructural f = m :=
      graphStructural_rep_witness m f h
    have hp : i.hom = m ≫ prod.fst := by
      calc
        i.hom = i.hom ≫ (𝟙 A) := by simp
        _ = (i.hom ≫ graphStructural f) ≫ prod.fst := by simp [Category.assoc]
        _ = m ≫ prod.fst := by rw [wi]
    rw [← hp]
    infer_instance
  · intro hi
    letI : IsIso (m ≫ prod.fst) := hi
    let p : R ⟶ A := m ≫ prod.fst
    let f : A ⟶ B := inv p ≫ (m ≫ prod.snd)
    refine ⟨f, ?_⟩
    apply Subobject.mk_eq_mk_of_comm m (graphStructural f) (asIso p)
    apply prod.hom_ext
    · simp [graphStructural, Category.assoc, p]
    · change (p ≫ graphStructural f) ≫ prod.snd = m ≫ prod.snd
      calc
        (p ≫ graphStructural f) ≫ prod.snd = p ≫ f := by
          simp [Category.assoc]
        _ = (p ≫ inv p) ≫ (m ≫ prod.snd) := by
          simp [f]
        _ = m ≫ prod.snd := by simp

/-- La recuperacion usa una instancia explícita de `IsIso` únicamente para
que `inv` sea una expresión bien tipada. El teorema principal demuestra que
dicha instancia se obtiene de la condición gráfica, sin hipótesis axiomáticas. -/
theorem tf_thm_00005_recover (m : R ⟶ A ⨯ B) [Mono m]
    [IsIso (m ≫ prod.fst)]
    (f : A ⟶ B) (h : Subobject.mk m = Subobject.mk (graphStructural f)) :
    f = inv (m ≫ prod.fst) ≫ (m ≫ prod.snd) := by
  let i : R ≅ A := Subobject.isoOfMkEqMk m (graphStructural f) h
  have wi : i.hom ≫ graphStructural f = m :=
    graphStructural_rep_witness m f h
  have hp : i.hom = m ≫ prod.fst := by
    calc
      i.hom = i.hom ≫ (𝟙 A) := by simp
      _ = (i.hom ≫ graphStructural f) ≫ prod.fst := by simp [Category.assoc]
      _ = m ≫ prod.fst := by rw [wi]
  have hq : i.hom ≫ f = m ≫ prod.snd := by
    calc
      i.hom ≫ f = (i.hom ≫ graphStructural f) ≫ prod.snd := by
        simp [Category.assoc]
      _ = m ≫ prod.snd := by rw [wi]
  symm
  rw [← hp, ← hq]
  calc
    inv i.hom ≫ (i.hom ≫ f) = (inv i.hom ≫ i.hom) ≫ f :=
      (Category.assoc _ _ _).symm
    _ = f := by simp

/-- La función representada es única para el producto A ⨯ B fijado. -/
theorem tf_thm_00005_unique (m : R ⟶ A ⨯ B) [Mono m]
    (f g : A ⟶ B)
    (hf : Subobject.mk m = Subobject.mk (graphStructural f))
    (hg : Subobject.mk m = Subobject.mk (graphStructural g)) : f = g := by
  letI : IsIso (m ≫ prod.fst) := (tf_thm_00005 m).mp ⟨f, hf⟩
  calc
    f = inv (m ≫ prod.fst) ≫ (m ≫ prod.snd) := tf_thm_00005_recover m f hf
    _ = g := (tf_thm_00005_recover m g hg).symm

/-- Una sustitución isomorfa de representante no cambia la función recuperada.
Los dos testigos de `IsIso` indican explícitamente cuándo se define `inv`. -/
theorem tf_thm_00005_invariant {S : C} (m : R ⟶ A ⨯ B)
    (n : S ⟶ A ⨯ B) [Mono m] [Mono n]
    (e : R ≅ S) (he : e.hom ≫ n = m)
    [IsIso (m ≫ prod.fst)] [IsIso (n ≫ prod.fst)] :
    inv (m ≫ prod.fst) ≫ (m ≫ prod.snd) =
      inv (n ≫ prod.fst) ≫ (n ≫ prod.snd) := by
  obtain ⟨f, hf⟩ := (tf_thm_00005 m).mpr inferInstance
  obtain ⟨g, hg⟩ := (tf_thm_00005 n).mpr inferInstance
  have hmn : Subobject.mk m = Subobject.mk n :=
    Subobject.mk_eq_mk_of_comm m n e he
  have hfg : f = g := by
    have hgn : Subobject.mk m = Subobject.mk (graphStructural g) :=
      hmn.trans hg
    exact tf_thm_00005_unique m f g hf hgn
  calc
    inv (m ≫ prod.fst) ≫ (m ≫ prod.snd) = f :=
      (tf_thm_00005_recover m f hf).symm
    _ = g := hfg
    _ = inv (n ≫ prod.fst) ≫ (n ≫ prod.snd) :=
      tf_thm_00005_recover n g hg

end MatematicaAbierta.TeoriaDeFunciones
