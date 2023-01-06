def solve(N, M, Q, v, c, s):
    for i in range(Q):
        query = s[i]
        x = query[1]
        print(c[x-1])
        if query[0] == 1:
            # スプリンクラーを起動する
            # 頂点xに接続している頂点の色を書き換える
            for a in v:
                if a[0] == x:
                    c[a[1]-1] = c[x-1]
                if a[1] == x:
                    c[a[0]-1] = c[x-1]
        else:
            y = query[2]
            c[x - 1] = y


N, M, Q = map(int, input().split())
v = []
for i in range(M):
    v.append(list(map(int, input().split())))
c = list(map(int, input().split()))
s = []
for i in range(Q):
    s.append(list(map(int, input().split())))

solve(N, M, Q, v, c, s)
