import re

contained_counter = 0 
input = open("input.txt")
for line in input:
    is_fully_contained = 0
    line = line.strip()
    split_line = re.split(r'-|,', line)
    split_line = [int(line) for line in split_line]
    """
    split_line[0]=int(split_line[0])
    split_line[1]=int(split_line[1])
    split_line[2]=int(split_line[2])
    split_line[3]=int(split_line[3])
    """
    if split_line[0]<=split_line[2]:
        if split_line[1]>=split_line[3]:
            is_fully_contained = 1
    if split_line[2]<=split_line[0]:
        if split_line[3]>=split_line[1]:
            is_fully_contained = 1
    if is_fully_contained == 1:
        contained_counter+=1
print(contained_counter)
