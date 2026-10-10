# Biblioteca formal de Matemática Abierta

Proyecto Lean independiente de Quarto, alojado en `lean/`. La web no importa ni publica estos archivos automáticamente.

## Versiones y reproducibilidad

- Lean: `v4.34.0` (`lean-toolchain`).
- Mathlib: etiqueta `v4.34.0` (`lakefile.toml`).
- Dependencias transitivas: revisiones concretas fijadas en `lake-manifest.json`, generado y comprobado en GitHub Actions. No ejecutes `lake update` en el trabajo ordinario: se reserva para actualizar deliberadamente las dependencias y revisar el cambio en una PR.

## Entorno en la nube (GitHub Codespaces)

Una vez incorporada esta configuración a `main`, abre el repositorio en GitHub y selecciona **Code → Codespaces → Create codespace on main**. El contenedor `.devcontainer/` instala Elan, Lean, Mathlib y la extensión Lean 4 de VS Code y realiza la compilación inicial. En la terminal del Codespace:

```bash
cd lean
lake build
```

Si necesitas probar los cambios antes de integrarlos, crea el Codespace específicamente sobre la rama `setup/lean4-cloud-ci`. Si modificas la configuración del contenedor, usa la opción de reconstrucción. Codespaces puede generar costes dependiendo de las cuotas y el tipo de máquina de tu cuenta.

## Entorno local (Mac)

En una copia actualizada de este repositorio:

```bash
cd lean
lake exe cache get
lake build
```

El manifest se descarga junto con el repositorio y fija todas las dependencias. No añadas `lean/.lake/` a Git: contiene paquetes descargados y archivos generados.

## Organización y comprobación

- Escribe demostraciones terminadas en `MatematicaAbierta/<Area>.lean`.
- Importa cada módulo desde `MatematicaAbierta.lean`; lo no importado no forma parte del objetivo de compilación.
- No se admiten marcadores `sorry` ni `admit` en los módulos publicados. CI busca dichos marcadores y compila con Lean. Esta búsqueda textual es una protección inicial, no una auditoría formal de axiomas.
- `.github/workflows/lean.yml` se ejecuta en PR hacia `main`, tras cambios relevantes en `main` o manualmente desde Actions. Es independiente de los procesos de Quarto.

La demostración actual es una prueba mínima de instalación; todavía no se han formalizado los tratados.
