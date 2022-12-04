priority = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
input = open("input.txt")
while True:
    clean_1 = input.readline().strip()
    clean_2 = input.readline().strip()
    clean_3 = input.readline().strip()
    for char in clean_1:
        if char in clean_2:
            if char in clean_3:
                priority += letters.rfind(char)+1
                break
    if clean_1 == '':
        break
print(priority)