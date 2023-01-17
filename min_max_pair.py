# https://atcoder.jp/contests/abc262/tasks/abc262_c

N = int(input())
A = list(map(int, input().split()))

# ai < aj のとき
# i = ai
# j = aj
# インデックスと値が一致している

count = 0
for i in range(1, N + 1):
    if i == A[i - 1]:
        count += 1

r = count * (count - 1) // 2

# ai = aj はありあえない

# ai > aj のとき
# aj = i
# ai = j

r2 = 0
for i in range(1, N + 1):
    v = A[i - 1]
    vv = A[v - 1]
    if i == vv and i != v:
        r2 += 1

print(r + r2 // 2)
