# X | X の形式になっている
# Xが部分的に隅文字列になっていることもありうる
# 1文字ずつ消して、それが隅文字列になっているかを確かめる
# 隅文字列ということは偶数長の文字列であるはず

def is_gumoji(S):
    l = len(S)
    p = l // 2
    a = S[:p]
    b = S[p:]
    return a == b


def solve(S):
    l = len(S)
    for step in range(l // 2):
        ss = S[:l - 2 * (step + 1)]
        if (is_gumoji(ss)):
            return len(ss)

    return ""


S = input()
print(solve(S))
