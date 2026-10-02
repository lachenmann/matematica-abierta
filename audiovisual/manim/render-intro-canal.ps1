$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

Write-Host "Render: IntroCanal — Matemática Abierta" -ForegroundColor Cyan
Write-Host "1920x1080 · 60 fps · Manim Community" -ForegroundColor DarkGray

$env:PYTHONPATH = "$Root\escenas\comunes"

uv run manim -p -r 1920,1080 --fps 60 --disable_caching `
  ".\escenas\comunes\intro_canal.py" IntroCanal

if ($LASTEXITCODE -ne 0) {
    throw "El render de IntroCanal terminó con código $LASTEXITCODE."
}
