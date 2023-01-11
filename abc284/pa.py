N = int(input())
sli = []
for i in range(N):
    sli.append(input())

for i in range(N):
    print(sli[-(i + 1)])
