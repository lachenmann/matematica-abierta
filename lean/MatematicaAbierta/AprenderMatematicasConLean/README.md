# Aprender matemáticas con Lean (MCL)

Subbiblioteca educativa de la biblioteca formal de **Matemática Abierta**.

## Principio rector

> La matemática es el objeto de aprendizaje; Lean es el laboratorio.

MCL enseña matemática y Lean simultáneamente. Las construcciones de Lean se introducen cuando una necesidad matemática las vuelve pertinentes; el proyecto no presupone un curso preliminar separado de Lean.

## Fuente humana y fuente ejecutable

La documentación pedagógica canónica vive en la bóveda de Obsidian:

`Matemática/Matemática Abierta/Aprender matemáticas con Lean/`

El código ejecutable vive aquí:

`lean/MatematicaAbierta/AprenderMatematicasConLean/`

Cada lección humana debe indicar su módulo Lean correspondiente, y cada módulo Lean debe conservar en sus docstrings los identificadores MCL pertinentes.

## Organización inicial

- `M00.lean` — agregador de **MCL-M00 · Aprender a demostrar**.
- `M00/Leccion01.lean` — **MCL-M00-L01 · ¿Qué significa demostrar?**

La ampliación prevista continúa con `M01` (números naturales) y el tramo inicial de `M03` (álgebra elemental).

## Reglas técnicas

- Se usa el proyecto Lake existente de Matemática Abierta; MCL no mantiene un segundo entorno Lean.
- Las versiones de Lean y Mathlib son las fijadas por `lean/lean-toolchain` y `lean/lakefile.toml`.
- `autoImplicit = false`.
- No se admiten `sorry` ni `admit` en módulos publicados.
- La automatización no debe ocultar una idea matemática que todavía sea objeto de aprendizaje.
- Cada módulo publicado debe quedar importado, directa o indirectamente, por `MatematicaAbierta.lean` para entrar en CI.
