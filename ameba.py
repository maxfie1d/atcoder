N = int(input())
A = list(map(int, input().split()))

# メモ化が必要かな
memo = {}


def solve(start):
    count = 0
    k = start
    while k != 1:
        count += 1
        anc = -1
        if k % 2 == 1:
            anc = (k - 1) // 2
        else:
            anc = k // 2
        k = A[anc - 1]
        v = memo.get(k, None)
        if v is not None:
            return count + v

    memo[start] = count
    return count


for k in range(1, 2 * N + 1 + 1):
    print(solve(k))
