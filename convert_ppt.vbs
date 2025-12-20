On Error Resume Next

Set pptApp = CreateObject("PowerPoint.Application")
If Err.Number <> 0 Then
    WScript.Echo "Error creating PowerPoint object: " & Err.Description
    WScript.Quit 1
End If

Set pres = pptApp.Presentations.Open(WScript.Arguments(0), -1, 0, 0)
If Err.Number <> 0 Then
    WScript.Echo "Error opening presentation: " & Err.Description
    pptApp.Quit
    WScript.Quit 1
End If

' ppFixedFormatTypePDF = 2
' ppFixedFormatIntentMinimumSize = 2
' msoFalse = 0, ppPrintHandoutVerticalFirst = 1, ppPrintOutputSlides = 1, ppPrintAll = 1
pres.ExportAsFixedFormat WScript.Arguments(1), 2, 2, 0, 1, 1, 0, Nothing, 1, "", True, True, True, True, False

If Err.Number <> 0 Then
    WScript.Echo "Error exporting to PDF: " & Err.Description
    pres.Close
    pptApp.Quit
    WScript.Quit 1
End If

pres.Close
pptApp.Quit

WScript.Echo "Successfully converted: " & WScript.Arguments(0)
