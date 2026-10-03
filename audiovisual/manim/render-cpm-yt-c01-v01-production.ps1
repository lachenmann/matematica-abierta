$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

$VoiceRoot = Join-Path $Root "cpm_yt_c01_v01\voice-reference"
$Audio = Join-Path $VoiceRoot "audio\CPM-YT-C01-V01-reference.wav"
$Rpp = Join-Path $VoiceRoot "CPM-YT-C01-V01-reference.rpp"

if (-not (Test-Path $Audio)) {
    throw "Falta el WAV de referencia: $Audio"
}
if (-not (Test-Path $Rpp)) {
    throw "Falta el proyecto Reaper: $Rpp"
}

Write-Host "Preparando cortina musical de IntroCanal..." -ForegroundColor Cyan
& ".\prepare-intro-music.ps1" -Force

if ($LASTEXITCODE -ne 0) {
    throw "La preparacion de la cortina musical termino con codigo $LASTEXITCODE."
}

Write-Host "Analizando marcadores Reaper..." -ForegroundColor Cyan
uv run python ".\cpm_yt_c01_v01\analyze_voice_reference.py"

if ($LASTEXITCODE -ne 0) {
    throw "El analisis de voz termino con codigo $LASTEXITCODE."
}

Write-Host "Render integrado: CPM-YT-C01-V01" -ForegroundColor Cyan
Write-Host "1920x1080 - 60 fps - voz Reaper - intro canonica 7 s + voz desde 7.00 s" -ForegroundColor DarkGray

uv run manim -p -r 1920,1080 --fps 60 --disable_caching `
  ".\clases\cpm_yt_c01_v01_production.py" CPMYTC01V01Production

if ($LASTEXITCODE -ne 0) {
    throw "El render integrado termino con codigo $LASTEXITCODE."
}
