param(
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

$DestDir = Join-Path $Root "assets\audio\intro"
$Dest = Join-Path $DestDir "CPM-intro-music.wav"

if ((Test-Path $Dest) -and -not $Force) {
    Write-Host "Cortina canonica ya preparada: $Dest" -ForegroundColor DarkGray
    exit 0
}

$ffmpeg = Get-Command ffmpeg -ErrorAction SilentlyContinue
if (-not $ffmpeg) {
    throw "No se encontro ffmpeg en PATH. Manim necesita ffmpeg para preparar la cortina."
}

$audioExtensions = @(".wav", ".mp3", ".flac", ".ogg", ".m4a", ".aac")

$Candidates = Get-ChildItem $Root -Recurse -File |
    Where-Object {
        $audioExtensions -contains $_.Extension.ToLowerInvariant() -and
        $_.FullName -ne $Dest -and
        (
            $_.Name -match "524847" -or
            $_.BaseName -match "(?i)simple.*piano.*logo" -or
            $_.BaseName -match "(?i)cpm[-_ ]intro[-_ ]music"
        )
    } |
    ForEach-Object {
        $score = 0
        if ($_.Name -match "524847") { $score += 100 }
        if ($_.BaseName -match "(?i)simple.*piano.*logo") { $score += 50 }
        if ($_.Extension -ieq ".wav") { $score += 10 }
        [PSCustomObject]@{ File = $_; Score = $score }
    } |
    Sort-Object -Property @{Expression="Score"; Descending=$true}, @{Expression={$_.File.FullName}; Descending=$false}

if (-not $Candidates) {
    throw "No se encontro Simple Piano Logo (Freesound sound ID 524847) dentro de $Root."
}

$Source = $Candidates[0].File.FullName
New-Item -ItemType Directory -Force -Path $DestDir | Out-Null

Write-Host "Preparando cortina oficial..." -ForegroundColor Cyan
Write-Host "Fuente:  $Source" -ForegroundColor DarkGray
Write-Host "Destino: $Dest" -ForegroundColor DarkGray
Write-Host "8.00 s - 48 kHz - stereo - fade-out 0.65 s" -ForegroundColor DarkGray

& $ffmpeg.Source -hide_banner -loglevel error -y `
    -i $Source `
    -af "apad=pad_dur=8,atrim=0:8,asetpts=PTS-STARTPTS,afade=t=out:st=7.35:d=0.65" `
    -ar 48000 -ac 2 -c:a pcm_s16le `
    $Dest

if ($LASTEXITCODE -ne 0 -or -not (Test-Path $Dest)) {
    throw "No se pudo generar la cortina canonica."
}

Write-Host "Cortina preparada correctamente." -ForegroundColor Green
