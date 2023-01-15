# https://atcoder.jp/contests/abc270/tasks/abc270_c
import sys
from collections import defaultdict

sys.setrecursionlimit(2 * 10 ** 5 + 1)

seen = defaultdict(lambda: False)
stack = []
flag = False

N, X, Y = map(int, input().split())
tree = defaultdict(lambda: set())
for i in range(N - 1):
    a, b = tuple(map(int, input().split()))
    tree[a].add(b)
    tree[b].add(a)

# その頂点は訪問済みか?


def dfs(start, end):
    global flag
    if not flag:
        stack.append(start)
    seen[start] = True
    if start == end:
        flag = True
        return

    for next in tree[start]:
        if not seen[next]:
            dfs(next, end)

    if not flag:
        stack.pop()


dfs(X, Y)
print(" ".join(map(str, stack)))
