
with open ('Day8/data.txt') as f:
    d = f.readlines()
    d = [ line.strip() for line in d ]

def get_acc():
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

    return acc
        
acc = get_acc()

print(acc)