from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(2 * 10 ** 5 + 1)


def solve(current, ladders, seen):
    # currentからすすめる先を調べる
    seen[current] = True
    r = current
    for next in ladders[current]:
        if not seen[next]:
            r = max(r, solve(next, ladders, seen))
    return r


N = int(input())
ladders = defaultdict(list)
seen = defaultdict(lambda: False)
for i in range(N):
    a, b = map(int, input().split())
    ladders[a].append(b)
    ladders[b].append(a)

print(solve(1, ladders, seen))

# ループする場合は弾く ok
# はしごが存在しない場合もはじく ok
# 深さ優先探索でいいのかな
# N < 2*10^5
# もっとも値が大きければよい
