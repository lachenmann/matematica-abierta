param([switch]$Preliminar)
$ErrorActionPreference='Stop'
Set-Location $PSScriptRoot
$maRenderPython=Join-Path (Resolve-Path ../../../manim/experimentos/MA_VIDEO_EXP003) '.venv/Scripts/python.exe'
if (-not (Test-Path $maRenderPython)) { throw 'No existe el entorno Manim ya preparado de EXP003; no se modifica ni instala automáticamente' }
$maVoiceRoot=$PSScriptRoot
Set-Location demo
$env:PYTHONUTF8='1'
if ($Preliminar) {
    & $maRenderPython -m manim -r '1280,720' --fps 30 --disable_caching escena.py EXP003 *> render_preliminar.log
} else {
    & $maRenderPython -m manim -r '1920,1080' --fps 60 --disable_caching escena.py EXP003 *> render_final.log
}
if ($LASTEXITCODE) { throw 'Falló render; revisar log de la copia' }
if (-not $Preliminar) {
    if (Test-Path MA_VOICE_003_DEMO.mp4) {
        $maPreviousDemo='MA_VOICE_003_DEMO_anterior_'+(Get-Date -Format 'yyyyMMdd_HHmmss')+'.mp4'
        Copy-Item -LiteralPath MA_VOICE_003_DEMO.mp4 -Destination $maPreviousDemo
    }
    $maDuration=(& "$maVoiceRoot/.venv/Scripts/python.exe" -c "import json; print(json.load(open('generados/timing_produccion.json',encoding='utf8'))['duracion_total'])")
    & ffmpeg -v error -y -i media/videos/escena/1080p60/EXP003.mp4 -i DEMO_AUDIO.wav -i EXP003_SUBTITULOS.srt -map 0:v -map 1:a -map 2:s -c:v copy -c:a aac -b:a 192k -c:s mov_text -metadata:s:s:0 language=spa -disposition:s:0 0 -t $maDuration -movflags +faststart MA_VOICE_003_DEMO.mp4
    if ($LASTEXITCODE) { throw 'Falló mux final' }
}
