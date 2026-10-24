$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not (Test-Path .venv/Scripts/python.exe)) { uv venv .venv --python 3.11.16 }
uv pip install --python .venv/Scripts/python.exe --require-hashes -r requirements-hashes.txt
if ($LASTEXITCODE) { throw 'Falló la instalación aislada' }
& .venv/Scripts/python.exe prepare.py
if ($LASTEXITCODE) { throw 'Falló la preparación' }
& .venv/Scripts/python.exe generate.py supertonic
if ($LASTEXITCODE) { throw 'Falló Supertonic' }
& .venv/Scripts/python.exe generate.py qwen
if ($LASTEXITCODE) { throw 'Falló Qwen' }
# VoiceDesign is optional. Run separately after checking available RAM:
# & .venv/Scripts/python.exe download_design.py
# & .venv/Scripts/python.exe generate.py design
& .venv/Scripts/python.exe normalize.py
if ($LASTEXITCODE) { throw 'Falló normalización' }
& .venv/Scripts/python.exe asr.py
if ($LASTEXITCODE) { throw 'Falló ASR' }
& .venv/Scripts/python.exe inventory.py
if ($LASTEXITCODE) { throw 'Falló inventario' }
& .venv/Scripts/python.exe verify_models.py
if ($LASTEXITCODE) { throw 'Falló verificación de modelos' }
& .venv/Scripts/python.exe audio_checks.py
if ($LASTEXITCODE) { throw 'Falló comprobación de audio' }
& .venv/Scripts/python.exe check_protection.py
if ($LASTEXITCODE) { throw 'Cambió un original protegido' }
& .venv/Scripts/python.exe report.py
& .venv/Scripts/python.exe reading_notes.py
if ($LASTEXITCODE) { throw 'Falló QA' }
& .venv/Scripts/python.exe package_results.py
