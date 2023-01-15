N = int(input())
A = list(map(int, input().split()))

li = sorted(A)
ruiseki = [0] * N +1

for i in range(N):
    ruiseki[i + 1] = ruiseki[i] +

print(li)
print(ruiseki)