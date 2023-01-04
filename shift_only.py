# 各要素が何回2で割れるかを調べて
# これらの最小値をとればよい

def how_many_times(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count


def solve(n, li):
    return min(map(how_many_times, li))


N = int(input())
A = list(map(int, input().split()))

print(solve(N, A))
