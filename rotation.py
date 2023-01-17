N, Q = map(int, input().split())
S = input()
qli = []
for i in range(Q):
    qli.append(tuple(map(int, input().split())))

offset = 0
for query in qli:
    t, x = query
    if t == 1:
        offset = (offset + x) % N
    elif t == 2:
        idx = (x - 1 - offset) % N
        print(S[idx])
