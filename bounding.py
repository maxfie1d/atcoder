# 足し上げた上で、 Xより大きくなったところでストップする
def solve(N, X, li):
    count = 1
    d = 0
    for v in li:
        d += v
        if d > X:
            break
        count += 1

    return count


N, X = map(int, input().split())
li = list(map(int, input().split()))

print(solve(N, X, li))
