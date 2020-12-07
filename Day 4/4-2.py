#Advent of Code 2020 Day 4 Part 2

import re

field_conditions = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: re.search('^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$', x),
    'hcl': lambda x: re.search('^#([a-f]|[0-9]){6}$', x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: re.search('^[0-9]{9}$', x)
    }

def check_passport(f):
    for field, condition in field_conditions.items():
        if field not in f or not condition(f[field]):
            return False
    return True

with open("Day 4/data.txt", "r") as file:
    passports = file.read().split('\n\n')
    valid = 0
    for passport in passports:
        fields = { match.group(1): match.group(2) for match in re.finditer('([a-z]{3}):(.[^\s]+)', passport) }
        if check_passport(fields):
            valid += 1
    print(valid)