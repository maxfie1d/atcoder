from collections import defaultdict

N = int(input())
reqs = []
for i in range(N):
    reqs.append(tuple(input().split()))

G = defaultdict(list)
for i in range(N):
    a, b = reqs[i]
    G[a].append(b)

flag = True

keys = list(G.keys())
for key in keys:
    seen = set()
    c = key
    while c not in seen:
        seen.add(c)
        v = G[c]
        if len(v) == 0:
            break
        c = v[0]
        if c in seen:
            flag = False

print("Yes" if flag else "No")
