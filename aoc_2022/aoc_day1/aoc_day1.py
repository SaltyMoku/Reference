top_calories = [0,0,0]
temp_calory = 0
for line in open("input.txt"):
    calory = line.split("\n")[0]
    if calory == "":
        if temp_calory > min(top_calories):
            for i in range(len(top_calories)):
                if top_calories[i] == min(top_calories):
                    top_calories[i] = temp_calory
                    print(top_calories)
                    break
        temp_calory = 0
    else:
        temp_calory = temp_calory + int(calory)
print(top_calories[0] + top_calories[1] + top_calories[2])