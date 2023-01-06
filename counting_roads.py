# 都市0には何本の道路があるか

def solve(N, M, li):
    for i in range(N):
        count = 0
        for v in li:
            if (i + 1) in v:
                count += 1
        print(count)


N, M = map(int, input().split())
li = []
for i in range(M):
    li.append(list(map(int, input().split())))

solve(N, M, li)
