N = int(input())
P = list(map(int, input().split()))

# 親をたどって1にたどりつくまでを調べればよい
count = 0
c = N
while c != 1:
    c = P[c - 2]
    count += 1

print(count)


