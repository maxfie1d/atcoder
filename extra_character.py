S = input()
T = input()

idx = 0
while idx < len(S) and S[idx] == T[idx]:
    idx += 1

print(idx + 1)
