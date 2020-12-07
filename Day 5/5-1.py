#Advent of Code 2020 Day 5 Part 1

def getRow(pp):
    lo = 0
    hi = 127

    for i in range(6):
        half = (hi + lo) // 2
        if pp[i] == 'F':
            hi = half

        elif pp[i] == 'B':
            lo = half + 1

    if pp[6] == 'F':
        return lo
    else:
        return hi

def getCol(pp):
    lo = 0
    hi = 7

    for i in range(2):
        half = (hi + lo) // 2 
        if pp[i] == 'L':
            hi = half
        elif pp[i] == 'R':
            lo = half + 1

    if pp[2] == 'L':
        return lo
    else:
        return hi

largest = 0 

with open('Day 5/data.txt') as f:
    d = f.readlines()
    d = [ line.strip() for line in d ]

    for pp in d:
        row = getRow(pp[:7])
        col = getCol(pp[7:])

        id = int(row) * 8 + int(col)

        if id > largest:
            largest = id

print(largest)


