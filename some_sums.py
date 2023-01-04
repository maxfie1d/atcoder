def digit_sum(n):
    r = 0
    while n > 0:
        r += n % 10
        n = n // 10
    return r


def solve(n, a, b):
    r = 0
    for v in range(1, n + 1):
        vv = digit_sum(v)
        if a <= vv <= b:
            r += v

    return r


N, A, B = map(int, input().split())

print(solve(N, A, B))
