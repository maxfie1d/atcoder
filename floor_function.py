import math


def solve(A, B, N):
    x = min(B - 1, N)

    r = math.floor(A * x / B) - math.floor(x / B)
    return r


A, B, N = map(int, input().split())
print(solve(A, B, N))
