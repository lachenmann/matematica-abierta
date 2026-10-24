param([switch]$RenderDemo)
$ErrorActionPreference='Stop'
Set-Location $PSScriptRoot
if (-not (Test-Path .venv/Scripts/python.exe)) { uv venv .venv --python 3.11.16 }
uv pip install --python .venv/Scripts/python.exe --require-hashes -r requirements-hashes.txt
if ($LASTEXITCODE) { throw 'Falló instalación aislada' }
& .venv/Scripts/python.exe prepare.py
if ($LASTEXITCODE) { throw 'Falló preparación' }
& ./run_voice.ps1
& ./postprocess.ps1
& .venv/Scripts/python.exe audio_qa.py
if ($RenderDemo) {
    & ./render_demo.ps1
    & .venv/Scripts/python.exe inspect_video.py
    & .venv/Scripts/python.exe full_sheets.py
}
& .venv/Scripts/python.exe report.py
& .venv/Scripts/python.exe qa_final.py
& .venv/Scripts/python.exe package.py
