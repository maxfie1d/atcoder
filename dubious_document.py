# 共通する文字をできるだけ多く選べばいい?

# a=2, b=1, c=1
# a=2, b=0, c=2, d=1
# a=3, b=0, c=2, d=0

# 2,0,1,0

from collections import defaultdict


def solve(n, li):
    # 縦にアクセスしたいな
    buckets = []
    for i in range(n):
        bucket = defaultdict(int)
        for v in li[i]:
            bucket[v] += 1
        buckets.append(bucket)

    r = ""
    for v in "abcdefghijklmnopqrstuvwxyz":
        l = min(map(lambda x: x[v], buckets))
        if l > 0:
            r += v * l

    return r


n = int(input())
li = []
for i in range(n):
    li.append(input())

print(solve(n, li))
