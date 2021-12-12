f = open("../input2.txt")

lines = list()

for line in f.readlines():
    d, val = line.split()
    val = int(val)
    lines.append((d, val))


def solve2_1():
    dxs = list()
    dys = list()
    for direction, v in lines:
        if direction == 'down':
            dys.append(v)
        elif direction == 'up':
            dys.append(-v)
        elif direction == 'forward':
            dxs.append(v)
    print(sum(dxs) * sum(dys))


def solve2_2():
    aim = 0
    depth = 0
    pos = 0
    for direction, X in lines:
        if direction == 'down':
            aim += X
        elif direction == 'up':
            aim -= X
        elif direction == 'forward':
            pos += X
            depth += aim * X
    print(depth * pos)


solve2_1()
solve2_2()
