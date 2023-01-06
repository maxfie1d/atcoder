def solve(N, M, K, A):
    bucket = [0] * M
    for i in range(N):
        k = K[i]
        for j in range(k):
            bucket[A[i][j] - 1] += 1

    count = 0
    for i in range(M):
        if bucket[i] == N:
            count += 1

    return count


N, M = map(int, input().split())
K = []
A = []
for i in range(N):
    li = list(map(int, input().split()))
    K.append(li[0])
    A.append(li[1:])

print(solve(N, M, K, A))
