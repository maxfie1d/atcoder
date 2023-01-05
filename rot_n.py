def solve(N, S):
    li = list(S)
    for i in range(len(li)):
        c = li[i]
        index = ((ord(c) - ord('A')) + N) % 26
        li[i] = chr(ord('A') + index)
    return "".join(li)


N = int(input())
S = input()

print(solve(N, S))
