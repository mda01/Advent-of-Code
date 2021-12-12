f = open('../input10.txt')

lines = list()

for line in f.readlines():
    lines.append(line.rstrip('\n'))

chars = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}
scores1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

scores2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def solve10_1():
    score = 0
    for line in lines:
        stack = []
        for c in line:
            if c in chars:
                stack.append(c)
            else:
                o = stack.pop()
                if c != chars[o]:
                    score += scores1[c]
                    break  # go to the next line
    print(score)


def solve10_2():
    scores = []
    for line in lines:
        stack = []
        corrupted = False
        for c in line:
            if c in chars:
                stack.append(c)
            else:
                o = stack.pop()
                if c != chars[o]:
                    corrupted = True
                    break  # go to the next line
        if not corrupted:
            score = 0
            for c in reversed(stack):
                score = score * 5 + scores2[c]
            scores.append(score)
    scores.sort()
    print(scores[len(scores) // 2])


solve10_1()
solve10_2()
