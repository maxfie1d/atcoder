from collections import defaultdict

N, M = map(int, input().split())
edges = []
for i in range(M):
    edges.append(list(map(int, input().split())))

# make graph
graph = defaultdict(lambda: set())
for edge in edges:
    graph[edge[0]].add(edge[1])
    graph[edge[1]].add(edge[0])

for n in range(1, N+1):
    connected = sorted(list(graph[n]))
    l = len(connected)
    rest = " ".join(map(str, connected))
    print(l, end=" ")
    print(rest)

