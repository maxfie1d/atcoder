N = int(input())
S = input()

# 等しいかどうか入れておく
# 等しいならば1,そうでないならば0
G = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        if S[i] == S[j]:
            G[i][j] = 1

for n in range(1, N):
    l = 0
    i = 1
    j = 1 + n
    while l < N - n and G[i - 1][j - 1] == 0:
        l += 1
        i += 1
        j += 1
    print(l)
