def same_char(a, b):
    count = set()
    for c in a:
        if any(map(lambda x: x == c, list(b))):
            count.add(c)
    return len(count)


def solve(N, S):
    r = 0
    for i in range(N):
        a = S[0:i]
        b = S[i:]
        r = max(r, same_char(a, b))

    return r


N = int(input())
S = input()

print(solve(N, S))
