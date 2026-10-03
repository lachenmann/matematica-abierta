param(
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

$DestDir = Join-Path $Root "assets\audio\intro"
$Dest = Join-Path $DestDir "CPM-intro-music.wav"
$SourceCache = Join-Path $DestDir "Simple-Piano-Logo-source.wav"

$ffmpeg = Get-Command ffmpeg -ErrorAction SilentlyContinue
if (-not $ffmpeg) {
    throw "No se encontro ffmpeg en PATH. Manim necesita ffmpeg para preparar la cortina."
}

New-Item -ItemType Directory -Force -Path $DestDir | Out-Null

if (-not (Test-Path $SourceCache)) {
    $audioExtensions = @(".wav", ".mp3", ".flac", ".ogg", ".m4a", ".aac")

    $Candidates = Get-ChildItem $Root -Recurse -File |
        Where-Object {
            $audioExtensions -contains $_.Extension.ToLowerInvariant() -and
            $_.FullName -ne $Dest -and
            $_.FullName -ne $SourceCache -and
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

    if ($Candidates) {
        $Source = $Candidates[0].File.FullName
        Copy-Item -LiteralPath $Source -Destination $SourceCache -Force
    }
    elseif (Test-Path $Dest) {
        # Compatibilidad: una cortina canónica de la ronda anterior (8 s)
        # puede servir como fuente para reconstruir la nueva versión de 7 s.
        Copy-Item -LiteralPath $Dest -Destination $SourceCache -Force
    }
    else {
        throw "No se encontro Simple Piano Logo (Freesound sound ID 524847) dentro de $Root."
    }
}

Write-Host "Preparando cortina oficial..." -ForegroundColor Cyan
Write-Host "Fuente:  $SourceCache" -ForegroundColor DarkGray
Write-Host "Destino: $Dest" -ForegroundColor DarkGray
Write-Host "7.00 s - 48 kHz - stereo - fade-out 0.65 s" -ForegroundColor DarkGray

& $ffmpeg.Source -hide_banner -loglevel error -y `
    -i $SourceCache `
    -af "apad=pad_dur=7,atrim=0:7,asetpts=PTS-STARTPTS,afade=t=out:st=6.35:d=0.65" `
    -ar 48000 -ac 2 -c:a pcm_s16le `
    $Dest

if ($LASTEXITCODE -ne 0 -or -not (Test-Path $Dest)) {
    throw "No se pudo generar la cortina canonica."
}

Write-Host "Cortina preparada correctamente." -ForegroundColor Green
