param([int]$QwenProcessId)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if ($QwenProcessId) { Wait-Process -Id $QwenProcessId -ErrorAction SilentlyContinue }
foreach ($name in @('qwen06_Ryan.wav','qwen06_Aiden.wav')) {
    if (-not (Test-Path "raw/$name")) { throw "No se completó $name" }
}
& .venv/Scripts/python.exe -u generate.py design *> design.log
if ($LASTEXITCODE) { throw 'Falló la prueba VoiceDesign; revisar design.log' }
& .venv/Scripts/python.exe normalize.py *> normalize.log
if ($LASTEXITCODE) { throw 'Falló la normalización' }
& .venv/Scripts/python.exe -u asr.py *> asr.log
if ($LASTEXITCODE) { throw 'Falló ASR' }
& .venv/Scripts/python.exe audio_checks.py *> audio_checks.log
if ($LASTEXITCODE) { throw 'Falló comprobación de audio' }
& .venv/Scripts/python.exe inventory.py
& .venv/Scripts/python.exe verify_models.py
& .venv/Scripts/python.exe check_protection.py
& .venv/Scripts/python.exe report.py
