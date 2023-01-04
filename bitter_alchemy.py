def solve(N, X, li):
    rest = X - sum(li)
    sort = sorted(li)
    return rest // min(sort) + len(li)


N, X = map(int, input().split())
li = []
for i in range(N):
    li.append(int(input()))

print(solve(N, X, li))
