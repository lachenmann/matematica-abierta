param(
    [ValidateSet('verify','plan','generate','import-approved')][string]$Command = 'verify',
    [string]$Script,
    [string]$Output,
    [ValidateSet('qwen-base','kokoro-preview')][string]$Engine = 'qwen-base',
    [string]$Python,
    [string]$Dictionary,
    [string]$Cache,
    [double]$Offset = 7,
    [string]$Model,
    [string]$KokoroModel,
    [string]$KokoroVoices
)
$ErrorActionPreference = 'Stop'
if (-not $Python) {
    $Python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
    if (-not (Test-Path -LiteralPath $Python)) {
        $Python = Join-Path $PSScriptRoot 'experimentos\MA_VOICE_003\.venv\Scripts\python.exe'
    }
}
if (-not (Test-Path -LiteralPath $Python)) { throw 'Preparar entorno aislado con setup.ps1 o especificar -Python.' }
$Python = [IO.Path]::GetFullPath($Python)
$cliArgs = @('-m','ma_voice.cli',$Command,'--engine',$Engine,'--offset',"$Offset")
foreach ($pair in @(@('--script',$Script),@('--output',$Output),@('--dictionary',$Dictionary),@('--cache',$Cache),@('--model',$Model),@('--kokoro-model',$KokoroModel),@('--kokoro-voices',$KokoroVoices))) {
    if ($pair[1]) { $cliArgs += $pair }
}
# Resolve user paths before changing the module working directory.
for ($i=0; $i -lt $cliArgs.Count; $i++) {
    if ($cliArgs[$i] -in @('--script','--output','--dictionary','--cache','--model','--kokoro-model','--kokoro-voices')) {
        $cliArgs[$i+1] = [IO.Path]::GetFullPath($cliArgs[$i+1]); $i++
    }
}
Push-Location $PSScriptRoot
try { & $Python @cliArgs; if ($LASTEXITCODE -ne 0) { throw "MA-VOICE falló: $LASTEXITCODE" } }
finally { Pop-Location }
