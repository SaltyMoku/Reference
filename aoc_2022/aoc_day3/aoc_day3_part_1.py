priority = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

input = open("input.txt")
for line in input:
    clean_line = line.strip()
    tmp_len = len(clean_line)
    if tmp_len%2 == 0:
        part1 = line[0:int(tmp_len/2)]
        part2 = line[int(tmp_len/2):int(tmp_len)]
    else:
        part1 = line[0:round(tmp_len/2)]
        part2 = line[round(tmp_len/2):int(tmp_len)]
    for char1 in part1:
        for char2 in part2:
            if char1 == char2:
                priority += letters.rfind(char1)+1
                break
        if char1 == char2:
            break
print(priority)