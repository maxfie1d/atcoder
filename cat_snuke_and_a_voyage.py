# 経路長2で目的値にたどり着けるかどうか調べる
# 全探索すればよさそう

def solve(N, M, li):
    dict = set()
    for v in li:
        dict.add(v)

    for i in range(2, N):
        a = (1, i) in dict
        b = (i, N) in dict
        if a and b:
            return "POSSIBLE"
    return "IMPOSSIBLE"


N, M = map(int, input().split())
li = []
for i in range(M):
    li.append(tuple(map(int, input().split())))

print(solve(N, M, li))
