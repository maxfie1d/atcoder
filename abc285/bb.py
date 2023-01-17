N = int(input())
S = list(input())

for i in range(1, N):
    l = 0

    for dx in range(N - i):
        if S[dx] != S[dx + i]:
            l += 1
        else:
            break
    print(l)
