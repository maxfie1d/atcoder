def solve(r, g, b):
    v = r * 100 + g * 10 + b
    return "YES" if v % 4 == 0 else "NO"


r, g, b = map(int, input().split())

print(solve(r, g, b))
