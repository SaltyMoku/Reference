# Wordlists

## Wordlistctl - Wordlist Manager

[Wordlistctl](https://github.com/BlackArch/wordlistctl) is a CLI tool to fetch, install, update and search wordlists.

Search online. It can search up both wordlist names or categories
```
wordlistctl search rockyou
```
```
wordlistctl search facebook
```
```
wordlistctl list -g fuzzing
```

Search local:
```
wordlistctl search -l rockyou
```

Download wordlist (compressed) - Default path `/usr/share/wordlists/passwords/`:
```
wordlistctl fetch -l rockyou
```

Download wordlist (decompressed):
```
wordlistctl fetch -l rockyou -d
```

## Mentalist - GUI Wordlist Generator

[Mentalist](https://github.com/sc0tfree/mentalist) is a GUI tool that generates wordlists and rules.
![6205e8e5fb4ac01cfdb92fa829d59949.png](:/b956383b631f43ccbe330364ab5d28b9)

## CeWL - Wordlist from Website

[CeWL](https://github.com/digininja/CeWL) is a CLI tool that generates a wordlist from a website.

Generate wordlist from *example.org* with a depth of 2:
```
cewl -d 2 -w $(pwd)/example.txt https://example.org`
```

## TTPassGen - Wordlist from scrach

[TTPassGen](https://github.com/tp7309/TTPassGen) is a CLI tool that crafts wordlists from scratch.
It can also combine rules and wordlists.

Generate list of all lowercase chars combinations of length 1 to 3:
```
ttpassgen --rule '[?l]{1:3:*}' abc.txt
```

Combine wordlists *pin.txt* and *abc.txt*:
```
ttpassgen --dictlist 'pin.txt,abc.txt' --rule '$0[-]{1}$1' combination.txt
```

## Others

- [Munge](https://github.com/Th3S3cr3tAg3nt/Munge): Python script that takes a clean wordlist as input, and generates a new wordlist changing characters with similar ones.