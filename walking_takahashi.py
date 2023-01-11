def solve(X, K, D):
    count = min(K, X // D)
    rest_count = K - count
    a = X - count * D
    b = X - (count + 1) * D
    v = a if rest_count % 2 == 0 else b
    return abs(v)


X, K, D = map(int, input().split())

print(solve(X, K, D))
