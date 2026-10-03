import Mathlib

/-!
# MCL-U00-L01 — Qué es una proposición

Objetivo matemático:
reconocer una proposición como una afirmación que puede ser demostrada
y comenzar a leer el estado de prueba de Lean.

Estado pedagógico: DRAFT

Documento humano:
Obsidian/Vault/Matemática/Matemática Abierta/Aprender matemáticas con Lean/
-/

namespace MCL.U00.L01

/-- MCL-U00-L01-E01:
Una primera proposición verdadera cuya prueba es reflexiva. -/
theorem dos_es_dos : (2 : ℕ) = 2 := by
  rfl

/-- MCL-U00-L01-E02:
Si suponemos una proposición `P`, entonces podemos demostrar `P`. -/
theorem usar_hipotesis (P : Prop) (h : P) : P := by
  exact h

/-- MCL-U00-L01-E03:
Una proposición implica a sí misma. -/
theorem identidad_logica (P : Prop) : P → P := by
  intro h
  exact h

end MCL.U00.L01
