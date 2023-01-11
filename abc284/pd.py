import math


def solve(test):
    route_n = math.floor(math.sqrt(test))
    yakusuu = 0
    for i in range(2, route_n + 1):
        if test % i == 0:
            yakusuu = i
            break
    # 見つかった約数がqである場合
    pp = test // yakusuu
    p = math.sqrt(pp)
    if p.is_integer():
        print(int(p), end=" ")
        print(yakusuu)
    else:
        print(yakusuu, end=" ")
        q = test // (yakusuu ** 2)
        print(q)



T = int(input())
tests = []
for i in range(T):
    solve(int(input()))
