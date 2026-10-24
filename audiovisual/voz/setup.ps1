param([switch]$DownloadModel)
$ErrorActionPreference = 'Stop'
$venv = Join-Path $PSScriptRoot '.venv'
$python = Join-Path $venv 'Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) {
    uv venv --python 3.11.16 $venv
    if ($LASTEXITCODE -ne 0) { throw 'No se pudo crear el entorno de voz' }
    uv pip sync --python $python --torch-backend cpu (Join-Path $PSScriptRoot 'perfiles\MA-VOICE-v1.0\requirements-original.txt')
    if ($LASTEXITCODE -ne 0) { throw 'No se pudieron instalar las dependencias fijadas' }
}
if ($DownloadModel) {
    & $python (Join-Path $PSScriptRoot 'download_model.py')
    if ($LASTEXITCODE -ne 0) { throw 'Descarga/verificación falló' }
}
& (Join-Path $PSScriptRoot 'narrar.ps1') -Python $python -Command verify
