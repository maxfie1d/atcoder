N, T = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)
rest = T % s
i = 0
while rest > 0:
    v = A[i % N]
    rest -= v
    i += 1

idx = (i - 1)
ans = rest + A[idx % N]
print(idx + 1, ans)
