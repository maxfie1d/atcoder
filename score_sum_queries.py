N = int(input())
students = []
for i in range(N):
    students.append(tuple(map(int, input().split())))
Q = int(input())
qli = []
for i in range(Q):
    qli.append(tuple(map(int, input().split())))

# 1組の累積和を求める
f_sum_list = [0] * (N + 1)
s_sum_list = [0] * (N + 1)

for i in range(N):
    s = students[i]
    v = s[1] if s[0] == 1 else 0
    f_sum_list[i + 1] = f_sum_list[i] + v

    vv = s[1] if s[0] == 2 else 0
    s_sum_list[i + 1] = s_sum_list[i] + vv

for i in range(Q):
    l, r = qli[i]
    print(f_sum_list[r] - f_sum_list[l - 1], end=" ")
    print(s_sum_list[r] - s_sum_list[l - 1])
