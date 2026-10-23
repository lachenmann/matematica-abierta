param([ValidateSet('media','alta')][string]$Calidad='alta',[switch]$SoloVoz)
$ErrorActionPreference='Stop'
Set-Location $PSScriptRoot
$env:PYTHONUTF8='1'
$LocalReady=(Test-Path 'models/kokoro-v1.0.onnx') -and (Test-Path 'models/voices-v1.0.bin')
$SharedReady=(Test-Path '../MA_Video_Kokoro_v02/models/kokoro-v1.0.onnx') -and (Test-Path '../MA_Video_Kokoro_v02/models/voices-v1.0.bin')
if (-not ($LocalReady -or $SharedReady)) { & ./setup-kokoro.ps1 }
$Params=@('run','--locked','python','produccion.py','--calidad',$Calidad)
if ($SoloVoz) { $Params+='--solo-voz' }
& uv @Params
if ($LASTEXITCODE -ne 0) { throw 'Falló la producción.' }
