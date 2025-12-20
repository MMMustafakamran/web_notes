$baseDir = "C:\Users\dynamic computer\Desktop\work\FAST\semester 7\webdev\notes\lecture slides"
$vbsScript = "C:\Users\dynamic computer\Desktop\work\FAST\semester 7\webdev\notes\convert_ppt.vbs"

# Get all PPTX files recursively
$pptxFiles = Get-ChildItem -Path $baseDir -Filter "*.pptx" -Recurse

Write-Host "Found $($pptxFiles.Count) PowerPoint files to convert."

foreach ($file in $pptxFiles) {
    $inputPath = $file.FullName
    $outputPath = $inputPath -replace '\.pptx$', '.pdf'
    
    Write-Host "Converting: $($file.Name)..." -NoNewline
    
    # Run VBScript converter
    $process = Start-Process cscript.exe -ArgumentList "//nologo", "`"$vbsScript`"", "`"$inputPath`"", "`"$outputPath`"" -Wait -NoNewWindow -PassThru
    
    if ($process.ExitCode -eq 0) {
        Write-Host " [OK]" -ForegroundColor Green
    } else {
        Write-Host " [FAILED]" -ForegroundColor Red
    }
}

Write-Host "All conversions completed."
