def solve(a, b):
    x = a + b
    y = a - b
    z = a * b

    return max(x, y, z)


a, b = map(int, input().split())

print(solve(a, b))
