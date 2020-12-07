#Advent of Code 2020 Day 6 Part 1

def getUnique(response):
    questions = []

    for char in response:
        if char not in questions:
            questions.append(char)

    return len(questions)

with open('Day 6/data.txt') as f:
    d = f.readlines()
    d = [ line.strip() for line in d ]

sum = 0
currentResponse = ''
for line in d:
    if line != '':
        currentResponse += line

    else:
        sum += getUnique(currentResponse)
        currentResponse = ''

sum += getUnique(currentResponse)

print(sum)