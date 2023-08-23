# Hashcat

[Hashcat](https://hashcat.net/hashcat/) is a tool that cracks hashes.
Hashcat Codes with examples are available [here](https://hashcat.net/wiki/doku.php?id=example_hashes).

**NOTE**: Windows requires [Cuda Toolkit](https://developer.nvidia.com/cuda-downloads) to run Hashcat

## Usage

Identify the hash format using [haiti](./tutorial.md)

Hashcat cat use multiple attack modes, showed by running `hashcat --help`.
Each mode has its own syntax.

Crack of *hash.txt* (type 13100 - Kerberos 5) using the wordlist *wordlist.txt*, applying the rule *numbers.rule*, and printing on screen each word tested.:
```
hashcat -m 13100 -a 0 hash.txt wordlist.txt -r numbers.rule --stdout 
```

Crack without using cache with `--potfile-disable`.  
Hashcat saves each test in a temporary file to avoid repeating the same words on multiple tests. This is useful when testing a times or new rule:
```
hashcat -m 13100 -a 0 hash.txt wordlist.txt --potfile-disable -r numbers.rule -r case.rules
```

Crack of numeric password with Bruteforce attack mode.  
Generally good when used on multiple Wi-Fi password hashes:
```
hashcat -m 22000 -a 3 hash.txt ?d?d?d?d?d?d?d?d
```

Crack password using a [combinator attack](https://hashcat.net/wiki/doku.php?id=combinator_attack). It allows to combine two dictionaries.  
`-j` and `-k`  options allow to apply rules to the first and second dictionary respectively and separately.
```
hashcat -m 0 -a 1 hash.txt dict1.txt dict1.txt
```
```
hashcat -m 0 -a 1 hash.txt dict1.txt dict1.txt -j '$-' -k '$!'
```

Crack using a [hybrid attack](https://hashcat.net/wiki/doku.php?id=hybrid_attack), mixing a wordlist attacck and a bruteforce attack that appens digits from 00 to 99:
```
hashcat -m 0 -a 6 hash.txt wordlist.txt ?d?d
```