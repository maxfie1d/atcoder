from collections import defaultdict

N = int(input())
S = []

dict = defaultdict(int)

for i in range(N):
    S.append(input())

for i in range(N):
    s = S[i]
    count = dict[s]
    vv = "(" + str(count) + ")" if count > 0 else ""
    print(s + vv)
    dict[s] += 1
