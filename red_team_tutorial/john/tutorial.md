# John the Ripper

[John](https://www.openwall.com/john/) is a tool that cracks hashes.

## Usage

Identify the hash format using [haiti](./tutorial.md)

Crack of *hash.txt* using the wordlist *wordlist.txt*, applying the rule *CustomRule*:
```
john hash.txt --format=raw-md5 --wordlist=wordlist.txt --rules=CustomRule
```

Crack using all rules (`--rules=ALL`):
```
john hash.txt --format=raw-md5 --wordlist=wordlist.txt --rules=ALL 
```

## Configuration

John configuration may be located at:
- `/etc/john/john.conf`
- `/usr/share/john/john.conf`

Default rules are cointained inside the configuration folder.
Make custom rules by creating the file `john-local.conf` in the configuration directory.

Rule that appens two digits at the end of each word:
```
[List.Rules:CustomRule]
$[0-9]$[0-9]
```

Rules can be crafted manually, or using tools such as Mentalist.