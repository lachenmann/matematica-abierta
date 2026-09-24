# ADR-0001 — Entorno local de desarrollo en D:\MA-Practica

- **Fecha:** 2026-09-22
- **Estado:** aceptada como decisión de arquitectura; configuración física del equipo pendiente de ejecutar por el usuario.
- **Ámbito:** organización local del código y separación de fuentes; no modifica contenido matemático ni el sitio publicado.

## Contexto

MA-Práctica tiene especificación pedagógica y contenido matemático canónicos en Obsidian/Google Drive (MA-APP-0004); el código ya vive en el repositorio `lachenmann/matematica-abierta`, subdirectorio `practica/`. Desarrollar dentro de la bóveda mezcla código y archivos derivados con los manuscritos y puede propagar recursos técnicos innecesarios mediante sincronización.

## Decisión

1. Usar `D:\MA-Practica` como **directorio local de trabajo y raíz de un clon completo** de `https://github.com/lachenmann/matematica-abierta.git`, sin crear un repositorio remoto adicional.
2. El código específico de la aplicación vive en `D:\MA-Practica\practica`; la raíz del clon conserva Quarto, workflows y demás archivos del sitio para verificar integración.
3. El trabajo inicial continúa en `feature/ma-practica-v0.1` y PR #168; no desarrollar sobre `main` ni `gh-pages` directamente.
4. Obsidian/Drive mantiene los enunciados matemáticos canónicos, soluciones revisadas, planificación pedagógica y `MA-APP-0004`; GitHub controla código, pruebas, ADR, issues y PR. Transferir contenido mediante exportación explícita y revisión, no mediante sincronización bidireccional de carpetas.
5. Archivos generados, cachés, entornos locales, credenciales y configuraciones privadas no se suben a Git ni se copian a la bóveda; respetar `.gitignore` y revisar `git status` antes de cada commit.
6. Esta ADR **no prueba ni presupone** que exista la unidad `D:` o la carpeta en el equipo del usuario. Verificar la ruta y posibles proyectos preexistentes antes de clonar: nunca ejecutar un comando destructivo ni sobrescribir un repositorio existente.

## Inicialización prevista (PowerShell, solo si la ruta aún no existe)

```powershell
Test-Path 'D:\MA-Practica'
git clone https://github.com/lachenmann/matematica-abierta.git D:\MA-Practica
Set-Location 'D:\MA-Practica'
git fetch origin
git switch --track origin/feature/ma-practica-v0.1
node --test practica/tests/engine.test.mjs
```

Ejecutar `git clone` **únicamente** cuando `Test-Path` devuelva `False`. Si devuelve `True`, inspeccionar qué contiene la carpeta y decidir sin sobrescribir nada. Si la rama ya existe localmente, utilizar `git switch feature/ma-practica-v0.1` en lugar de `--track`.

## Consecuencias y verificación

El clon contiene más que la aplicación, intencionalmente: permite pruebas integradas de Quarto. La carpeta física debe configurarse desde Windows; no puede crearse mediante un commit remoto. La decisión queda versionada con el proyecto y no implica que la app esté publicada, sea PWA ni que sus verificaciones pendientes estén satisfechas.
