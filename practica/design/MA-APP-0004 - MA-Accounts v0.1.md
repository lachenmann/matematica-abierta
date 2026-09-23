---
title: "MA-APP-0004 — MA-Accounts v0.1"
id: MA-APP-0004-ACCOUNTS-v0.1
project: MA-Práctica
content-type: implementation-specification
status: canonical
version: 0.1
date: 2026-09-23
parent-specification: "MA-APP-0004 - MA-Práctica.md"
roadmap: "MA-APP-0004 - Roadmap v0.2.md"
implementation-status: in-development
---

# MA-APP-0004 — MA-Accounts v0.1

## 1. Objetivo

Introducir persistencia opcional del progreso de MA-Práctica sin convertir la cuenta en requisito de uso. El modo local actual debe seguir funcionando íntegramente cuando el usuario no quiera sincronizar o cuando el backend no esté disponible.

Estados de identidad admitidos:

1. **Local:** progreso solo en `localStorage`; sin identidad remota.
2. **Anónimo sincronizado:** identidad Supabase anónima con `user_id` estable mientras la sesión sea recuperable; progreso sincronizado entre recargas del mismo entorno.
3. **Cuenta recuperable:** la identidad existente se vincula a correo mediante Magic Link/OTP, conservando el mismo `user_id`, ratings e historial.

No se requieren nombre real, alias público, fecha de nacimiento, avatar ni perfil social.

## 2. Principios

- **Local-first:** el entrenamiento no depende de autenticación ni de red.
- **Cuenta opcional:** nunca bloquear la práctica detrás de un formulario de registro.
- **Servidor canónico para Elo sincronizado:** cuando existe identidad remota, el backend decide si un ejercicio todavía puede puntuar y persiste el movimiento Elo de forma atómica.
- **Sin ranking público:** el Elo es personal y experimental.
- **Compatibilidad:** `progress.mjs`, la política `first-attempt-v03` y los ejercicios existentes no se recalculan ni cambian por introducir cuentas.
- **Importación explícita:** el progreso local solo se incorpora a una identidad remota mediante una acción visible del usuario.
- **Degradación segura:** si falla Supabase, la sesión puede continuar localmente sin perder el ejercicio en curso.

## 3. Contrato de persistencia

La aplicación debe consumir una interfaz abstracta de almacenamiento en lugar de acoplarse directamente a `localStorage`.

Contrato local mínimo:

- `load()` → estado normalizado;
- `save(progress)` → persistencia local;
- `clear()` → borrado local;
- `kind` → `local`;
- `isAvailable()` → disponibilidad del adaptador.

El adaptador remoto **no acepta sobrescrituras arbitrarias del Elo**. `AccountProgressStore` expone operaciones orientadas a eventos: `load()`, `recordRatedExercise(...)`, `saveSession(record)`, `importLocal(snapshot)` y `clearHistory()`. El movimiento Elo remoto se efectúa únicamente mediante RPC atómica; el cliente no puede escribir directamente `user_ratings` ni `rated_exercises`.

Adaptadores implementados/preparados:

- `LocalProgressStore`: encapsula el comportamiento actual de `localStorage`;
- `AccountProgressStore`: reconstruye progreso remoto, registra eventos Elo por RPC, guarda sesiones e importa progreso local una única vez;
- durante la transición, `app.mjs` continúa usando solo el adaptador local para no activar tráfico remoto antes de configurar y validar Supabase.

## 4. Esquema remoto v0.1

### `user_ratings`

Una fila por `user_id + area` con rating actual y marca temporal.

### `rated_exercises`

Registro inmutable de cada ejercicio que produjo movimiento Elo. Restricción única `(user_id, exercise_id)` para impedir doble puntuación entre dispositivos. Campos mínimos: área, dificultad usada, resultado binario, rating anterior/posterior, delta, política y fecha.

### `practice_sessions`

Historial sincronizable de sesiones, puntuadas o no, almacenado como datos estructurados compatibles con `normalizeProgress`. El historial remoto no autoriza a recalcular Elo histórico.

## 5. Autoridad Elo

Para una identidad remota, la actualización Elo debe ejecutarse transaccionalmente en PostgreSQL mediante una función/RPC. La función:

1. comprueba si `(user_id, exercise_id)` ya existe;
2. obtiene o crea el rating por área con valor inicial 1200;
3. calcula el movimiento con K=24 y dificultad del ejercicio suministrada por el banco;
4. inserta el evento puntuado;
5. actualiza `user_ratings`;
6. devuelve `rating_before`, `rating_after`, `delta` y si el evento fue nuevo.

La base de datos impide duplicados aun si dos dispositivos intentan puntuar el mismo ejercicio simultáneamente.

## 6. RLS y privacidad

