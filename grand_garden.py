# 再帰とかが使えるような気がするな
# 0になった場所があればsplitする
# 全てを足し合わせる
# 今までどれだけ水をやったか

# 1 2 2 1 2 2 1
# 0 1 1 0 1 1 0
# 0 0 0 0 0 0 0

# hは数列
# nは今までに何回水をやったか
def solve(h):
    mizu = min(h)
    h = list(map(lambda x: x - mizu, h))

    chunks = []
    i = 0
    while i < len(h) and h[i] == 0:
        i += 1

    while i < len(h):
        j = i + 1
        while j < len(h) and h[j] > 0:
            j += 1
        chunks.append(h[i:j])
        i = j + 1

    if len(chunks) == 0:
        return mizu

    return mizu + sum(map(solve, chunks))


N = int(input())
h = list(map(int, input().split()))

print(solve(h))
