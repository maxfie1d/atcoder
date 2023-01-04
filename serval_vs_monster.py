def solve(H, A):
    c = H // A
    d = H % A
    return c if d == 0 else c + 1


print(solve(10000, 1))
