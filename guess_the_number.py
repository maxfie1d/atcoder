# 桁の指定があったものはその桁を使う
# 桁の指定がないものは0のままでよい

def solve(N, M, sli, cli):
    if M == 0:
        if N == 1:
            return 0
        else:
            return 10 ** (N - 1)

    rli = [-1] * N
    for i in range(M):
        s = sli[i]
        v = rli[s - 1]
        vv = cli[i]
        # -1か同じであれば代入する
        if v == -1 or v == vv:
            rli[s - 1] = vv
        else:
            return -1

    if N > 1 and rli[0] == 0:
        return -1

    r = 0
    for i in range(N):
        v = rli[i]
        if v == -1:
            if (i == 0):
                v = 1
            else:
                v = 0
        r += v * (10 ** (N - i - 1))

    return r


N, M = map(int, input().split())
sli = []
cli = []
for i in range(M):
    s, c = map(int, input().split())
    sli.append(s)
    cli.append(c)

print(solve(N, M, sli, cli))
