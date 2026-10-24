$ErrorActionPreference='Stop'
Set-Location $PSScriptRoot
& .venv/Scripts/python.exe -u synthesize.py clone *> clone_batched.log
if ($LASTEXITCODE) { throw 'Falló síntesis Base; revisar clone_batched.log' }
& .venv/Scripts/python.exe -u synthesize.py direct *> direct.log
if ($LASTEXITCODE) { throw 'Falló síntesis VoiceDesign; revisar direct.log' }
