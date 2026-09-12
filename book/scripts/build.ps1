param(
    [Parameter(Position = 0)]
    [ValidateSet("all", "light", "dark")]
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"
$BookDir = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $BookDir

$env:PATH = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64;$env:PATH"

function Require-PdfLaTeX {
    if (-not (Get-Command pdflatex -ErrorAction SilentlyContinue)) {
        Write-Error "pdflatex is not on PATH. Install MiKTeX or TeX Live."
    }
}

function Invoke-Edition {
    param([string]$Root)

    New-Item -ItemType Directory -Force -Path build | Out-Null
    Write-Host "Building $Root ..."
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build $Root | Out-Host
    $stem = [System.IO.Path]::GetFileNameWithoutExtension($Root)
    $aux = Join-Path $BookDir "build\$stem.aux"
    $needsBib = (Test-Path $aux) -and (Select-String -Path $aux -Pattern '\\bibdata' -Quiet)
    if ($needsBib -and (Get-Command bibtex -ErrorAction SilentlyContinue)) {
        bibtex "build/$stem" | Out-Host
    }
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build $Root | Out-Host
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build $Root | Out-Host

    $destDir = Join-Path $BookDir "..\website\apps\web\public\pdfs"
    if (Test-Path (Split-Path $destDir -Parent)) {
        New-Item -ItemType Directory -Force -Path $destDir | Out-Null
        Copy-Item (Join-Path $BookDir "build\$stem.pdf") (Join-Path $destDir "$stem.pdf") -Force
        Write-Host "Copied $stem.pdf to website/apps/web/public/pdfs/"
    }
}

Require-PdfLaTeX

if ($Target -eq "all" -or $Target -eq "light") {
    Invoke-Edition "book-light.tex"
}
if ($Target -eq "all" -or $Target -eq "dark") {
    Invoke-Edition "book-dark.tex"
}
