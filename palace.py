# Aとの差がもっとも小さい場所を選ぶ


def solve(N, T, A, li):
    min_diff = 100000
    r = 0
    for i in range(N):
        h = li[i]
        t = T - h * 0.006
        diff = abs(A - t)
        if diff < min_diff:
            min_diff = diff
            r = i

    return r + 1


N = int(input())
T, A = map(int, input().split())
li = list(map(int, input().split()))

print(solve(N, T, A, li))
