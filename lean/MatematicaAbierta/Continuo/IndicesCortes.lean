import MatematicaAbierta.Continuo.TerminacionCortes

/-!
# FDC-AUD-023 — O3: codificación efectiva de consultas y búsqueda

Las consultas se representan por dos numeradores naturales y un denominador
positivo; las comparaciones usan únicamente sumas, productos, potencias y
orden de naturales. La construcción de códigos parciales es uniforme en el
programa. La certificación semántica y de totalidad se verifica por separado.
-/

namespace Continuo.Indices

open Denumerable

/-- Codificación sobreyectiva prevista: `((u,v),d)` representa `(u-v)/(d+1)`.
No se presupone que la enumeración de `ℚ` elegida por una instancia sea PR. -/
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

/-- Comparador universal de fracciones con numeradores firmados por diferencia.
La aproximación es `(plus-minus)/s` y el radio es `1/t`.
`d`, `s`, `t` deben ser positivos para interpretar los certificados. -/
def arithmeticStage (u v d plus minus s t : ℕ) : Option Bool :=
  if u * s * t + minus * d * t + s * d < v * s * t + plus * d * t then
    some true
  else if plus * d * t + v * s * t + s * d < u * s * t + minus * d * t then
    some false
  else none

/-- Composición uniforme del comparador con siete funciones PR arbitrarias. -/
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

/-- Tipo de entrada de una etapa: `((programa,consulta),precisión)`. -/
def shiftedNumericStage (w : (Code × ℕ) × ℕ) : Option Bool :=
  arithmeticStage (queryPositive w.1.2) (queryNegative w.1.2)
    (queryDenominator w.1.2) (shiftedPair w.1.1 w.2).1 0
    (shiftedPair w.1.1 w.2).2 (2 ^ w.2)

/-- En el extremo negativo, `-sqrtTwoName` se expresa con numerador
positivo cero y numerador negativo igual al del nombre de raíz. -/
def negativeNumericStage (w : ℕ × ℕ) : Option Bool :=
  arithmeticStage (queryPositive w.1) (queryNegative w.1)
    (queryDenominator w.1) 0 (sqrtTwoPair w.2).1
    (sqrtTwoPair w.2).2 (2 ^ (w.2 + 2))

set_option maxHeartbeats 1000000 in
theorem primrec_shiftedNumericStage : Primrec shiftedNumericStage := by
  have hc : Primrec (fun w : (Code × ℕ) × ℕ => w.1.1) :=
    Primrec.fst.comp Primrec.fst
  have hq : Primrec (fun w : (Code × ℕ) × ℕ => w.1.2) :=
    Primrec.snd.comp Primrec.fst
  have hn : Primrec (fun w : (Code × ℕ) × ℕ => w.2) := Primrec.snd
  have hname : Primrec (fun w : (Code × ℕ) × ℕ => shiftedPair w.1.1 w.2) :=
    primrec_shiftedPair.comp hc hn
  have hpow : Primrec (fun w : (Code × ℕ) × ℕ => 2 ^ w.2) :=
    (Primrec₂.unpaired'.1 Nat.Primrec.pow).comp (Primrec.const 2) hn
  exact (primrec_arithmeticStage
    (fun w => queryPositive w.1.2) (fun w => queryNegative w.1.2)
    (fun w => queryDenominator w.1.2)
    (fun w => (shiftedPair w.1.1 w.2).1) (fun _ => 0)
    (fun w => (shiftedPair w.1.1 w.2).2) (fun w => 2 ^ w.2)
    (primrec_queryPositive.comp hq) (primrec_queryNegative.comp hq)
    (primrec_queryDenominator.comp hq)
    (Primrec.fst.comp hname) (Primrec.const 0)
    (Primrec.snd.comp hname) hpow).of_eq fun _ => rfl

set_option maxHeartbeats 1000000 in
theorem primrec_negativeNumericStage : Primrec negativeNumericStage := by
  have hq : Primrec (fun w : ℕ × ℕ => w.1) := Primrec.fst
  have hn : Primrec (fun w : ℕ × ℕ => w.2) := Primrec.snd
  have hname : Primrec (fun w : ℕ × ℕ => sqrtTwoPair w.2) :=
    primrec_sqrtTwoPair.comp hn
  have hn2 : Primrec (fun w : ℕ × ℕ => w.2 + 2) :=
    Primrec.nat_add.comp hn (Primrec.const 2)
  have hpow : Primrec (fun w : ℕ × ℕ => 2 ^ (w.2 + 2)) :=
    (Primrec₂.unpaired'.1 Nat.Primrec.pow).comp (Primrec.const 2) hn2
  exact (primrec_arithmeticStage
    (fun w => queryPositive w.1) (fun w => queryNegative w.1)
    (fun w => queryDenominator w.1) (fun _ => 0)
    (fun w => (sqrtTwoPair w.2).1)
    (fun w => (sqrtTwoPair w.2).2) (fun w => 2 ^ (w.2 + 2))
    (primrec_queryPositive.comp hq) (primrec_queryNegative.comp hq)
    (primrec_queryDenominator.comp hq) (Primrec.const 0)
    (Primrec.fst.comp hname) (Primrec.snd.comp hname) hpow).of_eq fun _ => rfl

end Continuo.Indices
