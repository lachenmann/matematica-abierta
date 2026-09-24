param(
    [Parameter(Mandatory = $true)][string]$ProjectUrl,
    [Parameter(Mandatory = $true)][string]$PublishableKey
)

$ErrorActionPreference = 'Stop'
$ProjectUrl = $ProjectUrl.Trim().TrimEnd('/')
$PublishableKey = $PublishableKey.Trim()

if ($ProjectUrl -notmatch '^https://[a-z0-9-]+\.supabase\.co$') {
    throw 'ProjectUrl no parece una URL válida de Supabase.'
}
if (-not $PublishableKey) {
    throw 'Falta PublishableKey.'
}

$target = Join-Path (Split-Path $PSScriptRoot -Parent) 'supabase-config.local.mjs'
$urlLiteral = $ProjectUrl.Replace("'", "\'")
$keyLiteral = $PublishableKey.Replace("'", "\'")

@"
// Archivo local de desarrollo. No versionar.
export const projectUrl = '$urlLiteral';
export const publishableKey = '$keyLiteral';
"@ | Set-Content -Path $target -Encoding UTF8

Write-Host "Configuración local escrita en: $target"
Write-Host 'Este archivo está ignorado por Git.'
