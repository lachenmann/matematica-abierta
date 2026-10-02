$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

Write-Host "Render local: CPM-YT-C01-V01" -ForegroundColor Cyan
Write-Host "Manim Community + LaTeX. Fondo oscuro. Sin audio." -ForegroundColor DarkGray

uv run manim -pql --disable_caching ".\clases\cpm_yt_c01_v01_preview.py" CPMYTC01V01Preview

if ($LASTEXITCODE -ne 0) {
    throw "El render local de Manim terminó con código $LASTEXITCODE."
}
