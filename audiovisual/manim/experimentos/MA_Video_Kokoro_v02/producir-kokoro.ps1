# Entrada recomendada, preserva Manim y demás dependencias del repositorio.
param(
  [ValidateSet('media','alta')][string] $Calidad = 'alta',
  [ValidateSet('em_alex','em_santa','ef_dora')][string] $Timbre = 'em_alex',
  [switch] $SoloVoz,
  [switch] $RegenerarVoz
)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) { throw 'Falta uv en PATH.' }
if (-not (Test-Path '.\models\kokoro-v1.0.onnx') -or
    -not (Test-Path '.\models\voices-v1.0.bin')) { .\setup-kokoro.ps1 }
$env:PYTHONUTF8 = '1'
if ($Timbre -ne 'em_alex') { throw 'La producción cerrada usa em_alex. Para experimentar con otras voces utiliza demo.py.' }
$Params = @('run','--locked',
            'python','produccion.py',
            '--calidad',$Calidad)
if ($SoloVoz) { $Params += '--solo-voz' }
if ($RegenerarVoz) { $Params += '--regenerar-voz' }
& uv @Params
if ($LASTEXITCODE -ne 0) { throw "Producción fallida (código $LASTEXITCODE)" }
