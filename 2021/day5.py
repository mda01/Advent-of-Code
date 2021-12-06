f = open('2021/input5.txt')

lines = list()

for line in f.readlines():
    line = line.rstrip('\n').split(' ')
    line = [line[0], line[2]]
    line = list(map(lambda x: x.split(','), line))
    line = ((int(line[0][0]),
             int(line[0][1])),
            (int(line[1][0]),
             int(line[1][1])))
    lines.append(line)
                
def solve5_1():
    grid = [[0 for x in range(1000)] for x in range(1000)]
    for (x1, y1), (x2, y2) in lines:
        if x1 == x2 or y1 == y2:
            minx = min(x1, x2)
            maxx = max(x1, x2)
            miny = min(y1, y2)
            maxy = max(y1, y2)
            for x in range(minx, maxx + 1):
                for y in range(miny, maxy + 1):
                    grid[x][y] += 1
    cnt = 0
    for l in grid:
        for v in l:
            if v > 1 :
                cnt += 1
    print(cnt)

def solve5_2():
    grid = [[0 for x in range(1000)] for x in range(1000)]
    for (x1, y1), (x2, y2) in lines:
        minx = min(x1, x2)
        maxx = max(x1, x2)
        miny = min(y1, y2)
        maxy = max(y1, y2)
        if x1 == x2 or y1 == y2:
            for x in range(minx, maxx + 1):
                for y in range(miny, maxy + 1):
                    grid[x][y] += 1
        elif (x2 - x1) == (y2 - y1):
            for i in range(maxx - minx + 1):
                grid[minx + i][miny + i] += 1
        elif (x2 - x1) == -(y2 - y1):
            for i in range(maxx - minx + 1):
                grid[minx + i][maxy - i] += 1
    cnt = 0
    for l in grid:
        for v in l:
            if v > 1 :
                cnt += 1
    print(cnt)
                
solve5_1()
solve5_2()
