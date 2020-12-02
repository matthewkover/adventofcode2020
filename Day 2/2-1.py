#Advent of Code 2020 Day 2 Part 1
from collections import Counter

with open("Day 2/data.txt") as text_file:
    choices = list(text_file.readlines())
    valid_passwords = []

for item in choices:
    items = item.split(" ")
    min_val, max_val = items[0].split("-")
    char = items[1].strip(":")
    string = items[2].strip("\n")
    total = Counter(string)

    if int(min_val) <= int(total[char]) <= int(max_val):
        valid_passwords.append(string)

print(len(valid_passwords))