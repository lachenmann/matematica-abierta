import Mathlib
import Mathlib.Computability.Halting

/-!
# FDC-AUD-023 — Simulación acotada de programas parciales

Primer tramo de O1. Se utiliza la semántica de códigos `Nat.Partrec.Code`
y el evaluador finito `evaln` de la revisión fijada de Mathlib.

IMPORTANTE: `evaln k` acota valores intermedios, no un número literal de pasos
de una máquina de Turing. La primera etapa exitosa se define respecto de `k`.

Este archivo NO demuestra todavía la cota de error del real de detención,
ni los teoremas T002b/T002f, ni la computabilidad de un transformador de índices.
-/

namespace Continuo.Indices

abbrev Code := Nat.Partrec.Code

/-- Entrada diagonal, codificada por la numeración efectiva de Mathlib. -/
def diagonal (c : Code) : ℕ := Nat.Partrec.Code.encodeCode c

/-- Evaluación finita que devuelve `none` cuando la cota resulta insuficiente. -/
def run (c : Code) (k : ℕ) : Option ℕ :=
  Nat.Partrec.Code.evaln k c (diagonal c)

/-- El evaluador de cota cero nunca produce una respuesta. -/
theorem run_zero (c : Code) : run c 0 = none := rfl

/-- La simulación finita nunca afirma una salida falsa. -/
theorem run_sound {c : Code} {k x : ℕ} (hx : x ∈ run c k) :
    x ∈ Nat.Partrec.Code.eval c (diagonal c) := by
  exact Nat.Partrec.Code.evaln_sound hx

/-- Una respuesta ya observada persiste al aumentar la cota de evaluación. -/
theorem run_mono {c : Code} {k l x : ℕ} (hkl : k ≤ l)
    (hx : x ∈ run c k) : x ∈ run c l := by
  exact Nat.Partrec.Code.evaln_mono hkl hx

/-- La ejecución semántica termina exactamente cuando alguna etapa finita da salida. -/
theorem halts_iff_exists_run (c : Code) :
    (∃ x : ℕ, x ∈ Nat.Partrec.Code.eval c (diagonal c)) ↔
      ∃ k x : ℕ, x ∈ run c k := by
  constructor
  · rintro ⟨x, hx⟩
    obtain ⟨k, hk⟩ := (Nat.Partrec.Code.evaln_complete).mp hx
    exact ⟨k, x, hk⟩
  · rintro ⟨k, x, hx⟩
    exact ⟨x, run_sound hx⟩

/-- Primera etapa exitosa estrictamente anterior a `N`, si existe. -/
def firstHit (c : Code) : ℕ → Option ℕ
  | 0 => none
  | N + 1 =>
      match firstHit c N with
      | some k => some k
      | none => if (run c N).isSome then some N else none

/-- Peso diádico racional asignado a una primera etapa exitosa. -/
def dyadic (k : ℕ) : ℚ := (1 : ℚ) / (2 : ℚ) ^ (k + 2)

/-- Aproximación racional finita, computada sin consultar la detención global. -/
def approximant (c : Code) (N : ℕ) : ℚ :=
  (firstHit c N).elim 0 dyadic

/-- La aproximación inicial es cero. -/
theorem approximant_zero (c : Code) : approximant c 0 = 0 := rfl

end Continuo.Indices
