Cmd Utilities
--------------------

Research string (grep):
```
ipconfig | findstr DNS
```

Copy to clipboard:
```
ipconfig | clip
```

ipconfig:
```
ipconfig /all
ipconfig /release
ipconfig /renew
ipconfig /displaydns
ipconfig /flushdns
```

nslookup tramite server 1.1.1.1:
```
nslookup google.com 1.1.1.1
```

nslookup diversi tipi di DNS:
```
nslookup -type=mx google.com
nslookup -type=txt google.com
nslookup -type=ptr google.com
```

Get MAC address for all components:
```
getmac /v
```

Association filetype-program:
```
assoc
assoc .mp4=VLC.vlc
```

Check disk:
```
chkdsk /f
chkdsk /r
sfc /scannow
```

Fix system image:
```
DISM /Online /Cleanup-Image CheckHealth
DISM /Online /Cleanup-Image CheckHealth /ScanHealth
DISM /Online /Cleanup-Image CheckHealth /RestoreHealth
```

List and kill processes:
```
tasklist | findstr chrome.exe
taskkil /f /pid 13245
```

netsh:
```
netsh interface show interface
netsh interface ip show address | findstr "IP Address"
netsh interface ip show dnsservers
netsh advfirewall set all profiles state off
netsh advfirewall set all profiles state on
```

Tracert without DNS (faster):
```
tracert -d google.com
```

Netstat - Show all connections:
-af shows all ports
-o shows PID assigned
-e -t 5 shows traffic sent/received every 5 sec
```
netstat
netstat -af
netstat -o
netstat -e -t 5
```

Show routing table and set routing rule:
```
route print
route add 192.168.10.0 mask 255.255.255.0 10.1.2.3
route delete 192.168.10.0
```

Restart PC to BIOS:
```
shutdown /r /fw /f /t 0
```

Show logical disks (volumes letter):
```
wmic logicaldisk get name
```

Show more information about logical disks:
```
wmic logicaldisk get deviceid, volumename, description
```

Show partitions:
```
wmic partition list
```
