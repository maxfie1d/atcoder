# https://atcoder.jp/contests/arc153/tasks/arc153_a

N = int(input())


# 下3桁がどのように変化するか
def fv1(v):
    carry = False
    if v[1] < 9:
        v[1] += 1
    else:
        v[1] = 0
        if v[0] == 9 and v[2] == 9:
            carry = True
            v[0] = 0
            v[2] = 0
        else:
            v[0] += 1
            v[2] += 1
    return v, carry


def fv2v4(v):
    carry = False
    if v[0] == 9:
        carry = True
        v[0] = 0
        v[1] = 0
    else:
        v[0] += 1
        v[1] += 1
    return v, carry


def fv3(v):
    carry = False
    if v[1] == 9:
        v[1] = 0
        if v[0] == 9:
            carry = True
            v[0] = 0
        else:
            v[0] += 1
    else:
        v[1] += 1

    return v, carry


# 7桁目 ~ 9桁目
v1 = [0, 0, 0]
# 5桁目 ~ 6桁目
v2 = [0, 0]
# 3桁目 = 4桁目
v3 = [0, 0]
# 1桁目 ~ 2桁目
v4 = [1, 1]

for i in range(N - 1):
    _, c1 = fv1(v1)
    if c1:
        _, c2 = fv2v4(v2)
        if c2:
            _, c3 = fv3(v3)
            if c3:
                _, c4 = fv2v4(v4)

s = map(str, v4 + v3 + v2 + v1)
print(int("".join(s)))
