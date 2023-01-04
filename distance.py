import math


def distance(li):
    return math.sqrt(li[0] ** 2 + li[1] ** 2)


def solve(N, D, li):
    return len(list(filter(lambda x: x <= D, map(distance, li))))


N, D = map(int, input().split())
# listのlistを作る?
# tuppleみたいなビルトインの型があるのかな
li = []
for i in range(N):
    li.append(list(map(int, input().split())))

print(solve(N, D, li))
