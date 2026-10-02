$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

$DestDir = Join-Path $Root "cpm_yt_c01_v01\intro-music"
$Dest = Join-Path $DestDir "CPM-intro-music.wav"

New-Item -ItemType Directory -Force $DestDir | Out-Null

$Candidates = Get-ChildItem -Path $Root -Recurse -File -Filter *.wav |
    Where-Object {
        $_.FullName -notlike "*voice-reference*" -and
        $_.FullName -ne $Dest -and
        $_.Length -lt 10MB
    } |
    Sort-Object LastWriteTime -Descending

if (-not $Candidates) {
    throw "No encontre un WAV corto para usar como cortina musical."
}

$Source = $Candidates[0]
Copy-Item $Source.FullName $Dest -Force

Write-Host "Cortina musical preparada:" -ForegroundColor Cyan
Write-Host "  origen:  $($Source.FullName)"
Write-Host "  destino: $Dest"
Write-Host ""
Write-Host "La produccion usara este WAV solo al comienzo del video." -ForegroundColor DarkGray
