f = open('2021/input1.txt')

nums = list()

for line in f.readlines():
    nums.append(int(line))


def solve1_1():
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cnt += 1
    print(cnt)


def solve1_2():
    cnt = 0
    for i in range(3, len(nums)):
        if nums[i] + nums[i - 1] + nums[i - 2] > nums[i - 1] + nums[i - 2] + nums[i - 3]:
            cnt += 1
    print(cnt)


solve1_1()
solve1_2()
