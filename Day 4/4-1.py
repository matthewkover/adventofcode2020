#Advent of Code 2020 Day 4 Part 1

with open('Day 4/data.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]

valid = 0

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def isValid(pp):
    for field in fields:
        if field not in pp:
            return False
    return True

currentPass = ''
for line in data:
    if line != '':
        currentPass += line

    else:
        if isValid(currentPass):
            valid += 1

        currentPass = ''

if isValid(currentPass):
    valid += 1

print(valid)