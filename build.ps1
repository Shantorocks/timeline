$years = "2021","2022","2023","2024","2025"
$extensions = ".jpg",".jpeg",".png",".webp",".gif"
$manifest = @{}

foreach ($year in $years) {
    $folder = "works/$year"
    $files = @()
    if (Test-Path $folder) {
        $files = Get-ChildItem $folder | 
            Where-Object { $extensions -contains $_.Extension.ToLower() } | 
            Sort-Object Name |
            ForEach-Object { "works/$year/$($_.Name)" }
    }
    $manifest[$year] = @($files)
    Write-Host "$year  $($files.Count) image(s)"
}

$manifest | ConvertTo-Json -Depth 3 | Set-Content manifest.json
Write-Host "`n✓ manifest.json updated — push to GitHub and reload."