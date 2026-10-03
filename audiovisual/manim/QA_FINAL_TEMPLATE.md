# <VIDEO-ID> — Auditoría audiovisual final

Fecha: <AAAA-MM-DD>  
Rama: `<rama>`

## Alcance

- Master: `exports/<VIDEO-ID>-production.mp4`
- Fuente: `clases/<fuente-production.py>`
- Protocolo: `AUDIOVISUAL_PRODUCTION_PROTOCOL.md`
- Renders iterativos: <n>

## Hallazgos y correcciones

| Severidad | Tramo | Problema | Corrección |
|---|---|---|---|
| | | | |

## Tiempos fijos del autor

| Tiempo | Acción |
|---|---|
| | |

## Insumos protegidos

- WAV SHA-256: `<hash>`
- Proyecto de voz SHA-256: `<hash>`

## Validación final

- BLOCKER abiertos: 0
- MAJOR abiertos: 0
- MINOR abiertos: <n>
- COSMETIC abiertos: <n>

### Inspección

- Pasada cronológica: <método>
- Secuencias críticas: <método>
- Resolución completa: <sí/no>
- Cues fijos comprobados: <sí/no>

### Validación técnica

- `py_compile`: <PASS/FAIL>
- `git diff --check`: <PASS/FAIL>
- layout verifier: <PASS/NA>
- `SYNC WARN`: <0/observaciones>
- voz preservada: <sí/no>
- deriva de audio: <resultado>

## Master final

- Duración: <hh:mm:ss>
- Resolución: 1920×1080
- FPS: 60
- SHA-256: `<hash>`
- Ruta: `exports/<VIDEO-ID>-production.mp4`

## Evidencia local

`exports/<directorio-auditoria>/`

## Cierre

`PRODUCTION_READY` sólo si BLOCKER = 0 y MAJOR = 0.
