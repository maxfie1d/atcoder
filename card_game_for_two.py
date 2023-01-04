# 大きい順(降順)に並べる
# 10 9 8 7 6 5 4 3 2 1
# 奇数番号がalice
# 偶数番号をbobとする

def solve(li):
    li = sorted(li, reverse=True)
    alice = sum(map(
        lambda x: li[x],
        filter(lambda x: x % 2 == 0, range(len(li)))
    ))
    bob = sum(map(
        lambda x: li[x],
        filter(lambda x: x % 2 == 1, range(len(li)))
    ))
    return alice - bob


N = int(input())
li = list(map(int, input().split()))

print(solve(li))
