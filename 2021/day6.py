f = open('2021/input6.txt')

init_state = list(map(lambda x: int(x), f.readline().rstrip('\n').split(",")))


def solve(initial_state, nb_days):
    # just do a dict lol
    counts = dict()
    for i in range(9):
        counts[i] = 0
    for x in initial_state:
        counts[x] += 1
    for k in range(nb_days):
        newborns = counts[0]
        for i in range(8):
            counts[i] = counts[i + 1]
        counts[8] = newborns
        counts[6] += newborns
    cnt = 0
    for key in counts:
        cnt += counts[key]
    return cnt


def solve6_1():
    print(solve(init_state, 80))


def solve6_2():
    print(solve(init_state, 256))


solve6_1()
solve6_2()
