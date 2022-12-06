import re

contained_counter = 0 
input = open("input.txt")
for line in input:
    is_fully_contained = 0
    line = line.strip()
    split_line = re.split(r'-|,', line)
    split_line = [int(line) for line in split_line]
    if (split_line[0] in range(split_line[2],split_line[3]+1))|(split_line[1] in range(split_line[2],split_line[3]+1)):
            is_fully_contained = 1
    if (split_line[2] in range(split_line[0],split_line[1]+1))|(split_line[3] in range(split_line[0],split_line[1]+1)):
            is_fully_contained = 1
    if is_fully_contained == 1:
        contained_counter+=1
print(contained_counter)
