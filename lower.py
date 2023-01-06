def solve(N, H):
    i = 0
    r = []
    while i < N:
        j = i + 1
        while j < N and H[j] <= H[j - 1]:
            j += 1

        r.append(H[i:j])
        i = j

    return max(map(len, r)) - 1


N = int(input())
H = list(map(int, input().split()))

print(solve(N, H))
