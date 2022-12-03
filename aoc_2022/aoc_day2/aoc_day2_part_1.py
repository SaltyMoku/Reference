your_score = 0
for line in (open("input.txt")):
    line.split(" ")

    if line[2] == "X":
        if line[0] == "A":
            your_score = your_score + 3 + 1
        elif line[0] == "B":
            your_score = your_score + 0 + 1
        elif line[0] == "C":
            your_score = your_score + 6 + 1
        
    if line[2] == "Y":
        if line[0] == "A":
            your_score = your_score + 6 + 2
        elif line[0] == "B":
            your_score = your_score + 3 + 2
        elif line[0] == "C":
            your_score = your_score + 0 + 2

    if line[2] == "Z":
        if line[0] == "A":
            your_score = your_score + 0 + 3
        elif line[0] == "B":
            your_score = your_score + 6 + 3
        elif line[0] == "C":
            your_score = your_score + 3 + 3
print("Your score is: " + str(your_score))