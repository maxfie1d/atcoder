def solve(a, b):
    if a > 0:
        if b > 0:
            return "Positive"
        elif b <= 0:
            return "Zero"
    if a == 0:
        return "Zero"
    if a < 0:
        if b >= 0:
            return "Zero"
        if b < 0:
            r = b - a + 1
            return "Positive" if r % 2 == 0 else "Negative"


a, b = map(int, input().split())

print(solve(a, b))
