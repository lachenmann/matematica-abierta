import Mathlib

/-!
# MCL-U00-L02 — Igualdad: primera demostración

Objetivo matemático:
distinguir entre una igualdad que es verdadera por definición y una igualdad
que requiere utilizar una hipótesis o un teorema.

Estado pedagógico: DRAFT

Documento humano:
Obsidian/Vault/Matemática/Matemática Abierta/Aprender matemáticas con Lean/
-/

namespace MCL.U00.L02

/-- MCL-U00-L02-E01:
La reflexividad de la igualdad. -/
theorem igualdad_reflexiva (n : ℕ) : n = n := by
  rfl

/-- MCL-U00-L02-E02:
Una igualdad dada como hipótesis puede usarse directamente. -/
theorem usar_igualdad (a b : ℕ) (h : a = b) : a = b := by
  exact h

/-- MCL-U00-L02-E03:
La simetría de la igualdad se expresa invirtiendo una hipótesis de igualdad. -/
theorem igualdad_simetrica (a b : ℕ) (h : a = b) : b = a := by
  exact h.symm

/-- MCL-U00-L02-E04:
La transitividad permite encadenar dos igualdades. -/
theorem igualdad_transitiva (a b c : ℕ) (hab : a = b) (hbc : b = c) : a = c := by
  exact hab.trans hbc

end MCL.U00.L02
