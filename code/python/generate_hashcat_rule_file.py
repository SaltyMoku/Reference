# Generates a rule that appends numbers from 0 to 9999 in hashcat

def generate_hashcat_rules():
    rules = []
    for i in range(10):
        rules.append("T" + str(i))
        
    for i in range(10):
        for j in range(10):
            rules.append("T" + str(i) + "T" + str(j))
            
    for i in range(10):
        for j in range(10):
            for k in range(10):
                rules.append("T" + str(i) + "T" + str(j) + "T" + str(k))
                
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    rules.append("T" + str(i) + "T" + str(j) + "T" + str(k) + "T" + str(l))
                    
    return rules

hashcat_rules = generate_hashcat_rules()

with open("hashcat_rules.txt", "w") as file:
    file.write("\n".join(hashcat_rules))