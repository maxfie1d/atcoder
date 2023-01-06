# 10個ボールがあって
# それぞれに1122334455と書いてあるとする
# 1=2
# 2=2
# 3=2
# 4=2
# 5=2

# 3種類以下にするにはどうしたらいい
# もとは5種類ある
# 1種類しかないものを書き換える
# 2種類しかないものを書き換える
# これを繰り返してK以下になるようにする

# 1=2
# 2=2
# 5=1
#
from collections import defaultdict


def solve(N, K, li):
    bucket = defaultdict(int)
    for v in li:
        bucket[v] += 1

    k = len(bucket)
    # diff種類減らす必要がある
    diff = max(k - K, 0)

    values = sorted(bucket.values(), reverse=False)
    r = sum(values[0:diff])

    return r


N, K = map(int, input().split())
li = list(map(int, input().split()))

print(solve(N, K, li))
