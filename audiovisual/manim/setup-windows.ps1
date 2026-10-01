$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
Set-Location $PSScriptRoot

function Resolve-Uv {
    $cmd = Get-Command uv -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }

    Write-Host "Instalando uv..."
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

    $candidate = Join-Path $HOME ".local\bin\uv.exe"
    if (Test-Path $candidate) { return $candidate }

    $cmd = Get-Command uv -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }

    throw "uv se instaló pero no está visible en esta sesión. Abre una nueva PowerShell y ejecuta de nuevo el script."
}

$uv = Resolve-Uv

if (-not (Get-Command xelatex -ErrorAction SilentlyContinue) -or
    -not (Get-Command dvisvgm -ErrorAction SilentlyContinue)) {
    Write-Host ""
    Write-Host "Falta MiKTeX o no está en PATH." -ForegroundColor Yellow
    Write-Host "Instálalo con:"
    Write-Host "  winget install -e --id MiKTeX.MiKTeX"
    Write-Host "Después abre una nueva PowerShell y vuelve a ejecutar este script."
    exit 3
}

& $uv python install 3.13.15
& $uv sync
& $uv run python verify_environment.py

Write-Host ""
Write-Host "Entorno MA-Manim listo en Windows." -ForegroundColor Green
Write-Host "Render de prueba:"
Write-Host "  uv run manim -pql ma_cls_c13_p01/scene.py MAVizC13RiemannRefinement"
