$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

Write-Host "Preparando cortina musical de IntroCanal..." -ForegroundColor Cyan
& ".\prepare-intro-music.ps1" -Force

if ($LASTEXITCODE -ne 0) {
    throw "La preparacion de la cortina musical termino con codigo $LASTEXITCODE."
}

Write-Host "Render: IntroCanal + cortina oficial - Matematica Abierta" -ForegroundColor Cyan
Write-Host "1920x1080 - 60 fps - Manim Community" -ForegroundColor DarkGray

$env:PYTHONPATH = "$Root\escenas\comunes"

uv run manim -p -r 1920,1080 --fps 60 --disable_caching `
  ".\escenas\comunes\intro_canal.py" IntroCanalConMusica

if ($LASTEXITCODE -ne 0) {
    throw "El render de IntroCanal termino con codigo $LASTEXITCODE."
}
