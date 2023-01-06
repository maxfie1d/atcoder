# 長さ10のバケットを作る
# 文字ごとの数をカウントする
# このバケットの内容が等しければよい

def make_bucket(s):
    b = [0] * 26
    for i in range(10):
        index = ord(s[i]) - ord('a')
        b[index] += 1
    return b


def is_anagram(a, b):
    x = make_bucket(a)
    y = make_bucket(b)
    for i in range(26):
        if x[i] != y[i]:
            return False
    return True


def solve(N, li):
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            a = li[i]
            b = li[j]
            count += 1 if is_anagram(a, b) else 0

    return count


N = int(input())
li = []
for i in range(N):
    li.append(input())

print(solve(N, li))
