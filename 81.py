def solve(N):
    for i in range(1, 10):
        a = N % i
        b = N // i
        if a == 0 and 1 <= b <= 9:
            return "Yes"

    return "No"


N = int(input())
print(solve(N))
