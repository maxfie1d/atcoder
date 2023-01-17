h1, h2, h3, w1, w2, w3 = map(int, input().split())


def comb(n):
    arr = []
    for i in range(1, n - 1):
        for j in range(1, n - i):
            k = n - (i + j)
            arr.append((i, j, k))
    return arr


count = 0
for v1 in comb(w1):
    for v2 in comb(w2):
        v3a = h1 - (v1[0] + v2[0])
        v3b = h2 - (v1[1] + v2[1])
        v3c = h3 - (v1[2] + v2[2])
        v3 = [v3a, v3b, v3c]
        if sum(v3) == w3 and all(map(lambda x: x > 0, v3)):
            count += 1

print(count)
