# https://atcoder.jp/contests/abc279/tasks/abc279_c

H, W = map(int, input().split())
S = []
T = []

sli = []
tli = []
for i in range(H):
    S.append(list(input()))

for i in range(H):
    T.append(list(input()))

for j in range(W):
    s = ""
    for i in range(H):
        s += S[i][j]
    sli.append(s)

for j in range(W):
    s = ""
    for i in range(H):
        s += T[i][j]
    tli.append(s)

sli = sorted(sli)
tli = sorted(tli)

equal = True
for j in range(W):
    if sli[j] != tli[j]:
        equal = False
r = "Yes" if equal else "No"

print(r)
