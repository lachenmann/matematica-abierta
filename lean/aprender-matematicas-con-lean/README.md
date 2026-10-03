# Aprender matemáticas con Lean

Código rector: `MCL`.

Este directorio contiene la **fuente de verdad ejecutable** del proyecto de Matemática Abierta **Aprender matemáticas con Lean**.

Principio rector:

> La matemática es el objeto de aprendizaje; Lean es el laboratorio.

La documentación pedagógica y editorial canónica vive en la bóveda Obsidian:

`Obsidian/Vault/Matemática/Matemática Abierta/Aprender matemáticas con Lean/`

## Toolchain

- Lean 4.34.1
- Mathlib 4.34.1

## Compilación

```bash
cd lean/aprender-matematicas-con-lean
lake update
lake exe cache get
lake build
```

## Convención de IDs

- unidad: `MCL-U00`
- lección: `MCL-U00-L01`
- ejercicio: `MCL-U00-L01-E01`

Los IDs son compartidos por Obsidian, Lean y las futuras superficies web/juego.

## Estado inicial

- `MCL-U00-L01` — Qué es una proposición.
- `MCL-U00-L02` — Igualdad: primera demostración.

Estado del proyecto: `MCL-v0.1.0 — CANONIZED / INFRASTRUCTURE INITIALIZED`.
