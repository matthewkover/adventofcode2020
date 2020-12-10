with open ('Day 9/data.txt') as f:
    d = f.readlines()
    d = [ int(line.strip()) for line in d ]

def get_wrong_number():

    for i in range(25, len(d)):
        preamble = d[i - 25: i]
        num = d[i]
        found = False

        for j in range(len(preamble) - 1):
            for k in range(j+1, len(preamble)):
                if preamble[j] + preamble [k] == num:
                    found = True
                    break
                if found == True:
                    break
        if found == True:
            continue

        return num

num = get_wrong_number()

print(num)