Todas las tablas de usuario deben habilitar Row Level Security. Las políticas solo permiten leer o escribir filas cuyo `user_id = auth.uid()`.

La clave `service_role` nunca se expone al navegador. El cliente usa únicamente credenciales públicas apropiadas para Supabase y sesión autenticada/anónima. La eliminación administrativa de una identidad, si se incorpora, debe ejecutarse del lado servidor.

El aviso de privacidad de la aplicación deberá actualizarse antes de publicar cuentas: el modo local no transmite progreso; el modo sincronizado sí envía al backend identificadores técnicos, sesiones y progreso matemático necesarios para la función solicitada.

## 7. Migración desde el MVP local

- No migrar silenciosamente.
- Al activar sincronización por primera vez, ofrecer **«Importar progreso de este navegador»**.
- Si la cuenta remota está vacía, importar ratings, IDs puntuados e historial compatible.
- Si ya existe progreso remoto, no fusionar ratings aritméticamente. Resolver mediante reglas explícitas antes de activar importación bidireccional.
- Nunca volver a puntuar ejercicios históricos durante una importación.

## 8. Fases de implementación

### A. Capa de persistencia

Refactorizar el acceso local detrás de `LocalProgressStore`, con regresión que demuestre equivalencia funcional con el MVP.

### B. Esquema Supabase

Crear migración SQL con tablas, índices, RLS y función atómica de Elo. No ejecutar contra producción hasta que exista proyecto conectado y revisión del SQL.

### C. Adaptador de cuenta

`AccountProgressStore` y las funciones de autenticación ya están implementados contra una interfaz Supabase inyectada y cubiertos con dobles de prueba. La autenticación prevista usa `signInAnonymously()`; la vinculación de correo conserva la identidad mediante `updateUser({ email })`, sujeta a la verificación/configuración de Supabase. Falta conectar un proyecto real y ejecutar pruebas de integración.

### D. Interfaz

Añadir un control discreto `Guardar mi progreso` / `Mi cuenta`. El registro nunca debe interrumpir un ejercicio.

### E. Migración y QA

Probar cuenta nueva, importación local, segundo dispositivo, repetición del mismo ejercicio, cierre de sesión, pérdida de red, recuperación, borrado y RLS.

## 9. Criterios de aceptación

MA-Accounts v0.1 se considera implementado cuando:

- el modo local conserva exactamente su comportamiento actual;
- una identidad anónima puede persistir rating e historial en el backend;
- esa identidad puede vincularse a correo sin cambiar de `user_id`;
- un ejercicio puntuado no puede modificar Elo dos veces para el mismo usuario, incluso desde dos clientes;
- un usuario no puede leer ni modificar progreso ajeno bajo RLS;
- importar progreso local no recalcula Elo histórico;
- una caída de backend no impide continuar en modo local;
- pruebas automatizadas cubren contrato de persistencia y SQL crítico;
- no se anuncia la función públicamente antes de QA y autorización de integración.

## 10. Estado de implementación

**Inicio:** 23-09-2026.

La abstracción local, `AccountProgressStore`, autenticación anónima/vinculación de correo, snapshot de importación y migraciones SQL/RLS están implementados. El proyecto remoto `ma-practica-dev` ya recibió `accounts_v01` y `accounts_rpc_hardening`. La prueba de base de datos con dos identidades autenticadas simuladas pasó: aislamiento RLS, bloqueo de doble puntuación, importación única y rechazo de escritura cruzada. Queda pendiente la prueba de Auth real con dos `signInAnonymously()` desde cliente y, después, la integración controlada del botón «Guardar mi progreso».


## 11. Ubicación canónica

MA-Accounts se implementa íntegramente dentro de `D:\\MA-Practica\practica`. Esta especificación vive en `practica/design/`; SQL, adaptadores y pruebas viven junto al código. Obsidian/Drive no es fuente de implementación para esta fase.


## 12. QA remoto de desarrollo

El 23-09-2026 se verificó en `ma-practica-dev` que:

- las tres tablas tienen RLS activo;
- `anon` y `PUBLIC` no pueden ejecutar las RPC de Elo/importación;
- `authenticated` sí puede ejecutarlas;
- un ejercicio puntúa una sola vez por usuario;
- dos usuarios distintos pueden puntuar el mismo ejercicio de forma independiente;
- un usuario no ve filas del otro bajo RLS;
- una escritura cruzada de `practice_sessions` es rechazada;
- la importación local solo se admite sobre un remoto vacío;
- los datos de prueba fueron eliminados al finalizar.

La regresión reproducible vive en `practica/supabase/tests/0001_accounts_rls.sql`. La prueba de Auth real vive en `practica/supabase/tests/accounts-live-auth.ps1` y requiere URL de proyecto + clave publicable como parámetros locales; ninguna clave se versiona en Git.
