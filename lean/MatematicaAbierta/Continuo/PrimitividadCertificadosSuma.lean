import MatematicaAbierta.Continuo.SemanticaCertificadosSuma

/-!
# FDC-AUD-025-M04b — Primitividad recursiva de la etapa de certificados

Composición explícita de las proyecciones de cuaternas, aritmética
de los racionales codificados, evaluación finita de programas y pruebas
finitas de igualdad. Sin oráculos ideales y sin una cota que cuente
instrucciones de máquina.

Esta fuente verifica el requisito B1. La completitud por testigos
y la terminación bajo la promesa P025a se demuestran aparte.
-/

namespace Continuo.Indices

/-- Lectura efectiva del primer parámetro de la etapa. -/
theorem primrec_sumStageLeft : Primrec sumStageLeft := by
  exact (Primrec.fst.comp Primrec.unpair).of_eq fun _ => rfl

/-- Lectura efectiva del segundo parámetro. -/
theorem primrec_sumStageRight : Primrec sumStageRight := by
  exact
    (Primrec.fst.comp
      (Primrec.unpair.comp
        (Primrec.snd.comp Primrec.unpair))).of_eq fun _ => rfl

/-- Extracción de un margen estrictamente positivo y efectivamente codificado. -/
theorem primrec_sumStageMargin : Primrec sumStageMargin := by
  exact
    (Primrec.succ.comp
      (Primrec.fst.comp
        (Primrec.unpair.comp
          (Primrec.snd.comp
            (Primrec.unpair.comp
              (Primrec.snd.comp Primrec.unpair)))))).of_eq fun _ => rfl

/-- Extracción de la cota del evaluador parcial, nunca un reloj de máquina. -/
theorem primrec_sumStageFuel : Primrec sumStageFuel := by
  exact
    (Primrec.succ.comp
      (Primrec.snd.comp
        (Primrec.unpair.comp
          (Primrec.snd.comp
            (Primrec.unpair.comp
              (Primrec.snd.comp Primrec.unpair)))))).of_eq fun _ => rfl

