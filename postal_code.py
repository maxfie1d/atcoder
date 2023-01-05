def is_digit(c):
    return '0' <= c <= '9'


def solve(A, B, S):
    flag = True
    for i in range(A):
        c = S[i]
        if not is_digit(c):
            flag = False

    if S[A] != '-':
        flag = False

    for i in range(B):
        c = S[i + A + 1]
        if not is_digit(c):
            flag = False

    return "Yes" if flag else "No"


A, B = map(int, input().split())
S = input()

print(solve(A, B, S))
