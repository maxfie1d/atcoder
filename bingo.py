## True と Flase の2次元配列を作る

def check_yoko(card):
    # いずれかがすべてtrueであればよい
    for i in range(3):
        li = card[i]
        if all(li):
            return True


def check_tate(card):
    for j in range(3):
        if all([card[0][j], card[1][j], card[2][j]]):
            return True

    return False


def check_naname(card):
    a = all([card[0][0], card[1][1], card[2][2]])
    b = all([card[0][2], card[1][1], card[2][0]])
    return a or b


def check(card):
    return check_tate(card) or check_yoko(card) or check_naname(card)


def solve(li, N, bli):
    card = [[False] * 3, [False] * 3, [False] * 3]
    for v in bli:
        for i in range(3):
            for j in range(3):
                if v == li[i][j]:
                    card[i][j] = True

    return "Yes" if check(card) else "No"


li = []
for i in range(3):
    li.append(list(map(int, input().split())))
N = int(input())
bli = []
for i in range(N):
    bli.append(int(input()))

print(solve(li, N, bli))
