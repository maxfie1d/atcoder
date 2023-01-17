from collections import defaultdict

N, X, Y = map(int, input().split())

# 赤2
# 赤1, 青2*3
# 赤0, 青2*3 + 青1*3

# 赤は青に変換するのみ
# 青も青と赤に変換するのみ
# 青の数は単調増加する (ルートによって結果が変化することはない)
# 青が1になるまで繰り返し赤を変換すればよい
# Nの数も小さいので愚直に計算するで足りる
# 漸化式でも解けるかも

RED = defaultdict(int)
BLUE = defaultdict(int)
RED[N] = 1

for v in range(N, 1, -1):
    # そのレベルの赤がなくなるまで変換する
    red = RED[v]
    RED[v - 1] += red
    BLUE[v] += X * red
    # そのレベルの青がなくなるまで変換する
    blue = BLUE[v]
    RED[v - 1] += blue
    BLUE[v - 1] += Y * blue

print(BLUE[1])
