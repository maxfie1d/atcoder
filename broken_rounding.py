X, K = map(int, input().split())


def int2(s):
    if s == "":
        return 0
    else:
        return int(s)


def compute(n, i):
    s = str(n)
    s = s.rjust(max(len(s), i + 1), "0")
    head, tail = int2(s[0:-(i + 1)]), int2(s[-(i + 1):])

    v = 10 ** (i + 1)
    if tail >= v // 2:
        tail = v
    else:
        tail = 0

    r = head * (10 ** (i + 1)) + tail

    return r


n = X
for i in range(K):
    n = compute(n, i)

print(n)
