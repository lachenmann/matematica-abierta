# Biblioteca formal de Matemática Abierta

Proyecto Lean independiente de Quarto, alojado en `lean/`. La web no importa ni publica estos archivos automáticamente.

## Versiones

- Lean: `v4.34.0` (archivo `lean-toolchain`).
- Mathlib: etiqueta `v4.34.0` (archivo `lakefile.toml`).

## Entorno en la nube (GitHub Codespaces)

Desde el repositorio, abre **Code → Codespaces → Create codespace**. La configuración `.devcontainer/` prepara Elan, Lean, Mathlib, la extensión Lean 4 de VS Code y ejecuta la compilación inicial. En la terminal del Codespace:

```bash
cd lean
lake build
```

Si el Codespace ya está abierto y cambia la configuración, reconstruye el contenedor. Codespaces puede generar costes según la cuota y el tipo de máquina de tu cuenta; verifica sus condiciones antes de crearlo.

## Entorno local (Mac)

En una copia actualizada de este repositorio:

```bash
cd lean
lake update
lake exe cache get
lake build
```

`lake update` genera o actualiza `lean/lake-manifest.json`. Cuando quede resuelto, conviene incorporarlo al repositorio para fijar también las dependencias transitivas; **no** se considera bloqueado hasta entonces. No incorporar `lean/.lake/`, que contiene descargas y archivos generados.

## Organización y publicación

- Escribe demostraciones terminadas en `MatematicaAbierta/<Area>.lean`.
- Importa cada módulo desde `MatematicaAbierta.lean`; lo que no esté importado no forma parte del objetivo de compilación.
- No se admiten `sorry` ni `admit` en los módulos publicados. La comprobación automática rechaza estas marcas y compila la biblioteca con Lean.
- `lean.yml` se ejecuta en solicitudes de incorporación a `main`, tras cambios relevantes en `main`, o manualmente desde Actions. No reemplaza las pruebas editoriales ni el flujo de publicación de Quarto.

Las demostraciones actuales constituyen únicamente una prueba de instalación; no se ha formalizado todavía ninguno de los tratados.
