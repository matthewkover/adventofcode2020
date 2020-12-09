with open ('Day 8/data.txt') as f:
    d = f.readlines()
    d = [ line.strip() for line in d ]

def get_acc_end():
    acc = 0
    line = 0
    inst = []

    while line not in inst:
        inst.append(line)

        current_Instrution = d[line]
        current_Instrution = current_Instrution.split()
        cmd = current_Instrution[0]
        num = int(current_Instrution[1])

        if cmd == 'acc':
            acc += num
            line += 1
        elif cmd == 'jmp':
            line += num
        elif cmd == 'nop':
            line += 1
        if line >= len(d):
            return acc, True

    return acc, False

for i in range(len(d)):
    if 'jmp' in d[i]:
        d[i] = d[i].replace('jmp', 'nop')
        acc, found = get_acc_end()
        if found:
            print(acc)
            break
        else:
            d[i] = d[i].replace('nop', 'jmp')