with open('Day 3/data.txt') as data:
    map = data.readlines()
    map = [ line.strip() for line in map ]

treeCount = 0
row, col = 0,0

while row + 1 < len(map):
    row += 1
    col += 3

    space = map[row][col % len(map[row])]
    if space == '#':
        treeCount += 1

print(treeCount)