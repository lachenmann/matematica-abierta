$ErrorActionPreference='Stop'
Set-Location $PSScriptRoot
while (-not (Test-Path raw/direct/17_final.json)) { Start-Sleep -Seconds 10 }
Start-Sleep -Seconds 5
function Run-Step([string]$Script) {
    & .venv/Scripts/python.exe -u $Script *> ($Script.Replace('.py','.log'))
    if ($LASTEXITCODE) { throw "Falló $Script" }
}
Run-Step assemble.py
Run-Step asr.py
Run-Step review.py
Run-Step audio_qa.py
Run-Step identity.py
Run-Step verify.py
Run-Step integrate.py
Run-Step report.py
