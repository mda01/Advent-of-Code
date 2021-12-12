f = open('../input3.txt')

lines = list()

for line in f.readlines():
    lines.append(line.rstrip('\n'))


def solve3_1():
    counter = [0 for i in range(len(lines[0]))]
    for num in lines:
        for i in range(len(num)):
            counter[i] += num[i] == '1'

    gamma_list = []
    for x in counter:
        if x > len(lines) / 2:
            gamma_list.append(1)
        else:
            gamma_list.append(0)
    epsilon_list = []
    for x in gamma_list:
        if x:
            epsilon_list.append(0)
        else:
            epsilon_list.append(1)

    gamma = 0
    epsilon = 0
    exp = 0
    for x in reversed(gamma_list):
        gamma += x * 2 ** exp
        exp += 1
    exp = 0
    for x in reversed(epsilon_list):
        epsilon += x * 2 ** exp
        exp += 1
    print(gamma * epsilon)


def winner(compare_list, ind):
    cnt = 0
    for x in compare_list:
        if x[ind] == '1':
            cnt += 1
    return '1' if 2 * cnt >= len(compare_list) else '0'


def solve3_2():
    i = 0
    nl1 = lines.copy()
    while len(nl1) > 1:
        w = winner(nl1, i)
        nl1 = list(filter(lambda elt: elt[i] == w, nl1))
        i += 1
    o2 = 0
    exp = 0
    for x in reversed(nl1[0]):
        o2 += int(x) * 2 ** exp
        exp += 1

    i = 0
    nl2 = lines.copy()
    while len(nl2) > 1:
        w = winner(nl2, i)
        nl2 = list(filter(lambda elt: elt[i] != w, nl2))
        i += 1
    co2 = 0
    exp = 0
    for x in reversed(nl2[0]):
        co2 += int(x) * 2 ** exp
        exp += 1
    print(o2 * co2)


solve3_1()
solve3_2()
