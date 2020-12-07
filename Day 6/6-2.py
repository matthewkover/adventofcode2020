#Advent of Code 2020 Day 6 Part 2

def getYes(responses):
    questions = []

    for char in responses[0]:
        inAll = True
        for line in responses:
            if char not in line:
                inAll = False
    
        if inAll and char not in questions:
            questions.append(char)

    return(len(questions))

with open('Day 6/data.txt') as f:
    d = f.readlines()
    d = [ line.strip() for line in d ]

sum = 0
currentResponse = []

for line in d:
    if line != '':
        currentResponse.append(line)
    else:
        sum += getYes(currentResponse)
        currentResponse = []

sum += getYes(currentResponse)

print(sum)