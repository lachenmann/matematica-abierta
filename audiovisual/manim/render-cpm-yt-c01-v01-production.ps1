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

Write-Host "Comprobando sintaxis de producción..." -ForegroundColor Cyan
uv run python -m py_compile `
  ".\clases\cpm_yt_c01_v01_production.py" `
  ".\escenas\comunes\intro_canal.py" `
  ".\escenas\comunes\marca.py"

if ($LASTEXITCODE -ne 0) {
    throw "La comprobacion sintactica fallo con codigo $LASTEXITCODE."
}
Write-Host "Render integrado: CPM-YT-C01-V01" -ForegroundColor Cyan
Write-Host "1920x1080 - 60 fps - voz Reaper - intro canonica 7 s + voz desde 7.00 s" -ForegroundColor DarkGray

uv run manim -p -r 1920,1080 --fps 60 --disable_caching `
  ".\clases\cpm_yt_c01_v01_production.py" CPMYTC01V01Production

if ($LASTEXITCODE -ne 0) {
    throw "El render integrado termino con codigo $LASTEXITCODE."
}

$Rendered = Get-ChildItem (Join-Path $Root "media") -Recurse -File `
    -Filter "CPMYTC01V01Production.mp4" |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if (-not $Rendered) {
    throw "El render termino, pero no se encontro CPMYTC01V01Production.mp4."
}

$ExportDir = Join-Path $Root "exports"
$Export = Join-Path $ExportDir "CPM-YT-C01-V01-production.mp4"
New-Item -ItemType Directory -Force -Path $ExportDir | Out-Null
Copy-Item -LiteralPath $Rendered.FullName -Destination $Export -Force

$Hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $Export).Hash
$HashFile = "$Export.sha256"
"$Hash  CPM-YT-C01-V01-production.mp4" |
    Set-Content -LiteralPath $HashFile -Encoding ascii

Write-Host ""
Write-Host "Master de producción:" -ForegroundColor Green
Write-Host "  $Export"
Write-Host "SHA-256:" -ForegroundColor Green
Write-Host "  $Hash"
