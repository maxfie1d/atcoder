S = input()
T = input()


def solve(S, T):
    for i in range(len(S) - len(T) + 1):
        equal = True
        for j in range(len(T)):
            if S[i + j] != T[j]:
                equal = False
        if equal:
            return "Yes"
    return "No"


print(solve(S, T))
