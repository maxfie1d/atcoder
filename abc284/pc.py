# def concat(sub_graphs, u, v):
#     a = None
#     b = None
#     for i in range(len(sub_graphs)):
#         if u in sub_graphs[i]:
#             a = sub_graphs[i]
#             break
#     for i in range(len(sub_graphs)):
#         if v in sub_graphs[i] and sub_graphs[i] != a:
#             b = sub_graphs[i]
#             break
#     if a != None and b != None and a != b:
#         sub_graphs.remove(b)
#         sub_graphs.remove(a)
#         sub_graphs.append(a | b)
#
#     return sub_graphs


N, M = map(int, input().split())
edges = []
for i in range(M):
    edges.append(tuple(map(int, input().split())))

sub_graphs = []
for edge in edges:
    u = edge[0]
    v = edge[1]
    # uを含むsubgraphが存在するか?
    sub_graph_u = next(filter(lambda x: u in x, sub_graphs), None)
    sub_graph_v = next(filter(lambda x: v in x, sub_graphs), None)
    if sub_graph_u != None and sub_graph_v != None and sub_graph_u != sub_graph_v:
        sub_graphs.remove(sub_graph_u)
        sub_graphs.remove(sub_graph_v)
        sub_graphs.append(sub_graph_u | sub_graph_v)

    elif sub_graph_u != None:
        sub_graph_u.add(u)
        sub_graph_u.add(v)
    elif sub_graph_v != None:
        sub_graph_v.add(u)
        sub_graph_v.add(v)
    else:
        sub_graphs.append({u, v})

connected_count = sum(map(len, sub_graphs))
print(len(sub_graphs) + (N - connected_count))
