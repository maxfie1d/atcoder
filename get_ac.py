N, Q = map(int, input().split())
S = input()
qli = []
for i in range(Q):
    qli.append(tuple(map(int, input().split())))

# Sのうち、ACを含んでいる場所を累積和として持っていればよい

sum_list = [0]
for i in range(1, N + 1):
    s = S[0:i]
    v = 1 if s[-2:] == "AC" else 0
    sum_list.append(sum_list[i - 1] + v)

# クエリを処理していく

for i in range(Q):
    l, r = qli[i]
    print(sum_list[r] - sum_list[l])
