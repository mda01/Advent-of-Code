f = open('../input7.txt')

init_state = list(map(lambda x: int(x), f.readline().rstrip('\n').split(",")))


def compute_cost1(nums: dict, goal: int):
    cnt = 0
    for key in nums:
        cnt += abs(key - goal) * nums[key]
    return cnt


def compute_cost2(nums: dict, goal: int):
    cnt = 0
    for key in nums:
        diff = abs(key - goal)
        cnt += ((diff * (diff + 1)) // 2) * nums[key]
    return cnt


def solve7_1():
    nums = dict()
    b = -1
    for x in init_state:
        b = max(b, x)
        if x not in nums:
            nums[x] = 1
        else:
            nums[x] += 1

    a = 0
    c = b
    b = (a + c) // 2
    while c - b > 1 or b - a > 1:
        x1 = (a + b) // 2
        x2 = (b + c) // 2
        fx1 = compute_cost1(nums, x1)
        fx2 = compute_cost1(nums, x2)
        fxb = compute_cost1(nums, b)
        if fxb < fx1 < compute_cost1(nums, a):
            a = x1
        else:
            c = b
            b = x1
            continue
        if fxb < fx2 < compute_cost1(nums, c):
            c = x2
        else:
            a = b
            b = x2

    print(compute_cost1(nums, b))


def solve7_2():
    nums = dict()
    b = -1
    for x in init_state:
        b = max(b, x)
        if x not in nums:
            nums[x] = 1
        else:
            nums[x] += 1

    a = 0
    c = b
    b = (a + c) // 2
    while c - b > 1 or b - a > 1:
        x1 = (a + b) // 2
        x2 = (b + c) // 2
        fx1 = compute_cost2(nums, x1)
        fx2 = compute_cost2(nums, x2)
        fxb = compute_cost2(nums, b)
        if fxb < fx1 < compute_cost2(nums, a):
            a = x1
        else:
            c = b
            b = x1
            continue
        if fxb < fx2 < compute_cost2(nums, c):
            c = x2
        else:
            a = b
            b = x2

    print(compute_cost2(nums, b))


solve7_1()
solve7_2()
