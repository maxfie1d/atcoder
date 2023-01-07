def compute_kitaichi(p):
    return (1 + p) / 2


N, K = map(int, input().split())
pli = list(map(int, input().split()))

sum_list = [0] * (N + 1)
for i in range(N):
    p = pli[i]
    sum_list[i + 1] = sum_list[i] + compute_kitaichi(p)

result = 0
for l in range(N - K + 1):
    r = l + K
    v = sum_list[r] - sum_list[l]
    result = max(result, v)
print(result)
