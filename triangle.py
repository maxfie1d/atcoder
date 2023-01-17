from collections import defaultdict

N, M = map(int, input().split())

edges = []
graph = defaultdict(lambda: set())
for i in range(M):
    u, v = tuple(map(int, input().split()))
    graph[u].add(v)
    graph[v].add(u)
    edges.append((u, v))

triangles = set()
for a in graph.keys():
    for b in graph[a]:
        for c in graph[b]:
            if a in graph[c]:
                t = (a, b, c)
                triangles.add(tuple(sorted(t)))

print(len(triangles))
