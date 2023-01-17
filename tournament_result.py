N = int(input())

A = []
for i in range(N):
    A.append(list(input()))

correct = True
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a = A[i][j]
        b = A[j][i]
        if a == "W" and b == "W":
            correct = False
        if a == "L" and b == "L":
            correct = False
        if (a == "D" and b != "D") or (a != "D" and b == "D"):
            correct = False

print("correct" if correct else "incorrect")
