<#
.SYNOPSIS
    Download and catalog the war.gov UFO archive (Release 01, 2026-05-08).

.DESCRIPTION
    Pure PowerShell — no Python required. Uses Invoke-WebRequest -UseBasicParsing and
    Get-FileHash, both built into Windows.

    The script is fully resumable: re-running skips files whose recorded
    SHA-256 matches the on-disk hash. Polite 2-second delay between
    requests. Per-file metadata captured into metadata/index.json.

.EXAMPLE
    cd C:\Users\SeeingBlue\Documents\BluNET\war-gov-uap-archive
    .\scripts\run-archive.ps1

.NOTES
    Resolve videos via DVIDS API. PDFs/images come straight from war.gov.
    Snapshot folder is dated; re-running on a later date creates a new
    snapshot and only fetches new URLs.
#>

[CmdletBinding()]
param(
    [string]$SnapshotDate = (Get-Date -Format "yyyy-MM-dd"),
    [int]$DelaySeconds = 2,
    [string]$UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"  # speeds up Invoke-WebRequest -UseBasicParsing a lot

# PowerShell 5.1 defaults to TLS 1.0/1.1 which war.gov refuses.
[Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12

# Full Chrome-equivalent header bag - Akamia bot-detect rejects bare requests.
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

# ---- Paths -------------------------------------------------------------

$ProjectRoot   = Split-Path -Parent $PSScriptRoot
$SnapshotDir   = Join-Path $ProjectRoot "snapshots\$SnapshotDate"
$CsvPath       = Join-Path $SnapshotDir "uap-csv.csv"
$ManifestPath  = Join-Path $SnapshotDir "manifest.json"
$FilesDir      = Join-Path $ProjectRoot "files"
$PdfDir        = Join-Path $FilesDir   "pdfs"
$VideoDir      = Join-Path $FilesDir   "videos"
$ImageDir      = Join-Path $FilesDir   "images"
$MetadataDir   = Join-Path $ProjectRoot "metadata"
$IndexPath     = Join-Path $MetadataDir "index.json"
$IndexCsvPath  = Join-Path $MetadataDir "index.csv"
$PerFileDir    = Join-Path $MetadataDir "per-file"
$LogsDir       = Join-Path $ProjectRoot "logs"
$FetchLog      = Join-Path $LogsDir "fetch.log"
$ErrorLog      = Join-Path $LogsDir "errors.log"

foreach ($d in @($SnapshotDir, $PdfDir, $VideoDir, $ImageDir, $PerFileDir, $LogsDir)) {
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
}

# ---- Constants ---------------------------------------------------------

$CsvUrl       = "https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-csv.csv"
$DvidsApi     = "https://api.dvidshub.net/asset"
$DvidsApiKey  = "key-68bb60d16b35e"

# ---- Helpers -----------------------------------------------------------

function Now-Iso { (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ") }

function Log-Line {
    param([string]$Path, [string]$Line)
    "$((Now-Iso))`t$Line" | Out-File -FilePath $Path -Append -Encoding utf8
}

function Slugify {
    param([string]$Text, [int]$MaxLen = 60)
    if (-not $Text) { return "untitled" }
    $s = $Text.ToLowerInvariant() -replace '[^a-z0-9]+', '-'
    $s = $s.Trim('-')
    if ($s.Length -gt $MaxLen) { $s = $s.Substring(0, $MaxLen).TrimEnd('-') }
    if (-not $s) { return "untitled" }
    return $s
}

function Make-Id {
    param([string]$Agency, [int]$Seq, [string]$Title)
    $a = (Slugify $Agency 20)
    $t = (Slugify $Title)
    return "$a-{0:000}-$t" -f $Seq
}

function Classify-Type {
    param([string]$T)
    if (-not $T) { return "pdf" }
    $f = $T.Trim().Substring(0,1).ToUpperInvariant()
    if ($f -eq "V") { return "video" }
    if ($f -eq "I") { return "image" }
    return "pdf"
}

function Normalize-Agency {
    param([string]$Agency)
    if (-not $Agency) { return "unknown" }
    $a = $Agency.ToLowerInvariant()
    if ($a -match 'fbi')     { return "FBI" }
    if ($a -match 'war')     { return "DoW" }
    if ($a -match 'defense') { return "DoD" }
    if ($a -match 'nasa')    { return "NASA" }
    if ($a -match 'state')   { return "State" }
    return $Agency.Trim()
}

function Resolve-DvidsVideo {
    param([string]$VideoId)
    if (-not $VideoId) { return $null }
    try {
        $url = "$DvidsApi`?api_key=$DvidsApiKey&id=video:$VideoId"
        $r = Invoke-WebRequest -UseBasicParsing -Uri $url -Method Get -Headers $BrowserHeaders -TimeoutSec 30
        $data = $r.Content | ConvertFrom-Json
        $d = if ($data.results) { $data.results } elseif ($data.data) { $data.data } else { $data }
        $mp4s = @($d.files | Where-Object { $_.type -eq "video/mp4" })
        if (-not $mp4s) { return $null }
        $best = $mp4s | Sort-Object -Property height -Descending | Select-Object -First 1
        return [pscustomobject]@{ Url = $best.src; Title = $d.title }
    } catch {
        return $null
    }
}

# ---- Step 1: discover --------------------------------------------------

Write-Host "[archive] snapshot: $SnapshotDate"

if (-not (Test-Path $CsvPath) -or (Get-Item $CsvPath).Length -eq 0) {
    Write-Host "[discover] fetching CSV manifest..."
    try {
        Invoke-WebRequest -UseBasicParsing -Uri $CsvUrl `
            -OutFile $CsvPath `
            -Headers $BrowserHeaders `
            -TimeoutSec 30
        Log-Line $FetchLog "discover`tOK`t$CsvUrl`t$((Get-Item $CsvPath).Length)"
    } catch {
        Log-Line $ErrorLog "discover`tFETCH_FAIL`t$CsvUrl`t$_"
        Write-Error "Could not fetch CSV: $_"
        exit 2
    }
} else {
    Write-Host "[discover] using cached CSV at $CsvPath"
    Log-Line $FetchLog "discover`tCACHED`t$CsvUrl"
}

$csvRows = Import-Csv -Path $CsvPath
Write-Host "[discover] parsed $($csvRows.Count) rows from CSV"

# Build manifest
$seqByAgency = @{}
$assets = @()
foreach ($row in $csvRows) {
    $title = $row.Title
    if (-not $title) { continue }
    $title = $title.Trim()
    if (-not $title) { continue }

    $agencyRaw = ($row.Agency).Trim()
    $agency    = Normalize-Agency $agencyRaw
    $typeField = ($row.Type).Trim()
    $kind      = Classify-Type $typeField

    $pdfImage = $row.'PDF | Image Link'
    if ($pdfImage) { $pdfImage = $pdfImage.Trim() } else { $pdfImage = "" }

    $modalImg = $row.'Modal Image'
    if ($modalImg) { $modalImg = $modalImg.Trim() } else { $modalImg = "" }

    $dvidsId = $row.'DVIDS Video ID'
    if ($dvidsId) { $dvidsId = $dvidsId.Trim() } else { $dvidsId = "" }

    $sourceUrl = if ($kind -eq "video") { "" } else { $pdfImage }

    if (-not $seqByAgency.ContainsKey($agency)) { $seqByAgency[$agency] = 0 }
    $seqByAgency[$agency]++

    $assets += [pscustomobject]@{
        id                = Make-Id $agency $seqByAgency[$agency] $title
        type              = $kind
        title             = $title
        agency            = $agency
        agency_raw        = $agencyRaw
        type_code         = $typeField
        page_section      = "Release 01"
        release_date      = ($row.'Release Date'      ).Trim()
        incident_date     = ($row.'Incident Date'     ).Trim()
        incident_location = if ($row.'Incident Location') { ($row.'Incident Location').Trim() } else { "N/A" }
        summary           = ($row.'Description Blurb' ).Trim()
        redaction         = ($row.Redaction           ).Trim()
        video_pairing     = ($row.'Video Pairing'     ).Trim()
        pdf_pairing       = ($row.'PDF Pairing'       ).Trim()
        video_title       = ($row.'Video Title'       ).Trim()
        dvids_video_id    = $dvidsId
        modal_image_url   = $modalImg
        source_url        = $sourceUrl
        discovered_on     = (Now-Iso)
    }
}

$manifest = [pscustomobject]@{
    snapshot_date     = $SnapshotDate
    source_page       = "https://www.war.gov/UFO/"
    csv_manifest_url  = $CsvUrl
    discovered_on     = (Now-Iso)
    asset_count       = $assets.Count
    assets            = $assets
}
$manifest | ConvertTo-Json -Depth 6 | Out-File -FilePath $ManifestPath -Encoding utf8
Write-Host "[discover] manifest: $ManifestPath ($($assets.Count) assets)"

# Print breakdown
$byType   = $assets | Group-Object type   | Sort-Object Name | ForEach-Object { "$($_.Name)=$($_.Count)" }
$byAgency = $assets | Group-Object agency | Sort-Object Name | ForEach-Object { "$($_.Name)=$($_.Count)" }
Write-Host "[discover] by type:   $($byType -join ', ')"
Write-Host "[discover] by agency: $($byAgency -join ', ')"

# ---- Step 2: fetch ------------------------------------------------------

# Load existing index.json if present (for resumability)
$index = if (Test-Path $IndexPath) {
    Get-Content $IndexPath -Raw | ConvertFrom-Json
} else {
    [pscustomobject]@{
        schema_version = 1
        source_page    = "https://www.war.gov/UFO/"
        first_snapshot = $SnapshotDate
        last_updated   = $null
        files          = @()
    }
}
if (-not $index.first_snapshot) { $index.first_snapshot = $SnapshotDate }

$existingById = @{}
foreach ($f in @($index.files)) { $existingById[$f.id] = $f }

$fetched = 0; $skipped = 0; $failed = 0
$total = $assets.Count
$i = 0

foreach ($asset in $assets) {
    $i++
    $rec = $existingById[$asset.id]
    if (-not $rec) {
        # Build fresh record from asset
        $rec = [pscustomobject]@{
            id                  = $asset.id
            type                = $asset.type
            title               = $asset.title
            agency              = $asset.agency
            agency_raw          = $asset.agency_raw
            type_code           = $asset.type_code
            page_section        = $asset.page_section
            release_date        = $asset.release_date
            incident_date       = $asset.incident_date
            incident_location   = $asset.incident_location
            summary             = $asset.summary
            redaction           = $asset.redaction
            video_pairing       = $asset.video_pairing
            pdf_pairing         = $asset.pdf_pairing
            video_title         = $asset.video_title
            dvids_video_id      = $asset.dvids_video_id
            modal_image_url     = $asset.modal_image_url
            source_url          = $asset.source_url
            discovered_on       = $asset.discovered_on
            fetched_on          = ""
            local_path          = ""
            bytes               = 0
            sha256              = ""
            http_status         = 0
            content_type        = ""
            etag                = ""
            last_modified       = ""
            extracted_text_path = $null
            status              = "pending"
            notes               = ""
        }
        $existingById[$asset.id] = $rec
    } else {
        # Refresh page-level metadata in case it changed
        $rec.summary           = $asset.summary
        $rec.modal_image_url   = $asset.modal_image_url
        $rec.source_url        = $asset.source_url
    }

    # Already on disk with matching hash?
    $abs = if ($rec.local_path) { Join-Path $ProjectRoot $rec.local_path } else { "" }
    if ($rec.status -eq "ok" -and $rec.sha256 -and $abs -and (Test-Path $abs)) {
        $h = (Get-FileHash $abs -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($h -eq $rec.sha256) {
            $skipped++
            continue
        }
    }

    # Resolve videos via DVIDS
    if ($rec.type -eq "video" -and -not $rec.source_url) {
        $resolved = Resolve-DvidsVideo $rec.dvids_video_id
        if (-not $resolved) {
            $rec.status = "fetch_error"
            $rec.notes  = "DVIDS resolve failed for id=$($rec.dvids_video_id)"
            $failed++
            Log-Line $ErrorLog "fetch`tDVIDS_FAIL`t$($rec.dvids_video_id)"
            Start-Sleep -Seconds $DelaySeconds
            continue
        }
        $rec.source_url = $resolved.Url
        if ($resolved.Title -and -not $rec.video_title) { $rec.video_title = $resolved.Title }
    }

    # Decide local path
    $extFromUrl = ""
    if ($rec.source_url) {
        $cleanUrl = ($rec.source_url -split '\?')[0]
        if ($cleanUrl -match '\.([a-z0-9]+)$') { $extFromUrl = "." + $matches[1].ToLowerInvariant() }
    }
    if (-not $extFromUrl) {
        $extFromUrl = @{"pdf"=".pdf"; "video"=".mp4"; "image"=".jpg"}[$rec.type]
    }
    $destDir = @{"pdf"=$PdfDir; "video"=$VideoDir; "image"=$ImageDir}[$rec.type]
    $local = Join-Path $destDir "$($rec.id)$extFromUrl"

    Write-Host ("[{0}/{1}] {2} {3}" -f $i, $total, $rec.type, $rec.id)

    try {
        $r = Invoke-WebRequest -UseBasicParsing -Uri $rec.source_url `
            -OutFile $local `
            -Headers $BrowserHeaders `
            -TimeoutSec 60 `
            -PassThru
        $info = Get-Item $local
        $hash = (Get-FileHash $local -Algorithm SHA256).Hash.ToLowerInvariant()
        $rec.fetched_on    = (Now-Iso)
        $rec.local_path    = ($local -replace [regex]::Escape($ProjectRoot + "\"), "") -replace "\\","/"
        $rec.bytes         = $info.Length
        $rec.sha256        = $hash
        $rec.http_status   = [int]$r.StatusCode
        $rec.content_type  = $r.Headers["Content-Type"]
        $rec.etag          = $r.Headers["ETag"]
        $rec.last_modified = $r.Headers["Last-Modified"]
        $rec.status        = "ok"
        $fetched++
        Log-Line $FetchLog "fetch`tOK`t$($rec.source_url)`t$($info.Length)"
    } catch {
        $rec.status = "fetch_error"
        $rec.notes  = "$_"
        $failed++
        Log-Line $ErrorLog "fetch`tFAIL`t$($rec.source_url)`t$_"
    }

    # Per-file JSON
    $rec | ConvertTo-Json -Depth 4 | Out-File -FilePath (Join-Path $PerFileDir "$($rec.id).json") -Encoding utf8

    # Polite delay
    Start-Sleep -Seconds $DelaySeconds
}

# Save index
$index.files        = @($existingById.Values)
$index.last_updated = (Now-Iso)
$index | ConvertTo-Json -Depth 6 | Out-File -FilePath $IndexPath -Encoding utf8

# Flatten to CSV
$index.files |
    Select-Object id,type,title,agency,agency_raw,type_code,page_section,release_date,
                  incident_date,incident_location,summary,redaction,
                  video_pairing,pdf_pairing,video_title,dvids_video_id,
                  modal_image_url,source_url,discovered_on,fetched_on,
                  local_path,bytes,sha256,http_status,content_type,
                  etag,last_modified,extracted_text_path,status,notes |
    Export-Csv -Path $IndexCsvPath -NoTypeInformation -Encoding utf8

Write-Host ""
Write-Host "[fetch] fetched=$fetched skipped=$skipped failed=$failed total=$($index.files.Count)"
Write-Host "[fetch] index:   $IndexPath"
Write-Host "[fetch] csv:     $IndexCsvPath"
if ($failed -gt 0) { exit 1 } else { exit 0 }
