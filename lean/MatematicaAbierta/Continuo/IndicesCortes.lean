import MatematicaAbierta.Continuo.TerminacionCortes

/-!
# FDC-AUD-023 — O3: codificación de consultas y núcleo aritmético

Codificamos racionales mediante dos numeradores naturales y un denominador
positivo. La comparación se reduce a sumas, productos y orden de naturales.
Este módulo certifica la primitividad recursiva del comparador genérico,
pero NO certifica todavía la primitividad recursiva de sus especializaciones,
la equivalencia con `intervalStage` ni la extracción de índices de programas.
O3 permanece abierta.
-/

namespace Continuo.Indices

/-- `((u,v),d)` representa `(u-v)/(d+1)`. -/
def codedQuery (z : ℕ) : ℚ :=
  ((z.unpair.1.unpair.1 : ℚ) - (z.unpair.1.unpair.2 : ℚ)) /
    ((z.unpair.2 + 1 : ℕ) : ℚ)

def queryPositive (z : ℕ) : ℕ := z.unpair.1.unpair.1

def queryNegative (z : ℕ) : ℕ := z.unpair.1.unpair.2

def queryDenominator (z : ℕ) : ℕ := z.unpair.2 + 1

theorem queryDenominator_pos (z : ℕ) : 0 < queryDenominator z := by
  simp [queryDenominator]

theorem primrec_queryPositive : Primrec queryPositive := by
  exact (Primrec.fst.comp (Primrec.unpair.comp
    (Primrec.fst.comp Primrec.unpair))).of_eq fun _ => rfl

theorem primrec_queryNegative : Primrec queryNegative := by
  exact (Primrec.snd.comp (Primrec.unpair.comp
    (Primrec.fst.comp Primrec.unpair))).of_eq fun _ => rfl

theorem primrec_queryDenominator : Primrec queryDenominator := by
  exact (Primrec.succ.comp (Primrec.snd.comp Primrec.unpair)).of_eq fun _ => rfl

/-- Comparador de fracciones con numeradores representados como diferencias.
La aproximación es `(plus-minus)/s` y el radio es `1/t`.
Las equivalencias con desigualdades racionales requieren `d,s,t > 0`. -/
def arithmeticStage (u v d plus minus s t : ℕ) : Option Bool :=
  if u * s * t + minus * d * t + s * d < v * s * t + plus * d * t then
    some true
  else if plus * d * t + v * s * t + s * d < u * s * t + minus * d * t then
    some false
  else none

/-- El comparador es primitivo recursivo para siete parámetros PR arbitrarios. -/
theorem primrec_arithmeticStage {α : Type*} [Primcodable α]
    (u v d plus minus s t : α → ℕ)
    (hu : Primrec u) (hv : Primrec v) (hd : Primrec d)
    (hp : Primrec plus) (hm : Primrec minus) (hs : Primrec s)
    (ht : Primrec t) :
    Primrec (fun a => arithmeticStage (u a) (v a) (d a)
      (plus a) (minus a) (s a) (t a)) := by
  have hust : Primrec (fun a => u a * s a * t a) :=
    Primrec.nat_mul.comp (Primrec.nat_mul.comp hu hs) ht
  have hvst : Primrec (fun a => v a * s a * t a) :=
    Primrec.nat_mul.comp (Primrec.nat_mul.comp hv hs) ht
  have hpdt : Primrec (fun a => plus a * d a * t a) :=
    Primrec.nat_mul.comp (Primrec.nat_mul.comp hp hd) ht
  have hmdt : Primrec (fun a => minus a * d a * t a) :=
    Primrec.nat_mul.comp (Primrec.nat_mul.comp hm hd) ht
  have hsd : Primrec (fun a => s a * d a) := Primrec.nat_mul.comp hs hd
  have hl : Primrec (fun a => u a * s a * t a + minus a * d a * t a + s a * d a) :=
    Primrec.nat_add.comp (Primrec.nat_add.comp hust hmdt) hsd
  have hr : Primrec (fun a => v a * s a * t a + plus a * d a * t a) :=
    Primrec.nat_add.comp hvst hpdt
  have hl' : Primrec (fun a => plus a * d a * t a + v a * s a * t a + s a * d a) :=
    Primrec.nat_add.comp (Primrec.nat_add.comp hpdt hvst) hsd
  have hr' : Primrec (fun a => u a * s a * t a + minus a * d a * t a) :=
    Primrec.nat_add.comp hust hmdt
  have hlt : PrimrecPred (fun a =>
      u a * s a * t a + minus a * d a * t a + s a * d a <
        v a * s a * t a + plus a * d a * t a) :=
    Primrec.nat_lt.comp hl hr
  have hgt : PrimrecPred (fun a =>
      plus a * d a * t a + v a * s a * t a + s a * d a <
        u a * s a * t a + minus a * d a * t a) :=
    Primrec.nat_lt.comp hl' hr'
  exact (Primrec.ite hlt (Primrec.const (some true))
    (Primrec.ite hgt (Primrec.const (some false))
      (Primrec.const none))).of_eq fun a => by
        simp only [arithmeticStage]

/-- Especificación computacional de la etapa desplazada; la prueba PR se reserva. -/
def shiftedNumericStage (w : (Code × ℕ) × ℕ) : Option Bool :=
  arithmeticStage (queryPositive w.1.2) (queryNegative w.1.2)
    (queryDenominator w.1.2) (shiftedPair w.1.1 w.2).1 0
    (shiftedPair w.1.1 w.2).2 (2 ^ w.2)

/-- Especificación computacional de la etapa negativa; la prueba PR se reserva. -/
def negativeNumericStage (w : ℕ × ℕ) : Option Bool :=
  arithmeticStage (queryPositive w.1) (queryNegative w.1)
    (queryDenominator w.1) 0 (sqrtTwoPair w.2).1
    (sqrtTwoPair w.2).2 (2 ^ (w.2 + 2))

end Continuo.Indices
