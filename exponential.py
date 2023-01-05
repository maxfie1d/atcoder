# Xは1000以下となっている
import math


def solve(X):
    r = 0
    for b in range(1, 33):
        for p in range(2, 11):
            a = b ** p
            if a <= X:
                r = max(r, a)
    return int(r)


X = int(input())
print(solve(X))
