import math


def distance(D, p, q):
    ss = 0
    for i in range(D):
        ss += math.pow(p[i] - q[i], 2)

    return math.sqrt(ss)


def solve(N, D, li):
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            p = li[i]
            q = li[j]
            d = distance(D, p, q)
            if d.is_integer():
                count += 1

    return count


N, D = map(int, input().split())
li = []
for i in range(N):
    li.append(list(map(int, input().split())))

print(solve(N, D, li))
