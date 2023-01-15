from collections import defaultdict

N, M = map(int, input().split())

dict = defaultdict(lambda: set())
for i in range(M):
    A = list(map(int, input().split()))[1:]
    for i in range(len(A)):
        for j in range(len(A)):
            dict[A[i]].add(A[j])

r = "Yes" if all(map(lambda x: len(x) == N, dict.values())) else "No"
print(r)