/-- La etapa concreta es primitiva recursiva en todos sus parámetros. -/
theorem primrec_sumCertificateStage : Primrec sumCertificateStage := by
  let W := ((Code × Code) × ℕ) × ℕ

  have hz : Primrec (fun w : W => w.1.2) :=
    Primrec.snd.comp Primrec.fst
  have hi : Primrec (fun w : W => sumStageLeft w.2) :=
    primrec_sumStageLeft.comp Primrec.snd
  have hj : Primrec (fun w : W => sumStageRight w.2) :=
    primrec_sumStageRight.comp Primrec.snd
  have ht : Primrec (fun w : W => sumStageMargin w.2) :=
    primrec_sumStageMargin.comp Primrec.snd
  have hfuel : Primrec (fun w : W => sumStageFuel w.2) :=
    primrec_sumStageFuel.comp Primrec.snd

  have hqp : Primrec (fun w : W => queryPositive w.1.2) :=
    primrec_queryPositive.comp hz
  have hqn : Primrec (fun w : W => queryNegative w.1.2) :=
    primrec_queryNegative.comp hz
  have hqd : Primrec (fun w : W => queryDenominator w.1.2) :=
    primrec_queryDenominator.comp hz
  have hip : Primrec (fun w : W => queryPositive (sumStageLeft w.2)) :=
    primrec_queryPositive.comp hi
  have hjp : Primrec (fun w : W => queryPositive (sumStageRight w.2)) :=
    primrec_queryPositive.comp hj
  have hin : Primrec (fun w : W => queryNegative (sumStageLeft w.2)) :=
    primrec_queryNegative.comp hi
  have hjn : Primrec (fun w : W => queryNegative (sumStageRight w.2)) :=
    primrec_queryNegative.comp hj
  have hid : Primrec (fun w : W => queryDenominator (sumStageLeft w.2)) :=
    primrec_queryDenominator.comp hi
  have hjd : Primrec (fun w : W => queryDenominator (sumStageRight w.2)) :=
    primrec_queryDenominator.comp hj
  have hpos : Primrec (fun w : W =>
      sumStagePositive (sumStageLeft w.2) (sumStageRight w.2)) := by
    exact (Primrec.nat_add.comp
      (Primrec.nat_mul.comp hip hjd)
      (Primrec.nat_mul.comp hjp hid)).of_eq fun _ => rfl
  have hneg : Primrec (fun w : W =>
      sumStageNegative (sumStageLeft w.2) (sumStageRight w.2)) := by
    exact (Primrec.nat_add.comp
      (Primrec.nat_mul.comp hin hjd)
      (Primrec.nat_mul.comp hjn hid)).of_eq fun _ => rfl
  have hden : Primrec (fun w : W =>
      sumStageDenominator (sumStageLeft w.2) (sumStageRight w.2)) := by
    exact (Primrec.nat_mul.comp hid hjd).of_eq fun _ => rfl
  have hcomparison : Primrec (fun w : W =>
      sumStageComparison w.1.2 (sumStageLeft w.2)
        (sumStageRight w.2) (sumStageMargin w.2)) := by
    exact (primrec_arithmeticStage
      (fun w : W => queryPositive w.1.2)
      (fun w : W => queryNegative w.1.2)
      (fun w : W => queryDenominator w.1.2)
      (fun w : W => sumStagePositive (sumStageLeft w.2) (sumStageRight w.2))
      (fun w : W => sumStageNegative (sumStageLeft w.2) (sumStageRight w.2))
      (fun w : W => sumStageDenominator (sumStageLeft w.2) (sumStageRight w.2))
      (fun w : W => sumStageMargin w.2)
      hqp hqn hqd hpos hneg hden ht).of_eq fun _ => rfl

  have hcodeA : Primrec (fun w : W => w.1.1.1) :=
    Primrec.fst.comp (Primrec.fst.comp Primrec.fst)
  have hcodeB : Primrec (fun w : W => w.1.1.2) :=
    Primrec.snd.comp (Primrec.fst.comp Primrec.fst)

  have hanswerA : Primrec (fun w : W =>
      sumStageAnswerA w.1 (sumStageLeft w.2) (sumStageFuel w.2)) := by
    exact (Nat.Partrec.Code.primrec_evaln.comp
      ((hfuel.pair hcodeA).pair hi)).of_eq fun _ => rfl
  have hanswerB : Primrec (fun w : W =>
      sumStageAnswerB w.1 (sumStageRight w.2) (sumStageFuel w.2)) := by
    exact (Nat.Partrec.Code.primrec_evaln.comp
      ((hfuel.pair hcodeB).pair hj)).of_eq fun _ => rfl

  have htrueA : PrimrecPred (fun w : W =>
      sumStageAnswerA w.1 (sumStageLeft w.2) (sumStageFuel w.2) =
        some (Encodable.encode true)) :=
    Primrec.eq.comp hanswerA (Primrec.const (some (Encodable.encode true)))
  have htrueB : PrimrecPred (fun w : W =>
      sumStageAnswerB w.1 (sumStageRight w.2) (sumStageFuel w.2) =
        some (Encodable.encode true)) :=
    Primrec.eq.comp hanswerB (Primrec.const (some (Encodable.encode true)))
  have hfalseA : PrimrecPred (fun w : W =>
      sumStageAnswerA w.1 (sumStageLeft w.2) (sumStageFuel w.2) =
        some (Encodable.encode false)) :=
    Primrec.eq.comp hanswerA (Primrec.const (some (Encodable.encode false)))
  have hfalseB : PrimrecPred (fun w : W =>
      sumStageAnswerB w.1 (sumStageRight w.2) (sumStageFuel w.2) =
        some (Encodable.encode false)) :=
    Primrec.eq.comp hanswerB (Primrec.const (some (Encodable.encode false)))
  have htrueCmp : PrimrecPred (fun w : W =>
      sumStageComparison w.1.2 (sumStageLeft w.2)
        (sumStageRight w.2) (sumStageMargin w.2) = some true) :=
    Primrec.eq.comp hcomparison (Primrec.const (some true))
  have hfalseCmp : PrimrecPred (fun w : W =>
      sumStageComparison w.1.2 (sumStageLeft w.2)
        (sumStageRight w.2) (sumStageMargin w.2) = some false) :=
    Primrec.eq.comp hcomparison (Primrec.const (some false))

  have hinside : PrimrecPred (fun w : W => sumStageInterior w) :=
    ((htrueA.and htrueB).and htrueCmp).of_eq fun _ => by
      simp only [sumStageInterior, and_assoc]
  have houtside : PrimrecPred (fun w : W => sumStageExterior w) :=
    ((hfalseA.and hfalseB).and hfalseCmp).of_eq fun _ => by
      simp only [sumStageExterior, and_assoc]

  exact (Primrec.ite hinside (Primrec.const (some true))
      (Primrec.ite houtside (Primrec.const (some false))
        (Primrec.const none))).of_eq fun _ => rfl

end Continuo.Indices
