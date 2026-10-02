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

Write-Host "Analizando marcadores Reaper..." -ForegroundColor Cyan
uv run python ".\cpm_yt_c01_v01\analyze_voice_reference.py"

if ($LASTEXITCODE -ne 0) {
    throw "El análisis de voz terminó con código $LASTEXITCODE."
}

Write-Host "Render sincronizado: CPM-YT-C01-V01" -ForegroundColor Cyan
Write-Host "Manim Community + audio Reaper + timing canónico." -ForegroundColor DarkGray

uv run manim -pql --disable_caching ".\clases\cpm_yt_c01_v01_production.py" CPMYTC01V01Production

if ($LASTEXITCODE -ne 0) {
    throw "El render sincronizado terminó con código $LASTEXITCODE."
}
