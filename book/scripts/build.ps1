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

function Copy-BuiltPdf {
    param(
        [string]$From,
        [string]$To
    )

    try {
        Copy-Item -LiteralPath $From -Destination $To -Force
        Write-Host "Wrote $To"
        return $true
    } catch {
        Write-Warning "Could not replace $To. Close the PDF viewer or the website Read tab, then run the script again. Fresh file: $From"
        return $false
    }
}

function Invoke-PdfLaTeX {
    param(
        [string]$Root,
        [string]$JobName
    )

    $pdfArgs = @(
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory=build",
        "-jobname=$JobName",
        $Root
    )
    & pdflatex @pdfArgs | Out-Host
    if ($LASTEXITCODE -ne 0) {
        throw "pdflatex failed for $Root"
    }
}

function Invoke-Edition {
    param([string]$Root)

    $stem = [System.IO.Path]::GetFileNameWithoutExtension($Root)
    $work = "$stem-wip"
    New-Item -ItemType Directory -Force -Path build | Out-Null
    Write-Host "Building $Root ..."

    Invoke-PdfLaTeX -Root $Root -JobName $work
    $aux = Join-Path $BookDir "build\$work.aux"
    $needsBib = (Test-Path $aux) -and (Select-String -Path $aux -Pattern '\\bibdata' -Quiet)
    if ($needsBib -and (Get-Command bibtex -ErrorAction SilentlyContinue)) {
        & bibtex "build/$work" | Out-Host
    }
    Invoke-PdfLaTeX -Root $Root -JobName $work
    Invoke-PdfLaTeX -Root $Root -JobName $work

    $wipPdf = Join-Path $BookDir "build\$work.pdf"
    $finalPdf = Join-Path $BookDir "build\$stem.pdf"
    $destDir = Join-Path $BookDir "..\website\apps\web\public\pdfs"
    $destPdf = Join-Path $destDir "$stem.pdf"

    [void](Copy-BuiltPdf -From $wipPdf -To $finalPdf)
    if (Test-Path (Split-Path $destDir -Parent)) {
        New-Item -ItemType Directory -Force -Path $destDir | Out-Null
        if (Copy-BuiltPdf -From $wipPdf -To $destPdf) {
            Write-Host "App PDF: $destPdf"
        }
    }
}

Require-PdfLaTeX

if ($Target -eq "all" -or $Target -eq "light") {
    Invoke-Edition "book-light.tex"
}
if ($Target -eq "all" -or $Target -eq "dark") {
    Invoke-Edition "book-dark.tex"
}
