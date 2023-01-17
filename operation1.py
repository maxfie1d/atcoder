X, A, D, N = map(int, input().split())

l = A
r = A + (N - 1) * D
if X <= A:
    if D >= 0:
        print(abs(A - X))
    else:
        print()
    elif X >= r:
        print(abs(X - r))

elif D == 0:
    print(0)
else:
    v = (X - A) % D
    r = min(v, N - v)
    print(r)
