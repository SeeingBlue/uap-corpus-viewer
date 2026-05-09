<#
.SYNOPSIS
    Patch the one record where war.gov's CSV has a typo'd PDF URL.

.DESCRIPTION
    Record `fbi-010-65-hs1-834228961-62-hq-83894-serial-153` (Serial_153)
    has source_url ending in "8342289+M5+M11" in the source CSV - clearly
    a copy-paste error. The thumbnail URL on the same row uses the correct
    naming pattern, so we infer the intended PDF URL and try fetching it.

    If 200, downloads, hashes, updates index.json + index.csv.
#>

[CmdletBinding()]
param(
    [string]$UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)

$ErrorActionPreference = "Stop"
$ProgressPreference    = "SilentlyContinue"
[Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12

$ProjectRoot  = Split-Path -Parent $PSScriptRoot
$IndexPath    = Join-Path $ProjectRoot "metadata\index.json"
$IndexCsvPath = Join-Path $ProjectRoot "metadata\index.csv"
$PerFileDir   = Join-Path $ProjectRoot "metadata\per-file"
$PdfDir       = Join-Path $ProjectRoot "files\pdfs"

$BrowserHeaders = @{
    "User-Agent"                = $UserAgent
    "Accept"                    = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    "Accept-Language"           = "en-US,en;q=0.9"
    "Accept-Encoding"           = "gzip, deflate"
    "Cache-Control"             = "no-cache"
    "Pragma"                    = "no-cache"
    "Upgrade-Insecure-Requests" = "1"
    "Sec-Fetch-Site"            = "same-origin"
    "Sec-Fetch-Mode"            = "navigate"
    "Sec-Fetch-Dest"            = "document"
    "Sec-Fetch-User"            = "?1"
    "Referer"                   = "https://www.war.gov/UFO/"
    "DNT"                       = "1"
}

$TargetId    = "fbi-010-65-hs1-834228961-62-hq-83894-serial-153"
$InferredUrl = "https://www.war.gov/medialink/ufo/release_1/65_hs1-834228961_62-hq-83894_serial_153.pdf"
$LocalFile   = Join-Path $PdfDir "$TargetId.pdf"

Write-Host "[fix-153] target id:    $TargetId"
Write-Host "[fix-153] inferred URL: $InferredUrl"
Write-Host "[fix-153] downloading to: $LocalFile"

try {
    $r = Invoke-WebRequest -UseBasicParsing -Uri $InferredUrl `
        -OutFile $LocalFile `
        -Headers $BrowserHeaders `
        -TimeoutSec 60 `
        -PassThru
    Write-Host "[fix-153] OK status=$([int]$r.StatusCode) bytes=$((Get-Item $LocalFile).Length)"
} catch {
    Write-Error "[fix-153] download failed: $_"
    exit 1
}

$info = Get-Item $LocalFile
$hash = (Get-FileHash $LocalFile -Algorithm SHA256).Hash.ToLowerInvariant()

# Patch the index
$index = Get-Content $IndexPath -Raw -Encoding utf8 | ConvertFrom-Json
$rec = $index.files | Where-Object { $_.id -eq $TargetId } | Select-Object -First 1
if (-not $rec) {
    Write-Error "[fix-153] could not find record $TargetId in index.json"
    exit 1
}

$rec.source_url    = $InferredUrl
$rec.fetched_on    = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
$rec.local_path    = "files/pdfs/$TargetId.pdf"
$rec.bytes         = $info.Length
$rec.sha256        = $hash
$rec.http_status   = [int]$r.StatusCode
$rec.content_type  = $r.Headers["Content-Type"]
$rec.etag          = $r.Headers["ETag"]
$rec.last_modified = $r.Headers["Last-Modified"]
$rec.status        = "ok"
$rec.notes         = "source_url corrected from CSV typo (was: 65_hs1-8342289+M5+M11)"

$index.last_updated = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
$index | ConvertTo-Json -Depth 6 | Out-File -FilePath $IndexPath -Encoding utf8

# Refresh per-file JSON
$rec | ConvertTo-Json -Depth 4 | Out-File -FilePath (Join-Path $PerFileDir "$TargetId.json") -Encoding utf8

# Re-export index.csv from updated index
$index.files |
    Select-Object id,type,title,agency,agency_raw,type_code,page_section,release_date,
                  incident_date,incident_location,summary,redaction,
                  video_pairing,pdf_pairing,video_title,dvids_video_id,
                  modal_image_url,source_url,discovered_on,fetched_on,
                  local_path,bytes,sha256,http_status,content_type,
                  etag,last_modified,extracted_text_path,status,notes |
    Export-Csv -Path $IndexCsvPath -NoTypeInformation -Encoding utf8

Write-Host "[fix-153] index patched."
Write-Host "[fix-153] sha256: $hash"
Write-Host "[fix-153] DONE."
