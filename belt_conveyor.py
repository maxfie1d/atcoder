H, W = map(int, input().split())

G = []
for i in range(H):
    G.append(list(input()))

stop = False
infinite = False
l = (1, 1)
seen = set()
while not stop:
    if l in seen:
        stop = True
        infinite = True
        break

    seen.add(l)
    i, j = l
    v = G[i - 1][j - 1]
    if v == "U":
        if i != 1:
            l = (i - 1, j)
        else:
            stop = True
    elif v == "D":
        if i != H:
            l = (i + 1, j)
        else:
            stop = True
    elif v == "L":
        if j != 1:
            l = (i, j - 1)
        else:
            stop = True
    elif v == "R":
        if j != W:
            l = (i, j + 1)
        else:
            stop = True

if infinite:
    print(-1)
else:
    print(l[0], l[1])
