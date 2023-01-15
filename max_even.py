# https://atcoder.jp/contests/abc272/tasks/abc272_c

N = int(input())
A = list(map(int, input().split()))

# 偶数になる条件
# 偶数 + 偶数
# 偶数のうち最大のものを2つ選ぶ
# 奇数 + 奇数
# 奇数のうち最大のものを2つ選ぶ

gusuu = []
kisu = []

A = sorted(A)
for i in range(N):
    v = A[i]
    if v % 2 == 0:
        gusuu.append(v)
    else:
        kisu.append(v)

max1 = -1
max2 = -1
if len(gusuu) >= 2:
    max1 = gusuu[-1] + gusuu[-2]

if len(kisu) >= 2:
    max2 = kisu[-1] + kisu[-2]

print(max(max1, max2))
