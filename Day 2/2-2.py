#Advent of Code 2020 Day 2 Part 2
from collections import Counter

with open("Day 2/data.txt") as text_file:
    choices = list(text_file.readlines())
    valid_passwords = []

for item in choices:
    items = item.split(" ")
    first, last = items[0].split("-")
    char = items[1].strip(":")
    string = items[2].strip("\n")
    first = int(first) - 1
    last = int(last) - 1

    if string[first] == char and string[last] == char:
        continue

    if string[first] == char or string[last] == char:
        valid_passwords.append(string)

print(len(valid_passwords))