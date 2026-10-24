# Default narration entry point for NEW automated MA Video projects.
# Runs in a separate voice process; never installs anything in Manim.
& (Join-Path $PSScriptRoot '..\voz\narrar.ps1') @args
if ($LASTEXITCODE -ne 0) { throw 'MA-VOICE falló' }
