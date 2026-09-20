<#
.SYNOPSIS
    Render the book PDFs from the repository root.

.DESCRIPTION
    Compiles the light and dark editions by invoking book/scripts/build.ps1.
    Outputs land in book/build/ and are copied to the website reader.

.PARAMETER Target
    Which edition to build: all, light, or dark. Defaults to all.
#>
param(
    [Parameter(Position = 0)]
    [ValidateSet("all", "light", "dark")]
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Build = Join-Path $RepoRoot "book\scripts\build.ps1"

if (-not (Test-Path -LiteralPath $Build)) {
    Write-Error "Book build script not found: $Build"
}

& $Build $Target
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
