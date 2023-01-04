def solve(N, li):
    highest = 0
    count = 0
    for i in range(len(li)):
        v = li[i]
        if v >= highest:
            count += 1
        highest = max(highest, v)
    return count


N = int(input())
li = list(map(int, input().split()))

print(solve(N, li))
