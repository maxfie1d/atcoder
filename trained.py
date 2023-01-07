def solve(N, a):
    count = 0
    start = 1
    s = {1}
    while True:
        v = a[start]
        if v in s:
            return -1

        count += 1
        start = v
        s.add(v)

        if v == 2:
            return count


N = int(input())
a = [0] * (N + 1)
for i in range(1, N + 1):
    a[i] = int(input())

print(solve(N, a))
