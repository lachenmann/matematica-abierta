# Descarga local de los pesos de Kokoro. Solo se ejecuta una vez.
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$Models = Join-Path $PSScriptRoot 'models'
New-Item -Path $Models -ItemType Directory -Force | Out-Null
$Files = @(
  @{ Name='kokoro-v1.0.onnx'; Url='https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/kokoro-v1.0.onnx'; Min=300000000 },
  @{ Name='voices-v1.0.bin'; Url='https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/voices-v1.0.bin'; Min=20000000 }
)
$Expected = (Get-Content (Join-Path $PSScriptRoot 'modelos.json') -Raw | ConvertFrom-Json).archivos
foreach ($File in $Files) {
  $Target = Join-Path $Models $File.Name
  if ((Test-Path $Target) -and ((Get-Item $Target).Length -ge $File.Min)) {
    if ((Get-FileHash -LiteralPath $Target -Algorithm SHA256).Hash.ToLower() -ne $Expected.($File.Name)) { throw "Huella inesperada: $($File.Name)" }
    Write-Host "[CACHE] $($File.Name) ya existe."
    continue
  }
  $Tmp = "$Target.download"
  if (Test-Path $Tmp) { Remove-Item $Tmp -Force }
  Write-Host "[DESCARGANDO] $($File.Name)" -ForegroundColor Cyan
  & curl.exe --fail --location --retry 3 --connect-timeout 20 --max-time 240 --output $Tmp $File.Url
  if ($LASTEXITCODE -ne 0) { throw "Falló la descarga de $($File.Name)" }
  if ((Get-Item $Tmp).Length -lt $File.Min) {
    throw "Descarga incompleta de $($File.Name)"
  }
  Move-Item -Path $Tmp -Destination $Target -Force
  $Digest = (Get-FileHash -Path $Target -Algorithm SHA256).Hash
  if ($Digest.ToLower() -ne $Expected.($File.Name)) { throw "Huella inesperada: $($File.Name)" }
  "$Digest  $($File.Name)" | Set-Content "$Target.sha256" -Encoding ascii
  Write-Host "[OK] $($File.Name): SHA256 $Digest" -ForegroundColor Green
}
