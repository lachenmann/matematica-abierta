import MatematicaAbierta.Continuo.EtapasUniformes

/-!
# FDC-AUD-025-M04b — Etapa finita de certificados de suma

Esta fuente define una etapa concreta, finita, sin llamadas a oráculos ideales,
para dos códigos de decididores de cortes y una consulta racional codificada.
La búsqueda enumera también una cota finita de `evaln`, nunca pasos de máquina.

La corrección semántica, la primitividad recursiva de la etapa completa y la
terminación bajo promesa de suma irracional se separan para pruebas posteriores.
Este módulo NO acredita P025a y no altera los contratos O5/O6.
-/

namespace Continuo.Indices

/-- Primer nombre racional candidato en la etapa enumerada. -/
def sumStageLeft (n : ℕ) : ℕ := n.unpair.1

/-- Segundo nombre racional candidato. -/
def sumStageRight (n : ℕ) : ℕ := n.unpair.2.unpair.1

/-- Denominador positivo del margen racional estricto. -/
def sumStageMargin (n : ℕ) : ℕ := n.unpair.2.unpair.2.unpair.1 + 1

/-- Cota positiva del evaluador de programas. No es número de pasos. -/
def sumStageFuel (n : ℕ) : ℕ := n.unpair.2.unpair.2.unpair.2 + 1

/-- Toda cuaterna de parámetros aparece en alguna etapa. -/
theorem sumStageParameters_surjective (i j t k : ℕ) :
    let n := Nat.pair i (Nat.pair j (Nat.pair t k))
    sumStageLeft n = i ∧
    sumStageRight n = j ∧
    sumStageMargin n = t + 1 ∧
    sumStageFuel n = k + 1 := by
  simp [sumStageLeft, sumStageRight, sumStageMargin, sumStageFuel,
    Nat.unpair_pair]

/-- Numerador positivo de la suma de dos consultas racionales codificadas. -/
def sumStagePositive (i j : ℕ) : ℕ :=
  queryPositive i * queryDenominator j +
    queryPositive j * queryDenominator i

/-- Numerador negativo de la misma suma racional. -/
def sumStageNegative (i j : ℕ) : ℕ :=
  queryNegative i * queryDenominator j +
    queryNegative j * queryDenominator i

/-- Denominador positivo de la suma racional. -/
def sumStageDenominator (i j : ℕ) : ℕ :=
  queryDenominator i * queryDenominator j

/-- Comparación estricta de la consulta con la suma de dos testigos,
dejando un margen positivo `1/t` para certificar separación. -/
def sumStageComparison (z i j t : ℕ) : Option Bool :=
  arithmeticStage (queryPositive z) (queryNegative z)
    (queryDenominator z) (sumStagePositive i j)
    (sumStageNegative i j) (sumStageDenominator i j) t

/-- Consulta finita a ambos programas con la cota indicada. -/
def sumStageAnswerA (p : (Code × Code) × ℕ) (i fuel : ℕ) : Option ℕ :=
  Nat.Partrec.Code.evaln fuel p.1.1 i

def sumStageAnswerB (p : (Code × Code) × ℕ) (j fuel : ℕ) : Option ℕ :=
  Nat.Partrec.Code.evaln fuel p.1.2 j

/-- Certificado interior: dos respuestas afirmativas efectivamente observadas
y desigualdad estricta entre la consulta y la suma de testigos. -/
def sumStageInterior (w : ((Code × Code) × ℕ) × ℕ) : Prop :=
  sumStageAnswerA w.1 (sumStageLeft w.2) (sumStageFuel w.2) =
      some (Encodable.encode true) ∧
    sumStageAnswerB w.1 (sumStageRight w.2) (sumStageFuel w.2) =
      some (Encodable.encode true) ∧
    sumStageComparison w.1.2 (sumStageLeft w.2)
      (sumStageRight w.2) (sumStageMargin w.2) = some true

/-- Certificado exterior estricto: ambos testigos fuera de sus cortes y
separación racional estricta en la dirección opuesta. -/
def sumStageExterior (w : ((Code × Code) × ℕ) × ℕ) : Prop :=
  sumStageAnswerA w.1 (sumStageLeft w.2) (sumStageFuel w.2) =
      some (Encodable.encode false) ∧
    sumStageAnswerB w.1 (sumStageRight w.2) (sumStageFuel w.2) =
      some (Encodable.encode false) ∧
    sumStageComparison w.1.2 (sumStageLeft w.2)
      (sumStageRight w.2) (sumStageMargin w.2) = some false

/-- Etapa ejecutable por decisiones finitas. La evaluación acotada puede
devolver `none`; ello no se interpreta como decisión negativa del corte. -/
def sumCertificateStage (w : ((Code × Code) × ℕ) × ℕ) : Option Bool :=
  if sumStageInterior w then some true
  else if sumStageExterior w then some false
  else none

/-- Una respuesta positiva expone explícitamente los tres certificados. -/
theorem sumCertificateStage_true_iff (w : ((Code × Code) × ℕ) × ℕ) :
    sumCertificateStage w = some true ↔ sumStageInterior w := by
  by_cases h : sumStageInterior w <;>
    simp [sumCertificateStage, h]

/-- Una respuesta negativa nunca procede de la mera ausencia de respuesta. -/
theorem sumCertificateStage_false_sound (w : ((Code × Code) × ℕ) × ℕ)
    (h : sumCertificateStage w = some false) :
    sumStageExterior w := by
  by_cases hi : sumStageInterior w
  · simp [sumCertificateStage, hi] at h
  · by_cases he : sumStageExterior w
    · exact he
    · simp [sumCertificateStage, hi, he] at h

/-- La función por etapas está definida por cálculos finitos incluso cuando
los programas iniciales no terminan; la ejecución parcial no se invoca aquí. -/
theorem sumCertificateStage_total (w : ((Code × Code) × ℕ) × ℕ) :
    ∃ answer : Option Bool, sumCertificateStage w = answer :=
  ⟨sumCertificateStage w, rfl⟩

end Continuo.Indices
