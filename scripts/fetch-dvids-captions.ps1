<#
.SYNOPSIS
    Pull DVIDS metadata + WebVTT captions for all 28 video records.

.DESCRIPTION
    For each video record, hits api.dvidshub.net/asset?id=video:<id> and
    captures: title, date, duration, description, location, category,
    closed_caption_urls, files. If WebVTT captions are available, they
    are downloaded and appended to the existing extracted/<id>.md file
    under a "## Transcript" section.

    The DVIDS API key (key-68bb60d16b35e) is the public read key
    embedded in the war.gov page's inline JS — same one the page itself
    uses. Public, rate-limited, safe to mirror.

    Run from the project root.
#>

[CmdletBinding()]
param(
    [int]$DelayMs = 250,
    [string]$UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)

$ErrorActionPreference = "Stop"
$ProgressPreference    = "SilentlyContinue"
[Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12

$ProjectRoot   = Split-Path -Parent $PSScriptRoot
$IndexPath     = Join-Path $ProjectRoot "metadata\index.json"
$ExtractedDir  = Join-Path $ProjectRoot "extracted"
$DvidsCacheDir = Join-Path $ProjectRoot "metadata\dvids"

if (-not (Test-Path $DvidsCacheDir)) { New-Item -ItemType Directory -Path $DvidsCacheDir -Force | Out-Null }

$ApiKey = "key-68bb60d16b35e"
$Headers = @{
    "User-Agent"      = $UserAgent
    "Accept"          = "application/json, text/plain, */*"
    "Accept-Language" = "en-US,en;q=0.9"
    "Origin"          = "https://www.war.gov"
    "Referer"         = "https://www.war.gov/UFO/"
    "Sec-Fetch-Mode"  = "cors"
    "Sec-Fetch-Site"  = "cross-site"
    "Sec-Fetch-Dest"  = "empty"
}

# Load index
$indexJson = Get-Content $IndexPath -Raw -Encoding utf8
$index = $indexJson | ConvertFrom-Json

$videos = $index.files | Where-Object { $_.type -eq "video" -and $_.dvids_video_id }
Write-Host "[dvids] video records to enrich: $($videos.Count)"

$enriched = 0; $skipped = 0; $failed = 0

foreach ($v in $videos) {
    $vid = $v.dvids_video_id
    $cachePath = Join-Path $DvidsCacheDir "$($v.id).json"
    $mdPath = Join-Path $ExtractedDir "$($v.id).md"

    # Skip if already enriched (transcript or DVIDS metadata section present)
    if (Test-Path $mdPath) {
        $body = Get-Content $mdPath -Raw -Encoding utf8
        if ($body -match "## Transcript" -or $body -match "DVIDS metadata captured on") {
            $skipped++
            continue
        }
    }

    Write-Host "[dvids] $($v.id)  (id=$vid)"
    try {
        $url = "https://api.dvidshub.net/asset?api_key=$ApiKey&id=video:$vid"
        $r = Invoke-WebRequest -UseBasicParsing -Uri $url -Headers $Headers -TimeoutSec 30
        $data = $r.Content | ConvertFrom-Json
        $d = if ($data.results) { $data.results } elseif ($data.data) { $data.data } else { $data }

        # Cache full JSON
        $d | ConvertTo-Json -Depth 8 | Out-File -FilePath $cachePath -Encoding utf8

        # Try to fetch WebVTT captions
        $vttText = ""
        if ($d.closed_caption_urls -and $d.closed_caption_urls.webvtt) {
            try {
                $vttUrl = $d.closed_caption_urls.webvtt
                $rv = Invoke-WebRequest -UseBasicParsing -Uri $vttUrl -Headers $Headers -TimeoutSec 30
                $vttText = $rv.Content
                $vttPath = Join-Path $DvidsCacheDir "$($v.id).vtt"
                $vttText | Out-File -FilePath $vttPath -Encoding utf8
            } catch {
                Write-Host "    [warn] caption fetch failed: $_"
            }
        }

        # Append a "## DVIDS metadata" + optional "## Transcript" section to the .md
        if (Test-Path $mdPath) {
            $existing = Get-Content $mdPath -Raw -Encoding utf8
        } else {
            $existing = ""
        }

        $sb = [System.Text.StringBuilder]::new()
        $sb.AppendLine("") | Out-Null
        $sb.AppendLine("---") | Out-Null
        $sb.AppendLine("") | Out-Null
        $sb.AppendLine("## DVIDS metadata captured on $((Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ'))") | Out-Null
        $sb.AppendLine("") | Out-Null
        if ($d.title)        { $sb.AppendLine("- **Title:** $($d.title)") | Out-Null }
        if ($d.date)         { $sb.AppendLine("- **Date taken:** $($d.date)") | Out-Null }
        if ($d.date_published) { $sb.AppendLine("- **Date published:** $($d.date_published)") | Out-Null }
        if ($d.duration)     { $sb.AppendLine("- **Duration:** $($d.duration)s") | Out-Null }
        if ($d.category)     { $sb.AppendLine("- **Category:** $($d.category)") | Out-Null }
        if ($d.location -and $d.location.country_abbreviation) {
            $sb.AppendLine("- **Location (DVIDS):** $($d.location.country_abbreviation)") | Out-Null
        }
        if ($d.unit_name)    { $sb.AppendLine("- **Unit:** $($d.unit_name)") | Out-Null }
        if ($d.credit -and $d.credit.Count -gt 0) {
            $names = ($d.credit | ForEach-Object { $_.name }) -join ", "
            $sb.AppendLine("- **Credit:** $names") | Out-Null
        }
        if ($d.keywords -and $d.keywords.Count -gt 0) {
            $sb.AppendLine("- **Keywords:** $($d.keywords -join ', ')") | Out-Null
        }
        $sb.AppendLine("") | Out-Null
        if ($d.description) {
            $sb.AppendLine("### DVIDS description") | Out-Null
            $sb.AppendLine("") | Out-Null
            $sb.AppendLine($d.description) | Out-Null
            $sb.AppendLine("") | Out-Null
        }
        if ($vttText) {
            $sb.AppendLine("### Transcript (WebVTT)") | Out-Null
            $sb.AppendLine("") | Out-Null
            $sb.AppendLine('```vtt') | Out-Null
            $sb.AppendLine($vttText) | Out-Null
            $sb.AppendLine('```') | Out-Null
            $sb.AppendLine("") | Out-Null
        }

        # Replace placeholder if present, else append
        $append = $sb.ToString()
        $placeholder = "_Captions, transcripts, and full DVIDS metadata are fetched separately"
        if ($existing -match $placeholder) {
            # Find the start of the placeholder paragraph and replace it
            $newBody = [regex]::Replace(
                $existing,
                '## DVIDS metadata\s*\r?\n\s*\r?\n_Captions[\s\S]*?_\s*\r?\n',
                '',
                'Singleline'
            )
            $newBody = $newBody.TrimEnd() + "`n" + $append
            $newBody | Out-File -FilePath $mdPath -Encoding utf8
        } else {
            $append | Out-File -FilePath $mdPath -Encoding utf8 -Append
        }

        $enriched++
    } catch {
        Write-Host "    [fail] $_"
        $failed++
    }
    Start-Sleep -Milliseconds $DelayMs
}

Write-Host ""
Write-Host "[done] enriched=$enriched skipped=$skipped failed=$failed"
