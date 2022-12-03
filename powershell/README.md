Powershell Utilities
--------------------

Research file:
```powershell
Get-Childitem –Path C:\ -Include *.exe -Recurse -ErrorAction SilentlyContinue
```

Select single value:
```powershell
Get-Childitem -Path C:\ -Include uninstall.exe -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
```

Output a file txt:
```powershell
| Out-File -FilePath C:\Users\$env:UserName\Desktop\nomefile.txt
```

Output a JSON:
```powershell
| ConvertTo-Json
```

File hash:
```powershell
Get-FileHash C:\nomefile.txt
```

Search file and get file hash:
```powershell
Get-Childitem -Path C:\ -Include uninstall.exe -Recurse -ErrorAction SilentlyContinue | Get-FileHash | format-list *
```

Scheduled Task information:
```powershell
Get-ScheduledTask | ForEach-Object {
[pscustomobject]@{
Name = $_.TaskName
Path = $_.TaskPath
LastResult = $(($_ | Get-ScheduledTaskInfo).LastTaskResult)
NextRun = $(($_ | Get-ScheduledTaskInfo).NextRunTime)
Status = $_.State
Command = $_.Actions.execute
Arguments = $_.Actions.Arguments
}
} | Out-File -FilePath C:\Users\$env:UserName\Desktop\Scheduled.txt
```

AD Users created in the last 50 days:
```powershell
$DateCutOff = (Get-Date).AddDays(-50)
Get-ADUser -Filter * -Properties whenCreated | where {$_.whenCreated -gt $DateCutOff} | FT Name, whenCreated
```

Env variables:
```powershell
$env:UserName
$env:UserDomain
$env:ComputerName
```

Grep:
```powershell
| Select-String word
```

PowerShell to .exe:
```powershell
Install-Module -Name ps2exe
ps2exe '.\file.ps1'
```

AD User information:
```powershell
Get-ADUser -identity erricos -properties *
```

PS-History:
```powershell
Get-Content C:\Users\$env:UserName\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt
```

Port Forwarding:
```powershell
ssh -L [localport]:[LAN IP of remote device] [admin]@[bridge machine IP]
ssh -L 8855:192.168.15.15:443 root@100.127.202.3
```
Then connect to http://localhost:8855/ or https://localhost:8855/

Base64 Encode:
```powershell
[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes("echo asd"))
```

Base64 command exec (max 8192 char - UTF16LE):
```powershell
powershell.exe -encodedCommand RwBlAHQALQBXAG0AaQBPAGIAagBlAGMAdAAgAFcAaQBuADMAMgBfAFAAcgBvAGMAZQBzAHMAIAAtAEYAaQBsAHQAZQByACAAIgBuAGEAbQBlACAAPQAgACcAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACcAIgAgAHwAIABTAGUAbABlAGMAdAAtAE8AYgBqAGUAYwB0ACAAQwBvAG0AbQBhAG4AZABMAGkAbgBlAA==
```

Base64 from PasteBin (from CMD):
```powershell
powershell.exe (powershell.exe (curl https://pastebin.com/raw/BmHCFauX).Content)
powershell.exe (powershell.exe -encodedCommand (curl https://pastebin.com/raw/J5dr6xTa).Content)
```

Process infos (es. process launched in Powershell by other processes):
```powershell
Get-WmiObject Win32_Process -Filter "name = 'powershell.exe'" | Select-Object CommandLine
```

Port connection:
```powershell
Test-NetConnection -Port 443 -ComputerName google.com -InformationLevel Detailed
```

