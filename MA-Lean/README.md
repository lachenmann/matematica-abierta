# MA-Lean

Controlador de formalización y auditoría de Matemática Abierta.

## Genealogía

El motor histórico alcanzó al menos **v0.4.0** en el workspace local `D:\\MA-Lean`, con:

- `ma_lean.py`;
- `engine/inventory.py`;
- `engine/subsets.py`;
- `engine/empty.py`;
- pruebas unitarias;
- inventario por IDs;
- huellas SHA-256;
- integración controlada;
- compilación explícita;
- `#check` y `#print axioms`;
- separación entre verificación Lean y revisión semántica.

Este directorio inicia la migración estable al repositorio de Matemática Abierta. **No se debe interpretar como una reimplementación desde cero ni como sustitución silenciosa del motor histórico.**

## Integración MCL

`Aprender matemáticas con Lean` añade un perfil y un adaptador pedagógico:

- `profiles/mcl.json`
- `adapters/mcl.py`
- `mapeos/MCL/`

MCL usa la biblioteca formal única:

`lean/MatematicaAbierta`

No crea otro proyecto Lake.

El primer piloto es `MCL-U00-L01`.
