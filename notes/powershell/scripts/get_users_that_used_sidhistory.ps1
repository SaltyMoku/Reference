$ErrorActionPreference = "SilentlyContinue"
Write-Host "### $env:ComputerName ###`n"
$user_list = Get-ChildItem -Path C:\Users | Select-Object name
foreach ($user in $user_list){
    $current_username = $user.name
    $temp_history = Get-Content C:\Users\$current_username\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt | Select-String -Pattern '.*(?i)sidhistory.*'
    if ($null -ne ($error.categoryinfo).category){ # File non esistente
        Write-Host "$current_username powershell history not found"
        $error.Clear()
    } elseif ($null -eq $temp_history) { # File esistente ma vuoto
        Write-Host "$current_username powershell history empty"
    } else { # File esistente ma pieno
        Write-Host "$current_username history:"
        $temp_history
        Write-Host
    }
}