f = open('../input9.txt')

lines = list()

for line in f.readlines():
    line = list(map(lambda x: int(x), list(line.rstrip('\n'))))
    lines.append(line)


def find_sinks():
    sinks = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            x = lines[i][j]
            if i > 0 and lines[i - 1][j] <= x:
                continue
            if i < len(lines) - 1 and lines[i + 1][j] <= x:
                continue
            if j > 0 and lines[i][j - 1] <= x:
                continue
            if j < len(lines[i]) - 1 and lines[i][j + 1] <= x:
                continue
            sinks.append((i, j))
    return sinks


def solve9_1():
    cnt = 0
    for x, y in find_sinks():
        cnt += lines[x][y] + 1
    print(cnt)


def size_of_sink(visited, x, y):
    cnt = 1
    h = lines[x][y]
    visited[x][y] = True
    if x > 0 and lines[x - 1][y] > h and not visited[x - 1][y]:
        cnt += size_of_sink(visited, x - 1, y)
    if x < len(lines) - 1 and lines[x + 1][y] > h and not visited[x + 1][y]:
        cnt += size_of_sink(visited, x + 1, y)
    if y > 0 and lines[x][y - 1] > h and not visited[x][y - 1]:
        cnt += size_of_sink(visited, x, y - 1)
    if y < len(lines[x]) - 1 and lines[x][y + 1] > h and not visited[x][y + 1]:
        cnt += size_of_sink(visited, x, y + 1)
    return cnt


def solve9_2():
    # TODO create another map with visited points (starting with 9 heights)
    # for each sink, check if neighbours are visited, if not add point to sink and expand to neighbours recursively
    sink_sizes = []
    visited = [[False for i in range(len(lines[0]))] for i in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            visited[i][j] = lines[i][j] == 9
    for x, y in find_sinks():
        sink_sizes.append(size_of_sink(visited, x, y))
    sink_sizes.sort(reverse=True)
    print(sink_sizes[0] * sink_sizes[1] * sink_sizes[2])


solve9_1()
solve9_2()
