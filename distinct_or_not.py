def solve(N, li):
    s = set()
    for v in li:
        s.add(v)

    return "YES" if N == len(s) else "NO"


N = int(input())
li = list(map(int, input().split()))

print(solve(N, li))
