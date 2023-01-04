def solve(S, T):
    r = 0
    for i in range(3):
        if (S[i] == T[i]):
            r = r + 1
    return r


S = list(input())
T = list(input())

print(solve(S, T))
