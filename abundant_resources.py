N = int(input())
A = list(map(int, input().split()))

sum_list = [0] * (N + 1)
for i in range(N):
    sum_list[i + 1] = sum_list[i] + A[i]

for k in range(1, N + 1):
    result = 0
    for l in range(N - k + 1):
        r = l + k
        v = sum_list[r] - sum_list[l]
        result = max(result, v)
    print(result)
