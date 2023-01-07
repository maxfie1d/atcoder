def solve(A, B):
    return "Yay!" if A <= 8 and B <= 8 else ":("


A, B = map(int, input().split())

print(solve(A, B))
