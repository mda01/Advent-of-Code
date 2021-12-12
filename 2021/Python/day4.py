import re

f = open('../input4.txt')

lines = list()

for line in f.readlines():
    lines.append(re.sub(' +', ' ', line.rstrip('\n').lstrip(' ')))

nums = list(map(lambda x: int(x), lines[0].split(',')))
grids = list()
for i in range(2, len(lines), 6):
    g = list()
    for j in range(5):
        g.append(list(map(lambda x: int(x), lines[i + j].split(' '))))
    grids.append(g)


def is_win(grid, nums):
    N = len(grid)
    win = False
    for i in range(N):
        all_check_h = True
        all_check_v = True
        for j in range(N):
            all_check_h = all_check_h and grid[i][j] in nums
            all_check_v = all_check_v and grid[j][i] in nums
        win = win or all_check_h or all_check_v
    return win


def compute_score(grid, nums):
    cnt = 0
    for x in grid:
        for y in x:
            if y not in nums:
                cnt += y
    return cnt


def solve4_1():
    for i in range(5, len(nums)):
        for g in grids:
            if is_win(g, nums[:i]):
                print(compute_score(g, nums[:i]) * nums[i - 1])
                return


def solve4_2():
    gs = grids
    lwg = None
    for i in range(5, len(nums)):
        ng = list()
        for g in gs:
            if not is_win(g, nums[:i]):
                ng.append(g)
        gs = ng
        if len(gs) == 1:
            lwg = gs[0]
            break
    for i in range(len(nums)):
        if is_win(lwg, nums[:i]):
            print(compute_score(gs[0], nums[:i]) * nums[i - 1])
            break


solve4_1()
solve4_2()
